%Begreper i programmering og python  

## Innebygde datatyper
Datatypene `int`, `float` og `str` for henholdsvis heltall, flyttall(desimaltall) og streng(tekst) er inkludert i python.

Under ser du eksempler på flyttall
```
In [1]: 3.14
Out[1]: 3.14
```
Flyttallene skiller seg fra desimaltall i matematikken ved at en datamaskin bare kan representere et endelig antall sifre. I år 2018 kan du forholde deg til 15-16 desimaler etter komma, noe avhengig av hvilken datamaskin du bruker.

Under ser du to eksempler på strenger:

```
In [8]: "Hello World"
Out[8]: 'Hello World'

In [9]: "5.3"
Out[9]: '5.3'
```
I dagligtalen er en streng det samme som tekst. Du har neppe problemer med å se "likheten"
mellom strengen `"5.3"` og flyttallet `5.3`. I datamaskinen er dette to helt ulike ting, og derfor krever
disse objektene også et eget fagbegrep.

### De fire regneartene med python

Addisjon, subtraksjon, multiplikasjon og divisjon har standard notasjon i python.
```
In [19]: 5 + 3
Out[19]: 8

In [20]: 20 - 5
Out[20]: 15

In [21]: 3*4
Out[21]: 12

In [22]: 3/4
Out[22]: 0.75
```

Skal du beregne potensen $2^4$, bruker du følgende syntax:
```
In [23]: 2**4
Out[23]: 16
```

Dersom du ønsker å utføre heltallsdivisjon, bruker du to skråstreker.
F.eks

```
In [25]: 27/5   # For sammenligning
Out[25]: 5.4

In [26]: 27//5
Out[26]: 5
```
Merk at tekst som kommer til høyre for tegnet `#` er en kommentar, og blir ignorert av python

Ønsker du å vite resten fra en divisjon, bruker du tegnet `%` for modulo:

```
In [27]: 27 % 5
Out[27]: 2
```

## Kommentarer
For å gjøre koden lettere å lese for andre (og oss selv når vi tar den frem etter lang tid), bruker
vi kommentarer inne i koden. Vi kan kommentere med å skrive tekst til høyre for en
hashtag `#`.

```
In [44]: # Dette er en kommentar, og blir ignorert av python

In [45]: smartvar = 5.0 + 3.4

In [46]: smartvar
Out[46]: 8.4
```

Dersom vi behøver lengre kommentarer i script, kan vi bruke tre streng-tegn, og
lage en såkalt **doc-string**.

```
"""
Dette er en lang kommentar.
Den kan strekke seg over flere linjer
Det er nyttig når man skriver kompliserte programmer og
trenger fyldig dokumentasjon
"""

a = 5
b = 8

c = a*b
```

## Variable
Du bør tenke på variabelen som en lagringsenhet for et objekt. Hvis du ikke vet hva begrepet objekt betyr i programmering, kan du
trygt tenke et objekt det som en "ting". 

I koden under lagres flyttallet `5.0` i variabelen `a`.
```
a = 5.0
```
Python har tilgang til adressen i minnet på maskinen der tallet `5.0` ligger lagret. Alt vi behøver å tenke på, er at vi kan nå dette stedet og informasjonen den inneholder ved å referere til variabelen `a`.



### Bruk av variable i matematiske formler
Vi kan bruke variable til å gjøre matematiske formler mer leselig.
Vi ønsker å beregne høyden $h$ over bakken / utgangsposisjonen ved et lodrett kast,
gitt ved formelen
$$h(t) = v_0t + \frac{1}{2}gt^2,$$
der $v_0$ er utgangshastigheten i meter/sekund, $g=-9.81\text{m}/\text{s}^2$ er gravitasjonen, og $t$ er tiden målt i sekunder.

```
In [1]: g = -9.81   # gravitasjonskonstant

In [2]: t = 1.3

In [3]: v0 = 15     # utgangshastighet

In [4]: h = v0*t + 0.5*g*t**2

In [5]: h
Out[5]: 11.21055
```

Legg merke til forskjellen i lesbarhet sammenliknet med å hardkode dette:
```
# blir du litt svimmel av dette? 
In [10]: 15*1.3 + 0.5*(-9.81)*1.3**2
Out[10]: 11.21055
```



## Objekter
Alt i python er objekter. Du kan derfor tenke på alt i python som en ting eller
enhet som har tilhørende metoder for å forandre eller vise informasjon om dataene objektet inneholder.

I ipython kan du gjøre dette med f.eks følgende kode

```
In [32]: a = 5.0

In [33]: a.
```
trykker du på `tab`-tasten kommer det flere forslag.

Strenger har mange flere innebygde metoder, blant annet `upper`.
```
In [37]: b = "tekst"

In [38]: b.upper()
Out[38]: 'TEKST'
```

Såkalt objektorientert programmering dreier seg om å definere egne objekter med tilhørende metoder. Dette er neppe aktuelt i VGS på mange år.

## Gruppering og indeksering av data
Python tilbyr flere måter å samle og strukturere data på. Blant disse er listen
den enkleste å bruke. Koden under illustrerer hvordan en liste kan lages, og hvordan
du kan hente ut informasjon fra listen. Merk at elementene i listen nummereres fra $0$.

```
In [18]: # lag en liste

In [19]: stringlist = ['a', 'b', 'c', 'd', 'e', 'f']

In [20]: stringlist[0]          # hent ut første element, med indeks 0
Out[20]: 'a'

In [21]: stringlist[5]          # hent ut sjette element, med indeks 5
Out[21]: 'f'

In [22]: stringlist[1:5]        # hent ut en del av listen
Out[22]: ['b', 'c', 'd', 'e']
```

Den siste kommandoen `stringlist[1:5]` gir oss en liste med elementene i
indeksene 1, 2, 3, og 4 fra `stringlist`. Kommandoen er altså inklusiv 
fra start, og ekslusiv til slutt.

Lister kan inneholder objekter av ulike typer:

```
In [39]: mixedlist = ['a', 5, 5.2, 'b', 'c']

In [40]: mixedlist[3]
Out[40]: 'b'

In [41]: mixedlist[4]
Out[41]: 'c'
```

Siden en liste også er et objekt, kommer den med et sett innebygde metoder.
En svært nyttig metode er `append`

```
In [48]: somelist = [0.1, 0.2, 0.3, 0.4]

In [49]: somelist.append(0.5)

In [50]: somelist
Out[50]: [0.1, 0.2, 0.3, 0.4, 0.5]
```
Metoden tilføyer altså et element på slutten av listen.

Andre måter å indeksere data på i python er *numpy-arrays* og *dictionaries*.


