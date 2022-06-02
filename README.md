# DartsPlus API
A simple flask api based on sqlite include unit tests and documentation.
# Setup

Set up Python 3 virtual env and install all dependencies:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Create the database model:
```
flask db init
flask db migrate
flask db upgrade
```
Run current app:
```
flask run
```
Application runs on `localhost::5000`