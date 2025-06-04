import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("reviews.csv", quotechar='"')

def get_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Review"].apply(get_sentiment)

print(df)

sns.countplot(x="Sentiment", data=df)
plt.title("Sentiment Distribution")
plt.show()
