## Authors
Seb Olsen, Piter Nicolaas, Caspar de Jong

## Title
Creating spoiler-free summaries of sitcom television screenplays

## Abstract
_A max 150-word description of the project question or idea, goals, dataset used. What story you would like to tell and why? What's the motivation behind your project?_

This project aims to create spoiler-free summaries of TV show episodes using scripts from the sitcom Friends. By developing a model that identifies and omits the climax and resolution stages of the episodes, we seek to generate concise and engaging episode previews without revealing key plot points. This approach preserves the viewing experience, providing a glimpse into episodes without spoiling their outcomes.


## Research questions
_A list of research questions you would like to address during the project._
* How can we train a model to recognize the climax/resolution stage of a story?
* How can we train a summarisation model to ignore this stage in it's summary to avoid spoilers?

## Dataset
_List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show you've read the docs and are familiar with some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant._
* We use the followeing dataset of friends episode scripts available on Kaggle:
* [Friends dataset](https://www.kaggle.com/datasets/blessondensil294/friends-tv-series-screenplay-script)


## A tentative list of milestones for the project
_Add here a sketch of your planning for the coming weeks. Please mention who does what._

* Create a dataset by combining our input (scripts) and expected output (synopsis sentences)
* Clean up dataset to a usable format
* Create an NLP pipeline for preprocessing the datasets
* Try first attempt at training the model
* Look into the results and find room for improvement
* Modify model and try again


## Documentation
```data```: contains raw script data

```data_processed```: contains preprocessed script data

```results```: contains model runs

```climax_analysis.py```: integrates calls to climax analysis model + summarisation model with preprocessing

```crop_script.py```: contains climax analysis model

```imdb_scraper.py```: contains imdb webscraper

```main.py```: integrates preprocessing and model training

```model_predictions.py```: uses pretrained model to predict descriptions from script data

```model_training.py```: fine-tunes T5-small model

```preprocessing.py```: preprocesses data

