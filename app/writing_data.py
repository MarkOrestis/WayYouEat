from api_routes import getRecipes
import requests

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
    
    for i in recipes:
        ingredients = []
        diets = []
        label = i['recipe']['label']
        calories = i['recipe']['calories']
        ingredient_lines = i['recipe']['ingredientLines']
        diet_labels = i['recipe']['dietLabels']
        string_diet = ', '.join(ingredient_lines)
        print(string_diet)
        rec = Recipes(label, calories, ingredient_lines, diet_labels)
        list.append(rec)
    
    print(list[0].diets)
    

    # data = getRecipes()
    # print(data)
    
class Recipes:
    def __init__(self, label, calories, ingredients, diets):
        self.label = label
        self.calories = calories
        self.ingredients = ingredients
        self.diets = diets

please_work()


