from flask import Flask
from flask import request, redirect
from html import escape

app = Flask(__name__)

template = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">

    <title>My Todo List</title>
  </head>

  <body>
    <main>
      <h1>My Todo List</h1>
      <ul>
      {items}
      </ul>
      <form action="/items" method="post">
        <label>New Todo Item: <input type="text" name="item_add"></label>
        <input type="submit" value="Add Item">
      </form>
    </main>
  </body>
</html>
""".strip()

items = ["Finish Web Apps Project"]


def get_item_component(item_text):
    return f"""
        <li>
        <form action="/items" method="post">
            <input type="submit" value="Mark Complete">
            <input type="hidden" name="item_del" value="{item_text}" readonly>
            {item_text}
        </form>
        </li>
    """

#2. Update the `/items` route to support adding items in response to a `POST` request. Complete a 302 redirect to `/items` on success.
@app.route("/items", methods=["GET", "POST"])
def list_items():
    # if block to look for method
    if request.method == "POST":
        #3. Update the add item form to prevent users from submitting empty todo items
        new_item = request.form.get("item_add", "").strip()
        if new_item != "":
            items.append(new_item)
        # return stops the rest of code from running
        return redirect("/items")
    html = "".join([get_item_component(li) for li in items])

    return template.replace("{items}", html)

# 1. Use a redirect 302 to point the root page `/` to `/items`.
@app.route("/")
def reroute():
    return redirect("/items", 302)

if __name__ == "__main__":
    app.run(debug=True)
