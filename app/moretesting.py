def subset(array, num):
    result = []
    meals = []
    def find(arr, num, path=()):
        if not arr:
            return
        if arr[0][0] == num:
            result.append(path + (arr[0][0],arr[0][1]))
        else:
            find(arr[1:], num - arr[0][0], path + (arr[0][0], arr[0][1]))
            find(arr[1:], num, path)
    find(array, num)
    for i in range(len(result) - 1):
        if len(result[i]) == 6:
            meals.append(result[i])
    return meals

# arr = [3, 4, 12, 10, 8, 5, 9, 18, 20, 14, 1, 1, 2, 1]
arr = [(3, 'yo'), (4, 'hai'), (12, 'hi'), (10, 'allbymyself'), (8, 'ohmygod'), (5, 'awlord'), (9, 'please'), (18, 'plox'), (20, 'ihatehtis'), (14, 'but'), (1, 'shh'), (1, 'phmy'), (2, 'stap'), (1, 'nah')]

n = 20
meals = []

# for i in range(len(subset(arr, n)) - 1):
#     if len(subset(arr, n)[i]) == 3: 
#         meals.append(subset(arr,n)[i])
print(subset(arr, n))
