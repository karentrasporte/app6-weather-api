from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("dictionary.csv")


@app.route("/dict")
def dict_home():
    return render_template("dict.html")


@app.route("/api/v1/<word>")
def dict(word):
    definition = df.loc[df['word'] == word]['definition'].squeeze()
    response = {"definition":definition,"word":word}
    return response


if __name__ == "__main__":
    app.run(debug=True, port=5001)