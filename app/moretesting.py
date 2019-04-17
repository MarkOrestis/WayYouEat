import nltk
from fuzzywuzzy import fuzz
from nltk.corpus import wordnet as wn
import requests

ingredients = "1 cup soy sauce (preferably low-sodium), 1 cup Coca-Cola, 1/4 cup toasted sesame oil, 1/4 cup hoisin sauce, 4 cloves garlic, chopped, 4 scallions, minced, 2 rib-eye steaks (bone-in or boneless), or other steak, such as sirloin"
tokens = nltk.word_tokenize(ingredients)
tagged = nltk.pos_tag(tokens)

word_list = []
for i in tagged:
    if (i[1] == 'NN' or i[1] == 'NNS'):
      word_list.append(i[0])
result = ' '.join(word_list)

#Output
'cup soy sauce low-sodium cup cup oil cup hoisin sauce cloves scallions steaks bone-in boneless steak sirloin'


food = wn.synset('food.n.02')
food_lexicon = list(set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))
string = '1 inch-thick boneless shell steak'
string2 = '1 cup soy sauce (preferably low-sodium), 1 cup Coca-Cola, 1/4 cup toasted sesame oil, 1/4 cup hoisin sauce, 4 cloves garlic, chopped, 4 scallions, minced, 2 rib-eye steaks (bone-in or boneless), or other steak, such as sirloin'
words = string2.split()
for i in food_lexicon:
    if (result == i):
        print('I exist: ', i)
    # print(i)
# print(fuzz.partial_ratio(result, another_result))
# print(result)