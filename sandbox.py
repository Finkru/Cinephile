import nltk # https://www.nltk.org/
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import SnowballStemmer
import pymorphy3 # https://pymorphy2.readthedocs.io/en/stable/user/guide.html#id2
import pandas as pd
from collections import Counter

### Поиск в датасете
stop_words = stopwords.words("russian")
stop_words += ['это', 'свой', 'который', '-']
prev_word = ''
names = []
normalized_words_dataset = []
counter = 0
morph = pymorphy3.MorphAnalyzer()
df = pd.read_json('Reviews/kinopoisk.jsonl', encoding='utf8', lines=True)
reviews = df.get('content')
names_dataset = []
prev_word = ''
filtered_normalized_words_dataset = []
for review in reviews:
    review = review.split()
    for word in review:
        if word[0].isupper() and (prev_word != '.' or prev_word != ''):
            names_dataset.append(word)
        normalized = morph.parse(word)[0].normal_form
        normalized_words_dataset.append(normalized)
        prev_word = word
    for word in normalized_words_dataset:
        if word not in stop_words:
            filtered_normalized_words_dataset.append(word) 
    counter += 1
    if counter > 0:
        break

# Подсчёт ключевых слов в отзывах
most_common_dataset = Counter(filtered_normalized_words_dataset).most_common(10)
most_common_dataset = dict(most_common_dataset)
keywords_dataset = list(most_common_dataset.keys()) + names_dataset
print(keywords_dataset)