## Table of Content
1. [Bugs](#bugs)
2. [Validator Testing](#validator-testing)
    1. [HTML](#html)
    2. [CSS](#css)
    3. [Javascript](#javascript)
    4. [Python](#python)
    5. [Lighthouse](#lighthouse)
3. [Browser Testing](#browser-testing)
4. [Device Testing](#device-testing)
5. [Manual Testing](#manual-testing)
6. [Automated testing](#automated-testing)


Extensive testing was done to make sure all the features work as expected. I did both the automated test and the manual test.

## Bugs

|  Bug |  Solution  |Status   |
|--|--|--|
|  
User can book a consultation at the same date and time as another user | Add to the views.py file Booking.objects.filter(date=date, time=time).exists() | fixed |
|  
Form to change booking does not appear | add 'form': form to the views.py file  | fixed |
|  
Menu on mobile devices is positioned incorrectly | fixed CSS style   | fixed |
|  
Daterange filter doesn't work on admin panel | delete wrong version and install new   | fixed |

##### Back to [top](#table-of-content)<hr>

## Validator Testing

### HTML
The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML of the website. 
There were errors and warnings in the reports about unclosed elements and tags, incorrect values ​​and types of elements, unnecessary trailing slashes. All errors and warnings have been fixed, the project's HTML code has been re-checked without errors.
<details><summary>base.html</summary>
<img src="static/validation/validation-html-base.png">
</details>

<details><summary>index.html</summary>
<img src="static/validation/validation-html-index.png">
</details>

<details><summary>about.html</summary>
<img src="static/validation/validation-html-about.png">
</details>

<details><summary>blog.html</summary>
<img src="static/validation/validation-html-blog.png">
</details>

<details><summary>post_detail.html</summary>
<img src="static/validation/validation-html-post-detail.png">
</details>

<details><summary>booknow.html</summary>
<img src="static/validation/validation-html-booknow.png">
</details>

<details><summary>bookings.html</summary>
<img src="static/validation/validation-html-bookings.png">
</details>

<details><summary>delete-booking.html</summary>
<img src="static/validation/validation-html-delete-booking.png">
</details>

<details><summary>change-booking.html</summary>
<img src="static/validation/validation-html-change-booking.png">
</details>

<details><summary>contact-us.html</summary>
<img src="static/validation/validation-html-contact.png">
</details>

<details><summary>message-received.html</summary>
<img src="static/validation/validation-html-message-received.png">
</details>

<details><summary>login.html</summary>
<img src="static/validation/validation-html-login.png">
</details>

<details><summary>logout.html</summary>
<img src="static/validation/validation-html-logout.png">
</details>

<details><summary>signup.html</summary>
<img src="static/validation/validation-html-signup.png">
</details>
<br>

### CSS 
The website CSS style has successfully passed the [W3C Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/). 
<details><summary>style.css</summary>
<img src="static/validation/validation_css.png">
</details>
<br>

### Python

All Python code was manually checked using [CI Python Linter](https://pep8ci.herokuapp.com/). 

#### Blog app
<details><summary>admin.py</summary>
<img src="static/validation/validation-python-blog-admin.png">
</details>
<details><summary>forms.py</summary>
<img src="static/validation/validation-python-blog-forms.png">
</details>
<details><summary>models.py</summary>
<img src="static/validation/validation-python-blog-models.png">
</details>
<details><summary>tests_admin.py</summary>
<img src="static/validation/validation-python-blog-tests_admin.png">
</details>
<details><summary>tests_models.py</summary>
<img src="static/validation/validation-python-blog-tests_models.png">
</details>
<details><summary>tests_views.py</summary>
<img src="static/validation/validation-python-blog-tests_views.png">
</details>
<details><summary>urls.py</summary>
<img src="static/validation/validation-python-blog-urls.png">
</details>
<details><summary>views.py</summary>
<img src="static/validation/validation-python-blog-views.png">
</details>
<br>

#### Booking app

<details><summary>admin.py</summary>
<img src="static/validation/validation-python-booking-admin.png">
</details>
<details><summary>forms.py</summary>
<img src="static/validation/validation-python-booking-forms.png">
</details>
<details><summary>models.py</summary>
<img src="static/validation/validation-python-booking-models.png">
</details>
<details><summary>tests_models.py</summary>
<img src="static/validation/validation-python-booking-tests_models.png">
</details>
<details><summary>tests_views.py</summary>
<img src="static/validation/validation-python-booking-tests_views.png">
</details>
<details><summary>urls.py</summary>
<img src="static/validation/validation-python-booking-urls.png">
</details>
<details><summary>views.py</summary>
<img src="static/validation/validation-python-booking-views.png">
</details>
<br>

#### Contact app
<details><summary>admin.py</summary>
<img src="static/validation/validation-python-contact-admin.png">
</details>
<details><summary>forms.py</summary>
<img src="static/validation/validation-python-contact-forms.png">
</details>
<details><summary>models.py</summary>
<img src="static/validation/validation-python-contact-models.png">
</details>
<details><summary>tests_models.py</summary>
<img src="static/validation/validation-python-contact-tests_models.png">
</details>
<details><summary>tests_views.py</summary>
<img src="static/validation/validation-python-contact-tests_views.png">
</details>
<details><summary>urls.py</summary>
<img src="static/validation/validation-python-contact-urls.png">
</details>
<details><summary>views.py</summary>
<img src="static/validation/validation-python-contact-views.png">
</details>
<br>

### Lighthouse
Performance, best practices and SEO was tested using Lighthouse.

- Desktop
<details><summary>Home</summary>
<img src="static/lighthouse/lighthouse_desktop_home.png">
</details>
<details><summary>About</summary>
<img src="static/lighthouse/lighthouse_desktop_about.png">
</details>
<details><summary>Blog</summary>
<img src="static/lighthouse/lighthouse_desktop_blog.png">
</details>
<details><summary>Post details</summary>
<img src="static/lighthouse/lighthouse_desktop_postdetails.png">
</details>
<details><summary>Contact</summary>
<img src="static/lighthouse/lighthouse_desktop_contact.png">
</details>
<details><summary>Book Now</summary>
<img src="static/lighthouse/lighthouse_desktop_booknow.png">
</details>
<details><summary>Bookings</summary>
<img src="static/lighthouse/lighthouse_desktop_bookings.png">
</details>
<details><summary>Bookings edit</summary>
<img src="static/lighthouse/lighthouse_desktop_bookings_edit.png">
</details>
<details><summary>Bookings delete</summary>
<img src="static/lighthouse/lighthouse_desktop_bookings_delete.png">
</details>
<details><summary>Login</summary>
<img src="static/lighthouse/lighthouse_desktop_login.png">
</details>
<details><summary>Logout</summary>
<img src="static/lighthouse/lighthouse_desktop_logout.png">
</details>
<details><summary>Sign up</summary>
<img src="static/lighthouse/lighthouse_desktop_signup.png">
</details>
<br>

- Mobile
<details><summary>Home</summary>
<img src="static/lighthouse/lighthouse_mobile_home.png">
</details>
<details><summary>About</summary>
<img src="static/lighthouse/lighthouse_mobile_about.png">
</details>
<details><summary>Blog</summary>
<img src="static/lighthouse/lighthouse_mobile_blog.png">
</details>
<details><summary>Post details</summary>
<img src="static/lighthouse/lighthouse_mobile_postdetails.png">
</details>
<details><summary>Contact</summary>
<img src="static/lighthouse/lighthouse_mobile_contact.png">
</details>
<details><summary>Book Now</summary>
<img src="static/lighthouse/lighthouse_mobile_booknow.png">
</details>
<details><summary>Bookings</summary>
<img src="static/lighthouse/lighthouse_mobile_bookings.png">
</details>
<details><summary>Bookings edit</summary>
<img src="static/lighthouse/lighthouse_mobile_bookings_edit.png">
</details>
<details><summary>Bookings delete</summary>
<img src="static/lighthouse/lighthouse_mobile_bookings_delete.png">
</details>
<details><summary>Login</summary>
<img src="static/lighthouse/lighthouse_mobile_login.png">
</details>
<details><summary>Logout</summary>
<img src="static/lighthouse/lighthouse_mobile_logout.png">
</details>
<details><summary>Sign up</summary>
<img src="static/lighthouse/lighthouse_mobile_signup.png">
</details>
<br>

##### Back to [top](#table-of-content)<hr>

## Browser Testing

Testing has been carried out on the  following browsers: 
  - Google Chrome
  - Firefox
  - Microsoft Edge

The site was constantly tested during the process of creating the site in the Gitpod Environment and the deployed site on Heroku was also tested in terms of user experience.
The available functionality and user experience is reflected in the table below.

##### Back to [top](#table-of-content)<hr>

## Device Testing
The Project was tested using a multi-device emulator with different display sizes in the Google Chrome Developer Dashboard.
The following devices have been tested:

- Nest HubMax (Desktop)
- iPad Pro (Tablet)
- iPad Air (Tablet)
- iPad Mini (Tablet)
- Galaxy Tab S4 (Tablet)
- Nexus 7 (Mobile)
- Nokia N9 (Mobile)
- iPhone 5/SE (Mobile)
- iPhone 4 (Mobile)

##### Back to [top](#table-of-content)<hr>

## Manual Testing

### Site Navigation
| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| NavBar                |            |                                                                    |           |
| Site Brand (logo)     | Click      | Redirect to home                                                   | Pass      |
| Home Link             | Click      | Redirect to home                                                   | Pass      |
| About Link            | Click      | Open About page                                                    | Pass      |
| Blog link       | Click      | Open Blog page                                               | Pass      | 
| Contact link          | Click      | Open Contact page                                                  | Pass      |                                               | Pass      |
| Book link             | Click      | Open Book page                                                     | Pass      |
| Account Dropdown      | Click      | Open My Account dropdown                                           | Pass      |
| My Account Dropdown   | Display    | 'Bookings' and 'Logout' become visible                            | Pass      |
| Bookings link        | Click      | Open bookings dashboard page                                                | Pass      |
| Bookings link        | Display    | Only visible if user is logged in                                  | Pass      |
| Logout Link           | Click      | Open logout confirm page                                           | Pass      |
| Logout Link           | Display    | Only visible if user is logged in                                  | Pass      |
| Log In Link           | Click      | Open Login page                                                    | Pass      |
| Log In Link           | Display    | Not visible if user logged in                                      | Pass      |
| Sign Up Link          | Click      | Open Sign up page                                                  | Pass      |
| Mobile View           |            |                                                                    |           |
| Hamburger Menu        | Responsive | Display when screen size reduces to medium size                    | Pass      |
| Hamburger Menu        | Click      | Opens up hamburger menu                                            | Pass      |
| Site Brand (logo)     | Click      | Redirect to home                                                   | Pass      |
| Home Link             | Click      | Redirect to home                                                   | Pass      |
| About Link            | Click      | Open About page                                                    | Pass      |
| Blog link       | Click      | Open Treatments page                                               | Pass      |
| Contact link          | Click      | Open Contact page                                                  | Pass      |
| Book link             | Click      | Open Book page                                                     | Pass      |
| Account Dropdown      | Click      | Open My Account dropdown                                           | Pass      |
| My Account Dropdown   | Display    | 'Bookings' and 'Logout' become visible                            | Pass      |
| Bookings link        | Click      | Open bookings dashboard page                                                | Pass      |
| Bookings link        | Display    | Only visible if user is logged in                                  | Pass      |
| Logout Link           | Click      | Open logout confirm page                                           | Pass      |
| Logout Link           | Display    | Only visible if user is logged in                                  | Pass      |
| Log In Link           | Click      | Open Login page                                                    | Pass      |
| Log In Link           | Display    | Not visible if user logged in                                      | Pass      |
| Sign Up Link          | Click      | Open Sign up page                                                  | Pass      |
|                       |            |                                                                    |           |
| Footer                |            |                                                                    |           |
| All social media links             | Click      | Open in new tab                         | Pass      |
<br>

### Home Page
| Element               | Action  | Expected Result                 | Pass/Fail |
|-----------------------|---------|---------------------------------|-----------|
| Book Now! Button      | Click   | Open Book page                  | Pass      |
| Entire page           | Display | Responsive and readable         | Pass      |
| Carousel              | Display | Carousel display amount of picture  | Pass      |
| Carousel              | Display | Carousel displays pictures titles   | Pass      |
| Carousel              | Click   | Carousel displays next picture      | Pass      |
| Carousel              | Click   | Carousel displays previous picture  | Pass      |
<br>

### About Page
| Element               | Action  | Expected Result                 | Pass/Fail |
|-----------------------|---------|---------------------------------|-----------|
| Entire page           | Display | Responsive and readable         | Pass      |
<br>

### Blog Page
| Element               | Action  | Expected Result                 | Pass/Fail |
|-----------------------|---------|---------------------------------|-----------|
| Blog page           | Display | Responsive and readable         | Pass      |
| Title of post           | Display | 	Open Post details page       | Pass      |
<br>


### Post details Page
| Element               | Action  | Expected Result                 | Pass/Fail |
|-----------------------|---------|---------------------------------|-----------|
| Post page           | Display | Responsive and readable         | Pass      |
| Post details user logged      | Display                                   | Field that allows leave comment is displayed                | Pass      |
| Post details user not logged  | Display                                   | Field that allows leave comment is not displayed       | Pass      |
| Comment section user logged  | Click                                   | User can  leave a comment      | Pass      |
| Like section user logged  | Click                                   | User can  leave a like      | Pass      |
| Like section user not logged  | Click                                   | Unauthorized user can not leave a like      | Pass      |

<br>

### Contact page
| Element                    | Action                                    | Expected Result                            | Pass/Fail |
|----------------------------|-------------------------------------------|--------------------------------------------|-----------|
| Open page user logged      | Display                                   | Email field auto-filled                  | Pass      |
| Open page user not logged  | Display                             | Display page with requests authorization      | Pass      |
| Email field                | Insert incorrect format                   | On submit: form won't submit               | Pass      |
| Email field                | Insert incorrect format                   | Error message displays                     | Pass      |
| Email field                | Insert correct format                     | On submit: form submit                     | Pass      |
| Email field                | Leave empty                               | On submit: form won't submit               | Pass      |
| First name field           | Insert incorrect format                   | On submit: form won't submit               | Pass      |
| First name field           | Insert incorrect format                   | Error message displays                     | Pass      |
| First name field           | Insert correct format                     | On submit: form submit                     | Pass      |
| First name field           | Leave empty                               | On submit: form won't submit               | Pass      |
| Last name field            | Insert incorrect format                   | On submit: form won't submit               | Pass      |
| Last name field            | Insert incorrect format                   | Error message displays                     | Pass      |
| Last name field            | Insert correct format                     | On submit: form submit                     | Pass      |
| Last name field            | Leave empty                               | On submit: form won't submit               | Pass      |
| Message field              | Leave empty                               | On submit: form won't submit               | Pass      |
<br>

### Book page
| Element                    | Action                                    | Expected Result                            | Pass/Fail |
|----------------------------|-------------------------------------------|--------------------------------------------|-----------|
| Open page user logged      | Display                                   | Personal info auto-filled                  | Pass      |
| Open page user not logged  | Display                                   | Personal info not auto-filled              | Pass      |
| Service field            | Click                                     | Available services dropdown              | Pass      |
| Service field            | Leave empty                               | On submit: form won't submit               | Pass      |
| Sevice field            | Leave empty                               | Error message displays                     | Pass      |
| Name field           | Insert correct format                     | On submit: form submit                     | Pass      |
| Name field           | Leave empty                               | On submit: form won't submit               | Pass      |
| Name field           | Leave empty                   | Error message displays                     | Pass      |
| Date field           | Choose date from datepicker                     | On submit: form submit                     | Pass      |
| Date field           | Leave empty                               | On submit: form won't submit               | Pass      |
| Date field           | Leave empty                   | Error message displays                     | Pass      |
| Date/Time field           | Double book on the same date or time as another user       | Error message displays                     | Pass      |
| Datepicker for date             | Select date                               | Date becomes gray                          | Pass      |
| Datepicker for time               | Select time                               | Time becomes gray and filled in Date field | Pass      |
| Time field           | Choose time from datepicker                     | On submit: form submit                     | Pass      |
| Time field           | Leave empty                               | On submit: form won't submit               | Pass      |
| Time field           | Leave empty                   | Error message displays                     | Pass      |
| Book button                | Click                                     | Appointment gets booked, user redirected   | Pass      |
<br>

### Booking Dashboard
| Element                    | Action                                    | Expected Result                            | Pass/Fail |
|----------------------------|-------------------------------------------|--------------------------------------------|-----------|
| Open page user logged      | Display                                   | Dashboard page is displayed                | Pass      |
| Open page user not logged  | Display                                   | User gets redirected to login page         | Pass      |
| Delete button                     | Click                                     | Modal pops up asking for confirmation      | Pass      |
| Delete modal               | Click Cancel                              | Appointment gets canceled                  | Pass      |
| Change button              | Click                                     | Redirect to change booking page               | Pass      |
| Change booking page           | Display                                   | All info auto filled  | Pass      |
| Change booking page           | Change date/time                               | Date field is filled                       | Pass      |
| Change booking page           | Don't change date/time                               | Error message displays                      | Pass      |
| Change date button         | Click                                     | Form submits                               | Pass      |
<br>

### ***Test Users Stories***

1. As a first time user I can visit a website so that should help me understand what the site is about

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Open website | Home page displays nav bar, website description, about us section etc | Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_1.png">
</details>
<br>

2. As a User I can use a navbar and social icons so that I can navigate the site and access socials

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
 | Click on the 'Home' link in the navigation bar | Home page will load| Works as expected |
  | Click on the 'Logo' link in the navigation bar | Home page will load| Works as expected |
| Click on the 'Sign up' link in the navigation bar | Sign up page will load| Works as expected |
| Click on the 'Login' link in the navigation bar | Login page will load| Works as expected |
| Click on the 'About' link in the navigation bar | About page will load| Works as expected |
| Click on the 'Blog' link in the navigation bar | Blog page will load| Works as expected |
| Click on the 'Contact' link in the navigation bar | Contact page will load| Works as expected |
| Click on the 'Account Dropdown' link in the navigation bar  | Open My Account dropdown and 'Bookings' and 'Logout' become visible  |  Works as expected   |
| Click on the 'My Bookings' link in the navigation bar | Booking list page will load| Works as expected |
| Click on the 'Logout' link in the navigation bar | Logout page will load| Works as expected |
| Click on the 'Book Now' link in the navigation bar | Book Now page will load| Works as expected |
 | Scroll to footer at bottom of page | Find social links | Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_1.png">
<img src="static/user story/user_story_1.png">
<img src="static/user story/user_story_16_1.png">
<img src="static/user story/user_story_2_4.png">
<img src="static/user story/user_story_2_5.png">
<img src="static/user story/user_story_6.png">
<img src="static/user story/user_story_19_1.png">
<img src="static/user story/user_story_22.png">
<img src="static/user story/user_story_22.png">
<img src="static/user story/user_story_17_1.png">
<img src="static/user story/user_story_20_1.png">
<img src="static/user story/user_story_5.png">
</details>
<br>

3. As a User I can find a footer so that I can move to the social links, see working hours and find an address

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Scroll to footer at bottom of page | Find footer with social links, working hours and an address | Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_5.png">
</details>
<br>

4. As a User I can find testimonials so that I can read what clients are saying about company

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Scroll to testimonials at bottom of home page | Find slider with all testimonials | Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_4.png">
</details>
<br>

5. As a Website owner I can add about us section so that users can find information about company

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'About' link in the navigation bar | About page will load| Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_5.png">
</details>
<br>

6. As a User I can find a blog so that I can read regular updated legal posts

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|Click on the 'Blog' link in the navigation bar | Blog page will load and display all legal posts| Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_6.png">
</details>
<br>

7. As a user I can open the post details so that makes me more interested and I can read all information

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|Click on the title of the post on the blog page | Post details page will load and display post| Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_7.png">
</details>
<br>

8. As a Site Admin I can create, read, update and delete posts so that I can manage my blog content

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|Go to the admin panel, use "/admin" | Admin site will load and display Login page| Works as expected |
|Login as admin | Admin panel will load | Works as expected |
|Choose Blog model | Display blog model with function to add, delete, update or read post | Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_8_1.png">
<img src="static/user story/user_story_8_2.png">
<img src="static/user story/user_story_9_1.png">
</details>
<br>

9. As a Site Admin I can create draft posts so that I can finish writing the content later

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|On admin panel, choose Blog model and function add post | Display blog model with function to add post | Works as expected |
|when admin create a post choose save as draft | Post will save as draft| Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_9_1.png">
<img src="static/user story/user_story_9_2.png">
</details>
<br>

10. As a User I can view comments on an individual post so that I can read the conversation

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Scroll to comment section at bottom of post detail page | Find all comments that users left | Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_10.png">
</details>
<br>

11. As a User I can leave a comments so that allows me to participate in a forum-like discussion or leave my opinion

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|logged user open post details page and find a comment field | blog details page will display comment field for authorized user | Works as expected |
|write comment and click send button | Post will send and user received message about that| Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_11.png">
<img src="static/user story/user_story_18_6.png">
</details>
<br>

12. As a User I can view the number of likes on each post so that I can see which is the most popular or viral

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Open blog page | Find likes under each posts | Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_13_1.png">
</details>
<br>

13. As a User I can like a post so that I can interact with the content

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| open post details page and find a likes at the bottom of post | blog details page will display likes| Works as expected |
|logged user clicks on like | Red like will display on the screen| Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_13_1.png">
<img src="static/user story/user_story_13_2.png">
</details>
<br>

14. As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|Go on admin panel and choose comment model | Comment model will load | Works as expected |
|Choose a new comment and approve it or disapprove as admin | Comment will display or not on post detail page| Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_14_1.png">
<img src="static/user story/user_story_14_2.png">
</details>
<br>

15. As a Site Owner I can add site pagination so users can see splitting list of my website’s blog posts into separate pages

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|Go on blog page | splitting list of posts will displays into separate pages if more than 6 | Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_15.png">
</details>
<br>

16. As a user I can register an account so that gives me more options as leave comment, like and opportunity to booking

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|Click on the 'Sign Up' link in the navigation bar| Signup page will load | Works as expected |
|Fill the form | User will become authorazed and receive a message about this | Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_16_1.png">
<img src="static/user story/user_story_18_1.png">
</details>
<br>

17. As a user I can logout so that can save my data

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|Click on the 'Logout' link in the navigation bar | Logout page will load and Modal pops up asking for confirmation | Works as expected |
|Click on the 'Logout' button | User will become unauthorized | Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_17_1.png">
<img src="static/user story/user_story_18_2.png">
</details>
<br>

18. As a Site owner I can add alert messages for users so that users can receive message about their actions

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|User logs in | receives a message about it | Works as expected |
|User logs out | receives a message about it | Works as expected |
|User signs up | receives a message about it | Works as expected |
|User changes a booking | receives a message about it | Works as expected |
|User deletes a booking | receives a message about it | Works as expected |
|User leaves a comment | receives a message about it | Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_18_1.png">
<img src="static/user story/user_story_18_2.png">
<img src="static/user story/user_story_18_3.png">
<img src="static/user story/user_story_23_2.png">
<img src="static/user story/user_story_24_2.png">
<img src="static/user story/user_story_18_6.png">
</details>
<br>

19. As a user I can contact organization so that I can get in touch with a company

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Contact' link in the navigation bar | Contact page will load| Works as expected |
|Fill the form and click send |user redirected to contact page with message | Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_19_1.png">
<img src="static/user story/user_story_19_1.png">
</details>
<br>

20. As a User I can book a consultation so that I reserve a date and time for consultation

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|Click on the 'Book Now' button in the navigation bar or on home page  | Book now page  will load  | Works as expected |
|Fill the form and click send | Appointment gets booked, user redirected to bookings dashboard | Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_20_1.png">
<img src="static/user story/user_story_20_2.png">
</details>
<br>

21. As a User I can not book a consultation already booked so that my booking is valid and not double booked

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| From the bookings page, attempt to book a consultation and date already booked | Error message displays to say booking not possible | Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_21.png">
</details>
<br>

22. As a User I can find booking dashboard so I will see all my bookings

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|Click on the 'Bookings' link in the navigation bar | Booking dashboard will load  | Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_22.png">
</details>
<br>

23. As a user I can edit booking so I receive an opportunity to change the date/time of the consultation

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|From 'My Bookings' click 'Change' on booking to be changed | Change bookings form will load  | Works as expected |
|Change the date/time and click change | Appointment is changed, user redirected to bookings dashboard | Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_23_1.png">
<img src="static/user story/user_story_23_2.png">
</details>
<br>

24. As a user I can delete a booking so I can cancel my consultation reservation

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| From 'My Bookings' click 'Delete' on booking to be cancelled| Modal pops up asking for confirmation  | Works as expected |
| Click "Delete"| Booking will be delete  | Works as expected |

<details><summary>user story</summary>
<img src="static/user story/user_story_24_1.png">
<img src="static/user story/user_story_24_2.png">
</details>
<br>

##### Back to [top](#table-of-content)<hr>

## Automated testing
Testing was done using the built in Django module, unittest.
Coverage was also used to generate a report

***Contact app:***
<details><summary>Contact app tests_views.py </summary>
<img src="static/unittest/unit-test-contact-tests_views.png">
</details>
<details><summary>Contact app tests_models.py</summary>
<img src="static/unittest/unit-test-contact-tests_models.png">
</details>
<br>
<details><summary>Coverage Contact app</summary>
<img src="static/unittest/unit-test-contact-coverage.png">
</details>
<br>

***Booking app:***

<details><summary>Booking app tests_views.py </summary>
<img src="static/unittest/unit-test-booking-tests_views.png">
</details>
<details><summary>Booking app tests_models.py</summary>
<img src="static/unittest/unit-test-booking-tests_models.png">
</details>
<br>
<details><summary>Coverage Booking app</summary>
<img src="static/unittest/unit-test-booking-coverage.png">
</details>
<br>

***Blog app:***

<details><summary>Blog app tests_views.py </summary>
<img src="static/unittest/unit-test-blog-tests_views.png">
</details>
<details><summary>Blog app tests_models.py</summary>
<img src="static/unittest/unit-test-blog-tests_models.png">
</details>
<details><summary>Blog app tests_admin.py</summary>
<img src="static/unittest/unit-test-blog-tests_admin.png">
</details>
<br>
<details><summary>Coverage Blog app</summary>
<img src="static/unittest/unit-test-blog-coverage.png">
</details>
<br>


