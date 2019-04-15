from api_routes import getRecipes
import requests
import pickle

def please_work():
    params = {
        'q': 'steak',
        'app_id': 'ddf72e19',
        'app_key': '252dcc512fe4f78bd1ab7a3004b42e18',
        'diet': 'low-carb', 
        'from': 0,
        'to': 10
    }
    r = requests.get('https://api.edamam.com/search?', params=params)
    recipes=r.json()['hits']
    list = []
    
    for i in recipes:
        ingredients = []
        label = i['recipe']['label']
        calories = i['recipe']['calories']
        ingredientLines = i['recipe']['ingredientLines']
        for j in ingredientLines:
            ingredients.append(j)
        rec = Recipes(label, calories, ingredients)
        list.append(rec)
    print(ingredients)
    file1 = open('data.txt', 'w')
    file1.write(pickle.dumps(list))
    file1.close()

    # data = getRecipes()
    # print(data)
    
class Recipes:
    def __init__(self, label, calories, ingredients):
        self.label = label
        self.calories = calories
        self.ingredients = ingredients
please_work()


