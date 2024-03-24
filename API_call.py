import pandas as pd
from lyricsgenius import Genius

import helpers
import api_key

genius = Genius(api_key.client_access_token)
billboard_df = pd.read_csv("billboard_100.csv")

artists = helpers.generate(billboard_df)

artists_series = pd.Series(artists)
lyrics = []
num_songs = 1100

for i in range(num_songs):
    while True:
        try:
            song = genius.search_song(
                billboard_df["Title"][i], artists_series[i]
            )
            break
        except:
            pass
    lyrics.append(helpers.format_genius_lyrics(song.lyrics))

df = pd.DataFrame(
    {
        "No.": billboard_df["No."][:num_songs],
        "Title": billboard_df["Title"][:num_songs],
        "Artists": artists_series[:num_songs],
        "Year": billboard_df["Year"][:num_songs],
        "Lyrics": pd.Series(lyrics),
    }
)

lyrics_only = pd.DataFrame(pd.Series(lyrics))

df.to_csv("billboard_data_with_lyrics", encoding="utf-8", index=False)

lyrics_only.to_csv(
    "billboard_data_with_lyrics_only", encoding="utf-8", index=False
)
