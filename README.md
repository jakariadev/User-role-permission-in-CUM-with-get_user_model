# User-role-permission-in-CUM-with-get_user_model

![Project Image](https://miro.medium.com/max/571/1*RhvAHEfxPX67jIOlXWGlyg.png)

> docker, django, postgresql

---

### Table of Contents

- [Description](#description)
- [Technologies](#technologies)
- [How To Use](#how-to-use)

## Description

Docker is a platform for building, running, shipping applications in a consistent manner. It makes sure an application will work fine in other computers with different OS, different environments or different configuration settings even if the app is in development mode.

## Technologies

- [Docker](https://www.docker.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Django-Rest-Framework](https://www.django-rest-framework.org/)
- [Django](https://www.djangoproject.com/)

---

## How To Use
Make sure Docker, Python and pip are available on the system. Then simply execute the Docker Commands.

- Migrations:

```
    docker-compose exec web python manage.py makemigrations
    docker-compose exec web python manage.py migrate

```
- Create super user:

```
    docker-compose exec web python manage.py createsuperuser

```

- Build and Run(give 'sudo' if require):

```
    docker-compose up -d --build

```
- Find working or not (give 'sudo' if require):

```
    docker-compose logs

```

- Stop working with (give 'sudo' if require):

```
    docker-compose down

```

- Unit Testing (give 'sudo' if require):

```
    docker-compose exec web python manage.py test

```

## Author Info

- [@Jakaria](https://facebook.com/jakaria.pust)


[Back To The Top](#User-role-permission-in-CUM-with-get_user_model)

