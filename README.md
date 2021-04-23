
# Django template - with bootstrap

## Rename your project

> Not tested after adding models! Make sure to do it early in the project
```
python rename.py oldName newName
```

## If you don't have flask installed run

```
pip3 install django
or
pip install django
```

## To start the server

```
python manage.py runserver
```

> Website will now be accessible on http://localhost:8000

# WIKI
> For a full step-by-step guide visit: [Writing your first Django app](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)

## Add a new page
> Replace *page* with what the name of the page will be, for example: *blog*
- create `page.html` in `webpage/templates/webpage/`
- create `page.py` in `webpage/views/`
- add `path("page", page.page, name="page")`, in `webpage/urls.py`
	- `from .views import page`

- copy code from `index.py` to `page.py`
	- change _index.html_ to _page.html_
	- to send data and receive data see: *[Sending and receiving data](https://github.com/AndersFelde/Django-template#sending-and-receiving-data)*

- copy code from `index.html` to `page.html`
	- change `title` to _page_
	- change value of active element to _page_
		- hidden input element at the top

- change `webpage/templates/webpage/includes/navbar.html`
	- add a new element in navbar

> For more information visit: [Writing your first Django app](https://docs.djangoproject.com/en/3.1/intro/tutorial03/)

## Sending and receiving data

### Receiving data


##### POST
This is the example form which the user fills out
```jinja
<form method="POST">
{% csrf_token %}
    <input name="email" type="email">
    <input name="password" type="password">
    <button type="submit">Submit</button>
</form>
```
> The csrf_token is mandatory in Django. It is a security-feature to prevent XXS-attacks.

When the user submits the form, what the user typed into the input-fields is sent with the request.
To get the values in python:
```python
if request.method == "POST":
    email = request.POST.get("email")
    password = request.POST.get("password")
```
The first line check if the method of the request is "POST", which indicates that the user has submitted the form.
> The default request method is GET

##### GET
The same form will be used, except the first line is changed to:
```html
<form method="GET">
```
When the user hits the Submit-button, the user will be redirected to a URL that looks like this:

    http://localhost/form.html?email=joe@mama.com&password=password123
What the user typed in to the fields will be represented in the URL. To get the data in python:
```python
if "password" in request.GET:
    email = request.GET.get("email")
    password = request.GET.get("password")
```
In the first line we check if the "password" parameter exists in the URL. If it does it gets value of the "email" and "password" parameters.

### Sending data
Let's say you now want to send confirmation to the user that you received their email and password. We have now stored the values in variables, but want to represent them in the HTML.

To send data to the HTML-template use the ***context*** parameter in the *render*-function:
>The parameter requires a dictionary
```python
return render(request,
      "webpage/formPage.html",
      context={"email": email, "passwordLength": len(password)})
```
In the HTML write:

```jinja
{% if email %}
<p>
    Thank you for signing up: {{ email }} <br>
    Your password is {{ passwordLength }} characters long
</p>
{% endif %}
```
The first line checks if the email variable is set, if so it prints the value of email and passwordLength

## Sesssions

Sessions lets you temporarlily save data in the browser-session.

### Saving session data
```python
request.session['password'] = password
```
> If you are modifying for example an entry inside a dictionary: `request.session['creds']['password'] = password` you have to manuallet set `request.session.modified = True`

### Get session value by key
```python
password = request.session['password']
```

### Delete a session value
```python
del request.session['password']
```

> For more about session visit: [Sesssions | Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Sessions)

## Adding a new model


- create a new file "testModel.py" in webpage/submodels/
	- look at exampleModel.py to steal code

- import model in webpage/models.py
	- `from .submodels.testModel1 import modelName`

- run `python manage.py makemigrations webpage`
- run `python manage.py migrate`

- add admin.site.register(modelName) in webpage/admin.py
	- `from .submodels.testModel1 import modelName`


- log in to http://localhost:8000/admin to view the model
	- *admin:admin*
> For more information about html template visit: [Models | Django documentation](https://docs.djangoproject.com/en/3.1/topics/db/models/) 



Tips:
- define `__str__` in a model to make it look better on the admin page
	- make it return the name or id of the model
