import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_tfb3estd.json")
img_logo = Image.open("images/Logo.png")
img_knighttour_start = Image.open("images/Knight'sTour.png")
img_knighttour_result = Image.open("images/Knight'sTourResult.png")
img_sudoku = Image.open("images/Sudoku.png")
img_sudoku_result = Image.open("images/SudokuResult.png")
img_wordle_begin = Image.open("images/WordleBegin.png")
img_wordle_result = Image.open("images/WordleResult.png")

st.subheader("LogicPuzzles")
st.write("Developed by Brian Ta")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Developing Multiple Websites")
        st.write("##")
        st.write(
            """
           While working on this project I built website from PythonAnywhere, GitHub, Wix, Netlify, and StreamLit 
           to learn more about web devlopment. This Project has been worked on from Nov-Dec, 2022. StreamLit
           allows codes developed in Python to be displayed as a webpage. Most of the projects have been reworked  
           on for individual websites to run on their own, without the need of downloading codes into a repository.
           Previous Page built with Python in GitHub was transfered to Wix after continuous deployment errors. So
           the Wix Site mirrors what could of been the Python Website displayed in GitHub being 6 pages long.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_logo)
    with text_column:
        st.subheader("What is Logic Puzzles")
        st.write(
            """
            Logic Puzzles was an IB Project meant to create codes that was able to solve puzzles from Knight's Tour, Sudoku, and Wordle. 
            What makes something a logic puzzle is: Any problem that uses or requires thoughts and interpretations to come up with a 
            solution.
            """
        )
        st.write("[Link to Past Works >](https://github.com/PythonLogicPuzzle/LogicPuzzleProduct)")
        st.write("[Link to Wix Site >](https://logicpuzzlesproduc.wixsite.com/logic-puzzles)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_knighttour_start)
    with text_column:
        st.subheader("Knight's Tour")
        st.write(
            """
            This presents the format of the Knight's Tour Program made with Vue, a Javascript framework used to create interactable projects.
            With additional coding languages used like HTML and JavaScript. This program uses Warnsdroff's Algorithm to find possible solution 
            for Knight's Tour.
            """
        )
        st.write("[Link to Knight's Tour >](https://logicpuzzles-knights-tour.netlify.app/)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_knighttour_result)
    with text_column:
        st.subheader("Results of Knight's Tour Program")
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_sudoku)
    with text_column:
        st.subheader("Sudoku")
        st.write(
            """
            This presents the format of the Sudoku Program made with HTML, CSS, and JavaScript.
            """
        )
        st.write("[Link to Sudoku >](https://logicpuzzles-sudoku-solver.netlify.app/)")        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_sudoku_result)
    with text_column:
        st.subheader("Results of Sudoku Program")
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_wordle_begin)
    with text_column:
        st.subheader("Wordle")
        st.write(
            """
            This presents the format of the Wordle Program made with HTML, CSS, and JavaScript.
            """
        )
        st.write("[Link to Wordle >](https://logicpuzzles-wordle-solver.netlify.app/)") 
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_wordle_result)
    with text_column:
        st.subheader("Results of Wordle Program")
        


