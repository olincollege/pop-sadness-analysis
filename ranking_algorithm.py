# Step 1: Assign Scores Based on Ranking
# input variables: song rankings, and name of the artists
from extract_data import generate


scores_by_artist = {}
artists = generate()


for i in range(100):
    score = 101 - i  # Calculate the score based on ranking
    artist = artists[i]
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
