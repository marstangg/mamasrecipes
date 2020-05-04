

# Mamasrecipe

   You can find the website at :  https://mamarecipe-heroku.herokuapp.com/
   
   Everyone loves home-cooked food and every mama's cooking style and recipes are different. 
   This portal is a platform to appreciate all mama's effort and share their unique recipe with everyone.
   Great recipes will be made available for the next generations.
   
      - the website is user and mobile friendly
      - the website design helps to create a community for sharing
      - view and sort, filter recipes on the website, add recipes, edit recipes.

   The project was made from scratch following the guidance of the course material.
   
   The project was made keeping in mind possible future functionality updates.


## Features 

The features of this application are as follows: 

      - Ability to view others recipes
      - Ability to Create recipes and add.
      - Ability to Edit recipes
      - Ability to Delete recipes
      - Ability to search through other recipes through usernames or ingrediants/tags
      
      Limitation : 
      - Social media are not linked to own pages
      - Social media sharing are not enabled (future development)

## Technologies Used 

      1. Flask
      2. Python
      3. HTML
      4. CSS
      5. Bootstrap
      6. Mongodb

## Testing


Manual Testing on the following browsers. Firefox, Chrome, Edge and IE11. Scenarios

Test Results as follows :

*No* | *Steps* | *Expected Results* | *Observations*
--- | --- | --- | ---
1 | `On the Landing Page, click on the "Add recipe" in navbar`| `Link to the submission of new recipe page and show entry form`| **Pass** 
2 | `Enter the details in form and submit`|`Render successful submission page` | **Pass** 
3 | `Click on the 'Recipe' in navbar`|`display the full list of the recipe with details` | **Pass** 
3a | `In each recipe, click "Edit" link on bottom right of a recipe`|`Show form with details of selected recipe and allow user to enter new info` | **Pass** 
3b | `Click "Update recipe" to save the changes`|`Add to database and render to show list of all recipe` | **Pass** 
4a | `In each recipe, click "Delete" link on bottom right of a recipe`|`Render page to confirm deletion with user if the removal of the selected recipe` | **Pass** 
4b | `Click "No it is cooking well"`|`Return to recipe list page` | **Pass** 
4c | `Click "Remove it, I will submit better ones"`|`Delete from database and return to recipe list page` | **Pass** 
5 | `Click "Home" link on top right of page`|`Return to landing page` | **Pass** 
6 | `Landing page, select your preference cusine from the dropdown list`|`Show the list of recipes under the type of cusine selected` | **Pass**

## CONTRIBUTIONS

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated. 

      1. Fork the Project
      2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
      3. Commit your Changes (git commit -m 'Add some AmazingFeature')
      4. Push to the Branch (git push origin feature/AmazingFeature)
      5. Open a Pull Request

## Deployment 

During development, all code was written in Cloud 9 and updates were saved and tested locally. 

Throughout the process I used GitHub to keep track of changes and to maintain version control in my code base. 

The development version of my application is on GitHub and I push this code using **git push origin master** and the code is run and tested on Cloud 9 before being updated to heroku 

Create a remote Git repo for your app on Heroku 

      i ) Install Heroku using bash
      ii) Login to Heroku
      iii) Install gunicorn
      iv) Create Procfile and requirements.txt
      V) Commit and push to Heroku 
      vi) Set up the Environment Vasriables
      vii) Update Dependencies

## Credits

To Teachers assistant in my course for guidance and help
startbootstrap for theme layout

