import random
import click
from flask import Blueprint
from faker import Faker
from api.app import db
from api.models import User

fake = Blueprint('fake', __name__)
faker = Faker()


@fake.cli.command()
@click.argument('num', type=int)
def users(num):  # pragma: no cover
    """Create the given number of fake users."""
    for i in range(num):
        user = User(username=faker.user_name(), email=faker.email(),
                    about_me=faker.sentence())
        db.session.add(user)
    db.session.commit()
    print(num, 'users added.')


