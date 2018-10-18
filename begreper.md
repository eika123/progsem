%Begreper i programmering og python  

## Innebygde datatyper
Datatypene `int`, `float` og `str` for henholdsvis heltall, flyttall(desimaltall) og streng(tekst) er inkludert i python.

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

Skal du ta potenser, bruker du følgende syntax:
```
In [23]: 2**4
Out[23]: 16
```

Dersom du ønsker å utføre heltallsdivisjon, bruker du to skråstreker.
F.eks

```
In [25]: 27/5
Out[25]: 5.4

In [26]: 27//5
Out[26]: 5
```

Ønsker du å vite resten fra en divisjon, bruker du tegnet `%` for modulo:

```
In [27]: 27 % 5
Out[27]: 2
```

## Variable
Variabelen er navnet vi bruker på en adresse i minnet som holder et objekt.

I koden under lagres flyttallet `5.0` i variabelen `a`.
```
a = 5.0
```
Variabelen `a` ligger fysisk lagret i minnet på maskinen, og datamaskinen har en adresse til dette stedet. Alt vi behøver å tenke på, er at vi kan nå dette stedet ved
å referere til `a`.

Vi kan bruke variable til å gjøre matematiske formler mer leselig:

```
In [11]: a = -9.81

In [12]: a = -9.81 # gravitasjonskonstant

In [13]: t = 0.5

In [14]: v0 = 15   # utgangshastighet

In [15]: s = v0*t + 0.5*a*t**2

In [16]: s
Out[16]: 6.27375
```



## Objekter
Alt i python er objekter. Du kan derfor tenke på alle variable som en ting eller
enhet som har tilhørende metoder for å vise informasjon om dataene objektet inneholder.

I ipython kan du gjøre dette f.eks med følgende kode

```
In [1]: a = 5.0

In [2]: a.
```
trykker du på `tab`-tasten kommer det flere forslag.

Såkalt objektorientert programmering dreier seg om å definere egne objekter med tilhørende metoder. Dette er neppe aktuelt i VGS med det første.

## Samling av datatyper
Python tilbyr flere måter å samle og strukturere data på. Blant disse er listen
den enkleste å bruke. Koden under illustrerer hvordan en liste kan lages, og hvordan
du kan hente ut informasjon fra listen.

```
stringlist = ['a', 'b', 'c', 'd', 'e', 'f']

stringlist[0]
Out[6]: 'a'

stringlist[5]
Out[7]: 'f'

stringlist[-1]
Out[8]: 'f'

stringlist[1:5]
Out[9]: ['b', 'c', 'd', 'e']
```

Andre måter å indeksere data på i python er numpy-arrays og dictionaries.


