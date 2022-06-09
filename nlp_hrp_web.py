import streamlit as st
import pickle
import pandas as pd

# Extraer el modelo de machine learning


def main():
    st.title('Modelamiento de historias clinicas con word embedding')

    st.sidebar.header('User input pipeline')

    option_algo = ['Average','Clustering','PCA']
    option_word_emb = ['FastText','GloveNoCor', 'W2VNoCor', 'GloveCor', 'W2VCor', 'W2VTrained']
    option_ml_model = ['LogReg', 'MLP', 'SVC', 'RF', 'KNN']

    algo = st.sidebar.selectbox('Which algorithm do you like to use?',option_algo)
    word_emb = st.sidebar.selectbox('Which word embbeding do you like to use?',option_word_emb)
    ml_model = st.sidebar.selectbox('Which ML model do you like to use?',option_ml_model)


if __name__ == '__main__':
    main()