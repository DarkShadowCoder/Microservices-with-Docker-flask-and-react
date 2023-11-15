from flask.cli import FlaskGroup
import unittest

from project import create_app , db
from project.api.models import User

#app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.commands()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def test():
    """ Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('project/tests',pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@cli.command()
def seed_db():
    """ Seeds the database."""
    db.session.add(User(username='blackdot',email="eivoslandry@gmail.com"))
    db.session.add(User(username='yvan',email="yvanlandry1@gmail.com"))
    db.session.commit()

if __name__ == '__main__':
    cli()