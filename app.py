import pandas as pd
import streamlit as st
from dotenv import load_dotenv
import os
import pickle
import requests

def recommend_movies(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommend_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster
        recommend_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies , recommend_movies_posters




load_dotenv()
def fetch_poster(movie_id):
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    API_KEY = st.secrets.get("TMDB_API_KEY") or os.getenv("TMDB_API_KEY")

    if not API_KEY:
        st.error("TMDB API key not found. Configure it in Streamlit Secrets or your local .env file.")
        st.stop()
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise error for bad status codes
        data = response.json()

        poster_path = data.get('poster_path')
        if poster_path:
            # Constructing the full URL
            full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
            return full_path
        else:
            # Fallback image if movie has no poster
            return "https://via.placeholder.com/500x750?text=No+Poster+Available"

    except requests.exceptions.RequestException:
        # Fallback image if API call fails
        return "https://via.placeholder.com/500x750?text=Image+Error"




movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

# similarity = pickle.load(open('similarity.pkl','rb'))

@st.cache_resource
def load_similarity():
    with open("similarity.pkl", "rb") as f:
        return pickle.load(f)

similarity = load_similarity()


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Which one got your attention to new recommendation?",
    movies['title'].values,
    index=None,
    placeholder="Select contact method...",
)

st.write("You selected:", selected_movie_name)

if st.button("Recommend" ,type="secondary"):
    names , poster = recommend_movies(selected_movie_name)
    st.write("Here is your recommendations:")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(poster[0])
        st.text(names[0])

    with col2:
        st.image(poster[1])
        st.text(names[1])

    with col3:
        st.image(poster[2])
        st.text(names[2])

    with col4:
        st.image(poster[3])
        st.text(names[3])

    with col5:
        st.image(poster[4])
        st.text(names[4])


    # for name,poster in zip(names,poster):
    #     st.write(name)
    #     st.image(poster, caption=name)