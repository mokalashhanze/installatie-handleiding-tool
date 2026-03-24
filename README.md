# Pijplijn:Het identificeren van mutaties
Moderne DNA-sequencers genereren enorm veel ruwe data ("raw reads", van 300 kilobases tot enkele terabases per run)1. Deze data zijn voor mensen moeilijk te gebruiken door de grote hoeveelheid en doordat er niet altijd bekend is waar deze data zich in het genoom bevindt. Om de aanwezigheid van mutaties te bepalen is dat wel nodige informatie. Met onze eerste tool BWA-mem2 (https://github.com/bwa-mem2/bwa-mem2) gaan wij de data mappen/uitlijnen tegenover een referentiegenoom zoals het menselijk genoom. Hiermee kunnen we achterhalen waar de DNA-sequenties vandaan komen. Daarna verwerken we de uitlijning van BWA met Samtools (https://www.htslib.org/download/) die maakt van een groot tekstbestand (SAM) een klein computerbestand (BAM) om ruimte te besparen. Hierna gaan we met BCFTools (https://www.htslib.org/download/) kijken of er mutaties zijn opgetreden.  
Na deze stappen kan er worden gekeken of er bijvoorbeeld mutaties zijn in het genoom van een patiënt.
## Onderzoeksvraag: 
Welke specifieke mutaties heeft een individu ten opzichte van het menselijk referentiegenoom? In welke genen zitten de mutaties?  

# Installatie-handleiding-tool
Groepsopdracht: Markdown installatiehandleiding voor geselecteerde bio-informatica tools (bwa-mem2/SAMtools/BCFtools).
## Bwa-mem2 
Het pakt losse stukjes DNA en zoekt voor elk stukje de juiste plek op een grote kaart van het genoom.
## Installatie:
Volg deze stappen om de nieuwste versie van ***bwa-mem2*** te downloaden en te installeren op je Linux-systeem:
### Stap 1: bwa-mem2 Downloaden
1. Ga naar de website: [ https://github.com/bwa-mem2/bwa-mem2/releases ]( https://github.com/bwa-mem2/bwa-mem2/releases )
2. Klik op **bwa-mem2-2.3_x64-linux.tar.bz2**.
3. verplaats de bestand naar je eigen werk folder
### Stap 2: bwa-mem2 bestand uitpakken en openen
1. **Open de terminal:** Navigeer naar de map waar je **BWA-mem2** hebt verplaats.
2. Gebruik het **tar** commando om het gecomprimeerde bestand te openen:
   ```
      tar xf bwa-mem2-2.3_x64-linux.tar.bz2
      cd bwa-mem2-2.3_x64-linux
      
   ```
### Stap 3: bwa-mem2 toevoegen aan je PATH
Om BWA-mem2 vanuit elke map in de terminal te kunnen aanroepen, moet je deze stappen volgen
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
## Samtools:
Hij zet alle losse stukjes DNA op de juiste volgorde en ruimt de data netjes op zodat de computer het sneller kan lezen.
## Installatie:
Volg deze stappen om de nieuwste versie van ***Samtools*** te downloaden en te installeren op je Linux-systeem:
### Stap 1: Samtools downloaden
1. Ga naar de website [https://www.htslib.org/download/](https://www.htslib.org/download/)
2. klik op de groene knop **"Samtools-1.23"**
3. verplaats de bestand naar je eigen werk folder
### Stap 2: Samtools bestand uitpakken en openen
1. **Open de terminal:** Navigeer naar de map waar je **Samtools** hebt verplaats.
2. Gebruik het **tar** commando om het gecomprimeerde bestand te openen:
   ```
      tar xf samtools-1.23.tar.bz2
      cd samtools-1.23
   ```
### Stap 3: Samtools installeren:
   1. Gebruik het **configure**,**make** en **make install** commando om Samtools te installeren
   ```
      ./configure prefix=--/pad/naar/samtools-1.23
      make
      make install
   ```
      pass **-/pad/naar/samtools-1.23** naar je eigen werk plek aan
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
## BCFtools:
Hij vergelijkt DNA-stukjes om mutaties te laten zien 
## Installatie:
Volg deze stappen om de nieuwste versie van ***Bcftools*** te downloaden en te installeren op je Linux-systeem:
### Stap 1: Bcftools downloaden
1. Ga naar de website: [https://www.htslib.org/download/](https://www.htslib.org/download/)
2. klik op de groene knop **"Bcftools-1.23"**
3. verplaats de bestand naar je eigen werk folder
### Stap 2: Bcftools bestand uipakken en openen:
1. **Open de terminal:** Navigeer naar de map waar je **Bcftools** hebt verplaats.
2. Gebruik het **tar** commando om het gecomprimeerde bestand te openen:
   ```
      tar xf bcftools-1.23.tar.bz2
      cd bcftools-1.23
   ```
### Stap3: Bcftools installeren
   1. Gebruik het **configure**,**make** en **make install** commando om Samtools te installeren
   ```
      ./configure prefix=--/pad/naar/bcftools-1.23
      make
      make install
   ```
      pass **/pad/naar/bcftools-1.23** naar je eigen werk plek aan
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
### referenties:
1. Bwa.mem2:[bwa.mem](https://bio-bwa.sourceforge.net/)
2. Samtools [Samtools](https://samtools.sourceforge.net/)
3. Bcftools: [Bcftools](https://www.hpc.cineca.it/systems/software/bcftools/)
