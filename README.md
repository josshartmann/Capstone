## HarvardX CS50W: Web Programming with Python and JavaScript

### Course's link
See [here](https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript).

### Requirements
The final project is your opportunity to design and implement a dynamic website of your own. So long as your final project draws upon this course’s lessons, the nature of your website will be up to you, subject to some constraints as indicated below.

In this project, you are asked to build a web application of your own. The nature of the application is up to you, subject to a few requirements:

* Your web application must be sufficiently distinct from the other projects in this course (and, in addition, may not be based on the old CS50W Pizza project), and more complex than those.
    * A project that appears to be a social network is a priori deemed by the staff to be indistinct from Project 4, and should not be submitted; it will be rejected.
    * A project that appears to be an e-commerce site is strongly suspected to be indistinct from Project 2, and your README.md file should be very clear as to why it’s not. Failing that, it should not be submitted; it will be rejected.
* Your web application must utilize Django (including at least one model) on the back-end and JavaScript on the front-end.
* Your web application must be mobile-responsive.
* In a README.md in your project’s main directory, include a writeup describing your project, and specifically:
    * Why you believe your project satisfies the distinctiveness and complexity requirements, mentioned above.
    * What’s contained in each file you created.
    * How to run your application.
    * Any other additional information the staff should know about your project.
* If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to a requirements.txt file!
* Though there is not a hard requirement here, a README.md in the neighborhood of 500 words is likely a solid target.

Beyond these requirements, the design, look, and feel of the website are up to you!

### Final project

My final project is Coach in Air Quotes. Users are able to register, edit their profile, calculate how much exercise they need to do to compensate a cheat meal, save that on a log so they can "pay" the exercise later and then remove from the "log" tab. They can also use the website do generate a gym workout by choosing the muscular groups they want.

The project was built using Django as a backend framework and JavaScript as a frontend programming language. All generated information are saved in database(SQLite by default).

All webpages of the project are mobile-responsive.

#### Installation
  - Install project dependencies by running `pip install -r requirements.txt`.
  - Make and apply migrations by running `python manage.py makemigrations` and `python manage.py migrate`.
  - Go to website address and register an account.

#### Files and directories
  - `capstone` - main application directory.
    - `static/capstone` - contains all static content.
        - `images` - contais all images used on the project.
        - `style.css` - contains compiled CSS file and its map.
        - `capstone.js` - all JavaScript files used in project.
    - `templates/capstone` - contains all application templates.
        - `home.html` - profile page, first page a user sees after login.
        - `index.html` - main templates, shows when user is not logged in.
        - `layout.html` - base template. All other tempalates extend it.
        - `log.html` - this template shows the all the cheat meals the user has consumed.
        - `results.html` - template that shows the amount of exercise an user have to do to burn the cheat meal he has chosen.
        - `should-i-eat.html` - this one has the "cheat meal calculator".
        - `workout-generator.html` - here the user can generate a gym workout.
        - `workout.html` - this one show the gym workout he has chosen.
    - `admin.py` - here I added some admin classes to help the superuser experience.
    - `models.py` contains four models I used in the project. `User` the standard User model, `Profile` used to store all user additional info, `ShouldIEat` is where stays all the cheat meal data and `Quotes` that contains all the inspirational quotes shown to the user in `home.html`.
    - `urls.py` - all application URLs.
    - `views.py` respectively, contains all application views.
  - `web_project` - project directory.

The project's video: https://www.youtube.com/watch?v=MAuJFAd8WZw