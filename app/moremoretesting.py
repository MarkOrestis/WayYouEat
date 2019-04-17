from pyeasyga import pyeasyga

# setup data
data = [{'recipe': 'Korean Steak', 'value': 4, 'calories': 12},
        {'recipe': 'Salmon Kabayaki', 'value': 2, 'calories': 1},
        {'recipe': 'Pasta Frittata', 'value': 10, 'calories': 4},
        {'recipe': 'Persian Chicken', 'value': 1, 'calories': 1},
        {'recipe': 'Tuna Confit', 'value': 2, 'calories': 2}]


ga = pyeasyga.GeneticAlgorithm(data)       

# define a fitness function
def fitness(individual, data):
    values, calories = 0, 0
    for selected, recipe in zip(individual, data):
        if selected:
            values += recipe.get('value')
            calories += recipe.get('calories')
    if calories > 15:
        values = 0
    return values

ga.fitness_function = fitness              
ga.run()                                    
print(iterations)
print(ga.best_individual())   

#Output
(15, [0, 1, 1, 1, 1])               