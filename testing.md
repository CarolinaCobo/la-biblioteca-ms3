# La Biblioteca - Testing

[View the live project here.](https://la-biblioteca-ms3.herokuapp.com/)

## Table of Contents

* [La BibliotecaProject Testing Details](#t)

  * [Table of Contents](#table-of-contents)
  * [Automated Testing](#automated-testing)
    * [Validation Services](#validation-services)

  * [Manual Testing](#manual-testing)
    * [Unit Testing](#unit-testing)
    * [Testing undertaken on desktop](#testing-undertaken-on-desktop)
    * [Testing undertaken on tablet and phone devices](#testing-undertaken-on-tablet-and-phone-devices)
  * [Bugs discovered](#bugs-discovered)
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
| To immediately  understand the purpose  of the page. | search for books and write comments |
| To see all the content without having to register.| enjoy a faster experience |
| To be able to search for keywords. | easily find what I'm looking for. |
| Easily navigate the site | quickly find what I need |
| To be able to register easily without having to input too much information.| register quickly. |
| See books information. | See the book information quickly to decide if I like it. |
| Comment on the different books | share my thoughts with other users. |
| Be able to add books | I can share them with other users |
| Be able to edit the books I added | I can communicate with them |
| Be able to contact the site owner | I can communicate with them |
|||

**As a returner user I would like to**: |  **So that I could**: |
| ------------- |:-------------:|
| Log in and out easily. | Log in everywhere easily. |
| Edit comments. | modify my comment. |
| Check the books I added and marked as favorite. | easily check it out any time. |
| Edit the book I  added | change the information in case I made a mistake |
| Delete the book I added.| delete it. |
| See books information. | See the book information quickly to decide if I like it. |
| Comment on the different books | share my thoughts with other users. |
| Be able to contact the site owner | I can communicate with them |
|||

## **Site owner objectives**

**As a site owner I would like to**: |  **So that I could**: |
| ------------- |:-------------:|
| Delete content added by  the users. | delete anything that shouldn't be there. |
| Add, delete or remove genres. | provide, change or delete them for the users. |
|||

<h1> 4. Bugs </h1>

The issue log is managed on the [GitHub Project Issues section](https://github.com/simonjvardy/the-reading-room/issues) using the standard GitHub [bug\_report.md template](https://github.com/simonjvardy/the-reading-room/blob/master/.github/ISSUE_TEMPLATE/bug_report.md)
and the [features_request.md template](https://github.com/simonjvardy/the-reading-room/blob/master/.github/ISSUE_TEMPLATE/feature_request.md)

## Bugs found and solved

## Unsolved bugs

