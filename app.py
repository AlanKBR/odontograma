from flask import Flask, redirect, render_template, url_for

app = Flask(
    __name__, static_url_path="", static_folder=".", template_folder="templates"
)


@app.route("/")
def home():
    """Render the home page with a button to open the odontogram"""
    return render_template("home.html")


@app.route("/odontogram")
def odontogram():
    """Redirect to the original odontogram HTML page"""
    return redirect(url_for("static", filename="index.html"))


if __name__ == "__main__":
    app.run(debug=True)
