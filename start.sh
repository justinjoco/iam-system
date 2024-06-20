#!/bin/sh
cd client_app
npm run lint && npm run format-fix
cd ..
cd user_mgmt
sh format.sh
cd ..
cd login
sh format.sh
cd ..
docker compose up --build