% Oppgaver: Kom i gang med python

## De fire regneartene

### Oppgave 1
a) Hvordan tror du python vil beregne utrykkene i koden under? Regn ut for hånd/kalkulator og sjekk svaret ditt med `ipython`.

i. `(5 - 2)/(20 - 14)`

ii. `-(6 - 2)/(36 - 45)*5`

iii.  `(5 - 3)/(20 - 18)**2*5`

b) Evaluer utrykkene under med `ipython`.

$$
\begin{aligned}
\mathbf{i)} & & & & & & \frac{8 - 2}{-22 + 28}\cdot 85 \\ \\ \\
\mathbf{ii)} & & & & & & \displaystyle \left(\frac{8 - 2}{-22 + 28}\right)^3\cdot 5
\end{aligned}
$$

## Bruk av variabler i formler og matematiske utrykk

### Oppgave 2
En bil akselerer med konstant akselerasjon $a = 8$ m/s fra startstreken med $v_0 = 0$ på en rettlinjet drag-bane.
Den tilbakelagte avstanden $s$, målt i meter, etter tiden $t$ målt i sekunder er gitt ved formelen

$$
s = \frac{1}{2}at^2
$$

a) Bruk ipython til å beregne den tilbakelaget avstanden etter 15 sekunder.

b) Snu formelen for $t$, og bestem hvor mange sekunder bilen bruker på å kjøre 100 meter.

### Oppgave 3
Kåre skal kjøre forbi en bil på motorveien. Han starter fra en hastighet på $v_0 = 80\text{ km/t}$. Gjennom hele forbikjøringen akselerer han med en konstant askelerasjon $a = 4\text{ m/s}$ til han når en hastighet på $v = 100 \text{ km/t}$.

Formelen $$ 2as = v^2 - v_0^2$$ gir sammenhengen mellom den tilbakelaget strekningen $s$, akselerasjonen $a$, starthastigheten $v_0$ og slutthastigheten $v$.

a) Snu formelen over, og lag en formel for $s$.

b) Bruk ipython til å beregne hvor mange meter Kåre brukte på forbikjøringen.


### Oppgave 4
Hookes lov gir oss sammenhengen mellom kraften fra en fjær og forlengelsen i fjæra.

Dersom vi strekker ut en fjær fra *hvilelengden* $L_0$ til lengden $L = L_0 + x$, er motkraften fra fjæra gitt ved Hookes lov:
$$ F = -kx, $$
der *fjærkonstanten* $k$ er et fast tall, som avhenger av fjærens utforming og materialene som er brukt i fjæra. Merk at det negative fortegnet sørger for at kraften virker i motsatt retning av forlengelsen $x$.

a) En fjær har fjærkonstant $k = 15 \text{kN/m}$. Fjæra blir forlenget med $0,8 \text{ cm}$. Bruk ipython og bestem kraften fra fjæra.

### Oppgave 5
Formelen for kroppsmasseindeks $I$ er gitt ved
$$
I = \frac{m}{h^2} ,
$$
der $h$ er personens høyde, målt i meter, og $m$ er personens masse, målt i kg.

a) Bruk ipython til å beregne kroppsmasseindeksen for en person som veier 75 kg og er 178 cm høy.

b) Bruk ipython til å beregne din egen kroppsmasseindeks.

c) Snu formelen for massen $m$. Beregn massen for en person som har en BMI på 24 og er 180 cm høy.

d) Snu formelen for høyden $h$. Beregn høyden for en person som har en BMI på 26 og veier 76kg.
HINT: du kan bruke syntaxen `a**0.5` for å ta kvadratroten av et tall `a`.


### Oppgave 6
Et objekt som beveger seg i en sirkulær bevegelse om et punkt $P$ opplever en sentripetalakselerasjon med retning fra objektet mot $P$. Sentripetalakselerasjonens størrelse (absoluttverdi) $a$ er gitt ved

$$ a = \frac{v^2}{r} ,$$

der $r$ er avstanden fra objektet til punktet $P$, og $v$ er objektets fart målt i meter per sekund.

Bruk `ipyton` til å beregne akselerasjonen for et objekt i sirkulær bevegelse med fart $12 \text{ m/s}$ og radius på $7 \text{ m}$.


### Oppgave 7
Dette er en fortsettelse av oppgave 3.

Newtons andre lov sier at summen av kreftene på et objekt er lik produktet av objektets masse og akselerasjon:

$$\Sigma F = ma$$

En bil kjører i en sving med radius på 125m med en fart på 80 km/h. Bilen veier 1500kg.

a) Tegn frilegemediagram.

b) Hvor stor er sentripetalkraften på bilen?

c) Hvor mange $g$-krefter tilsvarer denne sentripetalkraften?

En sving har radius på 80 m. En bil veier 1427 kg. 

d) Hvor stor fart kan bilen holde i svingen dersom sentripetalkraften skal holde seg under $3500$ Newton ?

### Oppgave 8
I en karusell beveger menneskene seg i en sirkel slik at de blir ''limt'' til veggen. Karusellen har en radius på $R = 5\text{ m}$ og bruker 4,2 sekunder på én omdreining.
Kåre veier 60 kg og tar en slik karusell.

a) Tegn frilegemediagram

b) Hvor stor er sentripetalakselerasjonen $a$?

c) Bruk newtons andre lov, $\Sigma F = ma$ til å bestemme summen av kreftene som virker på Kåre når han limes til veggen og følger en sirkulær bevegelse.


## Bruk av lister
