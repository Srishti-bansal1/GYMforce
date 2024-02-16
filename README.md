# Employee Management System using Authentication
swagger link - `http://127.0.0.1:8000/swagger/`

# Introduction <br>
This is a employee  management system project. In this project I used python language (version 3.9 ) & Django Rest framework (version 4.2.9). This project  used to created employee details, read the employee information, update the informations and delete the details. 
<br>
In this project, I designed a model and their fields are name, username, email, password, department, position, address. Migrated the model to create a Table. Connected with MYSQL database. Created APIs for Create, Read, Update and Delete operation. <br>

`http://127.0.0.1:8000/em/Em/show` use for read <br> `http://127.0.0.1:7000/em/Em/create` use for create <br> `http://127.0.0.1:8000/em/Em/<id>/modify` use for update <br> `http://127.0.0.1:8000/em/Em/delete_all` use for delete all registration. 
<br>
In this project, I created 2 HTML pages. 1st is SignUp page where I created the user.
2nd is Login page where I used authentication.


`http://127.0.0.1:8000/Signup` use for signup the user <br> `http://127.0.0.1:8000/login` use for login the user  <br> 
<br>
# SetUp for Linux or MAC <br>
step 1 : open terminal and clone the code by executing  

`git clone https://github.com/Srishti-bansal1/GYMforce.git`
<br>
step 2 : Install virtual environment  with command : 

`pip install virtualenv`
<br>
step 3 : Create virtual environment  with command : 

`virtualenv .env`
<br>
step 4 : Activate the virtual environment with command :

`source  .env/bin/activate`
<br>
step 5 : Move in projct file with command :

`cd GYMPro`
<br>
step 6 : Execute migration command to create table in database using command : 

`python mange.py migrate`
<br>
step 7 : Run the server with command : 

`python manage.py runserver 8003`
<br> 

# API Documentation -<br>
swagger link - `http://127.0.0.1:8000/swagger/`

