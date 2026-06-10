import re
import pandas as pd


def preprocessor(data):
    pattern='\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
    messages=re.split(pattern,data)[1:]
    dates=re.findall(pattern,data)
    dataframe={'User_message':messages,'message_date':dates}

    df=pd.DataFrame(dataframe)

    # convert message_date type 
    df['message_date']=pd.to_datetime(df['message_date'],format='%d/%m/%y, %H:%M - ')
    df.rename(columns={'message_date':'date'},inplace=True)

    df['user']=df['User_message'].str.split(':',expand=True)[0]
    df['message']=df['User_message'].str.split(':',expand=True)[1]

    mask=df['message'].isna()

    # moving notification to messaage

    df.loc[mask,'message']=df.loc[mask,'user']
    
    # set user as notification for group notification

    df.loc[mask,'user']='Notification'

    df['month']=df['date'].dt.month_name()
    df['Year']=df['date'].dt.year
    df['dates']=df['date'].dt.day
    df['day_name']=df['date'].dt.day_name()
    df['Hour']=df['date'].dt.hour
    df['Minute']=df['date'].dt.minute


    return df
