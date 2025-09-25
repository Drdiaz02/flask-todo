Todo App with Flask
===================

Learning Objectives
-------------------

After completing this assignment, students will be able to:

- Create forms to send custom HTTP POST request
- Use Flask to return dynamic pages
- Store and update dynamic page content

Tasks
-----

Clone this repository in order to access the starter code for a simple `flask` application. Add the following enhancements:

1. Use a redirect 302 to point the root page `/` to `/items`.
2. Update the `/items` route to support adding items in response to a `POST` request. Complete a 302 redirect to `/items` on success.
3. Update the add item form to prevent users from submitting empty todo items
4. Update the `/items` route to support deleting items in response to a `POST` request. Complete a 302 redirect to `/items` on success.
5. Secure the page to prevent malicious users from being able to modify the HTML structure of the page. Consider an input such as `"><h1>Hacked</h1><p "` and [html.quote](https://docs.python.org/3/library/html.html#html.escape).

Usage
-----

In order to run the handout code, you will need Python 3 and Flask installed. Flask includes [detailed installation instructions](https://flask.palletsprojects.com/en/stable/installation/), but it is available on PyPI and should be installable via pip like most other packages.

Once flask is installed, you should be able to run the handout code as:

```sh
python app.py
```
