from flask import Flask, render_template, request, redirect, url_for  
import os, pymongo
from bson.objectid import ObjectId

MONGO_URI= os.environ.get('MONGO_URI')
MONGO_DB= os.environ.get('MONGO_DB')

app = Flask(__name__)

# Setting up the MONGODB DATABASES to be link up	
MONGO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = 'mamarecipes'
COLLECTION_NAME = 'recipes'

# set up the connection to MONGO_URI which we set up in bashrc
conn = pymongo.MongoClient(MONGO_URI)
# set 'data' to be the name to represent the database link
recipe_data = conn[DATABASE_NAME][COLLECTION_NAME]

# Display Landing Page 
@app.route("/")
def index():
    return render_template("index.html")

""" Show all record in database """

# Display all recipes
@app.route("/recipes")
def recipes():
    recipes = recipe_data.find()
    return render_template("recipes.html", recipes=recipes)

# Add a new recipe
@app.route("/recipe_add")
def recipe_add():
    return render_template("recipe_add.html")
@app.route('/recipe_add', methods=['POST'])
def save_recipe():
    username = request.form["username"]
    time = request.form["est-time"]
    recipe_name = request.form["recipe-name"]
    recipe_tag = request.form["recipe-tag"]
    ingredients = request.form["ingredients"]
    directions = request.form["directions"]

    
    recipe_data.insert({
        "username": username,
        "time": time,
        "recipe_name": recipe_name,
        "recipe_tag": recipe_tag,
        "ingredients": ingredients,
        "directions": directions
    })
    return redirect(url_for('index'))

# Edit a recipe
@app.route('/recipe_edit/<recipe_id>')
def recipe_edit (recipe_id):
    selected_recipe = recipe_data.find_one({
        "_id": ObjectId(recipe_id)
    })
    return render_template ('recipe_edit.html', recipe=selected_recipe)
@app.route("/recipe_edit/<recipe_id>", methods=['POST'])
def recipe_update(recipe_id):

    username = request.form["username"]
    time = request.form["est-time"]
    recipe_name = request.form["recipe-name"]
    recipe_tag = request.form["recipe-tag"]
    ingredients = request.form["ingredients"]
    directions = request.form["directions"]
    
    recipe_data.update({
        "_id":ObjectId(recipe_id)    
    },
    {"$set":
        {
        "username": username,
        "time": time,
        "recipe_name": recipe_name,
        "recipe_tag": recipe_tag,
        "ingredients": ingredients,
        "directions": directions
        }
    })
    
    return redirect(url_for("recipes"))
    
# Check if user confirm delete a recipe
@app.route("/recipe_delete/<recipe_id>")
def recipe_delete(recipe_id):
    recipe = recipe_data.find({
        "_id": ObjectId(recipe_id)
    })
    return render_template("recipe_delete.html", recipe=recipe)
# Proceed to delete a recipe    
@app.route("/recipe_delete/<recipe_id>", methods=["POST"])
def proceed_delete(recipe_id):
    recipe_data.delete_one({
        "_id": ObjectId(recipe_id)
    })
    return redirect(url_for("recipes"))

# Search for a type of recipe
@app.route("/recipe_search/<search_tag>")
def recipe_search(search_tag):
    if (search_tag == 'all'):
        search_recipes = recipe_data.find({})
    else :
        search_recipes = recipe_data.find({
            "recipe_tag" : search_tag,
        })
    return render_template("recipes.html", recipes = search_recipes)
    
if __name__  == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
        