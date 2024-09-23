![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **May 14, 2024**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!


## Deployment
1. go to your account on render.com and press get started for free it will take you to the second page where you can see a New button in the navbar up , press it to have a dropdwn menue where you can choose web services.
2. you can see here a box that shows github button press it and add your github project URL then down the box will be another button with the word connect. press it to connect your github to render. The connect button will not be activated till you choose a project from within the box.
3. when you press connect you will be in the setting page. important is the following to be added:
   <br>a. Build command: pip install -r requirements.txt && npm install
   <br>b. Start command: node index.js
   <br>c. environment variables: port;8000 , 
                             PYTHON_VERSION;3.10.7
4. finished setting then press deploy web service butoon down in the page it will take you to the last page where you see your deployed link.
   I used the CI template on github after I deleted procfile and runtime.text.
