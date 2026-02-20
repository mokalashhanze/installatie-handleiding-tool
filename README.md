# Istallatie-handleiding-tool
Groepsopdracht: Markdown installatiehandleiding voor geselecteerde bio-informatica tools (BWA/SAMtools/BCFtools).
## Installatie van bwa-mem2 
Volg deze stappen om de nieuwste versie van ***bwa-mem2*** te downloaden en te installeren op je Linux-systeem:
### Stap 1: bwa-mem2 Downloaden
1. Ga naar de website: [ https://github.com/bwa-mem2/bwa-mem2/releases ]( https://github.com/bwa-mem2/bwa-mem2/releases )
2. Klik op **bwa-mem2-2.3_x64-linux.tar.bz2**.
3. verplaats de bestand naar de goede folder
### Stap 2: bwa-mem2 bestand uitpakken 
1. **Open de terminal:** Navigeer naar de map waar je **BWA-mem2** hebt verplaats.
2. Gebruik het **tar** commando om het gecomprimeerde bestand te openen:
   ```
      tar xf bwa-mem2-2.3_x64-linux.tar.bz2
   ```
### Stap 3: bwa-mem2 toevoegen aan je PATH
Om BWA vanuit elke map in de terminal te kunnen aanroepen, moet je deze stappen volgen
1. **Open je bash-configuratie:**
   ```
     nano ~/.bashrc
   ```
2. **Voeg het pad toe:** vervang */pad/naar/bwa-mem2-2.3_x64-linux.tar.bz2* door de werkelijke locatie op jouw computer
   ```
      export PATH="/pad/naar/bwa-mem2-2.3_x64-linux.tar.bz2:$PATH"
   ```
3. **Opslaan en afsluiten:**
Druk op Ctrl + O (opslaan), dan Enter, en daarna op Ctrl + X (afsluiten).
4. **Activeer de wijzigingen:** voer je in de commandline uit:
   ```
      source ~/.bashrc
   ```
### Stap 4: Controleer of de installatie gelukt is door de tool op te roepen:
   ```
      bwa-mem2
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
   1. Gebruik het **configure**,**make** en **make install** commando om Samtools te installeren
   ```
      ./configure
      make
      make install
   ```
   2. Controleer of de installatie gelukt is door de tool op te roepen:
   ```  
      ./Samtools
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
   1. Gebruik het **configure**,**make** en **make install** commando om Samtools te installeren
   ```
      ./configure
      make
      make install
   ```
   2. Controleer of de installatie gelukt is door de tool op te roepen:
   ```  
      ./Bcftools
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







