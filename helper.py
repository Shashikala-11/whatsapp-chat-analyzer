def fetch_stats(selected_user,df):
    if selected_user=='Overall':
        # 1. fetch number of messages
        num_messages=df.shape[0]
        # 2. number of words
        words=[]
        for message in df['message']:
            words.extend(message.split())
        return num_messages,len(words)    
    else:
        return df[df['user']==selected_user].shape[0]