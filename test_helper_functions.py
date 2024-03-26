import pytest
from helper_function import (
    remove_features,
    format_genius_lyrics,
    generate,
    split_text_into_words,
)

REMOVE_FEATURES_CASES = [
    # Test the case where a feature is present
    ("Software featuring Design", "Software"),
    # Test the case where a feature is not present
    ("design", "design"),
    # Test the case where multiple artists are featured
    ("Olin featuring College and of and Engineering", "Olin"),
]

FORMAT_GENIUS_LYRICS_CASES = [
    # Test that the function doesn't start counting lyrics until after it sees
    # "Lyrics"
    (
        "326ContributorsTranslationsThriftShopLyricscan we go thrift shopping?",
        "can we go thrift shopping?",
    ),
    # Test that the function excludes text within brackets
    (
        "Lyrics[Intro]Everybody get up [RANDOM INSERTION!]Everybody get up",
        "Everybody get up Everybody get up",
    ),
    # Test that the function ignores the random embed stuff
    (
        "LyricsI'm radioactive, radioactive328Embed",
        "I'm radioactive, radioactive",
    ),
    # Test that the function turns newlines into spaces
    ("Lyrics\n\nThen do the Harlem Shake\n", "  Then do the Harlem Shake "),
    # Check that the function does all of the above at the same time
    (
        "Lyrics[Intro]\nHey, Macklemore, can we go thrift shopping?\n179Embed",
        " Hey, Macklemore, can we go thrift shopping? ",
    ),
]

# Create some test data for the generate function to process
import pandas as pd

test_data = pd.DataFrame(
    {
        "Artists": ["Beyonce", "SZA", "Drake"],
        "Songs": ["Halo", "Kill Bill", "Hotline Bling"],
    }
)
test_data_2 = pd.DataFrame(
    {
        "Artists": ["Beyonce", "SZA", "Drake", "Beyonce", "Beyonce"],
        "Songs": [
            "Halo",
            "Kill Bill",
            "Hotline Bling",
            "7/11",
            "Texas Hold 'Em",
        ],
    }
)

GENERATE_CASES = [
    # Test case where no artists are repeated
    (test_data, ["Beyonce", "SZA", "Drake"]),
    # Test case where an artist is repeated
    (
        test_data_2,
        [
            "Beyonce",
            "SZA",
            "Drake",
            "Beyonce",
            "Beyonce",
        ],
    ),
]

SPLIT_TEXT_INTO_WORDS_CASES = [
    # Test case with 1 word
    ("Word", ["Word"]),
    # Test case with several words
    (
        "This is several Words",
        [
            "This",
            "is",
            "several",
            "Words",
        ],
    ),
    # Test that punctutation, newlines, and multiple spaces are not counted as words
    ("     \n  ?!><.:;   ", []),
    # Test that punctuations are not counted as part of words
    (
        "Words? Yes please!",
        [
            "Words",
            "Yes",
            "please",
        ],
    ),
    # Test the empty case
    ("", []),
]


@pytest.mark.parametrize("title_input,title_output", REMOVE_FEATURES_CASES)
def test_remove_features(title_input, title_output):
    """
    Given a string representing a song title, check that the remove_features
    function removes any artists that are featured.

    Args:
        title_input: a string representing the song's artists
        title_output: a string representing the song's artists (now excluding featured
        artists).
    """
    assert remove_features(title_input) == title_output


@pytest.mark.parametrize(
    "lyrics_input,lyrics_output", FORMAT_GENIUS_LYRICS_CASES
)
def test_format_genius_lyrics(lyrics_input, lyrics_output):
    """
    Given a string representing the contents of a Genius webpage containing the
    lyrics of a song, check that the string is converted into a useable and
    readable string that contains just the lyrics. This means any text within
    brackets (which contain information about song structure) is removed, as
    well as random webpage oddities that occur when scraping data through the
    Genius API.
    Args:
        lyrics_input: a string containing the scraped webpage data, which includes
        (but is not entirely) the lyrics.
        lyrics_output: a string representing the song's lyrics.
    """
    assert format_genius_lyrics(lyrics_input) == lyrics_output


@pytest.mark.parametrize("dataframe_input,artists_output", GENERATE_CASES)
def test_generate(dataframe_input, artists_output):
    """
    Given a dataframe that includes a series titled "Artists", check that the
    generate function returns a list of all Artists from the dataframe, ensuring
    that artists that have multiple entries are included multiple times.
    Args:
        dataframe_input: a dataframe containing a series titled "Artists", from which
        the list of artists will be made.
        dataframe_output: a list of all artists in the dataframe. Artists are included multiple times
        if they have multiple songs on the chart.
    """
    assert generate(dataframe_input) == artists_output


@pytest.mark.parametrize("text_input,words_output", SPLIT_TEXT_INTO_WORDS_CASES)
def test_split_text_into_words(text_input, words_output):
    """
    Given a string, check that the split_text_into_words function returns a list
    of all the words that occur in the string. If there are no words, the
    function should return an empty list.
    Args:
        text_input: a string representing the text to split
        text_output: a list of all the words in the string (in order).
    """
    # Test case with 1 word
    assert split_text_into_words(text_input) == words_output
