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

# Токенизация. Разбиения на слова
text = input()
words = word_tokenize(text, language="russian")

# Лемматизация. Приведение слов к нормальной (словарной) форме

morph = pymorphy3.MorphAnalyzer()
names = []
normalized_words = []
prev_word = ''
for word in words:
    if word[0].isupper() and (prev_word != '.' or prev_word != ''):
        names.append(word)
    normalized = morph.parse(word)[0].normal_form
    normalized_words.append(normalized)
    prev_word = word

# Удаление стоп-слов. Удаление "шума", слов, которые несут мало смысла
filtered_normalized_words = []
stop_words = stopwords.words("russian")
stop_words += ['это', 'свой', 'который', '-']
for word in normalized_words:
    if word not in stop_words:
        filtered_normalized_words.append(word) 

# Подсчёт ключевых слов в пользоавтельском тексте
most_common = Counter(filtered_normalized_words).most_common(10)
most_common = dict(most_common)
keywords = list(most_common.keys()) + names


### Поиск в датасете

prev_word = ''
names = []
normalized_words_dataset = []
counter = 0

df = pd.read_json('Reviews/kinopoisk.jsonl', encoding='utf8', lines=True)
reviews = df.get('content')
names_dataset = []
filtered_normalized_words_dataset = []
for review in reviews:
    review = review.split()
    for word in review:
        normalized = morph.parse(word)[0].normal_form        
        prev_word = review[review.index(word) - 2]
        if word[0].isupper() and (prev_word != '.' or prev_word != ''):
            names_dataset.append(word)
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


# Проверка
print(keywords)
print(names)
print(keywords_dataset)
print(names_dataset)
