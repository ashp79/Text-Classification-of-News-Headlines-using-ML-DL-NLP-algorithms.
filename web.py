import streamlit as st
import pickle
from textblob import TextBlob
from newsapi import get_news
import pandas as pd
import base64
from prediction import predict_sentiment,create_sent_list

st.set_page_config(layout="wide")
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('image11.jpg')
df=pd.DataFrame()

tfidf = pickle.load(open('Vectorizer_project.pkl','rb'))
model= pickle.load(open('projectmodel.pkl','rb'))
st.write('<h1 style="font-family: Georgia; font-size: 48px; font-weight: bold; color: black;text-align:center">  </h1>', unsafe_allow_html=True)


def predict_category(**news_dict):
    titles=news_dict['Titles']
    num_to_cat={'[0]':'World Affairs Related News','[1]':'Technology based news','[2]':'National/International News','[3]':'Sports News','[4]':'Entertainment News'}
    count=len(titles)
    result=[]

    for i in range(count):
        tf_titles=tfidf.transform([titles[i]])
        result.append(str(model.predict(tf_titles)))
    if count==1:
        st.text_area(label="Predicted Category",value=num_to_cat[(result[0])])
    elif count==2:
        left,right=st.columns(2)
        left.text_area(label="Predicted Category",value=num_to_cat[(result[0])],key='1')
        right.text_area(label="Predicted Category",value=num_to_cat[(result[1])],key='2')
    elif count==3:
        left,center,right=st.columns(3)
        left.text_area(label="Predicted Category",value=num_to_cat[(result[0])],key='3')
        center.text_area(label="Predicted Category",value=num_to_cat[(result[1])],key='4')
        right.text_area(label="Predicted Category",value=num_to_cat[(result[2])],key='5')
    elif count==4:
        left,center1,center2,right=st.columns(4)
        left.text_area(label="Predicted Category",value=num_to_cat[(result[0])],key='6')
        center1.text_area(label="Predicted Category",value=num_to_cat[(result[1])],key='7')
        center2.text_area(label="Predicted Category",value=num_to_cat[(result[2])],key='8')
        right.text_area(label="Predicted Category",value=num_to_cat[(result[3])],key='9')
    category=[]
    for i in range(count):
        category.append(num_to_cat[(result[i])])
    
    sentiment=create_sent_list(**news_dict)
    df = pd.DataFrame({
    'Date and Time of the news': news_dict['dates'],
    'News Headline': news_dict['Titles'],
    'News Breif': news_dict['Headlines'],
    'Link to the News':news_dict['Links'],
    'Predicted Category':category,
    'Predicted Sentiment':sentiment})
    text="There you go!"
    st.write(f"<span style='color:black;font-size:24px;font-family:Georgia'>{text}</span>",unsafe_allow_html=True)
    text="Here is a table of the final Predictions"
    st.write(f"<span style='color:black;font-size:30px;font-family:Georgia'>{text}</span>",unsafe_allow_html=True)
    st.table(df)
    

def create_text_input_boxes(**news_dict):

    """Function to create text input boxes dynamically based on given count
    """
    
    titles=news_dict['Titles']
    summaries=news_dict['Headlines']
    dates=news_dict['dates']
    counts=news_dict['counts']
    URL=news_dict['Links']
    if counts==0:
        column =st.columns(1)
        st.text_area(label="ERROR: ",value=" No news found that matches this keyword. Please try again with a diffferent 'keyword'")
    elif  counts==1:
        if st.button('Generate News'):
            st.text_area(label="Date: ",value=dates[0],height=100)
            st.text_area(label="News Headline",value=titles[0],height=100)
            st.text_area(label="",value=summaries[0],height=200)
            st.text_area(label="Link to the news",value=URL[0],height=200)
            st.markdown(f'<a href="{URL[0]}" target="_blank" style="text-decoration: underline">{"Link to the website"}</a>', unsafe_allow_html=True)
            

    elif  counts==2:
        left,right=st.columns(2)
        if st.button('Generate News'):
            for i in range(counts):
                if i==0:
                    left.text_area(label=f"Date {i+1}: ",value=dates[i],height=100)
                    left.text_area(label=f"Healine {i+1}: ",value=titles[i],height=100)
                    left.text_area(label=f"{i+1}:",value=summaries[i],height=200)
                    left.text_area(label="Link to the news",value=URL[i],height=200)
                    left.markdown(f'<a href="{URL[i]}" target="_blank" style="text-decoration: underline">{"Link to the website"}</a>', unsafe_allow_html=True)
                elif i==1:
                    right.text_area(label=f"Date{i+1}: ",value=dates[i],height=100)
                    right.text_area(label=f"Headline{i+1}: ",value=titles[i],height=100)
                    right.text_area(label=f" ",value=summaries[i],height=200)
                    right.text_area(label="Link to the news",value=URL[i],height=200)
                    right.markdown(f'<a href="{URL[i]}" target="_blank" style="text-decoration: underline">{"Link to the website"}</a>', unsafe_allow_html=True)

                
    elif  counts==3:
        left,center,right=st.columns(3)
        if st.button('Generate News'):
            for i in range(counts):
                if i==0:
                    left.text_area(label=f"Date{i+1}: ",value=dates[i],height=100)
                    left.text_area(label=f"Headline{i+1}: ",value=titles[i],height=100)
                    left.text_area(label=" ",value=summaries[i],height=200)
                    left.text_area(label="Link to the news",value=URL[i],height=200)
                    left.markdown(f'<a href="{URL[i]}" target="_blank" style="text-decoration: underline">{"Link to the website"}</a>', unsafe_allow_html=True)

                elif i==1:
                    center.text_area(label=f"Date{i+1}: ",value=dates[i],height=100)
                    center.text_area(label=f"Headline{i+1}: ",value=titles[i],height=100)
                    center.text_area(label=f" ",value=summaries[i],height=200)
                    center.text_area(label="Link to the news",value=URL[i],height=200)
                    center.markdown(f'<a href="{URL[i]}" target="_blank" style="text-decoration: underline">{"Link to the website"}</a>', unsafe_allow_html=True)

                else:
                    right.text_area(label=f"Date{i+1}: ",value=dates[i],height=100)
                    right.text_area(label=f"Headline{i+1}: ",value=titles[i],height=100)
                    right.text_area(label=f" ",value=summaries[i],height=200)
                    right.text_area(label="Link to the news",value=URL[i],height=200)
                    right.markdown(f'<a href="{URL[i]}" target="_blank" style="text-decoration: underline">{"Link to the website"}</a>', unsafe_allow_html=True)

                
                
    elif counts==4:
        left,center1,center2,right=st.columns(4)
        if st.button('Generate News'):
            for i in range(counts):
                if i==0:
                    left.text_area(label=f"Date{i+1}: ",value=dates[i],height=100)
                    left.text_area(label=f"Headline{i+1}: ",value=titles[i],height=100)
                    left.text_area(label=f" ",value=summaries[i],height=200)
                    left.text_area(label="Link to the news",value=URL[i],height=200)
                    left.markdown(f'<a href="{URL[i]}" target="_blank" style="text-decoration: underline">{"Link to the website"}</a>', unsafe_allow_html=True)

                elif i==1:
                    center1.text_area(label=f"Date{i+1}: ",value=dates[i],height=100)
                    center1.text_area(label=f"Headline{i+1}: ",value=titles[i],height=100)
                    center1.text_area(label=f" ",value=summaries[i],height=200)
                    center1.text_area(label="Link to the news",value=URL[i],height=200)
                    center1.markdown(f'<a href="{URL[i]}" target="_blank" style="text-decoration: underline">{"Link to the website"}</a>', unsafe_allow_html=True)

                elif i==2:
                    center2.text_area(label=f"Date{i+1}: ",value=dates[i],height=100)
                    center2.text_area(label=f"Headline{i+1}: ",value=titles[i],height=100)
                    center2.text_area(label=f" ",value=summaries[i],height=200)
                    center2.text_area(label="Link to the news",value=URL[i],height=200)
                    center2.markdown(f'<a href="{URL[i]}" target="_blank" style="text-decoration: underline">{"Link to the website"}</a>', unsafe_allow_html=True)

                else:
                    right.text_area(label=f"Date{i+1}: ",value=dates[i],height=100)
                    right.text_area(label=f"Headline{i+1}: ",value=titles[i],height=100)
                    right.text_area(label=f" ",value=summaries[i],height=200)
                    right.text_area(label="Link to the news",value=URL[i],height=200)
                    right.markdown(f'<a href="{URL[i]}" target="_blank" style="text-decoration: underline">{"Link to the website"}</a>', unsafe_allow_html=True)
                    

keyword=st.text_input("Enter the keyword you want to search for",help="For e.g.: India")
news_dict=get_news(keyword)
create_text_input_boxes(**news_dict)
if st.button('Predict Sentiment'):
    add_bg_from_local('image12.jpg')
    predict_sentiment(**news_dict)
if st.button('Predict Category'):
    predict_category(**news_dict)
    add_bg_from_local('image12.jpg')



