# Identity and Access Management System
Identity and access management system with user login/logout. Created only for learning
- Deals with user management, authentication (user credential validation), and authorization (roles and permissions)
- Auth flows are based on Oauth2 and OIDC


## System Design
Link: https://drive.google.com/file/d/1Nzqp5tkNK8iiA9B_o1vCYUOX3SASFdKi/view?usp=sharing

## Stack
- Client/Login-Frontend: React
- Auth/Resource Backend: Flask-Python
- Auth/Resource DB: Postgres
- Local development: Docker-compose/Minikube

### TODO
- Client Credentials
- Refresh Token
- Authorization Code Flow with Proof Key for Code Exchange

Authorization Code Flow with PKCE

3 Components
- React Frontend; Client application. Create a router with a auth/callback path for redirection
- Auth Backend - Will serve its own login page
- Resource Backend

1. Frontend creates code_verifier and code_challenge
2. Frontend sends auth code request and code callenge to auth server's /authorize endpoint
3. Auth server redirects user to its login page.
4. Frontend sends user creds to auth server via the login submit
5. If creds are valid, auth server redirects the user to the frontend's callback path, with the authorization code and code_verifier
6. Callback path gives the auth server the code and code_verifier, and the auth server responds with an access token
7. Callback path puts the access token into session storage

Client app features:
- User account page
- Org chart
    - Users with direct reports can add, update, or delete users in their reports
    - Users with direct reports can demote/promote permission roles, with self-balancing
    - Users can view user accounts of the entire org
    - Users can only see the permissions of themselves and their direct reports

Role hierarchy (from lowest to highest) with respect to access management:
- Individual contributor
- Manager
- Director
- Vice president
- C-suite
- Chief information officer (super admin -> can add, update, and delete any user)