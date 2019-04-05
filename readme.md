----------------------------------------START-------------------------------


#Rest API using Django framework
#Library and files needed
  Python
  Django        ~pip install django
  Djangorestframework     ~pip install djangorestframework
  
  ------DIRECTORY------- 
  //Create a folder for your project at any directory you want, name it
  
  //Open either CMD with administrative preferences or Visual code/Pycharm's terminal and install djangoreestframework
  
  //now cd to that project folder and create a project for yourself by writing following code...
  
  -------PROJECT FOLDER------
  
  ~django-admin startproject projectname
  
  // Now you will see a project is created with some py files with manage.py file.
  //Now go for creating webapp
  
  ~python manage.py startapp webapp
  
  // after this webapp folder will be created with some more py files.
  
  #Lets edit setting.py to tell about rest framework, go to the root project folder and edit setting.py
  
  ------------------SETTING.PY---------------
  
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'webapp',
]

// Add last two lines to your setting.py file as shown above

----------------------------MODEL.PY--------------------------------

//Now its time create models(database) with some details ex. employees. After creating the model we have to register that so that we can perform operations on that data.

---------------------------ADMIN.PY-------------------------------

//So let's open admin.py and register the table

//Now it need to be migrated(updates table structure), so within the terminal we have to write

~python manage.py makemigrations  

//Now migrations are made and its time to migrate(creating table with current structure)

~python manage.py migrate

//Creating superuser

~python manage.py createsuperuser
enter username*
enter email
enter password*
confirm password*

//Now let's test it by running the server

~python manage.py runserver

#open browser and type localhost:8000/admin, enter credentials and you will see you employee table created

-----------------------SERIALIZERS.PY----------------------

//Let's create the serializer class used to convert model to your JSON data, So withinn the webapp folder a new file is created naming serializers.py 

//Let's go to the views.py file and see what we let it to display when our API is hitted

---------------------------------VIEWS.PY--------------------------

Note: serializers convert model into JSON data and that data is views and used by others in that views.py file

#views.py consist of get and post method

-----------------------URL.PY----------------------------------

Now this JSON data needs to be linked with some url so we will move towards url.py

now that url will look like

Code : path('employees/', views.employeeList.as_view())

//test it by typing on the browser localhost:8000/employees

//Once it got shown on your browser, Go for postman testing

-------------------End------------------------







  
  
