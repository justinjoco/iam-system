#!/bin/sh
handle_error() {
    echo "An error occurred on line $1"
    exit 1
}

trap 'handle_error $LINENO' ERR

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