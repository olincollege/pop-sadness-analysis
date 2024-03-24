import nltk
import csv
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt


nltk.download("vader_lexicon")

from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def polarity(word):
    return analyzer.polarity_scores(word)


def split_text_into_words(text):
    # Split the text into words based on various non-word characters
    words = re.split(r"\W+", text)
    # Filter out empty strings
    words_list = [word for word in words if word]
    return words_list


csv_file_path = "billboard_data_with_lyrics.csv"


with open(csv_file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile)

    # This skips the header row if your CSV has one
    next(csvreader)
    words_dictionary = {}
    words_dictionary1 = {}
    words_dictionary2 = {}
    list_of_dictionary = [
        words_dictionary,
        words_dictionary1,
        words_dictionary2,
    ]

    for count, row in enumerate(csvreader, start=-1):

        # Process each row here
        # For example, you can print it
        index = 0
        for i in range(len(row)):
            if row[i] == '"':
                index = i + 1
                break

        words = split_text_into_words(row[index : len(row) - 1])
        for word in words:
            if polarity(word):
                list_of_dictionary[count // 300][word] += 1


def generate_word_cloud_from_frequencies(frequencies, title):
    wordcloud = WordCloud(
        width=800, height=400, background_color="white"
    ).generate_from_frequencies(frequencies)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(title)
    plt.show()


# Generate the word cloud

for i in range(3):
    generate_word_cloud_from_frequencies(
        list_of_dictionary[i], "Sample Word Cloud"
    )
