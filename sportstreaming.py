import requests
import re
import os
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import os
from dotenv import load_dotenv
load_dotenv()

# URL di partenza (homepage o pagina con elenco eventi)
base_url = "https://www.sportstreaming.net/"
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1",
    "Origin": "https://www.sportstreaming.net",
    "Referer": "https://www.sportstreaming.net/"
}

# Prefisso per il proxy dello stream
PROXY_STREAM_PREFIX = os.getenv("HLSPROXYMFP")

# Funzione helper per formattare la data dell'evento
def format_event_date(date_text):
    if not date_text:
        return ""
    match = re.search(
        r'(?:[a-zA-Zì]+\s+)?(\d{1,2})\s+([a-zA-Z]+)\s+(?:ore\s+)?(\d{1,2}:\d{2})',
        date_text,
        re.IGNORECASE
    )
    if match:
        day = match.group(1).zfill(2)
        month_name = match.group(2).lower()
        time = match.group(3)
        month_number = ITALIAN_MONTHS_MAP.get(month_name)
        if month_number:
            return f"{time} {day}/{month_number}"
    return ""


# Mappa dei mesi italiani per la formattazione della data
ITALIAN_MONTHS_MAP = {
    "gennaio": "01", "febbraio": "02", "marzo": "03", "aprile": "04",
    "maggio": "05", "giugno": "06", "luglio": "07", "agosto": "08",
    "settembre": "09", "ottobre": "10", "novembre": "11", "dicembre": "12"
}

# Funzione per trovare i link alle pagine evento
def find_event_pages():
    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        event_links = []
        seen_links = set()
        for a in soup.find_all('a', href=True):
            href = a['href']
            if re.match(r'/live-(perma-)?\d+', href):
                full_url = base_url + href.lstrip('/')
                if full_url not in seen_links:
                    event_links.append(full_url)
                    seen_links.add(full_url)
            elif re.match(r'https://www\.sportstreaming\.net/live-(perma-)?\d+', href):
                if href not in seen_links:
                    event_links.append(href)
                    seen_links.add(href)

        # Aggiungi i canali live-temp-1 fino a live-temp-40
        for i in range(1, 41):
            temp_url = f"https://sportstreaming.net/live-temp-{i}"
            if temp_url not in seen_links:
                event_links.append(temp_url)
                seen_links.add(temp_url)
#fine aggiunta
        return event_links

    except requests.RequestException as e:
        print(f"Errore durante la ricerca delle pagine evento: {e}")
        return []

# Funzione per estrarre il flusso video e i dettagli dell'evento dalla pagina evento
def get_event_details(event_url):
    try:
        response = requests.get(event_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        stream_url = None
        element = None
        for iframe in soup.find_all('iframe'):
            src = iframe.get('src')
            if src and ("stream" in src.lower() or re.search(r'\.(m3u8|mp4|ts|html|php)', src, re.IGNORECASE)):
                stream_url = src
                element = iframe
                break

        if not stream_url:
            for embed in soup.find_all('embed'):
                src = embed.get('src')
                if src and ("stream" in src.lower() or re.search(r'\.(m3u8|mp4|ts|html|php)', src, re.IGNORECASE)):
                    stream_url = src
                    element = embed
                    break

        if not stream_url:
            for video in soup.find_all('video'):
                src = video.get('src')
                if src and ("stream" in src.lower() or re.search(r'\.(m3u8|mp4|ts)', src, re.IGNORECASE)):
                    stream_url = src
                    element = video
                    break
                for source in video.find_all('source'):
                    src = source.get('src')
                    if src and ("stream" in src.lower() or re.search(r'\.(m3u8|mp4|ts)', src, re.IGNORECASE)):
                        stream_url = src
                        element = source
                        break

        # Estrai data e ora formattate
        formatted_date = ""
        date_span = soup.find('span', class_='uk-text-meta uk-text-small')
        if date_span:
            date_text = date_span.get_text(strip=True)
            formatted_date = format_event_date(date_text)

        # Estrai il titolo dell'evento dal tag <title>
        event_title_from_html = "Unknown Event"
        title_tag = soup.find('title')
        if title_tag:
            event_title_from_html = title_tag.get_text(strip=True)
            event_title_from_html = re.sub(r'\s*\|\s*Sport Streaming\s*$', '', event_title_from_html, flags=re.IGNORECASE).strip()

        # Estrai informazioni sulla lega/competizione
        league_info = "Event" # Default
        is_perma_channel = "perma" in event_url.lower()

        if is_perma_channel:
            if event_title_from_html and event_title_from_html != "Unknown Event":
                league_info = event_title_from_html
            # Se il titolo del canale perma non è stato trovato, league_info resta "Event"
        else:
            # Per canali non-perma (eventi specifici), cerca lo span della lega/competizione
            league_spans = soup.find_all(
                lambda tag: tag.name == 'span' and \
                            'uk-text-small' in tag.get('class', []) and \
                            'uk-text-meta' not in tag.get('class', []) # Escludi lo span della data
            )
            if league_spans:
                # Prendi il testo del primo span corrispondente, pulito
                league_info = ' '.join(league_spans[0].get_text(strip=True).split())
            # Se lo span non viene trovato per un evento non-perma, league_info resta "Event"

        return stream_url, formatted_date, event_title_from_html, league_info

    except requests.RequestException as e:
        print(f"Errore durante l'accesso a {event_url}: {e}")
        return None, "", "Unknown Event", "Event"

# Funzione per generare un tvg-id pulito
def generate_clean_tvg_id(name_input):
    if not name_input or name_input.lower() == "unknown event" or name_input.lower() == "event":
        return "unknown-event"
    # Converti in minuscolo
    s = name_input.lower()
    # Sostituisci spazi e caratteri speciali comuni con trattini
    s = re.sub(r'[\s\W_]+', '-', s)
    # Rimuovi eventuali trattini multipli o trattini all'inizio/fine
    s = re.sub(r'^-+|-+$', '', s)
    return s if s else "unknown-event"

# Funzione per aggiornare il file M3U8
def update_m3u_file(video_streams, m3u_file="sportstreaming_playlist.m3u8"):
    REPO_PATH = os.getenv('GITHUB_WORKSPACE', '.')
    file_path = os.path.join(REPO_PATH, m3u_file)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")

        perma_count = 1

        for event_url, stream_url, formatted_date, event_title, league_info in video_streams:
            if not stream_url:
                continue

            # Determina se è un canale permanente o standard
            is_perma = "perma" in event_url.lower()
            if is_perma:
                image_url = f"https://sportstreaming.net/assets/img/live/perma/live{perma_count}.png"
                perma_count += 1
            else:
                # Estrai il numero dall'URL per i canali standard (es. live-3 -> 3)
                match = re.search(r'live-(\d+)', event_url)
                if match:
                    live_number = match.group(1)
                    image_url = f"https://sportstreaming.net/assets/img/live/standard/live{live_number}.png"
                else:
                    image_url = "https://sportstreaming.net/assets/img/live/standard/live1.png"  # Fallback

            # Determina il tvg-name e il nome visualizzato
            if is_perma:
                display_name = league_info if league_info and league_info != "Event" else event_title
            else:
                display_name = event_title
            
            if not display_name or display_name == "Unknown Event":
                display_name = "Evento" # Fallback

            tvg_id_generated = generate_clean_tvg_id(display_name)

            # Codifica gli header per l'URL
            encoded_ua = quote_plus(headers["User-Agent"])
            encoded_referer = quote_plus(headers["Referer"])
            encoded_origin = quote_plus(headers["Origin"])

            # Costruisci l'URL finale con il proxy e gli header
            # stream_url qui è l'URL originale dello stream (es. https://xuione.sportstreaming.net/...)
            final_stream_url = f"{PROXY_STREAM_PREFIX}{stream_url}&h_user-agent={encoded_ua}&h_referer={encoded_referer}&h_origin={encoded_origin}"

            f.write(f"#EXTINF:-1 group-title=\"SportStreaming\" tvg-logo=\"{image_url}\" tvg-id=\"{tvg_id_generated}\" tvg-name=\"{display_name}\",{display_name} (SpS)\n")
            f.write(f"{final_stream_url}\n")
            f.write("\n") # Aggiungi una riga vuota dopo ogni canale


    print(f"File M3U8 aggiornato con successo: {file_path}")

# Esegui lo script
if __name__ == "__main__":
    event_pages = find_event_pages()
    if not event_pages:
        print("Nessuna pagina evento trovata.")
    else:
        video_streams = []
        for event_url in event_pages:
            print(f"Analizzo: {event_url}")
            stream_url, formatted_date, event_title, league_info = get_event_details(event_url)
            if stream_url:
                video_streams.append((event_url, stream_url, formatted_date, event_title, league_info))
            else:
                print(f"Nessun flusso trovato per {event_url}")

        if video_streams:
            update_m3u_file(video_streams)
        else:
            print("Nessun flusso video trovato in tutte le pagine evento.")
