from flask import Flask, render_template
app = Flask(__name__, "", "../front/dist", template_folder="../front/dist")

@app.errorhandler(404)
def catch_all(path):
    return render_template("index.html")

@app.route("/api")
@app.route("/api/")
def api():
    return "API"

if __name__ == '__main__':
    app.run()