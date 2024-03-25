import pandas as pd
import string

x = pd.read_csv("billboard_100.csv")

genius_characters = (
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789- "
)


def format_for_genius(string):
    formatted_string = ""
    for character in string:
        if character in genius_characters:
            formatted_string += character
        elif character == "&":
            formatted_string += "and"
    return formatted_string


def remove_features(string):
    for i in range(len(string)):
        if string[i : i + 9] == "featuring":
            string = string[: i - 1]
    return string


def generate():
    artists = []

    for i in range(len(x)):
        artists.append(format_for_genius(remove_features(x["Artist(s)"][i])))

    return artists


print(generate())
