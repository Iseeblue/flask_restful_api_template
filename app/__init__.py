# @Time : 2020/11/15 10:43
# @Author: dan
# @File : __init__.py.py
import os

from flask import Flask

from app.apis import register_blueprint
from app.extensions import init_extensions
from app.logs import setup_logs
from config import envs


def create_app(env):
    setup_logs(env)
    app = Flask(__name__)
    app.config.from_object(envs.get(env))

    init_extensions(app=app)

    register_blueprint(app)

    return app

