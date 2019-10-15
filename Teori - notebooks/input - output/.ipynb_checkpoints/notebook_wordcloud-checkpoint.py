from wordcloud import WordCloud
import matplotlib.pyplot as plt

# list of words
with open('wordcloud.py', 'r') as wordsfile:
    for line in wordsfile:
        print(line)