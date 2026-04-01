from flask import Flask, render_template

app = Flask(__name__)


@app.route("/dict")
def dict_home():
    return render_template("dict.html")



@app.route("/api/v1/<word>")
def dict(word):
    print(word.upper())
    return {"definition":word.upper(),"word":word}


if __name__ == "__main__":
    app.run(debug=True)