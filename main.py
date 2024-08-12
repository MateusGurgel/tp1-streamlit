import streamlit as st
import pandas as pd

def read_spotfy_date() -> pd.DataFrame:
    data = pd.read_csv("./data/spotfy.csv", encoding='latin1')
    return data

def get_three_musics(data: pd.DataFrame) -> pd.DataFrame:
    return data.sample(3)

def show_track(music_name: str, artist_name: str, number_of_streams: int, all_time_ranking: int) -> None:
    st.title(music_name)
    artist_name
    st.metric("Spotfy Streams", number_of_streams, all_time_ranking)

def dashboard():
    
    st.title("Most streamed songs")
    st.subheader("This is a simple Streamlit app about streamed songs.")
    st.dataframe(read_spotfy_date())

    st.title("Random Sample songs")
    
    columns = st.tabs(["firs song", "second song", "third song"])

    for track, column in zip(get_three_musics(read_spotfy_date()).iterrows(), columns):
        with column:
            show_track(track[1]["Track"], track[1]["Artist"], track[1]["Spotify Streams"], track[1]["All Time Rank"])



if __name__ == "__main__":
    dashboard()