import streamlit as st 
import preprocessor,helper
# from helper import fetch_stats

st.sidebar.title('Whatsapp Chat Analyzer')

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    #convert bytes data into utf-8 as encoding format
    data=bytes_data.decode("utf-8")
    # st.text(data)

    df=preprocessor.preprocessor(data)
    st.dataframe(df)

    # to fetch unique users
    user_list=df['user'].unique().tolist()
    user_list.remove('Notification')
    user_list.sort()
    user_list.insert(0,"Overall")

    # storing selected user names 

    selected_user=st.sidebar.selectbox("Show Analysis wrt",user_list)

    if st.sidebar.button("Show Analysis"):

        # passing the name of selected user to fetch_stats function to get the total no. of messages.

        num_messages=helper.fetch_stats(selected_user,df)
        col1,col2,col3,col4=st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        pass



