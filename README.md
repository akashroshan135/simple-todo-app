# simple-todo-app
a simple todo app made using Django that can perform basic CRUD operations. Create tasks, update them as completed and delete tasks from the list.

Run the following commands in the project's directory to create the database migrations
```
python manage.py makemigrations todo
python manage.py migrate todo
```

Use the following command to run the server
```
python manage.py runserver
```

Use the following command to create an admin user 
```
python manage.py createsuperuser
```
