<p><h1 align="center">Blog App</h>
<h3 align="center">This Blogging web application project is purely made with Django as the backend and Bootstrap as the frontend.</h3></p>

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
        (env)$ git clone 'link of project'
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

## How to run

### Default

You can run the application from the command line with manage.py.
Go to the root folder of the application.

Run migrations:
```bash
$ python manage.py migrate
```

Initialize data:
```bash
$ python manage.py loaddata users posts comments
```

Run server on port 8000:
```bash
$ python manage.py runserver 8000
```

#### Helper script

It is possible to run all of the above with helper script:

```bash
$ chmod +x scripts/run.sh
$ scripts/run.sh
```

### Docker

It is also possible to run the blog app using docker:

Build the Docker image:
```bash
$ docker build -t project_name -f docker\Dockerfile .
```

Run the Docker container:
```bash
$ docker run --rm -i -p 8000:8000 project_name
```

#### Helper script

It is possible to run all of the above with helper script:

```bash
$ chmod +x scripts/run_docker.sh
$ scripts/run_docker.sh
```

## Post Installation

Go to the web browser and visit `http://localhost:8000/home`

Admin username: **admin**

Admin password: **adminpassword**

User username: **uname**

User password: **userpassword**

## Helper Tools

### Django Admin

It is possible to add additional admin user who can login to the admin site. Run the following command:
```bash
$ python manage.py createsuperuser
```
Enter your desired username and press enter.
```bash
Username: admin_username
```
You will then be prompted for your desired email address:
```bash
Email address: admin@example.com
```
The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.
```bash
Password: **********
Password (again): *********
Superuser created successfully.
```

Go to the web browser and visit `http://localhost:8000/admin`

### Tests

#### Default
Activate virtual environment:

On macOS and Linux:
```bash
$ source env/bin/activate
```

On Windows:
```bash
$ .\env\Scripts\activate
```

Running tests:
```bash
$ python manage.py test blog
```

#### Docker

It is also possible to run tests using Docker:

Build the Docker image:
```bash
$ docker build -t project_name -f docker\Dockerfile .
```

Run the Docker container:
```bash
$ docker run --rm project_name test blog
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
