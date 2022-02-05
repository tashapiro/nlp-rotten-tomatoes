import streamlit as st 
import pandas as pd
import pickle 
import gdown


st.title('Movie Review Prediction')

st.subheader("What is this?")

st.write('This project uses NLP classification to assess whether a movie review is **Fresh** (good) or **Rotten** (bad).')

st.subheader("Let's Predict!")

st.write('Predict the review')

input_var = st.text_input(label="Enter your movie review here:")

#solution from https://discuss.streamlit.io/t/git-pull-failed-while-deploying/17258
model_url = 'https://drive.google.com/uc?id=1FEVxl4BY1d5ySV0IYIUMTwjik0-RaCDa'
output = 'svm_pickle.pkl'
pipe =  gdown.download(model_url, output, quiet=False) 


with open(pipe,mode='rb') as pickle_in:
    pipe_f = pickle.load(pickle_in)

pred = pipe_f.predict([input_var])[0]


if input_var == '':
    st.write("")

else:
    if pred == 'Fresh':
        emoji_var = '🍅'
    elif pred=='Rotten':
        emoji_var = '🤢'
    
    st.write(f'The movie review is **{pred}**. {emoji_var}')
