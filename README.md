# MovieSuggestions
 [TRY ME!](https://jennyflix.streamlit.app/)

[Kaggle_TMDB 5000 Movie Dataset](https://www.kaggle.com/code/ibtesama/getting-started-with-a-movie-recommendation-system)

*before you try this project, you must have a valid API key your own.
  - You can obtain an API key from the TMDB website. [TMDB](https://www.themoviedb.org/)
  - First, sign up and go to the settings in your profile. Then, click on the API tab.
  - There, you can generate your API key. Afterward, follow the steps below.


1. pip install python-dotenv
2. add "from dotenv import load_dotenv" and "load_dotenv()" in the app.py
3. replace st.secrets["API_KEY"] to os.getenv('API_KEY') in the app.py
4. create the .env and add "API_KEY=your API key"
5. you need to install streamlit and tmdbv3api => [pip install streamlit tmdbv3api]
6. start with 'streamlit run app.py'
