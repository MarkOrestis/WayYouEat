import requests, json, random, math
from flask import request

def subset(array, num):
    result = []
    meals = []
    def find(arr, num, path=()):
        if not arr:
            return
        else:
            recipe = arr[0]['label']
            calories = arr[0]['calories']

            if calories == num:
                result.append(path + (recipe + ' Calories: ' 
                    + str(calories), ))
            else:
                find(arr[1:], num - calories, path + 
                    (recipe + ' Calories: ' + str(calories), ))
                find(arr[1:], num, path)
    find(array, num)
    return result

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier