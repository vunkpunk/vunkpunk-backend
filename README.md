
# vunkpunk-backend
Backend for android app for SPbU dorms forum

---
## API structure and permissions

(!) I really advise you to use Postman
#### 1. Authentication

Authentication works by passing a special **Token** in the header of every HTTP-request, like so:
```
Authentication: "Token <paste user auth-token>"
```
To get this token user should be registered, and then get it by requesting. Here is the pipeline of registering:
1. **api/auth/users/** 
   **POST**-request, containing **email**, **username**, **password** (all mistakes in fields would be printed back)
New user created, now
2. **api/auth/token/login/**
   **POST**-request, containing **username** and **password**, answer will contain "auth-token", that you should paste into requests headers.

#### 2. Routes

(These are routes from server url)
1. **api/sales/**
   1. **GET** - prints all posts (**permissions**: Everyone)
   2. **POST** - creates new post (**fields**: **title**, **price**, **description**) (**permissions**: Authenticated)
2. **api/sales/<int: post_id>**
   1. **GET** - print single post (**permissions**: Authenticated)
   2. **PUT, PATCH, DELETE** - recreate, updates, deletes single post (**permissions**: Post Author or Admin)
3. **api/user/<int: user_id>**
   1. **GET** - print user info (**permissions**: Authenticated)
   2. **PUT, PATCH, DELETE** - recreate, updates, deletes user account (**permissions**: Post Author or Admin)
4. **admin/**
   Django regular admin panel
 
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