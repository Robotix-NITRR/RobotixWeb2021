# RobotixWeb 2021
## Set up instructions
### Install the virtualenv package
The virtualenv package is required to create virtual environments. You can install it with pip:
```
pip install virtualenv
```
### Create the virtual environment
To create a virtual environment, you must specify a path. For example to create one in the local directory called ‘mypython’, type the following:
```
virtualenv env
```
### Activate the virtual environment
You can activate the python environment by running the following command:

Mac OS / Linux
```
source env/bin/activate
```
Windows
```
env\Scripts\activate
```
You should see the name of your virtual environment in brackets on your terminal line e.g. (env).

Any python commands you use will now work with your virtual environment

### Deactivate the virtual environment
```
deactivate
```
### Installation of package
```
pip install -r new_requirements.txt
python manage.py runserver
```
## For now use new_requirements.txt file
