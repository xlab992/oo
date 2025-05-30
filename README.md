# 📺 Script per Liste M3U Italiane Personalizzate 🇮🇹

Questo repository contiene script Python per generare automaticamente liste M3U di canali televisivi italiani, con un focus sugli eventi sportivi e la possibilità di utilizzare un proxy per una maggiore stabilità dei flussi.

Si possono utilizzare due proxy, proxydd,tvproxy e mediaflow proxy
per OMG consiglio Mediaflow, a breve uscirà una versione che consentirà di far partire anche i flussi HAT (H) e (Hd) e Thisnot (TN)

**Link ai proxy**
https://github.com/ciccioxm3/proxydd 
https://github.com/nzo66/tvproxy
seguire le info di installazione nel readme

https://github.com/mhdzumair/mediaflow-proxy


questo invece serve per i link mpd, va installato senza API_PASSWORD!
https://github.com/aleZZ2001/mediaflow-proxy

per far girare anche i link HAT andarà installata una versione diversa di Mediaflow, quando sarà disponibile aggiornerò il readme

## ✨ Liste M3U Disponibili

Una volta configurati ed eseguiti gli script e i workflow GitHub Actions, avrai a disposizione le seguenti liste:

*   🌍 **TUTTE le liste in un file solo:**
    *   `listone.m3u8`


      
*   🇮🇹 **Canali Italiani Generali da DaddyLive con Hattrick e Skystreaming:**
    *   `247ita.m3u8`
*   🇮🇹 **Canali Italiani Filtrati da Vavoo:**
    *   `channels_italy.m3u8`
*   ⚽ **Eventi Sportivi Maggiori (Misto ITA/Internazionale):**
    *   `itaevents.m3u8`
*   🏆 **Eventi Sportivi Maggiori (Solo Flussi Italiani):**
    *   `fullita.m3u8`
*   🌍 **TUTTI gli Eventi Sportivi (Molto Estesa):**
    *   `onlyevents.m3u8`
---

## 🛠️ Configurazione Iniziale degli Script

Prima di poter generare le liste, è necessario configurare alcuni parametri negli script Python.

### 1. Script Basati su DaddyLive

Modifica il file:
*   `.env`
  
    Descrizione del file
  ```python
#Ci sono 3 modi per vedere i canali, 
# 1) Daddy e Vavoo con Proxy nostro (TVproxy) https://github.com/nzo66/tvproxy e tutto il resto con MFP normale dal branch originale (in questo modo non funzionano gli mpd)
# per questo primo caso va compilata la variabile : PROXY 
# LASCIARE TUTTE LE ALTRE VARIABILI VUOTE TRANNE GUARCAL,DADDY,SKYSTR, HEADER, NOMEGITHUB e NOMEREPO TUTTE LE ALTRE SOLO ""   PER ESEMPIO MFPDD="" 
#
# 2) Tutto con 1 MFP con Password, non funzionano link MPD  https://github.com/mhdzumair/mediaflow-proxy
# per questo secondo caso compilare le variabili : MFPDD, MFPDD2, PROXYMFP, PSWMFP
# LASCIARE TUTTE LE ALTRE VARIABILI VUOTE TRANNE GUARCAL,DADDY,SKYSTR, HEADER, NOMEGITHUB e NOMEREPO TUTTE LE ALTRE SOLO ""   PER ESEMPIO PROXY="" 
#
# 3) Tutto con 1 MFP senza password, fork di https://github.com/aleZZ2001/mediaflow-proxy
# per questo secondo caso compilare le variabili : MFPDD, MFPDDNOPSW(lasciare stringa come la trovate, non serve inserire nulla), PROXYMFPNOPSW, PROXYMFPMPD
# LASCIARE TUTTE LE ALTRE VARIABILI VUOTE TRANNE GUARCAL,DADDY,SKYSTR, HEADER, NOMEGITHUB e NOMEREPO TUTTE LE ALTRE SOLO ""   PER ESEMPIO PROXY="" 



PROXY=""
#https://link.proxy.tvproxy/proxy/m3u?url=

MFPDD="https://link.proxy.mfp/extractor/video?host=DLHD&d=" 
#inserire link mfp

MFPDD2=""  
#inserire password, lasciare vuoto se si vuole usare mfp senza psw. altrimenti    
#&redirect_stream=true&api_password=PASSWORD

MFPDDNOPSW="&redirect_stream=true"
#se si usa mfp con psw lasciare vuoto

GUARCAL="sbs"  
#cambiare se non funzionano i loghi per la serie a verificare sito guardacalcio
DADDY="dad"   
#cambiare se daddylive cambka dominio 
SKYSTR="stream"  
#cambiate se skystreaming non prende piu nessun link 

PROXYMFP=""  
#inserire link e password solo per vavoo e skystreaming lasciare vuoto se si usa mfp senza psw altrimenti 
#https://link.proxy.mfp/proxy/hls/manifest.m3u8?api_password=PASSWORD&d=

PROXYMFPNOPSW="https://link.proxy.mfp/proxy/hls/manifest.m3u8?&d=" 
#inserire link, per mfp senza psw

PROXYMFPMPD="https://link.proxy.mpd/proxy/mpd/manifest.m3u8" 
# inserire link, serve solo ler mfp quindi hattrick link H e Hd

PSWMFP="PASSWORD"  
# password mfp per mpd hattrick 

HEADER="&h_user-agent=VAVOO/2.6&h_referer= https://vavoo.to/"

NOMEGITHUB=NOMEGIT   
#nome utente di git

NOMEREPO=NOMEREPO  
#nome repo di gir default OMGTV
  ```
  
  
## ⚙️ Configurazione e Esecuzione dei Workflow GitHub Actions
Dopo aver modificato e committato gli script sul tuo repository GitHub:

1. Vai alla sezione Actions del tuo repository: https://github.com/TUO_USER_GITHUB/NOME_TUO_REPOSITORY/actions (Sostituisci TUO_USER_GITHUB e NOME_TUO_REPOSITORY con i tuoi dati).
2. Se i workflow non sono attivi, abilitali.
3. Vai su Settings del tuo repository: https://github.com/TUO_USER_GITHUB/NOME_TUO_REPOSITORY/settings
4. Nel menu a sinistra, clicca su Actions e poi su General .
5. Scorri fino alla sezione "Workflow permissions".
6. Seleziona l'opzione Read and write permissions .
7. Clicca su Save.

   
### Esecuzione dei Workflow (solo la prima volta, poi va in automatico)
### RINOMINA FILEmpd.m3u8 in mpd.m3u8 
Torna alla sezione Actions . 

Esegui i workflow nel seguente ordine:

1. 🚀 1 Update 24 7 :
   - Clicca sul nome del workflow.
   - Sulla destra, clicca su "Run workflow".
   - Conferma cliccando sul pulsante verde "Run workflow".
2. 🚀 2 Update hat :
   - Clicca sul nome del workflow.
   - Sulla destra, clicca su "Run workflow".
   - Conferma cliccando sul pulsante verde "Run workflow".
3. 🚀 3 Update skystreaming :
   - Clicca sul nome del workflow.
   - Sulla destra, clicca su "Run workflow".
   - Conferma cliccando sul pulsante verde "Run workflow".
4. 🚀 3.5 Update thisnot :
   - Clicca sul nome del workflow.
   - Sulla destra, clicca su "Run workflow".
   - Conferma cliccando sul pulsante verde "Run workflow".
5. 🚀 4 Update SportZone Scraper :
   - Clicca sul nome del workflow.
   - Sulla destra, clicca su "Run workflow".
   - Conferma cliccando sul pulsante verde "Run workflow".
3. 🚀 5 Update SportStreaming Scraper :
   - Clicca sul nome del workflow.
   - Sulla destra, clicca su "Run workflow".
   - Conferma cliccando sul pulsante verde "Run workflow".
6. 🚀 6 Update top1 Scraper :
   - Clicca sul nome del workflow.
   - Sulla destra, clicca su "Run workflow".
   - Conferma cliccando sul pulsante verde "Run workflow".
7. 🚀 7 Update itaEvents :
   - Clicca sul nome del workflow.
   - Sulla destra, clicca su "Run workflow".
   - Conferma cliccando sul pulsante verde "Run workflow".
8. ⏳ ATTENDI IL COMPLETAMENTO del workflow precedente (deve apparire una spunta verde ✅).

     
9. (Opzionale) 🌍1 Update OnlyEvents :
   - Se desideri la lista con TUTTI gli eventi sportivi (molto estesa e potenzialmente con sport di nicchia), esegui anche questo workflow dopo il completamento degli altri.
Attendi che tutti i workflow selezionati abbiano una spunta verde ✅. Questo indica che le liste M3U sono state generate e aggiornate nel tuo repository.

Per i giorni a seguire non serve fare nulla, partono in automatico, mettere l'aggiornamento delle playlist su OMG ogni ora


## 🔗 Usare la lista con OMG
Per utilizzare le liste generate basta andare ad inserire il link raw del file listone.m3u8

   
## 🔌 Utilizzo con OMG (o altre applicazioni)
1. Apri la tua applicazione (es. OMG).
2. Nel campo per l'inserimento dell'URL della lista M3U, incolla l'indirizzo link Raw di listone.m3u8.
3. Abilita l'opzione per l'EPG senza link.
5. Procedi con la generazione della configurazione o l'installazione dell'addon, come richiesto dalla tua applicazione.
🎉 Fatto! Ora dovresti avere accesso ai canali tramite le tue liste M3U personalizzate e auto-aggiornate.
