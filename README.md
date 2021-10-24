# LyfeHax

## Project Objective

To create a life hacks quick tips website where users can share their tips and tricks with other web users. They will be able to create a basic account which will allow them to post content. Content will contain a title, category and body element within which users can input data. Once the user posts their content to the page the post will be assigned the username of the content creator and will also have the date it was posted. Users will be able to edit and delete their posts as well but won't have the same ability to edit or delete other user posts. "Hax" is what I will be referring to as the plural of hacks for this project just to move away from the generic.

## Website Design Goals

- Design a front end for a data-driven web application that meets accessibility guidelines, follows the principles of UX design, meets its given purpose and provides a set of user interactions
- Implement custom HTML and CSS code to create a responsive full-stack application consisting of one or more HTML pages with relevant responses to user actions and a set of data manipulation functions
- Build a non-relational database-backed Flask web application that allows users to store and manipulate data records about a particular domain
- Design a database structure that is relevant for my domain, consisting of a minimum of one collection
- Design and implement manual test procedures to assess functionality, usability, responsiveness and data management within the Full Stack web application
- Write Python code that is consistent in style and conforms to the PEP8 style guide (or another explicitly mentioned style guide, such as Google's) and validated HTML and CSS code
- Include sufficient custom Python logic to to demonstrate my proficiency in the language
- Include functions with compound statements such as if conditions and/or loops in my Python code
- Write code that meets minimum standards for readability (comments, indentation, consistent and meaningful naming conventions)
- Name files consistently and descriptively, without spaces or capitalisation to allow for cross-platform compatibility
- Create functionality for users to create, locate, display, edit and delete records
- Ensure that final deployed code is free of commented out code and has no broken internal links
- Ensure that DEBUG mode is turned off in production versions

## User Stories

- As a user, I want to be able to navigate around the sight intuitively
- As a user, I want to be able to view the posts of website members
- As a user, I want to be able to join as a member with my own profile and username
- As a user, I want the website to store my membership credentials securely in a database
- As a user, I want the website to keep my posts assigned to my user profile with my username visible to other users
- As a user, I as a member, want to be able to edit and delete posts as well as submit posts

## User Requirements and Expectations

### Site Owner/Administrator

#### Requirements

The Site Owner/Administrator will require the site to collect and store data from user posts, such as text, date, username, and special key data. The text will be the users 'hax'. The posts include the date in the format: DD/MM/YYYY. The username will be the users identity for posting on the site. A special key will be assigned to the individual users so that they, and their previous contributions and actions on the site, can be tracked and identified quickly in the database. 

#### Expectations

The Site Owner/Administrator will expect the site to load correctly without visual errors. This means having all images, fonts and formats loading without overflowing or clashing with other sections of the page. The posts of users must be clearly distinguishable between each other with margins and borders marking where one post ends and the next begins. I want the username and date of posting to appear in the appropriate location on every post, with username in top left and date in top right, and to be of legible size on all screen widths. 

The site must scale appropriately on all screen widths and utilise the Bootstrap grid effectively. The colours and images must be appropriate for the theme of the website. The colours must be attractive to the user without affecting overall readability of the content.

### Standard User

#### Requirements

They will require the site to allow them to make a membership account and post onto the main page for other users to see. They also need the site to allow them to easily navigate around it. They need to be able to see other users posts with key identifiers such as usernames and dates posted. They need the site to scale appropriately for their large and small devices so that usability or appearance isn't affected when switching between them. 

#### Expectations

They will expect the navigation elements to be similiar to what they have seen on other sites (established norms), so they can easily jump in without having to learn specific UI quirks. They will want the navbar to be sticky so that they can always click on the site logo and other navbar elements to bring them wherever they want to go. For mobile devices and small screens, they will expect the nav elements to merge into a burger icon which produces a menu transition when tapped, so as not to crowd the screen. They will want all the text and posts to be styled and ordered well.


## Design Choices

### Visual Design Choices

#### Fonts

For fonts I went with [Urbanist](https://fonts.google.com/specimen/Urbanist#standard-styles), which is a low-contrast, geometric sans-serif inspired by Modernist typography and design. It was created using elementary shapesand its neutrality makes it a versatile display font for print and digital mediums. I went for the font weight of 400, 500, and 600. 

#### Icons

I am using icons from Font [Awesome's](https://fontawesome.com/v5.15/icons?d=gallery&p=2&m=free) free gallery. These icons include the recognisable icons used for popular social media platforms.

#### Colors

I used [Coolers](https://coolors.co/) to create this neat palette image. Detail on the use of of each color below.
![Cooler Palette](wireframes/lyfehax-palette.png)

- #222 Eerie Black: This will be the primary base color for the whole site; all other colors will be layered over it
- #ccc Light Grey: This will be used to color all text elements and form fields; text within form fields will inherit the #222 base color
- #dc3545 Rusty Red: I have used this as a warning color for any cancel or delete buttons. The visual feedback provides defensive measures against user error
- #198754 Sea Green: I have used this color as a background for the flash messages and any confirm buttons. This again provides some visual feedback for the user and draws attention to where it is needed.
- #0d6efd Blue Crayola

#### Structure

The structure is controlled using [Bootstrap v5.1.1](https://getbootstrap.com/docs/5.0/getting-started/introduction/). This grid system allowed me to set responsive html elements without the need to write media queries for each screen width breakpoint. I have written css styles for the various elements on the site and tweaked the positioning of certain elements within the row/column structure. For smaller screens I hide certain elements, such as hero images, so as not to crowd the page for the user.

## Wireframes

Here are the links to my wireframes. They were created using [Balsamic](https://balsamiq.com/wireframes/) software:

### [Desktop Wireframe Folder](wireframes/desktop)

### [Tablet Wireframe Folder](wireframes/mobile)

### [Mobile Wireframe Folder](wireframes/tablet)

## Database Structure

I have used MongoDB to set up the database for this project with the following collections:

#### users:

Key      | Value
---------|-----------
_id      | ObjectId
username | String
password | String

#### hax:

Key             | Value
----------------|-----------
_id             | ObjectId
category_name   | String
hax_title       | String
hax_text_body   | String
post_date       | String
posted_by       | String

#### categories:

Key             | Value
----------------|-----------
_id             | ObjectId
category_name   | String

## Features

### NavBar

The navbar has been set to sticky and will follow the user as they scroll down the page. The navbar contains the website brand, which is Lyfehax.ie, as well as the nav elements of Home, Hax, Sign Up, Log In, Log Out, Add New Hax, and Profile. These elements can merge into a hamburger on smaller screens and will appear as a dropdown menu once the hamburger element is clicked with items floated to the right.

### Home/Index Page

The home page has two image carousels depicting workshops, tool collections, and arts and crafts. These are to signal the purpose of the site to first time users and to add visual decoration. Beneath the hero images, the intro section details to new users the purpose of the site, explains what a "Life Hack" is and has a contact form section at the bottom for users to get in touch.

### Hax Page

 The 'Hax', what I will be referring to as the user posts, will be displayed in decending order. Each of the hax will have a title, the username of the poster, the date it was posted, and the body. If the user has created a hax they will have EDIT and DELETE buttons available to them. These buttons will highlight blue for edit, green for add, and red for delete to give user feedback on what they are clicking. 

### Sign Up Page

On this page the user will be encouraged to sign up to become a user on the site. This will allow them the ability to create, edit, and delete posts of their own where a standard visitor is only able to read posts. The form has three input sections: A Password, Repeat Password Check and Username. Once the user has completed the form correctly, and clicked the submit button, they will be linked to their new profile page, with a welcome message displayed, and the data they inputted in the form will be saved to the database. 

### Log In Page

 The Log In page has a similar layout to the Sign Up page with the only real difference being there is no password check for returning users. The grid is split into two colomns with a decorative image on one side and the injected Log In form on the other.

### Add Hax Post

The Add New Hax page will contain a form, decorated with FontAwesome icons, where users can create a new "HAX" post. They have between 5 and 50 characters for the title, a choice of available categories from a dropdown menu, and a main body with an allowed length of between 30 and 600 characters. This is to stop users from posting spam posts with little to no or too much data in them.

### Footer

The footer element is displayed across all pages and contains social media links for the site owner to link to this sites associated social media accounts. The links are to Facebook, Instagram, Youtube and Twitter. Their real world application would be for if Lyfehax became a recognisable brand and needed a social media footprint.

### Features in Summary

- Intuitive navigation
- Registration functionality
- Sign-In and Out functionality
- CRUD Functions:
    - Create: user posts assigned to your user id
    - Read: view the posts on the main hax page
    - Update: able to update previous user posts assigned to your username
    - Delete: able to remove previous posts assigned to username


### Features to be implemented

- Have the home page contact form provide visual feedback for the user upon completion and upload data to database
- Have a customizable user profile with, profile image, preferences and email to which you can send updates, newsletters etc
- Have a 'forget password' functionality
- Add pagination so the list of hax will be displayed with a max of 20 logs per page
- Give the pagination interface buttons for sorting such as by date, ascending or decending

### Languages

- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)

### Framworks & External Liberaries

- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)

### Tools

- [Git](https://git-scm.com/)
- [GitPod](https://www.gitpod.io/)
- [Heroku](https://www.heroku.com/)
- [Balsamic](https://balsamiq.com/wireframes/)
- [W3C HTML Validation Service](https://validator.w3.org/)
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- [MongoDB Atlas](https://www.mongodb.com/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [PyMongo](https://api.mongodb.com/python/current/tutorial.html)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

# Testing of Interactive Elements

### Navigaton

#### User Story:  As a user, I want to be able to navigate around the sight intuitively

### Plan

The user must be able to navigate the sight with ease and locate whatever they seek on the sight. This will require a responsive navbar, working buttons which provide visual feedback and an active class which reminds user what page they are on

### Implementation

The navbar is sticky and available across all pages of the site to give the user options wherever they go. It contains the website brand, which is Lyfehax.ie, as well as the nav elements of Home, Hax, Sign Up, Log In, Log Out, Add New Hax, and Profile. These elements can merge into a hamburger on smaller screens and will appear as a dropdown menu once the hamburger element is clicked with items floated to the right.

The active class has been enabled using jinja template language and will trigger based on whether the keyword matches up with the request path of the url. Log Out, Add New Hax, and Profile will be hidden to logged out users while Log In and Sign Up will be hidden for logged in users.

All button elements on forms will change color according to their associated role ie delete = red, add = green etc. They adopt their bootstrap class as the user hovers their cursor on the button.

### Test

I have clicked through every link on the navbar to make sure no paths are broken. I have observed that the active class trigger is working as intended and tracks the user based on what page they are on.

All button elements are hovered over and clicked on with the cursor. I have signed in and out to make sure the appropriate nav items are hiding as intended. I have scrolled up and down the page to test the sticky nav setting. I also checked smaller screen widths to see if burger collapse was working as intended.

### Result

All nav links working as intended and take the user to the intended location on the site. Active class is tracking as intended. Sticky setting and burger collapse working as intended.

Appropriate nav items are hiding as intended. Button elements working as intended.


### Sign Up

#### User Story: As a user, I want to be able to join as a member with my own profile and username

### Plan

To create a sign up form where the user can fill in a new username and password. The user will be asked to repeat password to confirm correct key inputs. After signing in, the user will be redirected to the profile page.

The user will be notified of their success via a flash message and they will now be able to create, edit, and delete posts assigned to their account. The signup page should detect if the user already exists in the database before actioning the new sign up request. This is to stop duplicate account creation.

### Implementation

The form is injected into the signup template from my template/components/forms folder. The inputs available are username, password, and repeat password. The user is notified to only use numbers and letters in their username and password creation and the form will only allow between 5 and 15 characters for each input field. The form cannot be submitted unless all fields are filled out.

Once the user has filled out the form and submitted, they will be taken to their profile with a welcome message displayed. Also, the nav elements "Sign Up" and "Log In", in the navbar, will be hidden from view as they are not relevant to the logged in user. The user profile also has buttons displayed that can take them to the main hax page, where all user hax are stored and displayed, or the Add New Hax form, allowing them to jump in and start adding posts right away.

### Test

I have tested each element of the form to make sure the code checks for required fields. I tested the form inputs by putting in special characters, names or passwords that are too short or too long.

I have created a few different user accounts. I also tried to create the same account again. I finally checked to see if the navbar changes based on my signed in state. 

I have tested all button links. I also checked for the appropriate username being displayed for welcoming new or returning users.

### Result

Sign up form elements working as intended. User is notified whenever they deviate from the requested formats or word length. The form also wont submit until all required fields are filled. The welcome message with corresponding username is working as intended. 

Sign Up and Log In elements are hidden as intended and replaced with Log Out, Add New Hax and Profile nav options. All buttons are working as intended and the flash message displays the in session username with the welcome message on their new profile.


### User Credential Storage

#### User Story: As a user, I want the website to store my membership credentials securely in a database

### Plan

My plan is to store user credentials in their own collection in the database. They will be stored in the database with 3 key:value pairs: ObjectId, Username, and Password. The user will be asked to enter their password twice to make sure they have entered what they wanted correctly.

### Implementation

I built a form which takes only letters and numbers between 5-15 characters as valid credentials. This is to have legitimate usernames and more secure passwords being used on the site. The form will notify the user if any of the form entries do not match the requested criteria. The form also wont submit if one or all of the fields are missing or incorrect. I used Werkzeug Security to import generate_password_hash and check_password_hash. These functions turn the user password into a string of randomly generated characters which makes the real password indecipherable without the appropriate tools or knowhow to unhash it. If there is a breach in access to the database user account passwords will be protected.

### Test

I have tried to enter the wrong credentials in the sign up and log in forms respectively. The app responds with the appropriate help messages requesting the right details. I clicked the submit button without filling in or filling in wrong the fields above but the app will not proceed. 

On completion of either the log in or sign up form I am taken to the profile page and the appropriate flash messages are being displayed. When I check the user credentials in the database the passwords are indeed being converted into a scramble of different characters.

### Result

Log in and sign up forms working as intended. User cannot proceed to completion unless everything is filled out as intended and in the case of sign up both passwords are correct. All flash messages displaying as intended. Passwords are being appropriately hashed in the database to improve site security.


### User Creation of Posts

#### As a user, I as a member, want to be able to submit posts avaialable for other users to see with the date it was posted visible

### Plan

I will need to create a page with a user form which allows the user options to fill in a new entry. I must label and style each part appropriately so the user knows where to input the data. Each post must require a title, category choice, and a text body. I must set limits on the title and body, as if they are too short they most likely will not contain anything meaningful, or if they are too long they will take up too much space on the main hax page. On the back end I will need the function which creates new hax posts to add a date to the new post.

### Implementation

I have created a separate page that the user can access once an account has been created. There are two options, either via the navbar link Add New Hax or via the button they would have seen on their new profile once they joined. The form has the title, body, and category selector as options. Each option has a placeholder informing the user of the length restrictions and what is required of them. The user has a submit button and a cancel button for if the user changes their mind about posting. The date function has been added using the datetime import and the output will display in the format DD/MM/YYYY.

### Test

I have tested the button links to the Add New Hax page. I have checked each form entry to see if checks for length are working. I tried entering to much and too little text as well as ignoring form fields. I also tried both submitting and cancelling. I finally checked to see if the users new post was displayed on the Hax page with the appropriate date and date format attatched.

### Result

Button links to Add New Hax page working as intended. All form entry checks are working as intended. Add and Cancel buttons working as intended. Session users new post displayed with the correct date and date format appearing towards the bottom of the post.


### User Posts Assigned Username / Paired to Session User

#### As a user, I want the website to keep my posts assigned to my user profile with my username visible to other users

### Plan

To accomplish this I will need to create buttons for user posts which give the option to edit and delete. I will need to have these buttons only show on hax posts linked to the user in session.

### Implementation

I have created the hax page to extract the hax data from the database. This includes the post date and the user who posted it. I have placed a jinja {% if else %} statement above the section where the edit and delete buttons are coded. The if else statement will check the posted_by variable to see if the user in session matches the user who posted. Since you cant create duplicate usernames this should work fine as a defensive measure. If the session user matches the posted_by variable on the hax post the user will be displayed the edit and delete buttons. I have also installed a model for the delete function as it was too easy before to misclick and accidentally delete a post.

### Test

I have signed into different user accounts to check whether the edit and delete buttons are appropriately shown or hidden. I also clicked each buttons to check what occurs. I also tried to create a duplicate user account to try and alter another users post.

### Result

Signing in to different accounts, I could see the buttons shown for the session users posts and hidden for other account posts. These buttons are working as intended. The defensive delete modal is also working as intended, warning the user of the finality of their action. I tried to create another account but was unsuccessful. The app notified me via flash message that the username is already in use.


## Deployment

### Local Deployment

I have created the LyfeHax.ie project using Github to store and [Gitpod](https://gitpod.io/) to write my code. 
Then I used commits followed by "git push" to forward my workspace work to my GitHub repository.
I have deployed this project to Heroku and utilized the "git push heroku master" command to make sure my pushes to GitHub were synced with Heroku. 

This project can be run locally by following the following steps: (
I used Gitpod for development, so the following steps will be specific to Gitpod. 
You will need to adjust them depending on your IDE. You can find more information about installing packages using pip and virtual environments [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


To clone the project: 

1. From the application's repository, click the "code" button and download the zip of the repository.
    Alternatively, you can clone the repository using the following line in your terminal:

    ``` 
    git clone https://github.com/AnoukSmet/Dog-Health-Tracker.git
    ``` 

1. Access the folder in your terminal window and install the application's [required modules](https://github.com/JMuckian94/MSP3-LyfeHax/blob/main/requirements.txt) using the following command:

    ```
    pip3 install -r requirements.txt
    ```

1. Sign-in or sign-up to [MongoDB](https://www.mongodb.com/) and create a new cluster
    - Within the Sandbox, click the collections button and after click Create Database (Add My Project Data) called lyfehax-project
    - Set up the following collections: categories, hax, users [Click here to see the exact Database Structure](#database-structure)
    - Under the Security Menu on the left, select Database Access.
    - Add a new database user, and keep the credentials secure
    - Within the Network Access option, add IP Address 0.0.0.0

1. In your IDE, create a file containing your environmental variables called env.py at the root level of the application. 
    It will need to contain the following lines and variables:
    ```
    import os

    os.environ["IP"] = "0.0.0.0"
    os.environ["PORT"] = "5000"
    os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"
    os.environ["DEBUG"] = "True"
    os.environ["MONGO_URI"] = "YOUR_MONGODB_URI"
    os.environ["MONGO_DBNAME"]= "DATABASE_NAME" 
    ```

    Please note that you will need to update the SECRET_KEY with your own secret key, as well as the MONGO_URI and MONGO_DBNAME variables with those provided by MongoDB.
    Tip for your SECRET_KEY, you can use a [Password Generator](https://passwordsgenerator.net/) in order to have a secure secret key.
    To find your MONGO_URI, go to your clusters and click on connect. Choose connect your application and copy the link provided. 
    Don't forget to update the necessary fields like password and database name. 

    If you plan on pushing this application to a public repository, ensure that env.py is added to your .gitignore file.

1. The application can now be run locally. In your terminal, type the following command 
    ```
    python3 app.py. 
    ```
    
### To deploy your project on Heroku, use the following steps: 

1. Login to your Heroku account and create a new app. Choose your region. 
1. Ensure the Procfile and requirements.txt files exist are present and up-to-date in your local repository.  
    Requirements:
    ```
    pip3 freeze --local > requirements.txt
    ```
    Procfile:
    ```
    echo web: python app.py > Procfile
    ```
1. The Procfile should contain the following line:
    ```
    web: python app.py
    ```

1. Scroll down to "deployment method"-section. Choose "Github" for automatic deployment.
1. From the inputs below, make sure your github user is selected, and then enter the name for your repo. Click "search". When it finds the repo, click the "connect" button.
1. Scroll back up and click "settings". Scroll down and click "Reveal config vars". Set up the same variables as in your env.py (IP, PORT, SECRET_KEY, MONGO_URI and MONGODB_NAME):
    !You shouldn't set the DEBUG variable in under config vars, only in your env.py to prevent DEBUG being active on live website. 

    ```
    IP = 0.0.0.0
    PORT = 5000
    SECRET_KEY = YOUR_SECRET_KEY
    MONGO_URI = YOUR_MONGODB_URI
    MONGO_DBNAME = DATABASE_NAME
    ```

1. Scroll back up and click "Deploy". Scroll down and click "Enable automatic deployment".
1. Just beneath, click "Deploy branch". Heroku will now start building the app. When the build is complete, click "view app" to open it.
1. In order to commit your changes to the branch, use git push to push your changes. 

---
## Credits

### Content / Media

Unsplash's users who create the images I used can be found in my [img](https://github.com/JMuckian94/MSP3-LyfeHax/tree/main/static/img) folder. Their names are contained within the jpg filenames. I thank the Unsplash community for making their contributions freely available to broke students like me. 

### Acknowledgements

I would like to thank the Code Institute Tutor Tim Nelson for his informative tutorials on how to build a flask application. I thank my mentor Simen [Eventyret_mentor](https://github.com/Eventyret) for looking over my work and keeping me on track. I thank the [Stackoverflow](https://stackoverflow.com/) community for being the light in the darkness when I am in a pit of bugs and confusion. Finally, I'd like to thank the Code Institute Slack community for being responsive and kind with their assistance.

