# Identity and Access Management System
Identity and access management system with user login/logout. Created only for learning
- Deals with user management, authentication (user credential validation), and authorization (roles and permissions)
- Auth flows are based on Oauth2 and OIDC


## System Design
Link: https://drive.google.com/file/d/1Nzqp5tkNK8iiA9B_o1vCYUOX3SASFdKi/view?usp=sharing

## Stack
- Frontend: React
- Backend: Flask-Python
- DB: Postgres
- Local development: Docker-compose/Minikube

### TODO
- Client Credentials
- Resource Owner Password
- Authorization Code Flow
- Authorization Code Flow with Proof Key for Code Exchange

Authorization Code Flow with PKCE
4 Components
- React frontend for some application
- Callback Server -> Middle man bw frontend and auth server for JWT retrieval
- Auth Server -> Has its own frontend

1. Frontend creates code_verifier and code_challenge
2. Frontend sends auth code request and code callenge to auth server's /authorize endpoint
3. Auth server redirects user to its login page.
4. Frontend sends user creds to auth server via the login submit
5. If creds are valid, auth server redirects the React frontend to the callback server, with the authorization code and code_verifier
6. Callback server gives the auth server the code and code_verifier, and the auth server responds with an access token
7. Callback server pipes back the access token to the frontend, which the frontend can put into its local storage