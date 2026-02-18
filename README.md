# installatie-handleiding-tool
Groepsopdracht: Markdown installatiehandleiding voor geselecteerde bio-informatica tools (BWA/SAMtools/BCFtools).
## Installatie van BWA 
Volg deze stappen om de nieuwste versie van BWA te downloaden en te installeren op je Linux-systeem:
### stap 1: BWA Downloaden
1. Ga naar de website: [https://github.com](https://github.com).
2. Klik op de groene knop **"Code"**.
3. Selecteer de optie **"Download ZIP"**.
4. Pak het bestand uit op je computer.
### Stap 2: BWA zip openen
1. **Open de terminal:** Navigeer naar de map waar je BWA hebt gedownload.
  ```bash
  cd bwa
  ` ` `
2. **Map openen en unzippen::** Gebruik het volgende commando:
  ```bash
  unzip bwa-master.zip
  cd bwa-master
  ```
### Stap 3: BWA Compileren
de software bouwen met het `make` commando

1. **Start de installatie:** Voer het volgende commando uit in de terminal:
   ```bash
   make
   ```
2. Controleer of de installatie is gelukt door de tool op te roepen:
  ```bash  
  ./bwa
   ```
### Stap 4: BWA toevoegen aan je PATH
Om BWA vanuit elke map in de terminal te kunnen aanroepen, voegen we de maplocatie toe aan je systeemvariabelen:
1. **Open je bash-configuratie:**
   ```bash
   nano ~/.bashrc
   ```
2. **Voeg het pad toe:** vervang */pad/naar/bwa-master* door de werkelijke locatie op jouw computer
  ```bash
  export PATH=$PATH:/pad/naar/bwa-master
3. **Opslaan en afsluiten:**
Druk op Ctrl + O (opslaan), dan Enter, en daarna op Ctrl + X (afsluiten).
4. **Activeer de wijzigingen:** voer je in de commandline uit:
  ```bash
  source ~/.bashrc
