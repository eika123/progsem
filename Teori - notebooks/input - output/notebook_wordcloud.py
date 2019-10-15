from wordcloud import WordCloud
import matplotlib.pyplot as plt
import codecs

no_use_words = ['en', 'et', 'ei', 'vi', 'du', 'som', 'er', 'til', 'dere', 'jeg', 'på', 'ny',\
    'nå','og', 'å', 'at', 'get_ipython',  'run_cell', 'magic', 'args', 'nparser', 'kan', '#',\
     'ntitle', 'In', '40', 'ut', 'hva','frac', '$', 'rad2deg','mellomrom', 'telefon', 'adresse',\
    'oppgave', 'Oppgave', 'gjør', 'gjøre', 'Gjør', 'Hva', '0b', 'Mellomrom', 'telefon2',\
    'telefon1', 'adresse1', 'adresse2', 'navn1', 'navn2', "Andersen'", '----', '`', '```', '\label',\
    '\begin', '\end', 'nvn', 'navn','navnet', 'tlf', 'adr', 'etternavn', '\\[1.1em]', '\\[1.2em]', 'Du',\
    'har', 'Har', 'Andersen', 'Klassiske', 'klassisk', 'først', 'av', 'for', 'to', 'bla', 'ved',\
    'likevel', 'fra', 'med', 'skal', 'bruke', 'om', 'skriv', 'være', 'fleste', 'prøv', 'gate',\
    'slik', 'disse', 'slike', 'ikke', 'se', 'de', 'man', 'tullings', 'john', "martin'",\
    'x3', 'An', 'nordiske', 'AMD64', 'kåre', 'MSC', 'telefonnummer', 'da', 'blir',\
    'marie', 'pøbelringen'
    ]

no_use_words += [word.capitalize() for word in no_use_words]
no_use_words = set(no_use_words)

print('en' in no_use_words, 'title' in no_use_words)
wordstring = ' '

with codecs.open('enkel_input_output.py', 'r', encoding='utf-8') as wordsfile:
    for line in wordsfile:
        if line.startswith('#'):
            words = line.split()
    
            for word in words:
                # sum and array of booleans. Word is allowed if it does not contain a forbidden word
                nouse = sum([(nouse_word in word) for nouse_word in no_use_words])
                if nouse == 0:
                    wordstring += ' ' + word
                    print(word)
        else:
            if 'get_ipython' in line:
                continue;
            else:
                wordstring += line


words_to_be_used = ("""
python
"hello, world!"
Hello, World!
"Hello, world!"
forandre
kort
inn
bindeledd
-
bruke
skrive
tekst
slik
python
tekst
Husk
for
bare
med
helt
'Hello, world!'
lesbart
tekst
lese
abstraksjon
konsept
nordiske tegn
for
mange
spesielle
nordiske tegn
bruke
tre
bytes.
tall.
bokstav """)

if __name__ == '__main__':

    wordcloudpicture = WordCloud(width=1780, height=780, margin=0, stopwords=no_use_words,\
        prefer_horizontal=0.75, mode="RGBA", background_color=None).generate(wordstring)

    plt.imshow(wordcloudpicture, interpolation='bilinear')
    plt.axis('off')
    plt.margins(x=0, y=0)
    plt.show()