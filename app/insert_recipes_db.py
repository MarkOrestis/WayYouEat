import app
def fill_database():
    params = {
        'q': 'turkey',
        'app_id': 'ddf72e19',
        'app_key': '252dcc512fe4f78bd1ab7a3004b42e18', 
        'diet': '',
        'from': 0,
        'to': 10
    }
    r = requests.get('https://api.edamam.com/search?', params=params)
    recipes=r.json()['hits']

    for i in recipes:
        label = i['recipe']['label']
        calories = round_up(i['recipe']['calories']/i['recipe']['yield'],-2)
        ingredient_lines = i['recipe']['ingredientLines']
        description = i['recipe']['url']
        diet_labels = i['recipe']['dietLabels']

        string_diet = ', '.join(diet_labels)
        string_ingredients = '- '.join(ingredient_lines)
        
        new_recipe = Recipe(label, calories, string_diet, string_ingredients, description)
        db.session.add(new_recipe)
        db.session.commit()
    return recipe_schema.jsonify(new_recipe)
    recipe = Recipe.query.filter(Recipe.label == 'Korean Steak')
    maybe = recipes_schema.dump(recipe)
    for i in maybe:
        if (i != {}):
            ingredients = i[0]['ingredients'].split('- ')
            # ingredients.append(i[0]['ingredients'])