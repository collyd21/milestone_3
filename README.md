# General Work Permits
Data Centric Development Milestone 3 Project.
General Work Permits is a browser based permit system for construction sites. Allowing easy creation of permits and accessiblility for these to be read at any time.
### User Stories
As a user I want be able to add a new permit for my days work task.

As site management I want view all permits submitted for the day so I can tell what tasks are being worked on.

As admin I want to be able to delete Permits and Users if required.
### Scope
The scope for this Milestone project is to exhibit the CRUD functions, Create, Read, Update and Delete. To do this I have created a template for filling out daily work permits for construction site workers. This task is generally done by manually on pen and paper. Doing this electronically will not only speed up the process and reduce paper waste, but it will also make all permits accessibile quickly and easy.
### Skeleton
[User Page](static/wireframes/users.png)

[Login Page](static/wireframes/login.png)

[Permits Page](static/wireframes/permits.png)

[Adding New User Page](static/wireframes/addUser.png)

[Adding New Permit Page](static/wireframes/addPermit.png)

### Structure

#### Navbar
There are 3 different versions selectable links of the Navbar on this site. The reason for this is that they will be dependant on who you are accessing the site. All of which show the "GWP" thumbnail and can be clicked to return to Homepage.

##### Not Logged-In View
Here the user of the site has the options of **Add User** or to continue to **Admin Login** page.

##### Admin Logged-In View  
Once logged in as the admin, the options in the navbar are **View Permits** and **View Users**.

##### User Logged-In View  
When logged in as a User. the options are **Add User**, **View Permits** and **Add Permit**.

#### User/Homepage
Here all users can be seen. And are arranged with a generic avatar image. Each card also includes the Users information and a login button.

#### User Login / Admin Login
The User and Admin login pages are the same basic layout with a welcome text and a password field. The page will display the Users first and last name or else will display Administrator if Admin login was selected.

#### Add User
On this page, a new user is created. All fields are required to be filled on this page so that a blank profile can not be set up. The information is stored in the MongoDB database and a User card is then displayed on the User page.

#### Viewing Permits List
On the view permits page, all created permits are displayed in a table with the headings of:  
- Date
- Contractor
- Location
- Crew Size

Depending on whether you are logged in as Admin or a User, you will also be given two button options.

**Admin** - View Permit or Delete Permit

**User** - View Permit or Edit Permit

#### New Permit

On this page the form is enclosed in a container of light grey colour. This is to mimic an actual paper form that a site worker would be use to filling out each day for their tasks. The form includes standard text input boxes, larger text input boxes, where more information is required and also toggle switches to say whether a hazard is applicable.

#### Edit Permit

When a User clicks the Edit permit button. this will bring them to the same form layout as the new permit page. The difference here is that the fields are pre populated with the information that was originally supplied when filling out the permit from new. The User alters the valves and selects submit at the bottom. The database is then updated witht he new information.

#### View Permit

Users have the option to just view a permit rather than edit. This will again display the same page as new and edit permit, but this time no field will be editable and toggle switch disabled.

#### Viewing User List

The Admin has an additional list to view all users. This is displayed in the same form as the permits list table. The rows for the User table are: 
- Name
- Title
- Company

This time the only button option is Delete user.

#### Delete Permit / Delete User

Once Admin is logged in. On either the Permit lists page or User List page, they have an option button of delete. This will remove the permit or user and the list will then be updated and displayed.


### Surface
The colour scheme for this project is light and clear. I wanted to make sure information in concise and easily read. The bootstrap button colours are used throughout to add accents of colour to the site.

![#007bff](https://via.placeholder.com/15/007bff/000000?text=+) #007bff

![#ffa500](https://via.placeholder.com/15/ffa500/000000?text=+) #ffa500

![#dc3545](https://via.placeholder.com/15/dc3545/000000?text=+) #dc3545

![#f0efed](https://via.placeholder.com/15/f0efed/000000?text=+) #f0efed

There is a stock construction background used with its opacity turned down. This makes the containers start out more from a solid colour background while also keeping in witht the construction theme.

## Technologies
For this project I used the following technologies:

[Github](https://github.com/) - Used for repository hosting service.

[Gitpod](https://gitpod.io/) - an online IDE, used to create and edit the project code.

[MongoDB Atlas](https://mongodb.com/cloud/atlas) - a fully-managed cloud database developed for applications.

[Heroku](https://heroku.com) - a Cloud Application Platform that enables developers to build, run, and operate applications entirely in the cloud

[Bootstrap 4](https://getbootstrap.com/) - a CSS Framework for developing responsive and mobile-first websites

[HTML 5](https://en.wikipedia.org/wiki/HTML5) - a markup language used for structuring and presenting content on the World Wide Web

[CSS 3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Cascading Style Sheets that describe how HTML elements are to be displayed on screen

[Python](https://www.python.org/doc/essays/blurb/) - a high-level, object-oriented programming language

[Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)) - a micro web framework written in Python

[jQuery](https://jquery.com/) - a JavaScript library that greatly simplifies JavaScript programming

[Slack](https://slack.com/intl/en-ie/) - used by the Code Institute community open duscussions, get answers and share information

[Stackoverflow](https://stackoverflow.com/) -  an open community for coders to ask questions and get answers

[W3Schools](https://www.w3schools.com/about/) - for tutorials and references on web development languages

[Free Formatter](https://www.freeformatter.com/javascript-beautifier.html) - a Javascript, HTML and CSS Beautifier.

[W3 Validator](https://validator.w3.org/) - a HTML and CSS Validator.

[Responsinator](http://www.responsinator.com/) - for testing site Responsiveness.

## Features

**Adding User**: Anyone visiting the site will need to create a new user profile so they can access the permits.

**Password**: When creating a profile, a user will be required to set a password. This is stored in the database. For now the login system used is a crude version, but gives an example of how the logging in would look. (This is due to my lack of knowledge around session, authorisation and login at this stage of the course)

**CRUD Functions**: Once logged in with their password the User has the following options:
- Create: By adding a new permit.
- Read: By viewing all permits or viewing an individual permit.
- Update: By editing a permit and submitting it.
- Delete: Deleting Users and Permits is only authorised by logging in as Admin. This is to replicate only management having the authority to do this.

**Mobile Responsiveness**: When viewed on mobile, everything is scaled down, but does not compromise ease of use. This is thanks to Bootstraps mobile-first approach.

## Future Features

**Profile Image**: An image of the User would replace the generic avatar.

**Encrypted-Login/Password**: Not storing the original password, but only an ecrypted version of it. So privacy/security is not compromised.

**Management Level Options** Giving more options to Users based on their job title (management role). This will allow them to sign off permits and delete if unacceptable.


## Testing

- Navbar links were checked to ensure they routed to correct locations
- Password input was tested with correct password and incorrect. Routing to correct page if correct and displaying an error if incorrect.
- Navbar links checked to make sure only the desired options appeared depending on who was logging in (Admin or User).
- CRUD Functions were thoroughly tested.
- HTML was formatted, some Illegal characters were found in the Jinja templates. But these are acceptable as Flask requires these to work properly.
- Full site was tested on Chrome Developer Tools.
- Responsiveness was tested using [Responsinator](http://www.responsinator.com/)

## Deployment
A live demo can be found here [General Work Permits App](https://colmdoyle-milestone-3.herokuapp.com/).

The website is hosted using Herkoku. It is linked from the master branch of my milestone repository [Colm Doyle Milestone 3 GitHub](https://github.com/collyd21/milestone_3). When new commits are added to the repository, the website will update with any changes.

**Cloning via Github**:
*	Open the Github Repository link.
*	Click on the 'Clone or Download' button.
*	Copy the URL provided.
*	Open Git Bash terminal.
*	Change the current working directory to the location where you want the cloned directory to be made.
*	Type 'git clone' and paste in the URL.
*	Press Enter.

**Deploying on Heroku**

- Navigate to [Heroku](https://heroku.com).
- Install the Heroku CLI (Command Line Interface)
- Creating an account is required. When at the Heroku dashboard, click the "New" button on top right. A dropdown appears and you now click "Create New app".
- Name your app. **Note app names must be unique**.
- Choose your region.
- On heroku dashboard navigate to "App connected to GitHub" and choose your relevant Github Repository to link to Heroku app.
- Go to your Bash Terminal.
- Login to Heroku using `$ heroku login`
- Create a requirements.txt file: `$ pip3 freeze --local > requirements.txt.`
- Create Procfile: `$ echo web: python app.py > Procfile` **Note capital "P" in procfile. Also replace "app.py" with that of the name of your python file if different.
- Git add, commit and push.
- Again on your Heroku dashboard, find the apps name, click and then go to "settings".
- Navigate to "Config Vars", click "Reveal Vars" and enter your IP and your port.

## Credits
### Media

Background image was sourced from [Adobe Stock Images](https://stock.adobe.com/uk/).

the avatar image was sourced from [Shutterstock](https://www.shutterstock.com/).

### Acknowledgements

The Code Institute community on Slack.

Stack Overflow community and previous threads/ questions that helped me through difficulties with my project.

W3schools for some very helpful tips.
