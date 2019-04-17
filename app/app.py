from flask import Flask, render_template, request, jsonify
from api_routes import subset, round_up
from get_price import getPrice
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import random
from random import randint
import os
import requests

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

@app.route('/')
def hello_world():
    # params = {
    #     'q': 'steak',
    #     'app_id': 'ddf72e19',
    #     'app_key': '252dcc512fe4f78bd1ab7a3004b42e18', 
    #     'diet': 'balanced',
    #     'from': 0,
    #     'to': 10
    # }
    # r = requests.get('https://api.edamam.com/search?', params=params)
    # recipes=r.json()['hits']

    # for i in recipes:
    #     label = i['recipe']['label']
    #     calories = round_up(i['recipe']['calories']/i['recipe']['yield'],-2)
    #     ingredient_lines = i['recipe']['ingredientLines']
    #     diet_labels = i['recipe']['dietLabels']

    #     string_diet = ', '.join(diet_labels)
    #     string_ingredients = '- '.join(ingredient_lines)
        
    #     new_recipe = Recipe(label, calories, string_diet, string_ingredients)
    #     db.session.add(new_recipe)
    #     db.session.commit()
    # return recipe_schema.jsonify(new_recipe)
    # recipe = Recipe.query.filter(Recipe.label == 'Korean Steak')
    # maybe = recipes_schema.dump(recipe)
    # for i in maybe:
    #     if (i != {}):
    #         ingredients = i[0]['ingredients'].split('- ')
    #         # ingredients.append(i[0]['ingredients'])
    return render_template('home.html')

#get all recipes
@app.route('/recipes', methods=['GET'])
def getDbRecipes():
    all_recipes = Recipe.query.all()
    result = recipes_schema.dump(all_recipes)
    return jsonify(result.data)

#get single recipe
@app.route('/recipes/<id>', methods=['GET'])
def get_recipe(id):
    recipe = Recipe.query.get(id)
    return recipe_schema.jsonify(recipe)

#delete single recipe
@app.route('/recipes/<id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    return recipe_schema.jsonify(recipe)

@app.route('/low-carb')
def low_carb():
    recipes = Recipe.query.filter(Recipe.diet_labels.contains('Low-Carb'))
    results = recipes_schema.dump(recipes)
    num = randint(0, 45)
    result = subset(results.data[num:(num+10)], 2000)
    random.shuffle(result)
    if results:
        print('Not empty')
        return render_template('low_carb.html', recipes=result)
    else:
        print('data empty')
        return

@app.route('/high-protein')
def high_protein():
    recipes = Recipe.query.filter(Recipe.diet_labels.contains('High-Protein'))
    results = recipes_schema.dump(recipes)
    # 47recipes
    num = randint(0, 37)
    result = subset(results.data[num:(num+10)], 2000)
    random.shuffle(result)
    return render_template('high_protein.html', recipes=result)

@app.route('/low-fat')
def low_fat():
    recipes = Recipe.query.filter(Recipe.diet_labels.contains('Low-Fat'))
    results = recipes_schema.dump(recipes)
    #47 recipes
    num = randint(0, 37)
    result = subset(results.data[num:(num+10)], 2000)
    random.shuffle(result)
    return render_template('low_fat.html', recipes=result)

@app.route('/balanced')
def balanced():
    recipes = Recipe.query.filter(Recipe.diet_labels.contains('Balanced'))
    results = recipes_schema.dump(recipes)
    # 47recipes
    num = randint(0, 37)
    result = subset(results.data[num:(num+10)], 2000)
    random.shuffle(result)
    return render_template('balanced.html', recipes=result)

@app.route('/recipe-details')
def price_form():
    return render_template('recipe_details.html')

@app.route('/recipe-details', methods=['GET', 'POST'])
def price_form_post():
    text = request.form['text']
    processed_text = text.lower()
    maybe = Recipe.query.filter(Recipe.label.contains(processed_text))
    result = recipes_schema.dump(maybe)
    price = getPrice(processed_text)
    final_price = "$" + str(price)
    return render_template('recipe_details.html', price=final_price , ingredients=result.data[0]['ingredients'],
        calories=result.data[0]['calories'])

#Recipe Class
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String, unique=True)
    calories = db.Column(db.Integer)
    diet_labels = db.Column(db.String)
    ingredients = db.Column(db.String)

    def __init__(self, label, calories, diet_labels, ingredients):
        self.label = label
        self.calories = calories
        self.diet_labels = diet_labels
        self.ingredients = ingredients

#Recipe Schema
class RecipeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'label', 'calories', 'diet_labels', 'ingredients')

#Init Schema
recipe_schema = RecipeSchema(strict=True)
recipes_schema = RecipeSchema(many=True, strict=True)
