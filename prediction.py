from textblob import TextBlob
import streamlit as st
sentiment=[]

def predict_sentiment(**news_dict):
    titles=news_dict['Titles']
    count=len(titles)
    if count==1:
        st.text_area(label="Predicted Sentiment",value=sentiment_analyzer(titles[0]),key='10')
    elif count==2:
        left,right=st.columns(2)
        left.text_area(label="Predicted Sentiment",value=sentiment_analyzer(titles[0]),key='11')
        right.text_area(label="Predicted Sentiment",value=sentiment_analyzer(titles[1]),key='12')
    elif count==3:
        left,center,right=st.columns(3)
        left.text_area(label="Predicted Sentiment",value=sentiment_analyzer(titles[0]),key='13')
        center.text_area(label="Predicted Sentiment",value=sentiment_analyzer(titles[1]),key='14')
        right.text_area(label="Predicted Sentiment",value=sentiment_analyzer(titles[2]),key='15')
    elif count==4:
        left,center1,center2,right=st.columns(4)
        left.text_area(label="Predicted Sentiment",value=sentiment_analyzer(titles[0]),key='widget1')
        center1.text_area(label="Predicted Sentiment",value=sentiment_analyzer(titles[1]),key='widget2')
        center2.text_area(label="Predicted Sentiment",value=sentiment_analyzer(titles[2]),key='widget3')
        right.text_area(label="Predicted Sentiment",value=sentiment_analyzer(titles[3]),key='widget4')
def sentiment_analyzer(headline):
    data=TextBlob(headline)
    polarity=data.sentiment[0]
    if(polarity>0):
        return 'Positive News'
    elif polarity<0:
        return 'Negative News'
    else:
        return 'Neutral'
    
def create_sent_list(**news_dict):
    titles=news_dict['Titles']
    count=len(titles)
    sentiment=[]
    for i in range(count):
        sentiment.append(sentiment_analyzer(titles[i]))
    return sentiment


