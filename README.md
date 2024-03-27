# Pop-sadness-analysis README

## About the project 
In this project, we analyse the trend in pop songs and see whether or they have gotten sadder over 10 years. Our research question is: "Has Pop Music Gotten Sadder over the Past 10 Years?" In order to answer this question, we have used web scrapping, and have used specific APIs such as the Genius API in order to gather song lyrics, and have used the wikipedia API to gather the top 100 songs from 2013 to 2023. 

In addition, we have visuals in order to justify our point in this data analysis project. We have made 3 visuals, and you could read more about the visuals in the computational essay. 


### Genius API Setup
- First, create a Genius account.
- Navigate to the Genius API client page and create a new API client.
- Insert your GitHub project link into the API client's website field, along with any other required details.
- Take note of your client access token and store it in a file named `api_key.py` within your project. Initialize a variable named `client_access_token` in this file with your token.



## Requirements

In order to get started, a few python modules have to be imported. For our sentimental analysis, we have used nltk. 

Requirements
To run this project, you will need Python installed on your machine along with the following packages:
```
nltk==3.8.1
numpy==1.22.0
pandas==1.4.0
matplotlib==3.5.1
regex==2023.12.25
lyricsgenius==3.0.1
wordcloud==1.9.3
mplcursors==0.5.3
pytest==8.1.1
```
These dependencies can be installed using the command:


```pip install -r requirements.txt ```

Ensure you have a requirements.txt file in your project directory with the above packages listed.

## Getting Started

1) Clone the repository to your local machine using Git:

```git clone <repository-url>```

2) Navigate to the project directory:

```cd pop-sadness-analysis```

3) Install the required Python packages:

```pip install -r requirements.txt```

4) Run the main analysis script (replace main_script.py with your script's filename):

```python main_script.py```


## Testing

Tests are written using pytest. To run the tests, navigate to the project directory and execute:

```pytest```


