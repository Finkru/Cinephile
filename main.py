# nltk.download('punkt')
# nltk.download('stopwords')
import nltk # https://www.nltk.org/
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import SnowballStemmer
import pymorphy3 # https://pymorphy2.readthedocs.io/en/stable/user/guide.html#id2
import pandas as pd

# Токенизация. Разбиения на слова
text = input()
words = word_tokenize(text, language="russian")

# Лемматизация. Приведение слов к нормальной (словарной) форме

morph = pymorphy3.MorphAnalyzer()
normalized_words = []
for word in words:
    normalized = morph.parse(word)[0].normal_form
    normalized_words.append(normalized)

# Удаление стоп-слов. Удаление "шума", слов, который не несут смысл
filtered_normalized_words = []
stop_words = stopwords.words("russian")
for word in normalized_words:
    if word not in stop_words:
        filtered_normalized_words.append(word) 

# Проверка получившихся нормальных слов
print(filtered_normalized_words)

# Пока что хиленькое выделение ключей, надо через tensorflow
frequency = FreqDist(filtered_normalized_words)
print(frequency.most_common(3))

# Чтение отзывов
reviews = pd.read_json('reviews/kinopoisk.jsonl', lines=True)
print(reviews.sample(5))







# One of the other reviewers has mentioned that after watching just 1 Oz episode you'll be hooked. They are right, as this is exactly what happened with me.<br /><br />The first thing that struck me about Oz was its brutality and unflinching scenes of violence, which set in right from the word GO. Trust me, this is not a show for the faint hearted or timid. This show pulls no punches with regards to drugs, sex or violence. Its is hardcore, in the classic use of the word.<br /><br />It is called OZ as that is the nickname given to the Oswald Maximum Security State Penitentary. It focuses mainly on Emerald City, an experimental section of the prison where all the cells have glass fronts and face inwards, so privacy is not high on the agenda. Em City is home to many..Aryans, Muslims, gangstas, Latinos, Christians, Italians, Irish and more....so scuffles, death stares, dodgy dealings and shady agreements are never far away.<br /><br />I would say the main appeal of the show is due to the fact that it goes where other shows wouldn't dare. Forget pretty pictures painted for mainstream audiences, forget charm, forget romance...OZ doesn't mess around. The first episode I ever saw struck me as so nasty it was surreal, I couldn't say I was ready for it, but as I watched more, I developed a taste for Oz, and got accustomed to the high levels of graphic violence. Not just violence, but injustice (crooked guards who'll be sold out for a nickel, inmates who'll kill on order and get away with it, well mannered, middle class inmates being turned into prison bitches due to their lack of street skills or prison experience) Watching Oz, you may become comfortable with what is uncomfortable viewing....thats if you can get in touch with your darker side
# Йеллоустоун – первый в мире национальный парк, одно из самых посещаемых мест в США. Но здесь, на границе цивилизации, происходит много такого, чего не видят туристы, что не освещается средствами массовой информации. Семья Даттон, главой которой является Джон Даттон, владеет огромным ранчо, сопредельным с территорией парка. На их землю претендует и сам парк, и индейская резервация, и жадные застройщики.

