from nltk.corpus import wordnet as wn
import requests, json

# def checkPrice(ingredients):
#     totalMealPrice = 0
#     mylist = []
#     food = wn.synset('food.n.02')
#     food_lexicon = list(set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()])) 
#     for i in food_lexicon:
#         for j in ingredients:
#             if (j.find(i)):
#                 mylist.append(i)

#     for i in mylist:    
#         params = {
#             'query': i,
#             'apiKey': 'adv6exs237w9pju9rug6bsuv',
#         }

#         r = requests.get('http://api.walmartlabs.com/v1/search?', params=params)
#         price = r.json()['items'][0]['salePrice']
#         totalMealPrice += price
#     return totalMealPrice

def getPrice(words):
    totalMealPrice = 0
    word_list = words.split()
    food_list = getFoodList()
    mylist = []
    for i in food_list:
        for word in word_list:
            if (word == i):
                mylist.append(i)
    for item in mylist:    
        params = {
            'query': item,
            'apiKey': 'adv6exs237w9pju9rug6bsuv',
        }
        r = requests.get('http://api.walmartlabs.com/v1/search?', params=params)
        price = r.json()['items'][0]['salePrice']
        totalMealPrice += price
    return totalMealPrice

def getFoodList():
    food = wn.synset('food.n.02')
    food_lexicon = list(set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))
    food_lexicon.append('rice')
    food_lexicon.append('gravy')
    return food_lexicon
