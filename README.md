# Movie Recommendation System

This project demonstrates how to build a movie recommendation system using a Netflix dataset. The system employs the cosine similarity algorithm and TF-IDF vectorizer to recommend similar movies based on the content of movie descriptions. Additionally, it includes a Streamlit app that allows users to input a movie title and receive recommendations for similar movies.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Data](#data)
- [Recommendation Algorithm](#recommendation-algorithm)
- [Code Explanation](#code-explanation)
- [References](#references)

## Introduction

The movie recommendation system suggests similar movies based on the content of movie descriptions from a Netflix dataset. The system uses a combination of TF-IDF vectorization and cosine similarity to calculate the similarity between movie descriptions and provide recommendations.

The project includes a Streamlit app that provides a user-friendly interface for inputting a movie title and receiving recommendations for similar movies.

## Features

- Uses a Netflix dataset for movie recommendations.
- Implements TF-IDF vectorizer for text representation.
- Uses cosine similarity to calculate similarity between movies.
- Streamlit app for recommending movies based on user input.

## Setup and Installation

1. **Clone the Repository**:
    - Clone the project repository to your local machine.
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a Virtual Environment**:
    - Create and activate a virtual environment (recommended).
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**:
    - Install the required Python packages using the provided `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Streamlit App**:
    - Start the Streamlit app.
    ```bash
    streamlit run app.py
    ```

2. **Provide Movie Title**:
    - In the app, you will be prompted to input a movie title from the dataset.
    
3. **Receive Recommendations**:
    - The system will display a list of recommended movies similar to the selected movie title.

## Data

- The Netflix dataset used in this project contains movie information, including movie titles and descriptions.
- The dataset is processed and used for building the recommendation system.

## Recommendation Algorithm

- The recommendation system employs the following methods:
    - **TF-IDF Vectorization**: Text descriptions of movies are transformed into numerical vectors using Term Frequency-Inverse Document Frequency (TF-IDF) vectorization.
    - **Cosine Similarity**: Cosine similarity is calculated between the input movie and all other movies based on their TF-IDF vectors to find the most similar movies.

## Code Explanation

- **app.py**:
    - The Streamlit app script for loading the Netflix dataset and running the movie recommendation system.
    - Provides a user-friendly interface for inputting a movie title and receiving recommendations for similar movies.
    - Uses TF-IDF vectorization to transform movie descriptions into vectors and calculates cosine similarity to recommend similar movies.

## References

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Cosine Similarity Explained](https://en.wikipedia.org/wiki/Cosine_similarity)
- [TF-IDF Explained](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
- [Streamlit Documentation](https://docs.streamlit.io/)

## Conclusion

This project provides an example of building a movie recommendation system using a Netflix dataset and a Streamlit app for user interaction. By employing TF-IDF vectorization and cosine similarity, the system can provide recommendations of similar movies based on user input. Feel free to customize and extend this project to suit your needs.
