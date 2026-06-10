import streamlit as st 
import preprocessor,helper
import matplotlib.pyplot as plt

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

        num_messages,words,num_media_messages,num_links=helper.fetch_stats(selected_user,df)
        col1,col2,col3,col4=st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Total Media Count")
            st.title(num_media_messages)
        with col4:
            st.header("Total Links Shared")
            st.title(num_links)

        # finding the busiest/ chatiest users in the group (Group level)
        st.title("Most Busy Users")
        if selected_user=='Overall':
           
            x,new_df=helper.fetch_most_busy_users(df)
            fig,ax=plt.subplots()
            
            

            c1,c2=st.columns(2)
            with c1:
                ax.bar(x.index,x.values,color='orange')
                plt.xticks(rotation=-270)
                st.pyplot(fig)

            with c2:
                st.dataframe(new_df)
                pass    
                



                    
        pass



