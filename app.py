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

""" Display Landing Page """    
@app.route("/")
def index():
    return render_template("index.html")

""" Show all record in database """

@app.route("/recipes")
def recipes():
    recipes = recipe_data.find()
    return render_template("recipes.html", recipes=recipes)

# """ Add a new recipe """
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

    
# @app.route("/search")
# def search():
    
#     return render_template("search.html")
    
# @app.route("/search", methods=["POST"])
# def submit_search():
    
#     conn = get_connection()
    
#     search_term = request.form["search-term"]
#     search_word = request.form["search-word"]
    
#     if search_term == "username":
#         search_by="username"
#     elif search_term == "ingredients":
#         search_by="ingredients"
#     else:
#         search_by="recipe_tag"
    
#     search_recipes = conn[MONGO_DB]["recipes"].find({
#         search_by:{"$regex":search_word, "$options":"i"}
#     })
    
    
#     return render_template("search.html", search_recipes=search_recipes)


# """ Edit Route """


@app.route('/recipe_edit')
def recipe_edit ():
    return render_template ('recipe_edit.html')
# @app.route("/edit_recipe/<recipe_id>")
# def edit_recipe(recipe_id):
    
#     conn = get_connection()
    
#     search_recipes = conn[MONGO_DB]["recipes"].find_one({
#         "_id": ObjectId(recipe_id)
#     })
    
#     # return render_template("edit.html", recipe_id=recipe_id, search_recipes=search_recipes)
#     return render_template ("recipe_edit.html")
# # @app.route("/edit_recipe/<recipe_id>", methods=["POST"])
# # def submit_edit(recipe_id):
    
# #     conn=get_connection()
    
# #     username = request.form["username"]
# #     time = request.form["est-time"]
# #     recipe_name = request.form["recipe-name"]
# #     recipe_tag = request.form["recipe-tag"]
# #     ingredients = request.form["ingredients"]
# #     directions = request.form["directions"]
    
# #     if recipe_tag == "chinese":
# #         tagged = "chinese"
# #     elif recipe_tag == "indian":
# #         tagged = "indian"
# #     elif recipe_tag == "malay":
# #         tagged = "malay"
# #     else:
# #         tagged = "western"
    
# #     conn[MONGO_DB]["recipes"].update({
# #         "_id":ObjectId(recipe_id)    
# #     },
# #     {"$set":
# #         {
# #         "username": username,
# #         "time": time,
# #         "recipe_name": recipe_name,
# #         "recipe_tag": tagged,
# #         "ingredients": ingredients,
# #         "directions": directions
# #         }
# #     })
    
# #     return redirect(url_for("recipes"))
    
# # """ Delete Route """    

# @app.route("/delete/<recipe_id>")
# def delete(recipe_id):
    
#     conn = get_connection()
    
#     search_recipes = conn[MONGO_DB]["recipes"].find({
#         "_id": ObjectId(recipe_id)
#     })
    
#     return render_template("delete.html", search_recipes=search_recipes, recipe_id=recipe_id)
    
    
# @app.route("/delete/<recipe_id>", methods=["POST"])
# def submit_delete(recipe_id):
    
#     conn = get_connection()
    
#     conn[MONGO_DB]["recipes"].delete_one({
#         "_id": ObjectId(recipe_id)
#     })
    
#     return redirect(url_for("recipes"))

    
    
    
    
if __name__  == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
        