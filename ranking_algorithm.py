# Sample data
data = [
    {
        "No.": 1,
        "Title": "Thrift Shop",
        "Artist(s)": "Macklemore & Ryan Lewis featuring Wanz",
        "Year": 2013,
    },
    {
        "No.": 2,
        "Title": "Blurred Lines",
        "Artist(s)": "Robin Thicke featuring T.I. and Pharrell Williams",
        "Year": 2013,
    },
    # Add all other entries here...
    {
        "No.": 100,
        "Title": "Still Into You",
        "Artist(s)": "Paramore",
        "Year": 2013,
    },
]

# Step 1: Assign Scores Based on Ranking
scores_by_artist = {}
for song in data:
    score = 101 - song["No."]  # Calculate the score based on ranking
    artist = song["Artist(s)"]
    if artist in scores_by_artist:
        scores_by_artist[artist] += score
    else:
        scores_by_artist[artist] = score

# Step 2 & 3: Sort Artists by Total Score
sorted_artists = sorted(
    scores_by_artist.items(), key=lambda x: x[1], reverse=True
)

# Step 4: Select the Top 5 Artists
top_5_artists = sorted_artists[:5]

# Print the top 5 artists
for rank, (artist, score) in enumerate(top_5_artists, start=1):
    print(f"{rank}. {artist} - Total Score: {score}")
