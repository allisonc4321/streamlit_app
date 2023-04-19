import streamlit as st

st.title('Title of your application')
st.markdown('this is **bold text**')
st.markdown('this is *italic text*')

st.sidebar.title('Title of sidebar')
st.sidebar.markdown('markdown **text** in the *sidebar*')

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')
    st.markdown('this is markdown **text**')

agree_sidebar = st.sidebar.checkbox('side bar checkbox')

if agree_sidebar:
    st.sidebar.write('side bar checked')
