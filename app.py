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


@app.route("/items", methods=["GET"])
def list_items():
    html = "".join([get_item_component(li) for li in items])

    return template.replace("{items}", html)


if __name__ == "__main__":
    app.run(debug=True)
