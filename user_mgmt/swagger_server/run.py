#!/usr/bin/env python3

import connexion
from connexion.middleware import MiddlewarePosition
from starlette.middleware.cors import CORSMiddleware

def create_app():
    application = connexion.FlaskApp(__name__, specification_dir='./swagger/')
    application.add_middleware(
        CORSMiddleware,
        position=MiddlewarePosition.BEFORE_EXCEPTION,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.add_api('swagger.yaml', arguments={'title': 'User Management Service'}, pythonic_params=True)
    return application

app = create_app()


