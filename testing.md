# La Biblioteca - Testing

[View the live project here.](https://la-biblioteca-ms3.herokuapp.com/)

## Table of Contents

* [Code validation](#code-validation)
  * [Validation Services](#validation-services)
* [Manual Testing](#manual-testing)
  * [Unit Testing](#unit-testing)
  * [Devices and browsers](#deviices-and-browsers)
* [User stories and site owner objectives testing](#user-stories-and-site-owner-objectives-testing)
* [Bugs](#bugs-discovered)
  * [Known Bugs](#known-bugs)
  * [Unsolved Issues](#unsolved-issues)

<h1> 1. Code Validation </h1>

## Validation Services

To validate the code the following **validation services** and **linters** were used to check the code:

* [W3C Markup Validator](https://validator.w3.org/)
    Checks the markup validity of Web documents in HTML, XHTML, SMIL, MathML, among others.
    ![W3C Markup Results image](static/images/testing/html-test-pass.png)

* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
    Checks the validity of cascading style sheets (css) and (X)HTML documents with style sheets.
    ![W3c CSS Results Image](static/images/testing/css-test-pass.png)

* [PEP8 Online validation](http://pep8online.com/checkresult)
    This linter checks the validity of Python code against the PEP8 requirements
    ![PEP8 results image](static/images/testing/pep8-test-pass.png)

* [Chrome DevTools Lighthouse](https://developers.google.com/web/tools/lighthouse)
    An open-source automated tool for improving webpages by running audits for performance, accessibility, progressive web apps, SEO etc.

    ![Lighthouse](static/images/testing/lighthouse.png)


<h1> 2. Manual Testing </h1>

### Unit Testing

All the site has been tested and all the steps have been documented, it can be found in the [Unit Testing document](https://drive.google.com/file/d/1eBxfC-XzAlOhbvxMPc1ZTM2ME3GABF90/view?usp=sharing)

### Devices and browsers

**Browser versions used in testing:**

* Google Chrome Version 89.0.4389.114 (Official Build) (x86_64).
* Safari Version 14.0.3 (16610.4.3.1.7).
* Firefox Version 87.0 (64-bit)

**Tested on the following devices using the Google Chrome Developer tools:**

* Moto G4
* Galaxy S5
* Pixel 2
* Pixel 2 XL
* iPhone 5/SE
* iPhone 6/7/8
* iPhone 6/7/8 Plus
* iPhone X
* iPad
* iPad Pr
* Surface Duo
* Galaxy Fold

**Tested on the following devices using the Firefox Developer tools:**

* Galaxy S9/S9+ Android 7.0
* iPad
* iPhone 6/7/8 iOS 11
* iPhone 6/7/8 plus iOS 11
* iPhone x/XS iOS 12
* Kindle Fire HDX Linux

**Tested on the following physical devices:**

* iPhone XS
* iPhone 12
* Samsung S20
* iPad Pro 12.9 2nd generation

<h1> 3. User stories and site owner objectives testing </h1>

## User stories

**As a user I would like to**: |  **So that I could**: |
| ------------- |:-------------:|
| 1. To immediately  understand the purpose  of the page. | search for books and write comments |
| 2. To see all the content without having to register.| enjoy a faster experience |
| 3. To be able to search for keywords. | easily find what I'm looking for. |
| 4. Easily navigate the site | quickly find what I need |
| 5. To be able to register easily without having to input too much information.| register quickly. |
| 6. See books information. | See the book information quickly to decide if I like it. |
| 7. Comment on the different books | share my thoughts with other users. |
| 8. Be able to add books | I can share them with other users |
| 9. Be able to edit the books I added | I can communicate with them |
| 10. Be able to contact the site owner | I can communicate with them |
|||

### Testing user stories

1. The user can read and access to the different parts of the site from both the home page and the navbar.

2. Users are not requested to log in to access the content, they'll have to do it if they want to interact with the website.

3. The users can use the search bar available in the books page, they don't need to be logged in to use this functionality.

4. The website has a simple design that is visually appealing using the same colour pallette.

5. The user only has to fill a simple form (name, username and password) to be registered in the page.

6. If a user is interested in a book they will only have to click on the + icon and the book information will open in a new page so they can easily go back and open another one once they finished reading, marking it as favorite or commenting on it.

7. The users can comment their thoughts on the books once they are registered and logged in.

8. The user can access to the add book functionality, the user can access to it from both the home page and navbar.

9. If the user has added a book they will be able to both edit it and delete it from the database. They'll need to be logged in to do so.

10. At the bottom of all pages the user can access their email address to contact the site owner.

The user might be using the page as a first time user or as a returner user.

Returner registered users would be more benefited of the site CRUD functionality as they could Create books or comments, read the content, update any information they have added to the site and delete it if they don't want it to be available for any reason.

## **Site owner objectives**

**As a site owner I would like to**: |  **So that I could**: |
| ------------- |:-------------:|
| Delete content added by  the users. | delete anything that shouldn't be there. |
| Add, delete or remove genres. | provide, change or delete them for the users. |
|||

The site owner will have access to the same functionalities listed above, but also will be the only one able to use the CRUD operations with thee Book Genres.

<h1> 4. Bugs </h1>

The bugs project can be found din the following [link](https://github.com/CarolinaCobo/la-biblioteca-ms3/projects/1)

## Bugs found and solved

  The issue log is managed on the [GitHub Project Issues section](https://github.com/simonjvardy/the-reading-room/issues) and linked to the solved commit.

  Probably one of the most challenging ones was to figure out why using a modal to confirm the book to be deleted to be a random one and not the selected. The code can be seen on the [Issue #3](https://github.com/CarolinaCobo/la-biblioteca-ms3/issues/3) To solve this bug I used the developer tools to compare what id was being injected into the modal.

  I found quite a few errors in the format of the HTML when used the different validation systems that were fixed on the go.

  Another mistake was not tracking the bugs on the project on Github, so I made it after, this would be avoided in future projects.

  ## Unsolved bugs

  In the bugs Project page the Format required in the input is stated as a not resolved bug. After research it seems Materialize doesn't allow to use patterns as used in previous projects. This will be solved in future work on the site.