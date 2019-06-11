# Test APP

```
For the test, please provide a barebones Django project with two view files (view1.py and view2.py) and each with a single function printing statements "This is View 1" and "This is View 2" respectively. Please set up two user groups with custom permissioning so that users in Group 1 can only access functions in view1.py and users in Group 2 can only access functions in view2.py.
```

## How to run project

1. Clone repo  `git clone `
2. Enter project repo `cd siwi`
3. **PROJECT REQUIRED PYTHON 3.7** Create python ENVIRONMENT `python3 -m venv /path/to/folder/.env` replace `/path/to/folder` with actual file path `pwd`
4. Active ENVIRONMENT `source .env/bin/activate`
5. Install requirements `pip install -r requirements.txt`
6. Run Database migrations `python manage.py migrate`
7. Create groups and testusers `python manange.py create_groups`
8. Run project `python manage.py runserver`

## Now you are ready to test.

open <a href='http://localhost:8000'>site</a>

you will have 2 users test1 and test2 that has access to view1 and view2, both has password `123123`