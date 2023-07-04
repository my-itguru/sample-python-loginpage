import streamlit as st
import pandas as pd

def load_credentials():
    credentials = pd.read_csv('credentials.csv')
    return credentials

def login(username, password):
    credentials = load_credentials()
    match = credentials[(credentials['username'] == username) & (credentials['password'] == password)]
    if len(match) == 1:
        return True
    else:
        return False

def main():
    st.title('User Login')

    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    login_button = st.button('Login')

    if login_button:
        if login(username, password):
            st.success('Login successful!')
        else:
            st.error('Invalid username or password')

if __name__ == '__main__':
    main()
