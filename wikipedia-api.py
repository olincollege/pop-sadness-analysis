import requests as rq

r = rq.get(
    "https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_2023"
)
print(r.json)
print(f"\n\n\n\n\n\n\n\n\n\nABCDEFGH\n\n\n\n\n\n\n\n\n\n")
print(r.content)
print(f"\n\n\n\n\n\n\n\n\n\nABCDEFGH\n\n\n\n\n\n\n\n\n\n")
print(r.text)
