# Django_Plaid_Project

## View Image folder for the images of the project

## Setup

Clone the project on your system.
```
git clone https://github.com/pravash21/Django_Plaid_Project.git
cd Django_Plaid_Project
```
Database is default sqlite database :

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
Setup Redis :

Download Redis for Windows or Linux.
Start the redis server on cmd.
```
redis-server
```

Setup Virtual Environment :

```
pip install virtualenv
virtualenv env
```
You need to add your secret keys to the environment variables in env/Scripts/activate file. You can get the list of keys which you need to store, in the plaid_link/keys.py. To add the variables open the file env/bin/activate and add environment variables:
```
export PLAID_SECRET='your_secret_key'
export PLAID_PUBLIC_KEY='your_public_key'
```
Activate the virtual environment
```
env/Scripts/activate
```
  
Setup Celery :
  
Install the dependencies
```
pip install -r requirements.txt
```
Migrate the changes for celery results
```
python manage.py migrate django_celery_results
```
Now start the worker process
```
celery -A plaid_django worker -l info
```
Now celery worker is running in background. You can call the tasks asynchronously. You can test this by running test_celery() in django shell
```
python manage.py shell

>>> from plaid_link.tests import test_celery
>>> test_celery()
```

Setup ngrok :

ngrok is used to capture response from webhooks. Install ngrok from ngrok.com.
After that,
```
ngrok http -host-header=localhost 8000
```
This should start up a secure tunnel that is connected to your local HTTP port. It will look something like this.
```
ngrok by @inconshreveable                                                                               (Ctrl+C to quit)                                                          Session Status                online                                                                               
Account                       Pravash Jha (Plan: Free)                                                                  
Version                       2.3.35                                                                                    
Region                        United States (us)                                                                   
Web Interface                 http://127.0.0.1:4040            
Forwarding                    http://e12115e38452.ngrok.io -> http://localhost:8000
Forwarding                    https://e12115e38452.ngrok.io -> http://localhost:8000
```

Run Server :

After setting up all the things you need to migrate the changes, create admin user and run the server.
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
python manage.py runserver
```
You can view the project in:
http://127.0.0.1:8000/signup

How to link a bank account via Plaid after login:

1. Click on 'Click here' to link the bank.
2. Select bank and put 'username' = user_good and password = 'pass_good'.
Now see the results in celery which fetches the transaction and save it on out sqlite db.

Home Page
![Home Page](https://github.com/pravash21/Django_Plaid_Project/blob/master/image/home.png?raw=true)

Signup Page
![Signup Page](https://github.com/pravash21/Django_Plaid_Project/blob/master/image/signup.png?raw=true)
