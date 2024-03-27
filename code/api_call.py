"""
This module uses the Genius API to scrape the song lyrics from every song on the
year-end Billboard Hot 100 chart from 2013 to 2023 and stores those lyrics in a
file.
"""

import pandas as pd
from lyricsgenius import Genius
import helper_function
import api_key  # You'll have to make one of these on the Genius website

genius = Genius(api_key.client_access_token)

# Load and format billboard data
billboard_df = pd.read_csv("data/billboard_100.csv")
artists = helper_function.generate(billboard_df)
artists_series = pd.Series(artists)
lyrics = []

# Number of songs to be scraped. If scraping all songs, should be 1100
NUM_SONGS = 1100

# Scrape the songs
for i in range(NUM_SONGS):
    while True:
        try:
            song = genius.search_song(
                billboard_df["Title"][i], artists_series[i]
            )
            break
        except:  # If the request times out (which often happens), request again
            pass
    lyrics.append(helper_function.format_genius_lyrics(song.lyrics))

# Save the scraped data into a DataFrame
df = pd.DataFrame(
    {
        "No.": billboard_df["No."][:NUM_SONGS],
        "Title": billboard_df["Title"][:NUM_SONGS],
        "Artists": artists_series[:NUM_SONGS],
        "Year": billboard_df["Year"][:NUM_SONGS],
        "Lyrics": pd.Series(lyrics),
    }
)

# Save the data to a file
df.to_csv("data/billboard_data_with_lyrics", encoding="utf-8", index=False)
