from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    html = """
    <!doctype html>
    <html lang="pt-BR">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>RecipeBook</title>
    </head>
    <body>
        <h1>RecipeBook</h1>
        <form action="/" method="post">
            <label for="recipe_input">Paste here the URL or recipe text:</label><br>
            <input type="text" id="recipe_input" name="recipe_input" placeholder="URL or recipe text">
            <button type="submit">Submit</button>
        </form>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
