# Home-Watch

A web application that allows users to be in the contact about everything happening in his/her neighborhood.

## Author
### [Abdimulhin Adan](https://github.com/AbdimulhinYussuf3675)

## Getting Started

Fork this repository or clone it to your local machine running Ubuntu by using the following commands:
```
git clone (https://github.com/Marcusjnls/biz-mtaani.git)
```

## Behavior Driven Development
* The program should navigate to the login page on load:

     **Input Example**: On page load

     **Output Example**: Navigate to the login page

* The program should navigate to sign up page when Sign Up is clicked on the login form:

     **Input Example**: Click on **Sign Up** on the login form

     **Output Example**: Redirected to the sign up page

* The program should navigate to the login page when Logout is clicked on the navigation bar:

     **Input Example**: Click on **Logout** on the navigation bar

     **Output Example**: Redirected to the login page

* The program should direct the user to their neighborhood page when logged in and already has a neighborhood:

    **Input Example**: Log in

    **Output Example**: Redirected to their neighborhood page

* The program should direct the user to the index page with neighborhood listings when logged in and has no neighborhood:

    **Input Example**: Log in

    **Output Example**: Redirect the user to the index page with neighborhood listings

* The program should navigate to the profile page when the My Profile is clicked on the navigation bar:

    **Input Example**: Click on **My Profile** on the navigation bar

    **Output Example**: Redirected to the profile page

* The program should navigate to the admin dashboard when one logs in as an admin:

    **Input Example**: Login in as Admin

    **Output Example**: Navigate to the admin dashboard

## Setup Instructions:
### Requirements

* set up a virtual environment using the following command
```
python3.8 -m venv --without-pip virtual
```

And activate it

```
source virtual/bin/activate
```
* install the latest version of pip

```
curl https://bootstrap.pypa.io/get-pip.py | python
```

* Install the requirements in the requirements.txt file using
```
pip install -r requirements.txt
```

* create a .env file in your rootfolder and add the following configurations
```
SECRET_KEY='<random-string>'
DEBUG=True
ALLOWED_HOSTS='*'
DATABASE_URL='postgres://databaseowner:password@localhost/databasename'
```

* create postgres database
```
CREATE DATABASE <your-database-name>
```

* create a migration using the following command
```
python3.6 manage.py makemigrations
```

and migrate

```
python3.6 manage.py migrate
```

* create an admin account
```
python 3.6 manage.py createsuperuser
```
and fill-in your credentials

* run the application using 
```
python3.6 manage.py runserver
```

* navigate to the admin panel by typing 
```
localhost:8000/admin
```

## Running the tests

Run the following commands:
```
python3.6 manage.py tests
```

## Deployment

View the following [document](https://github.com/bernie-haxx/Deployment_to_heroku_django) in order to deploy to a live system

## Built Using

* [Django](https://www.djangoproject.com/download/)
* [Bootstrap](https://getbootstrap.com)
* [MDBootstrap](https://mdbootstrap.com/)
* Html
* Python
* Materialize

# Contacts
adam.abdimulhi.001@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

