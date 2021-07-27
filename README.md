# Home-Watch

A web application that allows users to get information  about everything happening in his/her neighborhood.

## Author
### [Abdimulhin Adan](https://github.com/AbdimulhinYussuf3675)

## Getting Started



## User stories
A user can :
* Sign in with the application to start using.

* Set up a profile about me and a general location and my neighborhood name.

* Find a list of different businesses in my neighborhood.

* Find Contact Information for the health department and Police authorities near my neighborhood.

* Create Posts that will be visible to everyone in my neighborhood.


* Change My neighborhood when I decide to move out.

* Only view details of a single neighborhood.

## Setup Instructions:
### Requirements


Fork this repository or clone it to your local machine running Ubuntu by using the following commands:
```
git clone (https://github.com/AbdimulhinYussuf3675/home-watch.git)
```
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

* Python [Django](https://www.djangoproject.com/download/)
* [Bootstrap](https://getbootstrap.com)
* [MDBootstrap](https://mdbootstrap.com/)
* Html

# Contacts
adam.abdimulhi.001@gmail.com

## License
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](http://opensource.org/licenses/MIT)
>MIT license &copy;  2021 Abdimulhin

