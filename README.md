# Gaming Trivia

## Project Objective

To create a life hacks quick tips website where users can share their tips and tricks with other web users. They will be able to create a basic account which will allow them to post content. Content will just be text for now. Once the user posts their content to the page the post will be assigned the username of the content creator and will also have the date it was posted.

## Table of Contents
...

## Website Design Goals

- Design a front end for a data-driven web application that meets accessibility guidelines, follows the principles of UX design, meets its given purpose and provides a set of     user interactions
- Implement custom HTML and CSS code to create a responsive full-stack application consisting of one or more HTML pages with relevant responses to user actions and a set of data   manipulation functions
- Build a non-relational database-backed Flask web application that allows users to store and manipulate data records about a particular domain
- Design a database structure that is relevant for your domain, consisting of a minimum of one collection
- Design and implement manual test procedures to assess functionality, usability, responsiveness and data management within the Full Stack web application
- Write Python code that is consistent in style and conforms to the PEP8 style guide (or another explicitly mentioned style guide, such as Google's) and validated HTML and CSS     code
- Include sufficient custom Python logic to to demonstrate your proficiency in the language
- Include functions with compound statements such as if conditions and/or loops in your Python code
- Write code that meets minimum standards for readability (comments, indentation, consistent and meaningful naming conventions)
- Name files consistently and descriptively, without spaces or capitalisation to allow for cross-platform compatibility
- Design a data model that fits the purpose of the project
- Develop the model into a usable non-relational database where data is stored in a consistent
  and well-organised manner
- Create functionality for users to create, locate, display, edit and delete records
- Deploy a final version of the full-stack application code to a cloud-based hosting platform
  (e.g. Heroku) and test to ensure it matches the development version
- Ensure that final deployed code is free of commented out code and has no broken internal
  links
- Document the deployment process in a README file in English that also explains the
  application’s purpose and the value that it provides to its users
- Use Git & GitHub for version control of a Full Stack web application up to deployment, using
  commit messages to document the development process.
- Commit final code that is free of any passwords or security sensitive information, to the
  repository and to the hosting platform
- Use environment variables, or files that are in .gitignore, to hide all secret keys
- Ensure that DEBUG mode is turned off in production versions

## UX

### NavBar

For responsiveness on all platforms I used Bootstrap to control the spacing and layout of the page. The navbar has been set to sticky and will follow the user as they scroll down the page. The navbar contains the website brand, which is Lyfehax.ie, as well as the nav elements of Home, About, Join Up, and Contact. These elements can merge into a hamburger on smaller screens and will appear as a dropdown menu once the hamburger element is clicked.

### Home/Index Page

The home page has two images depicting workshops, tool collections, and arts and crafts. These are to signal the purpose of the site to first time users and to add visual decoration. Beneath the hero images, the primary content of the site will be displayed. The 'Hax', what I will be referring to as the user posts, will be displated in a 4x4 grid. Each hax will take up one of two collumns on larger screens. On smaller screens the hax will be displayed using full rows. Each of the hax will have a title, the username of the poster, the date it was posted, and a small preview of the full post. If the post is larger than X number of characters then the rest of the post will be hidden and a link (Read more...) will be displayed.

### About Page

The about page will have similar hero image layout at the top of the page. Beneath these images the 'About Us' section is displayed. This row contains a short paragraph explaining the purpose for the website in relation to the user. This paragraph has a complementing picture alongside it, providing decoration in an otherwise blank space. The sides have been reversed for the next row, with the text explaining what a life hack is and a picture alongside.

### Membership Page

On this page the user will be encouraged to sign up to become a user on the site. This will allow them the ability to create posts of their own where a standard user is only able to read posts. The form has three input sections: Email, Password (IMPLEMENT A REPEAT PASSWORD CHECK), and Username. Once the user has completed the form correctly, and clicked the submit button, the text on the page will change and the data they inputted in the form will be saved to the database. 

###
### User Stories

- As a user, I want to ...
- As a user, I want to ...
- As a user, I want to ...
- As a user, I want to ...
- As a user, I want to ...
- As a user, I want to ...
- As a user, I want to ...
- As a user, I want to ...


### User Requirements and Expectations

### Site Owner/Administrator

#### Requirements

For the Site Owner/Administrator's purposes I will require the site to collect and store data from user posts, such as text, date, username, and special key data. The text will be the users tips or 'lyfehax' as I will be naming them. The date will only include the date in the format: DD/MM/YYYY. No time will be included. The username will be that which the user chose as an identity for posting on the site. The special key will be assigned to the individual users so that they, and their previous contributions and actions on the site, can be tracked and identified quickly in the database. 

I want user posts to appear in the middle of the page with a margin on each side for medium sized screens upwards. The posts will take up the full screen on small screens and mobile devices. The posts will be scrollable with the newest posts appearing at the top and the oldest appearing at the bottom.

#### Expectations

I expect the site to load correctly without visual errors. This means having all images, fonts and formats loading without overflowing or clashing with other sections of the page. I want the posts of users to be clearly distinguishable between each other with margins and borders marking where one post ends and the next begins. I want the username and date of posting to appear in the appropriate location on every post, with username in top left and date in top right, and to be of legible size on all screen widths. 

I expect the site to scale appropriately on all screen widths and utilise the BOOTSTRAP grid effectively. I want the colours and images to be appropriate for the theme of the website. The colours must be attractive to the user without affecting overall readability of the content.

### Average User

#### Requirements

I require the site to allow me to make a membership account and post onto the main page for other users to see. I also need the site to allow me to easily navigate around it. I need to be able to see other users posts with key identifiers such as usernames and dates posted. I need the site to scale appropriately for my large and small devices so that usability or appearance isn't affected when switching between them. 

#### Expectations

I expect the navigation elements to be similiar to what I have seen on other sites, so I can easily jump in without having to learn specific UI quirks. I want the navbar to be sticky so that I can always click on the site logo to bring me back to the home page. For mobile devices and small screens I want the nav elements to merge into a burger icon which produces a menu transition when tapped. I want all the text and posts to be styled and ordered well.

### Design Choices

For small screens I have gone with a sticky navbar with the site logo and burger icon visible. Clicking on the logo will take the user back to the top and refresh the page. The burger will produce a menu of navigation options with pages such as "about", "contact us", and "...". The posts on mobile and small screens will be minimised to a preview of the content with the title of the post and the first couple of lines visible with a "Read more..." item that will make the post full screen and the rest of the text visible.

Each post will have clear border markings to seperate them from each other. Usernames will be positioned top left and date top right of each post.

#### Fonts

...

#### Icons

...

#### Colors

...

#### Structure

...

## Wireframes

Here are the links to my wireframes:

### [Desktop Wireframe Folder]()

### [Tablet Wireframe Folder]()

### [Mobile Wireframe Folder]()

## Features

### Intro Section

...

### Lets Play/High Scores Buttons

...

### Game Section

...

### Final Scores Section

...

## Features to be Implemented

...

### Languages

- HTML5
- CSS3
- Javascript ES2015
- Python3

### Framworks & External Liberaries

- [Bootstrap 4.6.0](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)

### Tools

- [Git](https://github.com/)
- [Gitpod](https://gitpod.io/workspaces)
- [Balsamiq](https://balsamiq.com/)
- [Coolors](https://coolors.co/)
- [Heroku](https://dashboard.heroku.com/)

## Testing of Interactive Elements

### Plan

...

### Implementation

...

### Test

...

### Verdict

...

---

## Deployment

This project was deployed via GitHub by executing the following steps. After writing the code, committing and pushing it to GitHub:

##### 1. Navigate to the repository on github and click Settings.
##### 2. From there, go to the Source section within the Github Pages section.
##### 3. Select master branch on the dropdown menu, and click save.
##### 4. Now the website is live.

Any time commits and pushes are sent to Github, the Github Pages site should update shortly after.

### To run the project locally:

##### 1. Fork the repository to your GitHub account.
##### 2. Choose a local folder for the cloned files.
##### 3. Clone the repository to your local machine.
##### 4. Configure the upstream remote value.

---
## Credits

### Content / Media

...

### Acknowledgements

...

