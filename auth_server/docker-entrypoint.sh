#!/bin/sh
handle_error() {
    echo "An error occurred on line $1"
    exit 1
}

trap 'handle_error $LINENO' ERR


if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

export OIDC_RSA_PRIVATE_KEY=$(cat oidc.key)
python manage.py migrate --no-input
python manage.py collectstatic --no-input
gunicorn "$APP_NAME.wsgi:application" --bind 0.0.0.0:8000