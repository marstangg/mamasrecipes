

Mamasrecipe - https://mamarecipe-heroku.herokuapp.com/
============
A fictitious online cookbook for people with the following requirements below:

- the website is user and mobile friendly
- the website design helps to create a community for sharing
- view and sort, filter recipes on the website, add recipes, edit recipes.

The project was made from scratch following the guidance of the course material. 

The project was made keeping in mind possible future functionality updates. 

The website has the following pages: 

Features 
=========
The features of this application are as follows: 

- Ability to view others recipes
- Ability to Create recipes and add.
- Ability to Edit recipes
- Ability to Delete recipes
- Ability to search through other recipes through usernames or ingrediants/tags

Technologies Used 
=================
1. Flask
2. Python
3. HTML
4. CSS
5. Bootstrap
6. Mongodb

Testing
=========

Manual Testing on the following browsers. Firefox, Chrome, Edge and IE11. Scenarios

adding a new recipe
searching for recipe based on ingrediants
searching for recipe based on username
searching for recipe based on tag
Edit a recipe
Delete a recipe

validated my HTML and CSS using the following:
HTML Validation

CONTRIBUTIONS
===============
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated. 

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

Deployment 
=============

During development, all code was written in Cloud 9 and updates were saved and tested locally. Throughout the process I used GitHub to keep track of changes and to maintain version control in my code base. 

The development version of my application is on GitHub and I push this code using git push origin master and the code is run and tested on Cloud 9 before being updated to heroku 

Create a remote Git repo for your app on Heroku 


PART 1 
1. 
   Install the following using pip3:
   
sudo pip3 install gunicorn

sudo pip3 install psycopg2



sudo pip3 install whitenoise
2. 
   Make sure to include the following settings for static files and uploads, if they are not there already:

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



3.  Create the requirements.txt file using bash

pip3 freeze --local > requirements.txt
6. 
   
   Create a local git repo for your project and connect it to a GitHub repo. Include the relevant .gitignore file.  If you have not done so. MAKE SURE migrations folder are not excluded!
   

sudo git init
sudo git add .
sudo git commit -m "First commit"
sudo git remote add origin <GITHUB REMOTE URL>

sudo git push origin master



7. 
   Put staticfiles/  and media/ inside .gitignore
   
8. 
   Log into heroku by typing in heroku login and pressing ENTER
   
9. 
   Create an app ( do it via the command line, don't do it via the Heroku webpage). If you opt for the command line and the push to Heroku
   
heroku create <PROJECT NAME> 

git remote -v


Part 2:

1. Commit the changed files

sudo pip3 freeze --local > requirements.txt
sudo git add .
git commit -m "<YOUR COMMENT MESSAGE>"

git push origin master


2. 
   Create the procfile:
   
   
touch Procfile
3. 
   And enter into the Procfile:
   
   
web: gunicorn <PROJECT_FOLDER>.wsgi:application
4. 
   Add the URL of the heroku app into the ALLOWED_HOST inside settings.py
   
5. 
   Add and commit, and create the superuser on the Heroku app:
   
git push heroku master

Credits
=========
To Teachers assistant in my course for guidance and help
startbootstrap for theme layout

