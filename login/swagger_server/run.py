#!/usr/bin/env python3

import connexion
from connexion.middleware import MiddlewarePosition
from starlette.middleware.cors import CORSMiddleware
from swagger_server.db.base import db
from swagger_server.logger import logger


def create_app():
    logger.info("Initializing app...")
    connex_app = connexion.FlaskApp(__name__, specification_dir='./swagger/')
    app = connex_app.app
    app.config["SQLALCHEMY_DATABASE_URI"
               ] = "postgresql://admin:password@auth_db/auth_db"
    # initialize the app with the extension
    db.init_app(app)

    connex_app.add_middleware(
        CORSMiddleware,
        position=MiddlewarePosition.BEFORE_EXCEPTION,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"], )
    connex_app.add_api('swagger.yaml',
                       arguments={'title': 'Login Service'},
                       pythonic_params=True)
    return connex_app


app = create_app()
