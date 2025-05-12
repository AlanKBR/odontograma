from flask import Flask, send_from_directory

app = Flask(
    __name__, static_url_path="", static_folder=".", template_folder="templates"
)


@app.route("/")
def odontogram():
    """Serve the odontogram as the only page."""
    return send_from_directory(".", "index.html")


if __name__ == "__main__":
    app.run(debug=True)
