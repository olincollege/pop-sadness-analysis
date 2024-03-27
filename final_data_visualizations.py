"""
This module produces the 3 visualizations of our data.
"""

import csv
import numpy as np
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from matplotlib.patheffects import withSimplePatchShadow
import mplcursors  # separate package must be installed
import helper_function

nltk.download("vader_lexicon")  # Run this line the first time you run this code

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Import data
loaded_data = pd.read_csv("billboard_data_with_lyrics")
lyrics_data = loaded_data["Lyrics"]

# PROCESS DATA
positivity_scores = []

# Add a Positivity series to the Billboard dataframe
for i in range(len(lyrics_data)):
    positivity_scores.append(
        analyzer.polarity_scores(lyrics_data[i])["compound"]
    )

all_data = pd.concat(
    [loaded_data, pd.DataFrame({"Positivity": positivity_scores})], axis=1
)

# Create dictionary of words and their frequencies
CSV_FILE_PATH = "billboard_data_with_lyrics.csv"

# List of words that are not very interesting, don't have interesting changes,
# and reduce the effectiveness of the word cloud visual
irrelevant_words = [
    "fuck",
    "bitch",
    "bitches",
    "dick",
    "niggas",
    "shit",
    "fucked",
    "bad",
    "damn",
    "ass",
]

with open(CSV_FILE_PATH, encoding="utf8", newline="") as csvfile:
    csvreader = csv.reader(csvfile)

    words_dictionary = {}
    words_dictionary1 = {}
    words_dictionary2 = {}
    list_of_dictionary = [
        words_dictionary,
        words_dictionary1,
        words_dictionary2,
    ]

    for count, row in enumerate(csvreader, start=0):
        words = helper_function.split_text_into_words(row[4])
        for word in words:
            # Ensure upper/lower case does not affect visual
            word = word.lower()
            if word in irrelevant_words:
                continue
            if helper_function.polarity(word)["compound"] < -0.3:
                # Choose the correct dictionary based on the count
                current_dict = list_of_dictionary[count // 400]
                # Use get to avoid KeyError, defaults to 0 if the key doesn't
                # exist
                current_dict[word] = current_dict.get(word, 0) + 1


# Ranking Algorithm to find Top 5 Artists:

# Step 1: Assign Scores Based on Ranking
# input variables: song rankings, and name of the artists

top_artist_polarityscore = []

with open("billboard_data_with_lyrics.csv", mode="r", encoding="utf-8") as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)

    # Convert it to a list to get the ability to use len() and indexing
    rows = list(csv_reader)

    # Iterate using indices
    for j in range(11):
        scores_by_artist = {}
        for i in range(100):
            score = 101 - i  # Calculate the score based on ranking
            artist = rows[j * 100 + i][2]
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
        top_5_artist_names = [artist[0] for artist in top_5_artists]

        polarity_score = {}
        polarity_count = {}
        for i in range(100):
            artist = rows[j * 100 + i][2]

            if (artist in top_5_artist_names) is False:
                continue

            if artist in polarity_score:
                polarity_score[artist] += helper_function.polarity(
                    rows[j * 100 + i][4]
                )["compound"]
                polarity_count[artist] += 1
            else:
                polarity_score[artist] = helper_function.polarity(
                    rows[j * 100 + i][4]
                )["compound"]
                polarity_count[artist] = 1

        for x, y in polarity_score.items():
            polarity_score[x] /= polarity_count[x]
        top_artist_polarityscore.append(polarity_score)

extended_data = top_artist_polarityscore


# FIRST VISUALIZATION - Polarity of Every Top Song with Trendline

# Plot average positivity scores for each year from the past 10 years
scores = [
    sum(positivity_scores[:101]) / 100,
    sum(positivity_scores[100:201]) / 100,
    sum(positivity_scores[200:301]) / 100,
    sum(positivity_scores[300:401]) / 100,
    sum(positivity_scores[400:501]) / 100,
    sum(positivity_scores[500:601]) / 100,
    sum(positivity_scores[600:701]) / 100,
    sum(positivity_scores[700:801]) / 100,
    sum(positivity_scores[800:901]) / 100,
    sum(positivity_scores[900:1001]) / 100,
    sum(positivity_scores[1000:1101]) / 100,
]
years = [
    2013.5,
    2014.5,
    2015.5,
    2016.5,
    2017.5,
    2018.5,
    2019.5,
    2020.5,
    2021.5,
    2022.5,
    2023.5,
]  # add .5 to all years to make visualization more effective

plt.figure()
plt.plot(years, scores, "r--")  # plot general trend line
plt.xlabel("Year")
plt.ylabel("Polarity Score")
plt.title("Polarity Score of Every Top 100 Song, 2013-2023")
# Plot every song and its score
indiv_scores = plt.scatter(
    np.linspace(2013, 2023.99, num=1100), positivity_scores
)


# Using the mplcursors library, display information about each data point
# when you hover over it.
def show_hover_panel(get_text_func=None):
    """
    Displays specified content whenever the cursor is hovering over a data
    point.

    Args:
        get_text_func: A string that contains text to be displayed. If it is
        None, no box will be displayed.

    Returns:
        a cursor object that displays a box contanining specified content
        whenever it hovers over a data point.
    """
    cursor = mplcursors.cursor(
        hover=2,  # Transient
        annotation_kwargs=dict(
            bbox=dict(
                boxstyle="square,pad=0.5",
                facecolor="white",
                edgecolor="#ddd",
                linewidth=0.5,
                path_effects=[withSimplePatchShadow(offset=(1.5, -1.5))],
            ),
            linespacing=1.5,
            arrowprops=None,
        ),
        highlight=True,
        highlight_kwargs={"linewidth": 2},
    )

    if get_text_func:
        cursor.connect(
            event="add",
            func=lambda sel: sel.annotation.set_text(get_text_func(sel.index)),
        )
    return cursor


def on_add(index):
    """
    Returns the text that should be displayed when the cursor is hovering over a
    specific data point.
    Args:
        index: an integer representing the index of the current data point in
        the dataset
        dataframe: the dataframe for the data being displayed.
    Returns:
        A string containing the text to be displayed when the specific data
        point is hovered over.
    """
    try:
        parts = [
            f"Song: {all_data['Title'][index]}",
            f"Artist: {all_data['Artists'][index]}",
            f"Chart Position: {all_data['No.'][index]}",
            f"Score: {all_data['Positivity'][index]}",
        ]
        return "\n".join(parts)
    except KeyError:  # don't hover when the cursor is over the trendline
        return None


show_hover_panel(on_add)  # add hover labels
plt.show()

# SECOND VISUALIZATION - Average Polarity Score of Top 5 Artists by Year

# Calculate the range of years
years = np.arange(2013, 2013 + len(top_artist_polarityscore))

# Calculate the average polarity score for each year
average_scores = [
    np.mean(list(year.values())) for year in top_artist_polarityscore
]

# Set up the plot
plt.figure(figsize=(12, 8))

# Create a bar chart
plt.bar(years, average_scores, color="skyblue")

# Make sure the Y-axis starts below zero if there are negative values
plt.ylim([min(average_scores) - 0.1, 1])

# Labeling
plt.title("Average Polarity Score of Top 5 Artists by Year")
plt.xlabel("Year")
plt.ylabel("Average Polarity Score")

# Add value labels on each bar
for i, score in enumerate(average_scores):
    plt.text(years[i], score, f"{score:.2f}", ha="center", va="bottom")

# Show the plot
plt.show()

# THIRD VISUALIZATION - Polarity Scores of Top 5 Artists from Every Year

# Determine global min and max polarity scores for consistent y-axis limits
all_scores = [
    score for yearly_data in extended_data for score in yearly_data.values()
]
global_min = min(all_scores)
global_max = max(all_scores)
NCOLS = 3
NROWS = len(top_artist_polarityscore) // NCOLS + (
    len(top_artist_polarityscore) % NCOLS > 0
)

# Create a large figure to hold all subplots
plt.figure(figsize=(NCOLS * 5, NROWS * 5))  # Width and height of entire figure

for i, yearly_data in enumerate(extended_data, start=1):
    ax = plt.subplot(NROWS, NCOLS, i)
    artists = list(yearly_data.keys())
    scores = list(yearly_data.values())
    y_pos = np.arange(len(artists))

    ax.bar(y_pos, scores, color=plt.cm.tab20(np.linspace(0, 1, len(artists))))
    ax.set_xticks(y_pos)
    ax.set_xticklabels(artists, rotation=90)
    ax.set_title(f"Year {2013 + i - 1}")

    # Set the same y-axis limit for all subplots
    ax.set_ylim(global_min, global_max)

    # Set the y-axis label only for the leftmost subplots
    if i % NCOLS == 1:
        ax.set_ylabel("Average Polarity Score")

# Adjust the layout so labels and titles do not overlap
plt.tight_layout()

# Display the visualization
plt.show()


# FOURTH VISUALIZATION - Word cloud of most commonly used negative words

# Generate the word cloud
YEAR = 2013
for i in range(3):
    helper_function.generate_word_cloud_from_frequencies(
        list_of_dictionary[i],
        f"Negative Word Cloud From Year {YEAR} to {YEAR + 3 - (i == 2)} ",
    )
    YEAR += 4
