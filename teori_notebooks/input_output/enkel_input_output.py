#!/usr/bin/env python
# coding: utf-8

# # Input og output fra programmer

# Vi skal først se på hvordan vi kan skrive noen enkle programmer som leser inn input fra brukeren,
# gjør noe med denne inputen, og skriver noe ut igjen til brukeren.
# 
# Vi starter med det aller enkleste, klassiske første programmet, nemlig et program som skriver
# "hello, world!" ut til brukeren når programmet kjøres.

# ## Hello, World!
# Dette programmet skriver ut teksten "Hello, world!" ut til brukeren. Prøv å forandre på teksten å se hva som skjer.

# In[1]:


print("Hello, world!")


# ### kort "obduksjon" av programmet
# Programmet sender inn en *streng* `"Hello, world!"` til *funksjonen* `print`.
# Funksjonen `print` virker som et bindeledd mellom programmet og `standard output`.
# I mer avanserte anvendelser kan det være hendig å endre på denne - men vanligvis
# er det greit å bruke `print` til å skrive tekst ut til kommandolinjen eller slik du ser her
# 
# 
# 
# 
# 
# 
# 

# ### Konsepter

# #### Datatypen streng
# Du har møtt på datatypen `str`. En streng i python kan du tenke på som tekst. Husk at for
# en datamaskin er det bare en remse med bokstaver - helt i bunnen er det en remse med bytes.
# Teksten 'Hello, world!" er for eksempel følgende remse med bytes:
#  
# 
# `01001000 01100101 01101100 01101100 01101111 0101100 00100000 01110111 01101111 01110010 01101100 01100100 00100001`
# 
# Som du kanskje synes, er det ikke spesielt lesbart. Derfor er det skrevet programmer som gjør dette om til tekst du kan
# lese, uten at du trenger å tenke noe på hvordan programmet fungerer. Du trenger vanligvis ikke tenke på at programmet en gang
# eksisterer. Dette kalles i informatikken for *abstraksjon*, og er et viktig konsept vi kommer tilbake til senere.

# #### Orienteringsstoff om strenger og utf8-encoding
# Standarden utf-8 bruker én byte for de fleste vanlige tegn. For nordiske tegn bruker den to bytes, og for mange spesielle tegn kan den bruke tre eller fire bytes.
# 
# I tabellen under ser du noen eksempler med bytene representert som binære tall.
# 
# 
# |  bokstav   |  byte nummer 1 |  byte nummer 2 | byte nummer 3  | byte nummer 4 |
# |------------|----------------|----------------|------------ ---|---------------|
# |   a        |  0b1100001     |                |                |               |
# |   b        |  0b1100010     |                |                |               |
# |   c        |  0b1100011     |                |                |               |
# |   ä        |  0b11000011    |  0b10100100    |                |               |
# |   æ        |  0b11000011    |  0b10100110    |                |               |
# |   ø        |  0b11000011    |  0b10111000    |                |               |
# |   å        |  0b11000011    |  0b10100101    |                |               |
# |   à        |  0b11000011    |  0b10100000    |                |               |
# |   â        |  0b11000011    |  0b10100010    |                |               |
# |   π        |  0b11001111    |  0b10000000    |                |               |
# |   ℵ        |  0b11100010    |  0b10000100    |  0b10110101    |               |
# |   ∇        |  0b11100010    |  0b10001000    |  0b10000111    |               |
# |   𣴯       |  0b11110000    |  0b10100011    |  0b10110100    |  0b10101111  |
# 

# #### Funksjoner
# Du har møtt din første funksjon, nemlig `print`. Funksjonen `print` tar inn en streng og skriver det ut til kommandolinjen/under cellen.
# Funksjoner generelt i python tar inn en verdi og gjør noe med eller noe som avhenger av disse verdiene.
# 
# Remsen med bytes for å representere strengen  `Hello, world!` generertm med programmet under. Ikke bruk tid på å gruble over koden enda, du vil om tid og stunder forstå helt greit hva som står her.

# In[2]:


# generer bytes for tegnene i strengen 'Hello, world!' slik de samsvarer i standarden utf8
for byte in map(bin, bytearray('Hello, world!', 'utf8')):
    print(byte, end=" ")


# ### Lese input fra bruker
# Vi kan bruke kommandoen `input` til å lese input fra en bruker.
# Under ser du et eksempel

# In[3]:


# les input fra bruker og skriv ut en hilsen me brukerens navn
name = input('Hva er navnet ditt? Skriv her: ')
print("Hallo " + name + "!" )


# ### Kort obduksjon
# Programmet ignorerer teksten bak tegnet `#`. Teksten bak dette tegnet er en kommentar for
# å gjøre koden lettere å lese for mennesker.
# 
# Programmet kaller på en funksjon `input`.
# Argumentet til `input` er strengen `Hva er navnet ditt? Skriv her: \`. Denne strengen blir skrevet ut til kommandolinje / under cellen. Poenget med denne beskjeden er å informere brukeren om hva slags input som skal skrives inn.
# Deretter lagres det brukeren mater inn i programmet fra kommandolinjen i *variabelen* `name`.

# ### Flere konsepter

# #### Variabler
# En variabel i Python kan du tenke på som navnet på en adresse i minnet til datamaskinen. Å lagre data i variabler gjør koden enklere å lese, og vi kan kombinere dataene med andre data på mange ulike måter.
# 
# Legg til deg gode vaner, og start å bruke variabler allerede nå!

# Store programmer kan være vanskelige å lese. For å gjøre programmene mer lesbare, er det viktig at du lager *beskrivende* navn til variablene dine. Dersom variabelen inneholder navnet til en kunde, kan den f.eks hete `navn`, men et enda bedre navn er da `kunde_navn`.
# 
# **NB!** Et lite aber er når vi jobber med matematikk - da ønsker vi å velge variablene slik at koden minner mest mulig om de matematiske utrykkene.

# #### Kommentarer
# Kommentarer i python starter med tegnet `#`. Kommentarene blir ikke kjørt som kode,
# men ignorert av datamaksinen når du kjører programmet.
# De gjør det lettere å forstå koden!
# Dersom kommentaren skal gå over flere linjer, bruker vi en såkalt doc-string. Du
# kan skrive dem med tredoble anførselstegn (dobbel x3 `"""` eller enkel x3 `'''`).

# Du kan bruke kommentarer til å holde orden på enheter, og fortelle i korte trekk hva
# en samling kommandoer skal gjøre. Skriv heller for mye kommandoer enn for få! Det er
# aldri et problem at kode er *for godt dokumentert*. Blir dokumentasjonen for lang, har de fleste *editorer* der koden skrives funksjonalitet for å "kollapse" tekst slik at du ikke trenger å bla i teksten, men kan åpne det du trenger å se.
# En svært vanlig "nybegynnerfeil" er å slurve med kommentarer, for deretter å bruke lang tid på å forstå egen kode noen dager eller uker senere. Å skrive gode kommentarer er en ferdighet på lik linje med selve programmeringen, og blir svært viktig når man arbeider i team med andre mennesker.

# Under ser du et eksempel på kode der vi har skrevet en del kommentarer
# Prøv å bruke kommentarene til å forstå hva koden gjør i hvert steg.
# Som du ser blir ikke tabellen helt "fint" formatert. Vi skal senere se på
# hvordan dette kan gjøres.

# In[46]:


"""
Dette programmet viser noen egenskaper ved strenger:
Hvis vi multipliserer en streng med et heltall n, gjentas strengen n antall ganger.
Når to strenger a og b legges sammen, føyes teksten i b på teksten i a.
For eksempel blir 'Martin' + ' Andersen' til strengen 'Martin Andersen'

Koden skriver ut en tabell med fornavn, telefonnummer og adresse
"""

n = 10 # antall mellomrom
mellomrom = "  "*n

# Tabelloverskrifter
tlf = "Telefon"
adr = "Adresse"
nvn = "Navn"

# Innhold i tabellen.
# Merk at etter semikolon kan en ny kommando skrives uten å starte en ny linje
navn1 = "Kåre"; telefon1 = "91248953"; adresse1 = "Pøbelringen 5"
navn2 = "Marie"; telefon2 = "39025847"; adresse2 = "John Tullings Gate 10"

print(nvn + mellomrom + tlf + mellomrom + adr) # tabelloverskrifter
print('--'*35)
print(navn1 + mellomrom + telefon1 + mellomrom + adresse1)
print(navn2 + mellomrom + telefon2 + mellomrom + adresse2)


# #### Minne på datamaskinen
# Det kan være lurt å tenke på minnet i datamaskinen som en lang remse med hus som hver inneholder 8 bokser. I hver av disse boksene kan vi sette enten verdien 0 eller 1. Vi kaller disse verdiene **bits**
# 
# Et hus er da en **byte**, og vi kan tenke på navnet til en variabel som adressen til huset. Nå er det ikke likevel alltid helt *så* enkelt, da vi for eksempel trenger åtte bytes for å representere for eksempel et flyttall. Men så lenge disse ligger inntil og i en bestemt retning fra vår adresse, går dette helt greit!

# Bits i minnet til datamaskinen representert ved at en transistor styrer strøm til en kondensator. Ved å måle spenningen over kondensatoren vet man om transistoren er slått "av eller på", og dermed kan man lese av verdien 1 når spenningen er over 50% av en "maksverdi", og 0 ellers.
# Du kan lese mer her: [https://computer.howstuffworks.com/ram.htm](https://computer.howstuffworks.com/ram.htm "https://computer.howstuffworks.com/ram.htm").

# ## Bruk av ipython som en kalkulator
# Vi kan bruke ipyhon som en kalkulator. Hvis du har en åpen terminal, kan du skrive inn kommandoen `ipython`.
# Da får du noe som ser ut som i kodesnutten under
# Ofte ønsker vi å bruke matematiske funksjoner som ikke er med i python fra før. Da må vi importere dem. Det
# kan vi gjøre med kommandoen `from pylab import *`. Vi importerer da alle kommandoer fra pakken `pylab`.

# ### Eksempel
# Under har vi regnet ut verdien av utrykket $$ 5\sqrt{2} + \left(\frac{3}{4}\right)^2.$$
# 
# ```
# In [1]: from pylab import *
# 
# In [2]: 5*sqrt(2) + (3/4)**2
# Out[2]: 7.6335678118654755
# 
# In [3]: pi
# Out[3]: 3.141592653589793
# ```

# In[4]:


from pylab import *
5*sqrt(2) + (3/4)**2


# #### Oppgave 1
# Regn ut følgende verdier med python eller ipython
# 
# * `sqrt(3)`
# * `log10(10)`
# * `log10(1)`
# * `2*pi`

# #### Oppgave 2
# 
# ##### a)
# Hva gjør koden under?
# 
# ```
# In [1]: from pylab import *
# 
# In [2]: rad2deg(2*pi)
# Out[2]: 360.0
# 
# In [3]: rad2deg(3*pi)
# Out[3]: 540.0
# 
# In [4]: rad2deg(pi)
# Out[4]: 180.0
# 
# In [5]: rad2deg(pi/2)
# Out[5]: 90.0
# 
# In [6]: rad2deg(pi/4)
# Out[6]: 45.0
# 
# In [7]: rad2deg(0)
# Out[7]: 0.0
# ```
# 
# ##### b)
# Hva tror du `rad2deg(pi/3)` vil gi ut?
# Du kan bruke cellen under eller i en egen ipython-terminal til å sjekke svaret ditt.

# In[ ]:


from pylab import *


# #### Oppgave 2
# 
# ##### a)
# Regn ut `deg2rad(0)` og `deg2rad(180)`
# 
# ---------
# 
# Hvis vi gir grader som input til trigonometriske funksjoner i python, får vi ikke riktig svar:
# ```
# In [2]: from pylab import *
# In [2]: sin(180)
# Out[2]: -0.8011526357338304
# ```
# 
# Hvis vi bruker funksjonen `deg2rad` på gradene slik at vi får vinkelen i radianer, går det bra.
# 
# ##### b)
# Bruk funksjonen `deg2rad` og regn ut to eller flere av verdiene under
# 
# \begin{align}
# \sin(30°) \\[1.1em]
# \sin(45°) - \frac{\sqrt2}{2} \label{exact1} \\[1.1em]
# \sin(60°) - \frac{\sqrt3}{2} \label{exact2} \\[1.1em]
# \sin(90°) \\[1.1em]
# \end{align}
# 

# #### Sammensatte utrykk
# Regn ut verdien av utrykket $$E = gv^n + \frac{b}{|u - w| + 1},$$ 
# 
# for $g = 14000$, $v = 1.0275$, $n=20$ og $b=2.3\cdot10^{4}$.

# I eksempelet under har vi definert tre variable `g`, `v`, `n`, og `b`. Vi gjør noen beregninger med disse og lagrer dem inn i variabelen `E`. 
# 
# ```
# Python 3.6.7 (default, Jul  2 2019, 02:21:41) [MSC v.1900 64 bit (AMD64)]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 7.8.0 -- An enhanced Interactive Python. Type '?' for help.
# 
# In [1]: g = 14000
# 
# In [2]: v = 1.0275
# 
# In [3]: n = 20
# 
# In [4]: b = 2.3E4
# 
# In [5]: u = 45
# 
# In [6]: w = 36
# 
# In [7]: E = g*v**n + b/(abs(u - w) + 1)
# 
# In [8]: E
# Out[8]: 26385.99803800328
# ```

# Hvis du jobber i en notebook, kan du gjøre slike interaktive beregninger i en kode-celle. Prøv deg på noen av oppgavene under

# -------------------------
# #### Oppgave 3
# I denne oppgaven undersøker vi hva funksjonen `abs` gjør.
# 
# * Regn ut `abs(-1)`, `abs(-2)`, `abs(-5)`. Hva gjør funksjonen?
# 
# * Skriv inn kommandoen `abs?` i en ipython-terminal og les en setning om funksjonen `abs`

# In[5]:


get_ipython().run_line_magic('pinfo', 'abs')


# ---------------------------
# 
# #### Oppgave 3
# 
# ##### a)
# La $G = 450000$, $V = 0.88$ og $n = 6$. Bruk ipython til å beregne verdien av $N$, som er gitt ved likningen
# 
# $$N = GV^n.$$
# 
# 

# In[3]:


# Du kan skrive programmet ditt her


# ##### b)
# Lag et eksempel på en praktisk situasjon som passer til likningen i oppgave a).
# 
# ---------------

# ----------------------------
# #### Oppgave 4
# 
# ##### a)
# La $g = -9.81$, $h_0 = 40$ og $t = 4.5$.
# 
# La
# 
# $$ h = h_0 + \frac{1}{2}gt^2.$$
# 
# Fullfør ipython-økten under slik at den regner ut verdien av $h$
# 
# ```
# In [1]: g = -9.81
# 
# In [2]: h_0 = 40
# 
# In [3]: t = 4.5
# ```
# 
# ##### b)
# Hvilken praktisk situasjon kan likningen i oppgave a) beskrive?

# In[ ]:





# ---------------------
# #### Oppgave 4
# 
# Se på ipython-økten under.
# 
# Kan du se hva som skjer?
# 
# ```
# In [1]: 1%4
# Out[1]: 1
# 
# In [2]: 2%4
# Out[2]: 2
# 
# In [3]: 3%4
# Out[3]: 3
# 
# In [4]: 4%4
# Out[4]: 0
# 
# In [5]: 5%4
# Out[5]: 1
# 
# In [6]: 6%4
# Out[6]: 2
# 
# In [7]: 7%4
# Out[7]: 3
# 
# In [8]: 8%4
# Out[8]: 0
# 
# In [9]: 9%4
# Out[9]: 1
# ```

# ## Flyttall
# Til å starte med kan du tenke på flyttall som et desimaltall lagret på datamaskinen. På engelsk kalles flyttal for *floating point number*, eller i korthet bare *float*. Derav navnet på datatypen i eksempelet over. Likevel er det noen spesielle egenskaper ved flyttall det er vel verd å være oppmerksom på.
# 
# Eksempelet under illustrerer et av problemene ved flyttall.
# Hvordan kan vi forklare hva som skjer - og er dette generelt litt skummelt?

# In[19]:


inaccurate_approximation = 1E23*(1/3)
print(f'{inaccurate_approximation:.4f}')


# Dette ser kanskje ikke lovende ut, men den relative feilen er av størrelsesorden
# 
# $$\epsilon \approx \frac{10^{14}}{10^{22}} = 10^{-8}.$$
# 
# Det bruker å gå fint å gjøre beregninger med flyttall - men vi skal senere se litt på noen tilfeller der 
# det likevel ikke går fullt så bra.

# ## Tall som input fra bruker

# 
# Hvis vi ønsker å lese inn et tall, må vi fortelle Python at det er et tall vi er ute etter
# 

# In[ ]:


name = input('Hva er navnet ditt? Skriv her: ')
print("Hallo " + name + "!" )

height_centimeters = input('Hvor høy er du? Gi svaret i cm uten enheter.')

#gjør strengen height_centimeters om til en float
height_centimeters = float(height_centimeters)

height_meters = height_centimeters/100

print("Høyden din i meter er:  ", height_meters)


# ## Oppgaver

# #### Oppgave 5
# Spør brukeren om navnet til brukeren.
# Skriv ut en hyggelig hilsen til brukeren som inneholder brukerens navn

# #### Oppgave 6
# Skriv et program som spør brukeren om etternavn, fornavn og alder.
# Alle strenger har en funksjon `lower` som kan brukes på følgendem måte:

# In[ ]:


etternavn = 'Marchussen'
etternavn.lower()


# Programmet skal skrive ut etternavnet med små bokstaver

# In[ ]:





# #### Oppgave 7
# Skriv et program som spør brukeren om en tekst. Programmet skal skrive teksten ut igjen med store bokstaver.

# #### Oppgave 8
# ##### a)
#     1) Forklar hva programmet under gjør 
#     2) Modifiser programmet slik at verdien av variabelen LHS blir skrevet ut

# In[24]:


x = 7
y = 13

LHS = x*y + x/(y + 1)


# ##### b)
# Skriv et program som tar inn to tall $x$ og $y$ fra brukeren, og regner ut en verdi for utrykket
# $xy + x + y$

# In[ ]:





# #### Oppgave 9
# Skriv et program som tar inn to tall $x$ og $y$ og regner ut en verdi for utrykket $$xy + \frac{x + 2y}{3}$$

# In[ ]:





# #### Oppgave 10
# Noen amerikanske og engelske matlagingsprogrammer har irriterende høy bruk av temperaturskaleaen fahrenheit.
# Formelen for å gjøre om fra fahrenheit til celcius er gitt ved
# 
# $$ C = (F - 32)\cdot\frac{5}{9} $$
# 
# Skriv et program som leser inn grader fahrenheit fra brukeren, og skriver ut temperaturen i grader celcius.

# 

# #### Oppgave 11
# I fysikken har du kanskje lært å bruke formelen
# 
# $$ h(t) = h_0 + v_0t - \frac{1}{2}gt^2 $$
# 
# ##### a)
# Se på koden under. Kan du fullføre den slik at det regnes ut en verdi for $h$?

# In[ ]:


g = 9.81   # tyngdens akselerasjon
h_0 = 4.0  # starthøyde
v_0 = 3.4  # vertikal start-fart

h = h_0 + v_0 - 0.5*...


# ##### b)
# Hvilke verdier vil variere fra kast til kast?
# Les disse verdiene inn fra brukeren, og regn ut hvor høyden.
# Skriv dette ut i en lesbar forståelig melding til brukeren.
# 

# In[ ]:





# ##### c)
# Utvid programmet fra b) slik at det leser inn den totale farten og utgangsvinkelen på kastet.
# Bruk en parameterfremstilling til å regne ut posisjonen etter $t$ sekunder.
# 
# Skriv denne posisjonen ut til brukeren
# 
# Du kan bli nødt til å importere funksjoner fra pakken `pylab`

# In[47]:


from pylab import *
# skriv resten av koden under her...


# #### Oppgave 12
# Under har Pål prøvd å skrive et program, men han får en feilmelding.
# ##### a) 
# Hjelp Pål med å reparere programmet

# In[ ]:


import sys
#gjør om mellom lysår og kilometer

light_year = 9460730472580.8 # ett lysår målt i km

distance_light_years = input('Write the distance in light years:  ')

distance_kilometers = distance_light_years*light_year

# print distansen i antall kilometer på stanardform
print(f'distansen i km er: {distance_kilometers:g}')


# I den siste linjen bruker vi en spesiell formatering av strenger.
# For å fortelle python at vi skal bruke en f-streng, setter vi bokstaven f foran strengen.
# 
# ##### b)
# Fjern tegnene kolon og g (`:` og `g`) i siste linjen i programmet. Hva skjer?
# 
# 
# ##### Mer om f-strings
# Vi vil komme tilbake til bruk av f-strings senere.
# Hvis du er nysjerrig - kan du se en video av [Corey Shafer om f-strenger](https://www.youtube.com/watch?v=nghuHvKLhJA).
# Videoen antar at du har hatt litt mer om dictionaries og løkker, men dette er ikke essensielt for innholdet i videoen. Du kan enten se begynnelsen av filmen og spare resten til senere,
# eller hvis du klarer å holde deg rolig uten å forstå alle detaljene kan du kanskje ha utbytte av flere deler av videoen.

# ## Input fra kommandolinje
# Når vi lager programmer vi kjører ofte, er det vanligvis lettere å gi input fra kommandolinjen.
# Til dette kan vi bruke pakken `sys`
# Under ser du et utsnitt av et program `hello_you.py` som tar inn navnet fra en person fra kommandolinjen, og skriver
# ut en hilsen
# 

# In[42]:


get_ipython().system('ls')


# In[45]:


get_ipython().run_cell_magic('writefile', 'add_args.py', 'import sys\n\n\na = sys.argv[1] # legg første argument fra kommandolinjen inn i a\na = float(a)    # omgjør a fra streng til desimaltall\n\nb = sys.argv[2] # Legg andre argument fra kommandolinjen inn i b\nb = float(b)\n\nprint(a + b)')


# Vi kan nå kjøre programmet. Enten fra notebooken som i cellen under, eller fra en terminal.
# Tilsvarende kjøring fra kommandolinjen ville vi fått med kommandoen
# `python add_args.py 1.5 2.8`

# In[49]:


run add_args.py 1.5 2.8


# ### Et veldig typisk eksempel
# Vi tar et kort eksempel på hvordan input kan leses fra kommandolinjen.
# Vi skal i de neste notebookene se på hvilke konsepter som brukes i programmet slik
# at du snart skal kunne skrive slike programmer selv

# In[30]:


get_ipython().run_cell_magic('writefile', 'aplot_andregradsfunksjon.py', "from pylab import *\nimport sys\n\n#programmet plotter grafen til en funksjon a*x**2 + b*x + c\n\n# les inn nødvendige parametere for å representere funksjonen\na = float(sys.argv[1])\nb = float(sys.argv[2])\nc = float(sys.argv[3])\n\n# les inn nødvendige parametere for xmin og xmax for plottet.\n# verdimengden behøver vi ikke bekymre oss om for plotting\nxmin = float(sys.argv[4])\nxmax = float(sys.argv[5])\n\n\nN = round(abs(xmax - xmin)*100) # hundre punkter i et intervall med bredde 1\n\n# Lag et intervall med flyttall fra xmin til xmax med N punkter\nx = linspace(xmin, xmax, N)\n\n# beregn en y-verdi for hvert av flyttallene generert over\ny = a*x**2 + b*x + c\n\nplot(x, y)\n\n#pynt på grafen\nxlabel('x', fontsize='24')\nxticks(fontsize='16', rotation=40)\nylabel('y', fontsize='24')\nyticks(fontsize='16')\ntitle(fr'${a}x^2 + {b}x + {c}$', fontsize='32') # skriv funksjonsuttrykket i tittelen\ngrid()\n\n# gcf: get current figure \nfig = gcf()\nfig.set_size_inches(10, 7)\n\n\nshow()\n")


# In[31]:


run aplot_andregradsfunksjon.py -2 2 5 -2 3


# Det er nå enkelt å endre på parametrene funksjonen får inn. Prøv selv!

# ------------
# 
# ## Orienteringsstoff: Bruk av pakken argparse når mange argumenter skal leses inn
# du synes kanskje at det kan være vanskelig å holde styr på hvilke argumenter som skal leses inn
# til programmet over.
# Vi kan lette dette ved å bruke pakken `argparse`. Da kan vi kjøre programmet ved å bruke *key-value pairs*.
# 
# `run plot_andregradsfunksjon.py --a 0 --b 2 --c 5 --xmin -2 --xmax 3`
# 
# Det vil da være lettere for brukeren å holde styr på hvilke argumenter som er hva

# In[38]:


get_ipython().run_cell_magic('writefile', 'plot_andregradsfunksjon.py', "\nfrom pylab import *\nimport argparse\n\n\nparser = argparse.ArgumentParser() # lag et objekt parser som kan lese input fra kommandolinjen\n\n# definer forventede argumenter fra kommandolinjen med key-value pairs\nparser.add_argument('--a', type=float)\nparser.add_argument('--b', type=float)\nparser.add_argument('--c', type=float)\n\nparser.add_argument('--xmin', type=float)\nparser.add_argument('--xmax', type=float)\n\n# antall grid-punkter i et intervall med lengde 1\nparser.add_argument('--grid_density', type=int, default=100)\n\n# les argumentene fra kommandolinjen\nargs = parser.parse_args()\na, b, c, xmin, xmax, grid_density = args.a, args.b, args.c, args.xmin, args.xmax, args.grid_density\n\nN = round(abs(xmax - xmin)*grid_density) # antall punkter i gridet\n\nx = linspace(xmin, xmax, N)\ny = a*x**2 + b*x + c\n\nplot(x, y)\n\nxlabel('x', fontsize=16); xticks(fontsize=14)\nylabel('y', fontsize=16); yticks(fontsize=14)\n\ntitle(fr'${a}x^2 + {b}x + {c}$', fontsize=20) # skriv funksjonsuttrykket i tittelen\ngrid()\n\n\n# gcf: get current figure \nfig = gcf()\nfig.set_size_inches(10, 7)\n\n\nshow()")


# In[39]:


run plot_andregradsfunksjon.py --a -0.5 --b 3 --c 2 --xmin -1.5 --xmax 7


# ----------------

# #### Oppgave 13
# I denne oppgaven må du modifesere programmet `aplot_andergradsfunksjon.py`. Du kan selvfølgelig velge å heller
# modifisere programmet `plot_andregradsfunksjon.py`.
# 
# Vi skal starte med å stille opp en annen matematisk modell. Du har følgende scenarie:
# 
# Antall bakterier i en bakteriekultur er ved morgenen klokken 8.00 målt til 12 000 bakterier.
# Klokken 10.00 er antall bakterier målt til 13 000 bakterier.
# 
# ##### a)
# Still opp to ulike modeller $A(t)$ og $B(t)$ for antall bakterier i bakteriekulturen.
# For hver modell skal du tegne grafen til modellen.
# 
# ------------
# 
# Tenk gjennom følgende for hver av modellene:
# 
# * Hvilken informasjon trenger du fra brukeren for å tegne grafen?
# * Hva må endres i programmet?
# 
# ------------
# 
# ##### c)
# Velg modellen fra oppgave b) du syns er mest realistisk.
# 
# Gjør de nødvendige endringene i programmet slik at du kan plotte grafen til funksjonen.
# 
# Lagre endringene i et nytt program `plot_bakteriepopulasjon.py`

# In[15]:


get_ipython().run_cell_magic('writefile', 'plot_bakteriepopulasjon.py', '# Du kan skrive koden din her')


# ------------

# #### Oppave 14
# Les inn noen data for loddrett kast i programmet over og plot grafen slik at du
# får høyde over bakken på y-aksen som funksjon av tiden etter kastet i sekunder på x-aksen.

# In[ ]:




