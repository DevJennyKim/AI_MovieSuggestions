import os
import pickle
import streamlit as st
from tmdbv3api import Movie, TMDb


api_key = st.secrets["API_KEY"] 

movie = Movie()
tmdb = TMDb()
tmdb.api_key = api_key


def get_recommendations(title):
  idx = movies[movies['title']==title].index[0]
  sim_scores=list(enumerate(cosine_sim[idx]))
  sim_scores = sorted(sim_scores,key = lambda x: x[1], reverse=True)
  sim_scores = sim_scores[1:11]
  movie_indices = [i[0] for i in sim_scores]
  images = []
  titles = []
  for i in movie_indices:
    id = movies['id'].iloc[i]
    details = movie.details(id)

    image_path = details['poster_path']
    if image_path:
      image_path = 'https://image.tmdb.org/t/p/w500'+ image_path
    else: image_path = 'no_image.png'

    images.append(image_path)
    titles.append(details['title'])

  return images, titles

movies = pickle.load(open('movies.pickle','rb'))
cosine_sim = pickle.load(open('cosine_sim.pickle', 'rb'))
st.set_page_config(layout = 'wide')
st.markdown("<h1 style='color: #e50914;'>JennyFlix</h1>", unsafe_allow_html=True)

movie_list = movies['title'].values
title= st.selectbox('Choose or write a movie you like ', movie_list)
if st.button('Recommend'):
  with st.spinner('Please wait...'):
    images, titles = get_recommendations(title)

    idx=0
    for i in range(0,2):
      cols = st.columns(5)
      for col in cols:
        col.image(images[idx])
        col.write(titles[idx])
        idx+=1 
