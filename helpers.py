def remove_features(string):
    for i in range(len(string)):
        if string[i : i + 9] == "featuring" or string[i : i + 4] == "with":
            string = string[: i - 1]
    return string


def format_genius_lyrics(string):
    lyrics_started = False
    formatted_string = ""
    bracket_open = False

    for i in range(len(string)):
        # The string Lyricsgenius returns starts with some text about the
        # number of contributors and '[Title] lyrics', so this code makes
        # sure it doesn't start reading until after it sees that word.
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
    artists = []
    for i in range(len(dataframe)):
        artists.append(remove_features(dataframe["Artist(s)"][i]))
    return artists
