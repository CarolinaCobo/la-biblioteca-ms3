# La Biblioteca
![Logo](assets/testing/responsive-screens.png)






tests:

name
incorrect password/username




delete shadow in navbar > https://github.com/Dogfalo/materialize/issues/1115

add Hoover effect https://ianlunn.github.io/Hover/ 



[Live site](https://la-biblioteca-ms3.herokuapp.com/index)

## Table of contents

1.[UX](#ux)

* [User Stories](#user-stories)
* [Site owner objectives](#site-owner-objectives)
* [Wireframes](#wireframes)
* [Structure](#structure)
* [Home page](#home-page)
* [Game page](#game-page)
* [Contact page](#contact-page)
* [Styling](#styling)
  * [Colours](#colours)
  * [Fonts](#fonts)
  * [Favicon](#favicon)

2.[Features](#features)

* [Existing features](#existing-features)
* [Future features](#future-features)

3.[Technologies used](#technologies-used)

* [Languages](#languages)
* [Libraries](#libraries)
* [Programs and tools](#programs-and-tools)

4.[Testing](#testing)

5.[Deployment](#deployment)

* [GitHub pages](#github-pages)
* [Cloning](#cloning)

6.[Credits](#credits)

* [Content](#content)
* [Media](#media)
* [Acknowledgements](#acknowledgements)
* [I received advice and support from](#user-stories)

## UX

### User stories

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

### Site owner objectives

**As a site owner I would like to**: |  **So that I could**: |
| ------------- |:-------------:|
| Delete content added by  the users. | delete anything that shouldn't be there. |
| Add, delete or remove genres. | provide, change or delete them for the users. |

### Wireframes

The wireframes for this project can be found below:

* Desktop:
  ![Desktop]()
* iPad:
   ![iPad]()
* Mobile:
  ![Mobile]()

### Structure

* The aim during the design and development process was to make the site simple and easy for the user to navigate it, finding relevant information and using visual buttons that would help them to use the different functionalities.
* All pages follow the same style and color palette that is simple and focus on the important information.
* The navbar on top of the page is static and have the links to the different pages of the site. It also has the logo. It's responsive on smaller devices.
* The home page has buttons to navigate the different parts of the site as well, the display will be different depending if the user is logged in or not.
* The Books page has a responsive grid display so the user can view the available books easily.
* The book page has a card with all the book information and buttons to mark as favorite, edit or delete the book as well as a comments section.

### Home page

In the home page buttons for the different functionalities can be found in both the navbar and the buttons in the parallax section. The display of the navbar and buttons is different depending on if the user is logged in or not.

### Books page

In this page from top to bottom, the user can search for a particular book in the search bar, or view all the available books in a grid. If the user has added the book they could also edit or delete it.

### Contact page

The contact page has three boxes with name, email, question and button to submit a question. Once the question is submitted an alert will open showing that the message was sent.

### Styling

#### Colours

Using [Colorhunt.co](https://colorhunt.co) I chose a palette with complementary colours that could be found in different sites:

* ![#fff](https://via.placeholder.com/15/fff/000000?text=+) `#fff` - h1, background in the instructions, score, footer.
* Gradient from the right of ![#7f53ac](https://via.placeholder.com/15/7f53ac/000000?text=+) `#7f53ac` and ![#657ced](https://via.placeholder.com/15/657ced/000000?text=+) `#657ced` - Background of the page and the modal.
* ![#c7a1f5](https://via.placeholder.com/15/c7a1f5/000000?text=+) `#c7a1f5` - Icons and buttons hover on the icons.
* ![#ccc](https://via.placeholder.com/15/ccc/000000?text=+) `#ccc` - Border of the button elements.
* ![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+) `#ffffff` - Game board background color.  

#### Fonts

For the logo and the Score I used  "Press Start 2P" and for the rest of the site "Poppins". Both imported from Google fonts. Used on the Universal selector to format the entire site.

#### Favicon

I used as Favicon one of the images used for the game. I converted it using Favicon.io.

## Features

### Existing Features

* Feature 1 - Landing page with two buttons that allows the user to pick between two options Play or How to Play.
* Feature 2 - Modal that covers the game.
  * Built with HTML, CSS and JS the modal disappears and let the user play the game.
  * Pressing the play button set the score to 0 as well.

* Feature 3 - Allows the user to click on "How to Play".
  * Built with HTML, CSS and JS once the button is clicked a modal appears with the instructions of how to play the game.

* Feature 4 - Two buttons on the top of the page, one to return to the main page and another to go to the contact page.
  * The buttons are SVG images and link with the Home page and contact page.

* Feature 4 - Allows users to send a message to the site owner.
  * Built with HTML, CSS and JS and used EmailJS API to send a message to the site owner.

* Feature 5 - Let the user replay the game from the game over screen.
  * Replay button displayed usually in games that let the user play again.

* Feature 6 - Timer.
  * 30 seconds timer that when is over triggers the game over modal, showing the score of that game, restart and home buttons.

### Future features

* Score board with a ranking of players.

## Technologies Used

### Languages

* [HTML](https://www.w3schools.com/html/) -  to build the structure of this site.
* [CSS](https://www.w3schools.com/css/) - to style and fix media queries and the max width.
* [JavaScript](https://www.javascript.com/) - to build the game and add interactivity with buttons and send messages to the site owner.

### Libraries

* [Google Fonts](https://fonts.google.com) - used for fonts on the site.
* [Hover.css](https://ianlunn.github.io/Hover/) - used for animation effects on social icons and various buttons throughout the site.
* [Google Fonts](https://fonts.google.com/) - Import the fonts used ont he site.
* [Hero Icons](https://heroicons.com/) - Site icons.
* [TailwindCSS](https://tailwindcss.com/docs/box-shadow) - For inspiration on the styles for the site.

### Programs and Tools

* [VSCode](https://code.visualstudio.com/) - used as IDE for the project.
* [Git](https://git-scm.com/) - used for version control.
* [Github](https://github.com/) - used to host repository and to generate the live website.
* [Github projects](https://github.com/CarolinaCobo/puppy-rush/projects/1) - used to track all the tasks, bugs and issues.
* [Balsamiq](https://balsamiq.com/) - used to create the wireframes.
* [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) - used to test and optimize the site.

## Testing

The test performed can be found at the [testing.md](testing.md) file.

## Deployment

### GitHub pages

My site is hosted on [GitHub pages](https://pages.github.com/), deployed directly from the master branch.
The steps to complete the hosting process.

1. Log into GitHub.
2. Pick the repository.
3. Go to settings.
4. Scroll down to GitHub Pages section.
5. Select as a source "master branch".
6. The page refreshes automatically and the project is deployed.
7. The URL for the page will be public automatically.

### Cloning

To run this code locally, you can clone this repository directly into the editor of your choice by following the steps below:

1.Go the [Github](https://github.com/) repository that you wish to clone:

* Click Code with the down arrow so the modal will open.  
* Click on the clip icon to copy the repository.

2.Open Terminal.

3.Change the current working directory to the location when you want the cloned directory.

4.Paste the link previously copied or type the following into your Terminal: git clone [https://github.com/CarolinaCobo/puppy-rush.git].

5.Press Enter to create a local clone.

To cut ties with this GitHub repository, type git remote rm origin into the terminal.
For more information regarding cloning of a repository click [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

## Credits

### Content

This project JS part was following [Ania Kubow tutorial](https://www.youtube.com/watch?v=XD5sZWxwJUk) in how to build a Candy Crush style game. I made some changes on the game and built the CSS and HTML pulling information from different sites referenced below in the acknowledgements.

### Media

* The color palette used in this site was obtained from [Colorhunt.co](https://colorhunt.co)
* The favicon for this site has been resized in [Favicon.io](https://favicon.io/)
* The Library [Tailwind](https://tailwindcss.com/) has been used for inspiration on styles.
* Icons are from [Hero Icons](https://heroicons.com/).
* The icons have been made for this project by a designer.

### Acknowledgements

I received inspiration for this project from:

* [Ania Kubow](https://www.youtube.com/channel/UC5DNytAJ6_FISueUfzZCVsw)
* [MDN Documentation](https://developer.mozilla.org/en-US/)
* [W3Schools](https://www.w3schools.com/)
* [CSS-Tricks](https://css-tricks.com/)
* [StackOverflow](https://stackoverflow.com/)
* [Codú Community](https://www.youtube.com/channel/UCvI5azOD4eDumpshr00EfIw)
* [FreeCodeCamp](https://www.freecodecamp.org/)
* [Anna Greaves](https://github.com/AJGreaves)
* [Bernardo Castilho](https://github.com/Bernardo-Castilho/dragdroptouch)

### I received advice and support from

* [Codú Community](https://discord.com/invite/NxSkYtZ)
* My mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/)
* [Niall Maher](https://www.linkedin.com/in/nialljoemaher/?originalSubdomain=ie)
* Code Institute [Slack Community](code-institute-room.slack.com)
