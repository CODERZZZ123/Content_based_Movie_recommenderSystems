import streamlit as st
import pickle
import requests
from PIL import Image


def get_poster_from_API(movie_id):
    variable = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=899ca74cbbef11c6b36dac3480f94676'.format(movie_id))
    data = variable.json()
    return "https://image.tmdb.org/t/p/original/"+ data['poster_path']

def recommend_movie(movie):
    index_movie = movies_list[movies_list['title'] == movie].index[0]
    movie_vector = sorted(list(enumerate(interaction_movies[index_movie])), reverse=True, key=lambda x: x[1])
    to_show_movies = []
    to_show_movies_poster = []
    to_show_overiew = []
    for i in range(1, 11):
        movie_id = movies_list.iloc[movie_vector[i][0]].id
        to_show_movies.append(movies_list.iloc[movie_vector[i][0]].title)
        to_show_movies_poster.append(get_poster_from_API(movie_id))
        to_show_overiew.append(ID_overview.iloc[movie_vector[i][0]].overview)
    return to_show_movies , to_show_movies_poster , to_show_overiew

movies_list = pickle.load(open("Movies_re.pkl",'rb'))
list_of_movies = movies_list['title'].values
interaction_movies = pickle.load(open("interaction_vector_movies.pkl",'rb'))
st.title('Movie Recommender Systems')
option = st.selectbox('Which movie you watched recently',list_of_movies)
ID_overview = pickle.load(open("ID_overview.pkl","rb"))

selected_movie = option
if st.button('Press for recommendations'):
    movie_to_show  , poster_to_show ,overview_to_show= recommend_movie(selected_movie)
    tab1, tab2, tab3 ,tab4 , tab5 , tab6 , tab7 , tab8 , tab9 , tab10 = st.tabs(movie_to_show)
    col1, col2, col3 , col4 , col5 , col6 , col7 , col8 ,col9 , col10 = st.columns(10,gap = "large")
    with tab1:
        st.text(movie_to_show[0])
        st.image(poster_to_show[0],width=200)
        st.write(overview_to_show[0])

    with tab2:
        st.text(movie_to_show[1])
        st.image(poster_to_show[1] ,width=200)
        st.write(overview_to_show[1])

    with tab3:
        st.text(movie_to_show[2])
        st.image(poster_to_show[2] , width=200)
        st.write(overview_to_show[2])

    with tab4:
        st.text(movie_to_show[3])
        st.image(poster_to_show[3],width=200)
        st.write(overview_to_show[3])

    with tab5:
        st.text(movie_to_show[4])
        st.image(poster_to_show[4],width=200)
        st.write(overview_to_show[4])

    with tab6:
        st.text(movie_to_show[5])
        st.image(poster_to_show[5],width=200)
        st.write(overview_to_show[5])

    with tab7:
        st.text(movie_to_show[6])
        st.image(poster_to_show[6],width=200)
        st.write(overview_to_show[6])

    with tab8:
        st.text(movie_to_show[7])
        st.image(poster_to_show[7],width=200)
        st.write(overview_to_show[7])

    with tab9:
        st.text(movie_to_show[8])
        st.image(poster_to_show[8],width=200)
        st.write(overview_to_show[8])

    with tab10:
        st.text(movie_to_show[9])
        st.image(poster_to_show[9],width=200)
        st.write(overview_to_show[9])

# st.write('You selected:', option)