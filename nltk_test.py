import nltk

nltk.download("vader_lexicon")

from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

text = """Bum bum be-dum bum bum be-dum bum
What's wrong with me?
Bum bum be-dum bum bum be-dum bum
Why do I feel like this?
Bum bum be-dum bum bum be-dum bum
I'm going crazy now
Bum bum be-dum bum bum be-dum bum
No more gas in the rig
(Can't even get it started)
Nothing heard, nothing said
(Can't even speak about it)
All my life on my head
(Don't want to think about it)
Feels like I'm going insane, yeah
It's a thief in the night to come and grab you
It can creep up inside you and consume you
A disease of the mind, it can control you
It's too close for comfort
Throw on your pretty lies
We're in the city of wonder
Ain't goin' play nice
Watch out, you might just go under
Better think twice
Your train of thought will be altered
So if you must falter be wise
Your mind's in disturbia
It's like the darkness is the light
Disturbia
Am I scaring you tonight
(Your mind's in) Disturbia
Ain't used to what you like
Disturbia
Disturbia
Bum bum be-dum bum bum be-dum bum
Bum bum be-dum bum bum be-dum bum
Bum bum be-dum bum bum be-dum bum
Bum bum be-dum bum bum be-dum bum
Faded pictures on the wall
(It's like they talkin' to me)
Disconnectin' all your call
(Your phone don't even ring)
I gotta get out
Or figure this out
It's too close for comfort, ooh
It's a thief in the night to come and grab you
It can creep up inside you and consume you
A disease of the mind, it can control you
I feel like a monster
Throw on your pretty lies
We're in the city of wonder
Ain't goin' play nice
Watch out, you might just go under
Better think twice
Your train of thought will be altered
So if you must falter be wise
Your mind's in disturbia
It's like the darkness is the light
Disturbia
Am I scaring you tonight
Disturbia
Ain't used to what you like
Disturbia
Disturbia
Bum bum be-dum bum bum be-dum bum
Bum bum be-dum bum bum be-dum bum
Bum bum be-dum bum bum be-dum bum
Disturbia
Bum bum be-dum bum bum be-dum bum
Release me from this curse I'm in
Trying to maintain but I'm struggling
You can't go, ho, ho, ho, ho-ho
I think I'm gonna oh, oh, oh
Throw on your pretty lies
We're in the city of wonder
Ain't goin' play nice
Watch out, you might just go under
Better think twice
Your train of thought will be altered
So if you must falter be wise
Your mind's in disturbia
It's like the darkness is the light
Disturbia
Am I scaring you tonight
(Your mind's in) Disturbia
Ain't used to what you like
Disturbia
Disturbia oh oh oh
Bum bum be-dum bum bum be-dum bum
Bum bum be-dum bum bum be-dum bum
Bum bum be-dum bum bum be-dum bum
Bum bum be-dum bum bum be-dum bum"""

scores = analyzer.polarity_scores(text)

print(scores)
