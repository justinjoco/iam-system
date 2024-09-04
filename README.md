# Identity and Access Management System
Identity and access management system with user login/logout, password reset, and user registration. Created only for learning
- Auth flows are based on Oauth2 and OIDC

## System Design
Link: https://drive.google.com/file/d/1Nzqp5tkNK8iiA9B_o1vCYUOX3SASFdKi/view?usp=sharing

## Stack
- Client frontend: React, Reactstrap
- Auth/Resource Backend: Python-Django, Django REST Framework, Django OAuth Toolkit
- Auth/Resource DB: Postgres
- Local development: Docker-compose

### TODO
- Login flow

docker exec -it containerId python manage.py createsuperuser