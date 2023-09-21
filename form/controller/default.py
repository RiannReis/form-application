from form import app


@app.route("/")
def register():
    return "Hello, World!"