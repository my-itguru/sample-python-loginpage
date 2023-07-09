import streamlit as st
import streamlit.components.v1 as components
import csv
import os

def login(username, password):
    """
    Checks if the username and password match a credential in the credentials.csv file.

    Args:
        username: The username to check.
        password: The password to check.

    Returns:
        True if the username and password match, False otherwise.
    """

    with open('credentials.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == username and row[1] == password:
                return True
    return False

def main():
    st.title('User Login')

    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    login_button = st.button('Login')

    if login_button:
        if login(username, password):
            st.success('Login successful!')
            st.write('Redirecting to home page...')
            st.session_state['username'] = username
            home_file = open('home.html','r')
            home = home_file.read()
            st.markdown(home,unsafe_allow_html=True)

            st.markdown('[Go to Settings](settings)')
            if st.session_state.get('page') == 'settings':
                st.write('Settings page')
                settings_file = open('settings.html','r')
                settings = settings_file.read()
                st.markdown(settings,unsafe_allow_html=True)
                settings = settings_file.close()
            home = home_file.close()

        else:
            st.error('Invalid username or password')

if __name__ == '__main__':
    main()
