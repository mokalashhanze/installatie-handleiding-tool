# Istallatie-handleiding-tool
Groepsopdracht: Markdown installatiehandleiding voor geselecteerde bio-informatica tools (BWA/SAMtools/BCFtools).
## Installatie van bwa-mem2 
Volg deze stappen om de nieuwste versie van ***bwa-mem2*** te downloaden en te installeren op je Linux-systeem:
### Stap 1: bwa-mem2 Downloaden
1. Ga naar de website: [https://github.com/bwa-mem2/bwa-mem2](https://github.com/bwa-mem2/bwa-mem2)
2. Klik op de groene knop **"Code"**.
3. Selecteer de optie **"Download ZIP"**.
4. Pak het bestand uit op je computer.
### Stap 2: bwa-mem2 zip openen
1. **Open de terminal:** Navigeer naar de map waar je BWA hebt gedownload.
2. **Map openen en unzippen::** Gebruik het volgende commando:
   ```
      unzip cd bwa-mem2-master
      cd cd bwa-mem2-master
   ```
### Stap 3: bwa-mem2 Compileren
de software bouwen met het `make` commando

1. **Start de installatie:** Voer het volgende commando uit in de terminal:
   ```
     make
   ```
2. Controleer of de installatie gelukt is door de tool op te roepen:
   ```  
      ./bwa-mem2
   ```
### Stap 4: bwa-mem2 toevoegen aan je PATH
Om BWA vanuit elke map in de terminal te kunnen aanroepen, moet je deze stappen volgen
1. **Open je bash-configuratie:**
   ```
     nano ~/.bashrc
   ```
2. **Voeg het pad toe:** vervang */pad/naar/bwa-mem2-master* door de werkelijke locatie op jouw computer
   ```
      export PATH="/pad/naar/bwa-mem2-master:$PATH"
   ```
3. **Opslaan en afsluiten:**
Druk op Ctrl + O (opslaan), dan Enter, en daarna op Ctrl + X (afsluiten).
4. **Activeer de wijzigingen:** voer je in de commandline uit:
   ```
      source ~/.bashrc
   ```
## Installatie van Samtools:
Volg deze stappen om de nieuwste versie van ***Samtools*** te downloaden en te installeren op je Linux-systeem:
### Stap 1: Samtools downloaden
1. Ga naar de website [https://www.htslib.org/download/](https://www.htslib.org/download/)
2. klik op de groene knop **"Samtools-1.23"**
3. pak het bestaand uit op je computer
### Stap 2: Samtools bestand uitpakken en openen
1. **Open de terminal:** Navigeer naar de map waar je **Samtools** hebt gedownload.
2. Gebruik het **tar** commando om het gecomprimeerde bestand te openen:
   ```
      tar xf samtools-1.23.tar.bz2
      cd samtools-1.23
   ```
### Stap 3: Samtools installeren:
Gebruik het **configure**,**make** en **make install** commando om Samtools te installeren
   ```
      ./configure
      make
      make install
   ```
### Stap 4: Samtools toevoegen aan je PATH
Om Samtools vanuit elke map in de terminal te kunnen aanroepen, moet je deze stappen volgen
1. **Open je bash-configuratie:**
   ```
      nano ~/.bashrc
   ```
2. **Voeg het pad toe:** vervang */pad/naar/samtools-1.23* door de werkelijke locatie op jouw computer
   ```
      export PATH="/pad/naar/samtools-1.23:$PATH"
   ```
3. **Opslaan en afsluiten:**
Druk op Ctrl + O (opslaan), dan Enter, en daarna op Ctrl + X (afsluiten).
4. **Activeer de wijzigingen:** voer je in de commandline uit:
   ```
      source ~/.bashrc
   ```
## Installatie van BCFtools:
Volg deze stappen om de nieuwste versie van ***Bcftools*** te downloaden en te installeren op je Linux-systeem:
### Stap 1: Bcftools downloaden
1. Ga naar de website: [https://www.htslib.org/download/](https://www.htslib.org/download/)
2. klik op de groene knop **"Bcftools-1.23"**
3. pak het bestaand uit op je computer
### Stap 2: Bcftools bestand uipakken en openen:
1. **Open de terminal:** Navigeer naar de map waar je **Bcftools** hebt gedownload.
2. Gebruik het **tar** commando om het gecomprimeerde bestand te openen:
   ```
      tar xf bcftools-1.23.tar.bz2
      cd bcftools-1.23
   ```
### Stap3: Bcftools installeren
Gebruik het **configure**,**make** en **make install** commando om Samtools te installeren
   ```
      ./configure
      make
      make install
   ```
### Stap 4: Bcftools toevoegen aan je PATH
Om Bcftools vanuit elke map in de terminal te kunnen aanroepen, moet je deze stappen volgen
1. **Open je bash-configuratie:**
   ```
      nano ~/.bashrc
   ```
2. **Voeg het pad toe:** vervang */pad/naar/bcftools-1.23* door de werkelijke locatie op jouw computer
   ```
      export PATH="/pad/naar/bcftools-1.23:$PATH"
   ```
3. **Opslaan en afsluiten:**
Druk op Ctrl + O (opslaan), dan Enter, en daarna op Ctrl + X (afsluiten).
4. **Activeer de wijzigingen:** voer je in de commandline uit:
   ```
      source ~/.bashrc
   ```







