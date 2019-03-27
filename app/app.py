from flask import Flask, render_template
from api_routes import getRecipes

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

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