from flask import Flask, render_template, request, jsonify
from api_routes import getRecipes
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

@app.route('/recipes', methods=['POST'])
def hello_world():
    label = request.json['label']
    calories = request.json['calories']
    recipe_yield = request.json['recipe_yield']
    # diet_labels = request.json['diet_labels']

    new_recipe = Recipe(label, calories, recipe_yield)
    db.session.add(new_recipe)
    db.session.commit()
    return recipe_schema.jsonify(new_recipe)
    # return render_template('home.html')

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
    data = getRecipes()
    if data:
        print('Not empty')
        return render_template('low_carb.html', recipes=data)
    else:
        print('data empty')
        return

@app.route('/high-protein')
def high_protein():
    return render_template('high_protein.html', recipes=getRecipes())

@app.route('/low-fat')
def low_fat():
    return render_template('low_fat.html', recipes=getRecipes())


#Recipe Class
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String, unique=True)
    calories = db.Column(db.Integer)
    recipe_yield = db.Column(db.Integer)
    # diet_labels = db.Column(db.String)

    def __init__(self, label, calories, recipe_yield):
        self.label = label
        self.calories = calories
        self.recipe_yield = recipe_yield
        # self.diet_labels = diet_labels

#Recipe Schema
class RecipeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'label', 'calories', 'recipe_yield')

#Init Schema
recipe_schema = RecipeSchema(strict=True)
recipes_schema = RecipeSchema(many=True, strict=True)