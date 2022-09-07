import streamlit as st
import pandas as pd
import extra_streamlit_components as stx

@st.cache(allow_output_mutation=True)

def get_manager():
    return stx.CookieManager()

cookie_manager = get_manager()


st.write("# Cookie Manager")
st.subheader("All Cookies:")
cookies = cookie_manager.get_all()
st.write(cookies)


if cookie_manager.get(cookie='user') != None:
    st.sidebar.write("## Signed in")
    if st.sidebar.button('Sign out'):
        cookie_manager.delete('user')

    placeholder1 = st.empty()
    placeholder2 = st.empty()
    placeholder1.title("SMARTS Webapp Home Page")
else:
    st.sidebar.write("## Sign in")
    text_input_container = st.sidebar.empty()
    df = pd.DataFrame({
        'first column': ["","Using a JWT token","Using Okta"],
    })
    option = st.sidebar.selectbox(
        'Which method would you want to?',
        df['first column'])

    if option=="Using a JWT token":
        st.text_input("JWT token", key="jwt_token")
        if st.session_state.jwt_token:
            cookie_manager.set('user', st.session_state.jwt_token)

    elif option=="Using Okta":
        st.text_input("Okta token", key="okta_state")
        if st.session_state.okta_state:
            cookie_manager.set('user', st.session_state.okta_state)
            






