import pandas as pd
import speech_recognition as sr
from textblob import TextBlob
df = pd.read_csv('D:\\AIDS\\TV\\7817_1.csv')
def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'
def analyze_sentiment_from_dataset():
    print("Analyzing sentiment from dataset:")
    for index, row in df.tail().iterrows():
        sentiment = analyze_sentiment(row['reviews.text'])  
        print(f"Sentiment of row {index + 1}: {sentiment}")
        print("Text Data:")
        print(row['reviews.text'])  
        print()
def audio_to_text_and_sentiment():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...") 
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)
        print("Processing...")  
        try:
            text = recognizer.recognize_google(audio_data)
            print("Text from audio:", text)  
            sentiment = analyze_sentiment(text)
            print("Sentiment from audio input:", sentiment)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
print("\n for data set")
analyze_sentiment_from_dataset()
print("\nAnalyzing sentiment from live audio input:")
audio_to_text_and_sentiment()
