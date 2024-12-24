
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
1. **api/auth/users/** \
   **POST**-request, containing **email**, **username**, **password** (all mistakes in fields would be printed back) \
2. New user created, but email activation is needed, so look into console if mock activation(by default) or open mailbox and copy the **activation code**.
3. **api/auth/activate/** \
   **POST**-request, containing "email" and "activation_code" fields(str and int). \
!**ATTENTION**! codes expire after 5 minutes, you can send new ones by **POST**-request with "email" and <"resend": true> fields. \
(IF YOU FEEL TOO LAZY, THEN JUST EDIT USER FIELD is_active IN DB)
4. **api/auth/token/login/** \
   **POST**-request, containing **username** and **password**, answer will contain "auth-token", that you should paste into requests headers.

#### 2. Routes

(These are routes from server url)
1. **api/sales/**
   1. **GET** - prints all posts (**permissions**: Everyone)
   2. **POST** - creates new post (**fields**: **title**, **price**, **description**, **is_published**) (**permissions**: Authenticated)
2. **api/sales/<int: post_id>**
   1. **GET** - print single post (**permissions**: Authenticated)
   2. **PUT, PATCH, DELETE** - recreate, updates, deletes single post (**permissions**: Post Author or Admin) \
      (!ATTENTION!) to delete picture from post send request with "images_to_delete": [1, 2, 3, ...] (integers, id of pictures you need to delete) 
3. **api/user/<int: user_id>**
   1. **GET** - print user info (**permissions**: Authenticated)
   2. **PUT, PATCH, DELETE** - recreate, updates, deletes user account (**permissions**: Post Author or Admin)
4. **api/image/salecard/<int: salecard_photo_id>**
   1. **GET** - shows picture, attached to some salecard, with id = **salecard_photo_id** (**permissions**: Everyone)
5. **api/image/user/<int: user_id>**
   1. **GET** - shows picture, attached to user profile (**permissions**: Everyone)
6. **api/comments/<int: post_id>**
   1. **GET** - shows all comments of salecard (**permissions**: Authenticated)
   2. **POST** - creates a new comment (**fields**: **content**) (**permissions**: Authenticated)
7. **api/categories/**
   1. **GET** - shows all categories (**permissions**: Authenticated)
8. **admin/**
   1. Django regular admin panel
 
## Development 

1. Install requirements
```bash
poetry install --with dev
```

2. Create file «.env» in vunkpunk/vunkpunk, then paste this variable in it:
```bash
SECRET_KEY="secret key(ask our dev team)"
``` 
**(EXTRA)** if you try working with real smtp, then add this
```bash
EMAIL_HOST = "smtp host (I suggest using mailtrap to mock smtp)"
EMAIL_PORT = <integer>
EMAIL_HOST_USER = "smtp username"
EMAIL_HOST_PASSWORD = "yeah, you guessed it, smtp user password"
```
**(EXTRA ENDED)**

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
