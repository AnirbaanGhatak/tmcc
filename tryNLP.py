import pandas as pd
import nltk
import seaborn as sns
import matplotlib.pyplot as plt



nltk.download('punkt')
nltk.download('stopwords')
# Load the credit card data from the Excel sheet
df = pd.read_excel('All_CC_Details.xlsx')

# Preprocess the data
def preprocess(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    # Lowercase the words
    words = [word.lower() for word in words]
    # Remove stop words
    stop_words = set(nltk.corpus.stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    # Stem the words
    stemmer = nltk.stem.PorterStemmer()
    words = [stemmer.stem(word) for word in words]
    # Join the words back into a single string
    return ' '.join(words)

# Preprocess the "Welcome Bonus" column
df['Welcome Bonus'] = df['Welcome Bonus'].astype(str).apply(preprocess)


# Convert the "Welcome Bonus" column into a bag of words representation
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['Welcome Bonus'])

# Use the bag of words representation to score the Welcome Bonus of each credit card
from sklearn.metrics.pairwise import cosine_similarity
scores = cosine_similarity(X)

# Get the indices of the credit cards with the highest scores
top_indices = scores.argmax(axis=1)

# Define a function to score the reward redemption policy
def score_policy(policy):

    return sum([1 for word in policy.split() if word in ["bonu", "voucher", "complimentari"]]) / len(policy.split()) * 10

# Add a new column to store the scores of each reward redemption policy
df['Welcome Bonus'] = df['Welcome Bonus'].astype(str).apply(score_policy)

# Print the credit cards with the highest scores
for i, score in enumerate(top_indices):
    print('Credit Card {}: {} '.format(i, df['Names'][score]))
