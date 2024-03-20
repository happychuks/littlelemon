# Meta Back-End Developer Capstone

![Coursera](https://img.shields.io/badge/Coursera-0747a6?style=flat&logo=coursera&logoColor=white)
![Meta](https://img.shields.io/badge/Meta-0668E1?style=flat&logo=meta&logoColor=white)
![Django](https://img.shields.io/badge/Django-092e20?style=flat&logo=django&logoColor=white)

Building RESTful APIs using [Django Rest Framework](https://www.django-rest-framework.org/) connected to a [MySQL](https://dev.mysql.com/downloads/) as part of the [Meta Back-End Developer Certificate](https://www.coursera.org/professional-certificates/meta-back-end-developer) teached by [Meta](https://www.facebook.com/business/learn/back-end-back-end-developer-certificate-coursera).

<p align="center">
    <a href="https://www.credly.com/org/facebook-blueprint/badge/meta-back-end-developer-certificate">
        <img src="./meta-backend-cert.png" width="30%" height="30%" />
    </a>
</p>

## This is the repository to my Meta Back-end developer course Capstone Project.

## 1. To clone this project:

- ```git clone https://github.com/happychuks/littlelemon.git```

## 2. Create the config files using this format:
create config.ini in the parent directory with the following configuration
```bash
# config.ini
    [django]
    SECRET_KEY = <Paste Django Secret Key here>
```

create dBconfig.cnf in the parent directory with the following configuration
```bash
# dBconfig.cnf
    [database]
    engine = django.db.backends.mysql
    name = <enter your database name here>
    user = <enter username here>
    password = <enter password here>
    host = 127.0.0.1
    port = 3306
```
- Please note that I did this just to emulate the production environment standard way of hiding credentials. You can choose to reveal your credentials in the settings.py file when working in development environment.

### 3. Install dependencies

```bash
pipenv install
```

### 4. Make migrations

```bash
py manage.py makemigrations
```

### 5. Migrate

```bash
py manage.py migrate
```

### 6. Run the app

```bash
py manage.py runserver
```

Note: You need to provide admin token in order to perform Create, Update, and Delete operations on items.

- Ensure to create a superuser to make these operations.

### 7. Paths for testing APIs on insomnia/postman:

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

Feel free to reachout to me for contributions or any questions
Happy coding!!!