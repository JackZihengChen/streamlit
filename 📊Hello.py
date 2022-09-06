import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")
st.sidebar.info('This is a purely informational message', icon="ℹ️")
st.sidebar.warning('This is a warning', icon="⚠️")
st.sidebar.error('This is an error', icon="🚨")



st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)


"### Code segment in Python"

code = '''
def hello():
    print("Hello, Streamlit!")
'''
st.code(code, language='python')

st.balloons()


"### Code segment in C"

code = '''
int hello(int input){
    printf("Hello, Streamlit!");
    return 5;
}
'''
st.code(code, language='c')


"### Modal not supported by cloud"
code = '''
import streamlit_modal as modal
'''
st.code(code, language='python')
# open_modal = st.button("Pop out window")
# if open_modal:
#     modal.open()

# if modal.is_open():
#     with modal.container():
#         "### Interacting with the modal refreshes the entire webpage"
#         st.write("Some fancy text")
#         value = st.checkbox("Check me")
#         st.write(f"Checkbox checked: {value}")
        
#         "### Inserting simple HTML with CSS stylesheet"
#         HtmlFile = open("Okta.HTML", 'r', encoding='utf-8')
#         source_code = HtmlFile.read() 
#         components.html(source_code, width=750, height=500, scrolling=True)