
# vunkpunk-backend
Backend for android app for SPbU dorms forum

---
## Development 

1. Install requirements
```bash
poetry install --with dev
```

2. Create file «.env» in vunkpunk/vunkpunk, then paste this variable in it:
```bash
SECRET_KEY="secret key(ask our dev team)"
```

3. Execute migrations
```bash
python vunkpunk/manage.py migrate
```

4. Run test server
```bash
python vunkpunk/manage.py runserver
```

5. (OPTIONAL) create admin account
```bash
python vunkpunk/manage.py createsuperuser
```