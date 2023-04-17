
# Text Classification of News Headline using ML/DL/NLP

Team QuadClan has tried to built a model for the following problem statement:

"To build a text classification system that can classify a given new headline in one or more categories.

Students are needed to develop a product that can search for recent headlines from the web related to an incident/person/event given by user and extract the most recent one

Students are supposed to scrap the most recent website and extract the headline from it.

Students are needed to use suitable NLP/ML/DL techniques to classify it into various categories and display the output.

Students are also needed to apply sentiment analysis on the headlines and classify them as positive, negative or neutral

Students should not use a pre-trained model directly for sentiment analysis but should also fine tune it themselves before using it in their product.

The product must provide a user interface that allows users to give an input, view the resulting headline and get the headline category.

The user interface should be easy to use and understand and should include features such as auto search complete."



## 🚀 Team QuadClan

- Aayush Kumar Mishra
(2nd Year),B.Tech. Electronics and communication Engineering, Indian Institute of Information Technlogy, Ranchi.


- Aarav Vijayvargiya
(2nd Year),B.Tech. Electronics and communication Engineering, Indian Institute of Information Technlogy, Ranchi.

- Ashish Kumar
(2nd Year),B.Tech. Electronics and communication Engineering, Indian Institute of Information Technlogy, Ranchi.

- Pushkar Prakash
(2nd Year),B.Tech. Electronics and communication Engineering, Indian Institute of Information Technlogy, Ranchi.
## Tech Stack

**Client:** Streamlit, CSS

**Server:** Machine learning algorithms(Logistic regression), Tfidf vector transform


## FAQ

#### What is our idea?

Answer : Our idea was to build a user friendly interface that takes a keyword as an input, searches for relevant news across the web, and predicts the sentiment and category associated with the news.

#### What is the approach behind this idea?

Answer: We tried to build a machine learning model using the natural language processing techniques of ML.
We used a 'BBC news' data set to train our model and predict the category. To predict the sentiment, we used the spacy Text Blob library. After finding out that it was logositic regression that was the most accurate algorithm we deployed the ML model on streamlit.




## Real Life applications

This project can used in the following domains:

- Filtering news based upon their sentiments.
- to customize the news feed based upon a specific category.




## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`pip install streamlit`

and finally run the web.py file in the terminal by the following command

`streamlit run web.py`


## Documentation

[Explore the website](https://drive.google.com/file/d/1jCdZH40tCHesGp_laHf52Hu2l00JeQjy/view?usp=share_link)

[Link to the youtube video](https://youtu.be/4ENHzCD4ZfA)

