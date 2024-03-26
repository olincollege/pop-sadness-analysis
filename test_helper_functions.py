import pytest
from helper_function import (
    remove_features,
    format_genius_lyrics,
    generate,
    split_text_into_words,
)


def test_remove_features():
    """
    Given a string representing a song title, check that the remove_features
    function removes any artists that are featured.
    """
    # Test the case where a feature is present
    assert remove_features("Software featuring Design") == "Software"
    # Test the case where a feature is not present
    assert remove_features("design") == "design"
    # Test the case where multiple artists are featured
    assert (
        remove_features("Olin featuring College and of and Engineering")
        == "Olin"
    )


def test_format_genius_lyrics():
    """
    Given a string representing the contents of a Genius webpage containing the
    lyrics of a song, check that the string is converted into a useable and
    readable string that contains just the lyrics. This means any text within
    brackets (which contain information about song structure) is removed, as
    well as random webpage oddities that occur when scraping data through the
    Genius API.
    """
    # Test that the function doesn't start counting lyrics until after it sees
    # "Lyrics"
    assert (
        format_genius_lyrics(
            "326 ContributorsTranslationsFrançaisThrift Shop Lyricscan we go thrift shopping?"
        )
        == "can we go thrift shopping?"
    )
    # Test that the function excludes text within brackets
    assert (
        format_genius_lyrics(
            "Lyrics[Intro]Everybody get up [RANDOM INSERTION!]Everybody get up [RANDOM INSERTION AGAINNN!]Hey, hey"
        )
        == "Everybody get up Everybody get up Hey, hey"
    )
    # Test that the function ignores the random embed stuff
    assert (
        format_genius_lyrics("LyricsI'm radioactive, radioactive328Embed")
        == "I'm radioactive, radioactive"
    )
    # Test that the function turns newlines into spaces
    assert (
        format_genius_lyrics("Lyrics\n\nThen do the Harlem Shake\n")
        == "  Then do the Harlem Shake "
    )
    # Check that the function does all of the above at the same time
    assert (
        format_genius_lyrics(
            "326 ContributorsTranslationsFrançaisThrift Shop Lyrics[Intro]\nHey, Macklemore, can we go thrift shopping?\n179Embed"
        )
        == " Hey, Macklemore, can we go thrift shopping? "
    )


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


def test_generate():
    """
    Given a dataframe that includes a series titled "Artists", check that the
    generate function returns a list of all Artists from the dataframe, ensuring
    that artists that have multiple entries are included multiple times.

    """
    # Test case where no artists are repeated
    assert generate(test_data) == ["Beyonce", "SZA", "Drake"]
    # Test case where an artist is repeated
    assert generate(test_data_2) == [
        "Beyonce",
        "SZA",
        "Drake",
        "Beyonce",
        "Beyonce",
    ]


def test_split_text_into_words():
    """
    Given a string, check that the split_text_into_words function returns a list
    of all the words that occur in the string. If there are no words, the
    function should return an empty list.
    """
    # Test case with 1 word
    assert split_text_into_words("Word") == ["Word"]
    # Test case with several words
    assert split_text_into_words("This is several Words") == [
        "This",
        "is",
        "several",
        "Words",
    ]
    # Test that the function doesn't count spaces, newlines, or punctuation as words
    assert split_text_into_words("     \n  ?!><.:;   ") == []
    # Test that the function ignores punctuations on words
    assert split_text_into_words("Words? Yes please!") == [
        "Words",
        "Yes",
        "please",
    ]
    # Test that an empty string returns an empty list
    assert split_text_into_words("") == []
