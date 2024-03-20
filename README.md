

# Capstone-project

## This is the repository to my Meta Back-end developer course Capstone Project.

To clone this project:

- ```git clone https://github.com/happychuks/littlelemon.git```
- cd into the parent directory
- next activate the virtual environment and install dependencies using pipenv
```bash 
pipenv shell
pipenv install
```
- run the server with the following command
```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 
```
PS: create the config.ini and dbconfig.cnf files and save the relevant credentials (SECRET_KEY and Database Credentials) in them

Note: You need to provide admin token in order to perform Create, Update, and Delete operations on items.

- Ensure to create a superuser to make these operations.

Paths for testing APIs on insomnia/postman:

- GET MenuList: http://127.0.0.1:8000/restaurant/menu-items/

- GET UserList: http://127.0.0.1:8000/auth/users/

- GET Your own User details: http://127.0.0.1:8000/auth/users/me/

- POST - Create new User: http://127.0.0.1:8000/auth/users/

- POST - Obtain the User Token: http://127.0.0.1:8000/restaurant/api-token-auth/

- POST - Create Token for the User: http://127.0.0.1:8000/auth/token/login/

- GET Booking Tables: http://127.0.0.1:8000/restaurant/booking/tables

- POST - Create menuItems: http://127.0.0.1:8000/restaurant/menu-items/

- Put - Update menu-items: http://127.0.0.1:8000/restaurant/menu-items/1

- Delete items: http://127.0.0.1:8000/restaurant/menu-items/1
