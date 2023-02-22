# Borrow A Story!
[View the live project here](https://borrow-a-story.herokuapp.com/)

## Introduction
"Borrow a Story" is a website for a public library, which catalogues all of its collections online. A visitor to the library can easily access the website and find books they would be interested in, read the summary, look-up the shelf they can find it on and borrow it via the website. All it takes is creating their account, which takes just a minute allowing them to explore the world of stories and information with the click of a button!

![Image of application responsiveness on different devices](./media/images/responsive.JPG)


## Table of Content
 -  [UX/UI](#ux)
    - [Site Purpose](#purpose])
    - [Site Objectives](#objectives)
    - [Target Audience](#audience)
    - [User Stories](#stories)
        1. [As an Admin](#admin)
        1. [As a User](#user)
    - [Design](#design)
        1. [Framework](#framework)
        1. [Schemas](#schemas)
        1. [Color](#color)
        1. [Typography](#typography)
 - [Features](#features)
    - [Present Features](#present)
        1. [Navbar](#nav)
        1. [Home Page](#home)
        1. [Book Borrow/Return Page](#borrow)
        1. [Book Issued/Returned Confirmation Page](#confirmation)
        1. [Profile](#profile)
        1. [Manage Book (For Admins)](#managebook)
        1. [Edit Book (For Admins)](#editbook)
        1. [Sign-up/Log-in/Log-out](#sign-in)
    - [Features to Implement](#future)
 - [Testing](#testing)
 - [Technologies and Libraries Used](#tech)
 - [Deployment](#deployment)
 - [Acknowledgements and Credits](#credits)

<br><br>

# UX/UI <a name="ux"></a>
## Site Purpose <a name="purpose"></a>
The purpose of this website is to provide a platform for both, the Library staff and the Library patrons, where they can access their objectives through the ease of navigation. A library staff can efficiently and conveniently catalogue books available at the library, look-up the status of books whether they are available or have been borrowed by a library patron, and manage the patron's information.
On the other hand, a library patron/user can conveniently find the book they might be interested in, find the location in the library where it is kept, and if available, borrow it easily via the website itself. 

## Site Objectives<a name="objectives"></a>
1. Provide an appealing and user friendly website.
1. Provide effective database mangement tools to the staffs.
1. Provide ease of navigation throughout the website.
1. Encourage more people to visit the library by coalescing digital media with print media.

## Target Audience <a name="audience"></a>
1. Regular visitors to the library.
1. Reluctant visitors who want to avoid the hassle of going to the counter and getting a book issued.
1. Youngsters who are more comfortable with digital platforms.
1. For every book lover out there.
1. For everyone who wants to try out the public library.

## User Story <a name="stories"></a>
 ### As An Admin <a name="admin"></a>
   - I can add and update new books to the catalogue.
   - I can view the complete borrow history of each book.
   - I can check which books are currently borrowed by which user.
   - I can check the return status of each book.

 ### As a User <a name="user"></a>
   - I can register easily.
   - I can check the book catalogue and where it is located in the library.
   - I can read the book summary and borrow it easily.
   - I can bookmark my favorite books to view them later.

![User Stories](./media/images/user-story.JPG)


## Design <a name="design"></a> <br>
 ### Framework <a name="framework"></a><br><br>
 
   #### Homepage: <br>
 ![Wireframe of the homepage](./media/images/wireframe-one.png)
 <br><br>

   #### Book Issue/Return Page: <br>
 ![Wireframe of the issue/retrun](./media/images/wireframe-two.png)
<br><br>

   #### Profile Page: <br>
 ![Wireframe of the profile page](./media/images/wireframe-three.png)
 <br><br>

## Database Schemas <a name="schemas"></a><br>

![Database schema](./media/images/database-schema.JPG)

## Color <a name="color"></a><br>
The color pallets have been selected form the MaterializeCSS's library and are used to appropriately brighten the website and entice the users.
<br><br>

![Color pallet](./media/images/color-pallets.jpg)

## Typography <a name="typography"></a><br>
The fonts used in the website are the standard fonts provided by MaterializeCSS framework, which is Roboto 2.0

# Features <a name="features"></a>

## Present Features <a name="present"></a>

### Navbar <a name="nav"></a>
The navbar is conveniently constructed to display the website name, clicking on which would take you to the homepage. It also displays the links depending on the user viewing the website. If it's a new user, it will display the log-in and sign-up links, if the user is logged in, it will display the profile and log-out links, and to an admin, it will display the 'admin' link instead of the profile link, so that the admin can easily access the database.
The navbar is also customised to wrap all the links into a burger menu for small-screen devices.
<br>

Nav-bar as seen by a logged-out user:
![Looged-out navbar](./media/images/nav-bar-loggedout.JPG)
<br>

Nav-bar as seen by a logged-in user:
![Logged-in navbar](./media/images/nav-bar-user.JPG)
<br>

Nav-bar as seen by an admin:
![Admin navbar](./media/images/nav-bar-admin.JPG)
<br>

Mobile-device Menu:

![Burger menu](./media/images/burger-menu.JPG)
<br>
<br>

### Homepage <a name="home"></a>
The homepage displays the catalogue of all the books at the library, and is paginated to show 9 books per page. The book information such as the title, author name, published year and the shelf it is kept on are all contained within the cards. The book cards are also customised. If the user is logged-out, it'll ask them to log-in to see the detail, where as to a logged-in user, it'll show either of three options: Borrow, Return or Not-Available depending on the status of the book. This card also has the bookmark icon, which the user can interact with and bookmark them.
<br><br>

Homepage as seen by a logged-out user:
![Logged-out homepage](./media/images/homepage-loggedout.JPG)
<br><br>

Homepage as seen by a logged-in user:
![Logged-in homepage](./media/images/homepage-loggedin.JPG)

### Book Borrow/Return Page <a name="borrow"></a>
Upon clicking Borrow/Return button, the user is redirected to a new page where the user can read a summary of the book, and if they want to borrow it, they can just select a return date and borrow it directly. For returning, the same can be done, by just clicking the Return button, the database will record the book as returned by the user.
<br>

![Borrow the book](./media/images/issue-page-1.JPG)

![Borrow the book](./media/images/issue-page-2.JPG)

![Return the book](./media/images/return.JPG)
<br>

### Book Issued/Returned Confirmation Page <a name="confirmation"></a>
After borrowing/returning the book, the user is redirected to the confirmation page, which displays the confirmation message and also, at the bottom shows a collection of a few books from the catalogue that the user might be interested in. Hence, encouraging them to explore and read more.
<br><br>

Book Borrowed Confirmation:

![Book Borrowed](./media/images/borrowed-1.JPG)
<br><br>

Book Returned Confirmation:

![Book Returned](./media/images/returned.JPG)
<br><br>

Selection of Books from the Catalogue the User Might Be Interested In:

![Book Selection](./media/images/borrowed-2.JPG)
<br><br>

### Profile <a name="profile"></a>
The profile page displays the basic information of the user that they provided while registering, like user_name and e-mail address. It also has a section for contact information, which the user can fill, like address and phone number. This information is handled by the django's form element to update the database.

This page also displays the books which have been borrowed by the user and the books bookmarked by them.
<br><br>

Bio Section:<br>

![User's Bio](./media/images/profile-bio.JPG)
<br><br>

Borrowed Books Section:<br>

![Borrowed Books](./media/images/borrowed-books.JPG)
<br><br>

Bookmarks:<br>

![Bookmarks](./media/images/bookmarks.JPG)
<br><br>


### Manage Book (For Admins) <a name="managebook"></a>
The Manage Book is available only for users with "admin" privilege. Here, an admin can run various functions for managing the inventory, like add new author, add a new book and edit/delete a book from the library.

![Add Author](./media/images/add-author.JPG)
<br><br>

![Add New Book](./media/images/add-another-book.JPG)
<br><br>

![Edit/Delete Book](./media/images/edit-delete-book.JPG)
<br><br>


### Edit Book (For Admins) <a name="editbook"></a>
This page is also available only for user with "admin" privilege. On this page, an admin can edit/correct any information regarding a particular book.

![Edit Book](./media/images/edit-book.JPG)
<br><br>


### Sign-up/ Log-in/ Log-out <a name="sign-in"></a>
The website's user authentication is taken care by the django-allauth service.
<br>

Sign-up page:<br>

![User sign-up](./media/images/signup-page.JPG)
<br><br>

Sign-in page:<br>

![User sign-in](./media/images/signin-page.JPG)
<br><br>

Sign-out page:<br>

![User sign-out](./media/images/signout.JPG)

## Features to Implement <a name="future"></a>
In the future, given more time to work on the website, I would like to implement the following features:
- Book Search feature on the homepage.
- Return/Explore buttons on the book catalogue on user's Profile page.
<br><br>

# Testing <a name="testing"></a>

## Manual Testing
1. Book cards weren't rendering properly.
    - The intention was to display 3 cards per row, however, it wasn't rendering properly even after using ```{% if forloop.counter|divisibleby:3 %}```.
    - The looped cards weren't closed within the ```<div class='row'></div>``` container properly, resulting in improper rendering.
    - This issue was solved by locating the closing ``div`` tag.

2. The Return button and Not-Available tags weren't showing as intended.
    - The intention was, if a particular book had been borrowed by the user, the ``Return`` button will show under the card, whereas, if the user is different and the book is borrowed, the ``Not Available`` tag will be shown.
    - Was using ``if`` statement which was trying to get data from a queryset in the template, hence it wasn't working as intended.
    - Used ``for`` loop to iterate through the queryset and get the proper data.

3. The button under the cards wasn't showing ``Return`` command to the current borrower of the book.
    - The ``Return`` button was only displayed to the user who was the first one to borrow it, even if they had returned it.
    - Was using ``{% if book.issue.issued_to==user %}`` which was getting the first entered data only and not the latest one.
    - ``{% for issue in book.issue.reverse|slice:":1" %}`` allowed the template to extract the latest entry of the Issue model.

4. CSS/JS links weren't working.
    - Customisation made in the CSS and JS files weren't affecting the website.
    - Had missed the ``{% load static %}`` tag in the base.html file.

5. The website wasn't opening via ``python3 manage.py runserver`` command.
    - Was throwing an error every time when trying to launch the site.
    - The DB_URL had changed on the Heroku side after scheduled maintenance.
    - Needed to update the url few time during the project lifecycle.

6. Non-logged user was able to access other pages of the website.
    - Copying the links of the book_issue.html and profile pages and launching them without logging-in allowed anyone to access these pages.
    - Added ``{% if user.is_authenticated %}`` tags to prevent non-authorised users from accessing such pages.

7. Bookmark button was not working properly on the Home page.
    - Clicking on the bookmark button, the icon wasn't changing.
    - The functionality of the bookmark button was working as intentded, and the database was being updated accordingly.
    - However, the icon change wasn't triggering.
    - The code in the template was not able to check whether the current user has bookmarked it or not.
    - Again, the code was not properly iterating through the queryset and hence wasn't checking the user's bookmarks as intended.
    - This was solved by adding a function ``user_bookmarked`` in the Book model class and changing the code, whose final form will be discussed in the next point.

8. The Book card on the Homepage was displaying multiple bookmark icons.
    - The code was iterating through the queryset and displayed the bookmarks according to all the users who had bookmarked the book.
    - ``user_bookmarked`` function was added to the Book model class, which extracted a list of users.
    - The code in the template was changed to its final form ``{% if user.id in book.user_bookmarked %}``, which now checks if the current user's name is in the list.
    - The bookmark works as intended now, both in functionality and display.

9. The Edit button on Profile page wasn't working properly.
    - The ``Edit`` button wasn't triggering the modal containing the contact information form if the user had no borrowed books.
    - The Bookmarks were also not displaying if no books were currently borrowed.
    - The borrowed books carousel wasn't properly closed withing the ``{% if %}`` statement, and the bug was removed by enclosing them within the statement.

10. The Return By section in the ``book_issue.html`` page wasn't working properly.
    - The intention of the Return By section was to show a date picker to the user.
    - It was appearing as text field.
    - Needed to add ``DateInput`` class in the ``form.py`` and call it within the ``IssueForm`` class via widgets to make it work.

11. The website was having issues while deployment via Heroku.
    - The website wasn't launching after deploying it through Heroku app.
    - The requirement.txt file wasn't updated properly when ``crispy-forms-materialize`` was installed.
    - The issue was solved by running ``pip3 freeze --local > requirements.txt`` command in the terminal.

12. The image was not being uploaded to Cloudinary when add a new book from Manage Book page by admin.
    - The issue was resolved by adding ``enctype="multipart/form-data"`` to FORM element in template and ``request.files`` in VIEWS while fetching the form data. 


## Validator Testings
  - HTML files passed through the [W3C Validator](https://validator.w3.org/) without any reported issue.
  <br><br>

     ![HTML Validator](./media/images/html-validator.JPG)
  <br><br>

  - CSS file passed through the [Jigsaw Validator](https://jigsaw.w3.org/css-validator/) without any reported issue.
  <br><br>

     ![CSS Validator](./media/images/css-validator.JPG)
  <br><br>

  - The website has great Accessibility score in Lighthouse. There are minor fluctuations in the Performance score, as MaterializeCSS has some unsued CSS tags.
  <br><br>

     ![Lighthouse score](./media/images/lighthouse.JPG)

  - Python passed through PEP8 test with no issues. As the online PEP8 website is down, had to use ``linter`` extension from GitPod. Initially it showed few errors due to long codes, which were rectified by changing the lines.

  - Tested on several browsers, including the standart Mozilla Firefox, Chrome and Safari. The website runs smoothly on all the browsers.

  ## Unfixed Bugs
  No bugs were found as of writing of this document. Any bug found during the development and deployment of the project was worked on and removed.


# Technologies And Libraries Used <a name="tech"></a>

- ## Languages
    1. [HTML5](https://en.wikipedia.org/wiki/HTML5)
    2. [CSS](https://en.wikipedia.org/wiki/CSS)
    3. [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    4. [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

- ## Database
    1. [PostgreSQL](https://www.postgresql.org/)

- ## Frameworks
    1. [Django](https://www.djangoproject.com/) - Python Framework 
    2. [MaterializeCSS](https://materializecss.com/) - CSS Framework
    3. [Crispy Forms](https://pypi.org/project/crispy-forms-materialize/) - Django Forms Application

- ### Hosting Platforms/Other Platforms
    1. [Heroku](https://www.heroku.com)
    2. [Cloudinary](https://cloudinary.com)
    3. [GitHub](https://github.com)
    4. [GitPod](https://gitpod.io)

- ### Supporting Programs/Softwares
    1. Balsamiq
    2. [DrawSQL](https://drawsql.app)

- ### Installed Packages
    ![Installed Packages](./media/images/installed-packages.JPG)


# Deployment <a name="deployment"></a>

The site was deployed to Heroku. The steps to deploy are as follows:

1. Install Django & Gunicorn: 
    ``pip3 install 'django<4' gunicorn``
1. Install Django database & psycopg: 
    ``pip3 install dj_database_url psycopg2``
1. Install Cloudinary: 
    ``pip3 install dj3-cloudinary-storage``
1. Create the requirements.txt file with the following command: 
    ``pip3 freeze --local > requirements.txt``
1. Create Django Project using: 
    ``django-admin startproject libraryData .``
1. After this, create an app as: 
    ``python3 manage.py startapp borrow_a_story``
1. Add this to the settings.py file within our project directory inside ``INSTALLED_APPS``.
1. Migrate these changes using: 
    ``python3 manage.py migrate``
1. Navigated to Heroku & create a new app ``borrow-a-story``.
1. Add the Heroku Postgres database to the Resources tab within Heroku.
1. Navigate to the Settings Tab to add the following key/value pairs to the configvars:

    - key: SECRET_KEY | value: randomkey
    - key: PORT | value: 8000
    - key: CLOUDINARY_URL | value: API environment variable
    - key: DATABASE_URL | value: value supplied by Heroku

1. Add the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the env.py file

1. Add the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the settings.py file

1. Add an import os statement for the env.py file.

1. Add Heroku to the ALLOWED_HOSTS in settings.py

1. Creat the Procfile

1. Push the project to Github

1. Connect the github account to Heroku through the Deploy tab

1. Connected the github project repository, and then click on the "Deploy" button

<br>

# Acknowledgements and Credits <a name="credits"></a>
- The images for the book covers were used from their respective websites.
- [Django Documentation](https://docs.djangoproject.com/en/4.1/) was heavily used to look-up and consult for various database manipulation.
- Huge thanks to the CodeInstitute Tutors for their valuable help and support.
- Great appreciation for my mentor Martina Terlevic, for her constant support.
