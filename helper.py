from urlextract import URLExtract


def fetch_stats(selected_user,df):
    if selected_user!='Overall':
        df=df[df['user']==selected_user]
    # 1. fetch number of messages
    num_messages=df.shape[0]
    # 2. number of words
    words=[]
    for message in df['message']:
            words.extend(message.split())
    # 3. fetch number of media messages
    num_media_messages=df['message'].str.contains('<Media omitted>\n',na=False).sum()
    # 4. fetch number of links across messages shared
    links=[]

    extractor=URLExtract()
    for message in df['message']:
         links.extend(extractor.find_urls(message))
    num_links=len(links)




    return num_messages,len(words),num_media_messages,num_links  

def fetch_most_busy_users(df):
     
    x=df['user'].value_counts().head()
    df=round((df['user'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={'user':'Name','count':'Percent'})

    return x,df



    