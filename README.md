Mamas Recipe 

A simple blog recipe book that allows users to look for recipes and add recipes of their own.
This makes this blog ultimately everyones friendly recipe book.

UX 
This website will be aimed at users of all cooking levels to share and to update their favourite recipes

Features
The features of this application are as follows:

Ability to search for Recipes based on username or ingrediants or cuisine.
Ability to Create, Edit, Delete and View recipes

Technologies Used
PYTHON FLASK JINJA2 HTML, CSS, SCSS , MONGODB

Testing
Manual Testing on the following browsers. Firefox, Chrome, Edge and IE11. Scenarios

adding a new recipe
searching for recipe based on ingrediants
searching for recipe based on username
searching for recipe based on tag
Edit a recipe
Delete a recipe

validated my HTML and CSS using the following:
HTML Validation

Deployment
Heroku
The site was deployed to Heroku via new branch (production) which was based on the master branch. 
A new app was created in the Heroku environment. Environment variables used for the database and the access keys for the Amazon S3 storage were replaced with corresponding config vars via the heroku dev center. 
Gunicorn server was installed as a dependency and a Procfile was created with the settings required to run the app using gunicorn.