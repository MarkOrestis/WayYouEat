import requests, json, random, math
from flask import request

def setDiet():
    if (request.path == '/low-carb'):
        diet = 'low-carb'
    elif (request.path == '/low-fat'):
        diet = 'low-fat'
    elif (request.path == '/high-protein'):
        diet = 'high-protein'
    return diet

def getRecipes():
    diet = setDiet()

    params = {
        'q': 'steak',
        'app_id': 'ddf72e19',
        'app_key': '252dcc512fe4f78bd1ab7a3004b42e18',
        'diet': diet, 
        'from': 0,
        'to': 10
    }
    r = requests.get('https://api.edamam.com/search?', params=params)
    recipes=r.json()['hits']
    
    return subset(recipes, 2000)

def subset(array, num):
    result = []
    meals = []
    def find(arr, num, path=()):
        if not arr:
            return
        else:
            recipe = arr[0]['recipe']['label']
            calories = round_up(arr[0]['recipe']['calories']/arr[0]['recipe']['yield'],-2)

            if calories == num:
                result.append(path + (recipe,))
            else:
                find(arr[1:], num - calories, path + (recipe,))
                find(arr[1:], num, path)
    find(array, num)
    # print('results ', result)
    # for i in range(len(result) - 1):
    #     if len(result[i]) == 3:
    #         meals.append(result[i])
    return result

# getRecipes()
# round_up(calories, -2)
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

# getRecipes()
# print(round(1114/6, -2))