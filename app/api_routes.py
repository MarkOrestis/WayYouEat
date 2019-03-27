import requests, json, random, math
from flask import request

start = 0

def getRange():
    if (request.path == '/low-carb'):
        start = round(random.uniform(0, 182294))
    elif (request.path == '/low-fat'):
        start = round(random.uniform(0, 88121))
    elif (request.path == '/high-protein'):
        start = round(random.uniform(0, 13401))
    return start

def getRecipes():
    # this is unnecessary since I can only call the first 100 recipes with each call
    # start = getRange()

    params = {
        'q': 'chicken, vegetables',
        'app_id': 'ddf72e19',
        'app_key': '252dcc512fe4f78bd1ab7a3004b42e18',
        'diet': 'low-carb', 
        'from': 0,
        'to': 10
    }
    print(params)

    r = requests.get('https://api.edamam.com/search?', params=params)
    recipes=r.json()['hits']
    print('Calories ' , round(recipes[0]['recipe']['calories']/recipes[0]['recipe']['yield']))
    results = subset(recipes, 2000)
    return results

def subset(array, num):
    result = []
    meals = []
    def find(arr, num, path=()):
        if not arr:
            return
        else:
            if round_up(arr[0]['recipe']['calories']/arr[0]['recipe']['yield'],-2) == num:
                result.append(path + (round_up(arr[0]['recipe']['calories']/arr[0]['recipe']['yield'],-2), arr[0]['recipe']['label']))
            else:
                find(arr[1:], num - round_up(arr[0]['recipe']['calories']/arr[0]['recipe']['yield'],-2), path + (round_up(arr[0]['recipe']['calories']/arr[0]['recipe']['yield'],-2), arr[0]['recipe']['label']))
                find(arr[1:], num, path)
    find(array, num)
    # print('results ', result)
    for i in range(len(result) - 1):
        if len(result[i]) == 6:
            meals.append(result[i])
    print('hallo')
    return meals

# getRecipes()
# round_up(calories, -2)
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

getRecipes()
# print(round(1114/6, -2))