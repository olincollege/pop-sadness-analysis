"""
This module includes all helper functions for our API call and data
visualizations.
"""

import re
import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")  # Run this line the first time you run this code

analyzer = SentimentIntensityAnalyzer()


def remove_features(string):
    """
    Removes any featured artists from a string representing the song's artists,
    which is necessary for scraping songs using the Genius API.
    Args:
        string: a string representing the song's artists
    Returns:
        a string representing the song's artists (now excluding featured
        artists).
    """
    for i in range(len(string)):
        if string[i : i + 9] == "featuring" or string[i : i + 4] == "with":
            string = string[: i - 1]
    return string


def format_genius_lyrics(string):
    """
    Format lyrics scraped from Genius into a useful and readable format,
    removing any text in brackets (which contain information about song
    structure) as well as random webpage oddities that are scraped through the
    API.
    Args:
        string: a string containing the scraped webpage data, which includes
        (but is not entirely) the lyrics.
    Returns:
        a string representing the song's lyrics.
    """
    lyrics_started = False
    formatted_string = ""
    bracket_open = False

    for i in range(len(string)):
        # The string Lyricsgenius returns starts with some text about the
        # number of contributors and '[Title] lyrics', so this code makes
        # sure it doesn't start reading until after it sees that word and
        # doesn't stop until it sees "Embed", which occurs right after the
        # lyrics end.
        if string[i - 6 : i] == "Lyrics":
            lyrics_started = True
        # Adds all text not in brackets
        if lyrics_started is True:
            if string[i] == "[":
                bracket_open = True
            if bracket_open is False:
                formatted_string += string[i]
            if string[i] == "]":
                bracket_open = False
            if string[i + 1 : i + 6] == "Embed":
                lyrics_started = False

    # LyricsGenius sometimes leaves a random string of numbers right
    # before the Embed at the end, so this makes sure we get rid of those
    while True:
        if formatted_string[-1] not in "1234567890":
            break
        formatted_string = formatted_string[:-1]
    # Turn newlines into spaces to improve formatting for sentiment analysis
    formatted_string = formatted_string.replace("\n", " ")

    return formatted_string


def generate(dataframe):
    """
    Generates list of all Artists from a dataframe.
    Args:
        dataframe: a dataframe containing a series titled "Artists", from which
        the list of artists will be made.
    Returns:
        a list of all artists in the dataframe. Artists are included multiple
        times if they have multiple songs on the chart.
    """
    artists = []
    for i in range(len(dataframe)):
        artists.append(remove_features(dataframe["Artists"][i]))
    return artists


def split_text_into_words(text):
    """
    Take a string of text and split it into a list of individual words.
    Args:
        text: A string representing the text to split
    Returns:
        a list of all the words in the string (in order).
    """
    words = re.split(r"\W+", text)
    # Filter out empty strings
    words_list = [word for word in words if word]
    return words_list


def polarity(word):
    """
    Returns the polarity of a word (from -1 to 1, with 1 being the most
    positive) using the NLTK VADER sentiment analyzer.
    Args:
        The word to be analyzed.
    Returns:
        A float representing the polarity of the word.
    """
    return analyzer.polarity_scores(word)


def generate_word_cloud_from_frequencies(frequencies, title):
    """
    Generates a word cloud visualization from a dictionary of words and their
    frequencies using matplotlib.
    Args:
        frequencies:
            a dictionary that maps words to the number of times they occur in a
            particular passage of text.
        title:
            A string representing the title that the plot will have.
    Returns:
        None
    """
    wordcloud = WordCloud(
        width=800, height=400, background_color="white"
    ).generate_from_frequencies(frequencies)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(title)
    plt.show()
