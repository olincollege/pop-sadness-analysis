# Pop-sadness-analysis README

## About the project 
In this project, we analyse the trend in pop songs and see whether or they have gotten sadder over 10 years. Our research question is: "Has pop music gotten sadder over the past 10 years?" In order to answer this question, we have used web scraping, and have used the Genius API in order to gather song lyrics.

In addition, we have visuals in order to justify our point in this data analysis project. We have made 4 visuals, and you can read more about the visuals in the computational essay. 


### Genius API Setup
- First, create a Genius account.
- Navigate to the Genius API client page and create a new API client.
- Insert your GitHub project link into the API client's website field, along with any other required details.
- Take note of your client access token and store it in a file named `api_key.py` within the code folder of your project. Initialize a variable named `client_access_token` in this file with your token. Change the variable name to your own api key, this is the only change in code you need.

The genius API will be important in order to scrape the lyrical data. In addition to that, we provide the billboard data in a csv file, which includes the top 100 pop songs over the for every year 2013-2023. This is how you can access the data. 



## Requirements

In order to get started, a few python modules have to be imported. For our sentimental analysis, we have used nltk. 

Requirements
To run this project, you will need Python installed on your machine along with the following packages:
```
lyricsgenius~=3.0.1
matplotlib~=3.7.2
mplcursors~=0.5.3
nltk~=3.8.1
numpy~=1.24.3
opencv_python~=4.9.0.80
opencv_python_headless~=4.9.0.80
pandas~=2.0.3
pytest~=7.4.0
wordcloud~=1.9.3
regex~=2023.12.25
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

## Generating visualizations from data

In order to generate the visualizations. In your terminal, run the following command:
```python final_data_visualizations.py```

## Testing

Tests are written using pytest. To run the tests, navigate to the project directory and execute:

```pytest```


