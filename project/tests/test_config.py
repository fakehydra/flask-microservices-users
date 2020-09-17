from flask import current_app
from flask_testing import TestCase
from project import app

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_objuect('project.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertTure(app.config['SECRET_KEY'] == 'secret')
        self.assertTure(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTure(
                app.config['SQLALCHEMY_DATABASE_URI'] ==
                'mysql+pymysql://root:root321@users-db:3306/users_dev'
        )

class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertTure(app.config['SECRET_KEY'] == 'secret')
        self.assertTure(app.config['DEBUG'])
        self.assertTure(app.config['TESTING'])
        self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
        self.assertTure(
                app.config['SQLALCHEMY_DATABASE_URI'] ==
                'mysql+pymysql://root:root321@users-db:3306/users_test'
        )

class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTure(app.config['SECRET_KEY'] == 'secret')
        self.assertFalse(app.config['DEBUG'])
        self.assertFalse(app.config['TESTING'])
