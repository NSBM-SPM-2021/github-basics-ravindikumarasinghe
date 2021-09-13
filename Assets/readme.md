<p><h1 align="center">Blog App</h></p><hr>

This Blogging web application project is purely made with Django as the backend and Bootstrap as the frontend.

## Installation Instructions

If you want to work with this project or create a version of it make sure to follow the steps below!

0. Make sure to install ` Python 3 `, ` pip ` and ` virtualenv `   
1. Create a project folder
   
    ```bash
        $ mkdir project
        $ cd project
    ```
2. Create a python 3 virtualenv, and activate the environment to install requirements.
    ```bash
        $ python3 -m venv env
        $ source env/bin/activate
    ``` 
3. Install the project dependencies from `requirements.txt`
    ```
        (env)$ pip install -r requirements.txt
    ```
4. Clone the repository
   
    ```bash
        (env)$ git clone https://github.com/akhil-s-kumar/django-blog-app.git
        (env)$ cd django-blog-app
    ```

You have now successfully set up the project on your environment.

## How to run  the project?

Make sure you are in `env` and then do the following each at a time.

```bash
(env)$ python manage.py makemigrations
(env)$ python manage.py makemigrations blogApp
(env)$ python manage.py makemigrations users
(env)$ python manage.py migrate
(env)$ python manage.py createsuperuser
(env)$ python manage.py runserver
```

## Features

### Blog list View
List all blog posts with Title, Tag, Number of total comments, Date Posted, Image, and some body part with Read More button.

### Recent Posts
List all the post which are created recently with Image thumb and Title.

### category list
List all the categories related to the posts with total number of posts each categories have.

### Search
List all blog posts with the search query that you enter.

### Pagination
To limit with a certain number of posts in each page.

### Blog Detail View
To view the complete blog post when clicked on Read More or on the Title.

### Login
Admin /Blog owner can login to the admin panel to get control over the site.

### Comment
Users can comment to any blog post after login or comment without login.

### Create Blog Post
Blog owner can add posts from admin panel 

### Edit Post
Blog owner can edit, delete, add media files to Posts.

## Tech Stacks

* **Language:**  Python 3.7
* **Framework:** Django 3.1.5

## How you can contribute to this project?

1. Fork this project to your GitHub account
2. Clone the repository to your local machine and follow the above Installation instructions.
3. Find an issue or feature and work on it.
4. Make a pull request.
