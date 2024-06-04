#!/bin/sh
handle_error() {
    echo "An error occurred on line $1"
    exit 1
}

trap 'handle_error $LINENO' ERR

cd client-app-frontend 
npm run lint && npm run format-fix
cd ..
cd login-frontend 
npm run lint && npm run format-fix
cd ..
cd auth_backend
sh format.sh
cd ..
docker compose up -d --build