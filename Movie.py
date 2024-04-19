
import streamlit as st
import numpy as np
import pandas as pd
import pickle
import re

class FlixHub:
    def __init__(self, df, cosine_sim):
        self.df = df
        self.cosine_sim = cosine_sim
    
    def recommendation(self, title, total_result=5, threshold=0.5):
        idx = self.find_id(title)
        self.df['similarity'] = self.cosine_sim[idx]
        sort_df = self.df.sort_values(by='similarity', ascending=False)[1:total_result+1]
        
        movies = sort_df['title'][sort_df['type'] == 'Movie']
        tv_shows = sort_df['title'][sort_df['type'] == 'TV Show']
        
        similar_movies = []
        similar_tv_shows = []
        
        for i, movie in enumerate(movies):
            similar_movies.append('{}. {}'.format(i+1, movie))
        
        for i, tv_show in enumerate(tv_shows):
            similar_tv_shows.append('{}. {}'.format(i+1, tv_show))
        
        return similar_movies, similar_tv_shows

    def find_id(self, name):
        for index, string in enumerate(self.df['title']):
            if re.search(name, string):
                return index
        return -1

# Load the necessary data and models
tfid_matrix = np.load('tfidf_matrix.npy', allow_pickle=True)
cosine_sim = np.load('cosine_sim_matrix.npy', allow_pickle=True)
with open('tfidf_vectorizer.pkl', 'rb') as f:
    tfid = pickle.load(f)
df = pd.read_csv('movie_data.csv')

# Create an instance of FlixHub
flix_hub = FlixHub(df, cosine_sim)

# Create the Streamlit app
st.title("Movie Recommendation System")

# Dropdown for selecting a movie
selected_movie = st.selectbox("Select a movie:", [''] + list(df['title']))

if selected_movie:
    # Get recommendations for the selected movie
    movies, tv_shows = flix_hub.recommendation(selected_movie, total_result=10, threshold=0.5)

    # Display recommended movies
    st.header("Recommended Movies:")
    for movie in movies:
        st.write(movie)

    # Display recommended TV shows
    st.header("Recommended TV Shows:")
    for tv_show in tv_shows:
        st.write(tv_show)
else:
    st.info("Please select a movie from the dropdown above.")
