# 📺 Script per Liste M3U Italiane Personalizzate 🇮🇹

Questo repository contiene script Python per generare automaticamente liste M3U di canali televisivi italiani, con un focus sugli eventi sportivi e la possibilità di utilizzare un proxy per una maggiore stabilità dei flussi.

Si possono utilizzare due proxy, proxydd,tvproxy e mediaflow proxy
per OMG consiglio Mediaflow, a breve uscirà una versione che consentirà di far partire anche i flussi HAT.

**Link ai proxy**
https://github.com/ciccioxm3/proxydd 
https://github.com/nzo66/tvproxy
seguire le info di installazione nel readme

https://github.com/mhdzumair/mediaflow-proxy

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
*   Descrizione del file
  ```python
#lasciare vuoto proxy e inserire mfpdd e mfpdd2 se si vuole tutto su mfp, altrimenti vuoto mfpdd e mfpdd2 con link proxy propolato
PROXY=""
#https://link.proxy.tvproxy**/proxy/m3u?url=  
MFPDD="link.proxy.mfp/extractor/video?host=DLHD&d=" 
#inserire link mfp
MFPDD2="&redirect_stream=true&api_password=PASSWORD"  
#inserire password
GUARCAL="sbs"  
#cambiare se non funzionano i loghi per la serie a verificare sito guardacalcio
DADDY="dad"   
#cambiare se daddylive cambka dominio 
SKYSTR="stream"  
#cambiate se slystreaming non prende piu nessun link 
PROXYMFP="link.proxy.mfp/proxy/hls/manifest.m3u8?api_password=PASSWORD&d="  
#inserire link e password solo per vavoo e skystreaming
PROXYMFPMPD="link.proxy.mpd/proxy/mpd/manifest.m3u8" 
# inserire link, serve solo ler mfp quindi hattrick link H e Hd
PSWMFP="PASSWORD"  
# password mfp per mpd hattrick 
HEADER="&h_user-agent=VAVOO/2.6&h_referer= https://vavoo.to/"
NOMEGITHUB=NOMEGIT   
#nome utente di git
NOMEREPO=NOMEREPO  
#nome repo di gir default OMGTV
  ```
All'interno di ciascuno di questi file, individua e modifica la riga seguente:

```python
Daddy
PRXLINK = "inserisci il tuo link proxy senza / finale"
```

  
### 2. Script Basato su Vavoo
Modifica lo script:

- vavoo.py
All'interno di questo file, individua e modifica le seguenti righe:

```python
Vavoo
USREPG = "inserisci il nome del tuo account github"
BRANCHEPG = "inserisci il nome del tuo fork"
MFPLINK = "inserisci url del tuo mfp (sempre formato embed)"     # non mettere lo / finale al link
MFPPSW = "inserisci password del tuo mfp"
```

### 3. Script Basato su Hattr1ck

Modifica lo script:

- hat.py
All'interno di questo file, individua e modifica le seguenti righe:

```python
MFPLINK = "inserisci url del tuo mfp (sempre formato embed)"     # non mettere lo / finale al link
```

  
## ⚙️ Configurazione e Esecuzione dei Workflow GitHub Actions
Dopo aver modificato e committato gli script sul tuo repository GitHub:

1. Vai alla sezione Actions del tuo repository: https://github.com/TUO_USER_GITHUB/NOME_TUO_REPOSITORY/actions (Sostituisci TUO_USER_GITHUB e NOME_TUO_REPOSITORY con i tuoi dati).
2. Se i workflow non sono attivi, abilitali.
3. Vai su Settings del tuo repository: https://github.com/TUO_USER_GITHUB/NOME_TUO_REPOSITORY/settings
4. Nel menu a sinistra, clicca su Actions e poi su General .
5. Scorri fino alla sezione "Workflow permissions".
6. Seleziona l'opzione Read and write permissions .
7. Clicca su Save .

   
### Esecuzione dei Workflow
Torna alla sezione Actions . Esegui i workflow nel seguente ordine:

1. 🚀 Update 24 7 VV DD ita and world :
   - Clicca sul nome del workflow.
   - Sulla destra, clicca su "Run workflow".
   - Conferma cliccando sul pulsante verde "Run workflow".
2. ⏳ ATTENDI IL COMPLETAMENTO del workflow precedente (deve apparire una spunta verde ✅).
3. ⚽ Update itaEvents :
   - Stesso procedimento del workflow precedente.
     
4. (Opzionale) 🌍 Update OnlyEvents :
   - Se desideri la lista con TUTTI gli eventi sportivi (molto estesa e potenzialmente con sport di nicchia), esegui anche questo workflow dopo il completamento degli altri.
Attendi che tutti i workflow selezionati abbiano una spunta verde ✅. Questo indica che le liste M3U sono state generate e aggiornate nel tuo repository.

## 🔗 Usare la lista con OMG
Per utilizzare le liste generate basta andare ad inserire il link raw del file listone.m3u8

## 🔗 Creare una Lista M3U Unica con GitHub Gist
Per utilizzare facilmente le tue liste M3U generate (ad esempio con l'applicazione OMG), puoi raggrupparle in un unico file Gist:

1. Vai su GitHub Gist https://gist.github.com/ 
2. Nel campo "Gist description...", inserisci un nome, ad esempio: Le mie liste M3U .
3. Nel campo "Filename including extension...", inserisci: liste.m3u (o lista.txt , l'importante è che sia un file di testo).
4. Nel box di testo principale, incolla gli URL diretti (RAW) delle liste M3U generate nel tuo repository. Assicurati di sostituire TUO_USER_GITHUB e TUO_BRANCH_GITHUB con i tuoi dati:
   
   ```python
   https://raw.githubusercontent.com/TUO_USER_GITHUB/NOME_TUO_REPOSITORY/refs/heads/TUO_BRANCH_GITHUB/channels_italy.m3u8
   
   https://raw.githubusercontent.com/TUO_USER_GITHUB/NOME_TUO_REPOSITORY/refs/heads/TUO_BRANCH_GITHUB/247ita.m3u8
   
   https://raw.githubusercontent.com/TUO_USER_GITHUB/NOME_TUO_REPOSITORY/refs/heads/TUO_BRANCH_GITHUB/itaevents.m3u8
   
   # Puoi aggiungere anche altre liste statiche
   
   se lo desideri, ad esempio:

   https://tivustream.website/ios/tivustream_list.m3u

   - Nota: Se preferisci la lista con TUTTI gli eventi, sostituisci itaevents.m3u8 con onlyevents.m3u8 .
     ```
   
5. Clicca sul pulsante verde Create secret gist (o Create public gist se preferisci).
6. Nella pagina del Gist appena creato, cerca il pulsante Raw in alto a destra.
7. Fai click con il tasto destro del mouse su Raw e seleziona "Copia indirizzo link". Questo è l'URL diretto al tuo Gist contenente tutte le liste.

   
## 🔌 Utilizzo con OMG (o altre applicazioni)
1. Apri la tua applicazione (es. OMG).
2. Nel campo per l'inserimento dell'URL della lista M3U, incolla l'indirizzo link del Raw Gist che hai copiato al passaggio precedente.
3. Abilita l'opzione per l'EPG senza link. **(per avere l'epg bisogna per forza avere la lista channels_italy.m3u8 in prima posizione nel file raw)**
5. Procedi con la generazione della configurazione o l'installazione dell'addon, come richiesto dalla tua applicazione.
🎉 Fatto! Ora dovresti avere accesso ai canali tramite le tue liste M3U personalizzate e auto-aggiornate.
