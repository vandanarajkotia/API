from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    data = response.json()
    return data["setup"], data["punchline"]

@app.route("/")
def home():
    setup, punchline = get_joke()
    return render_template("index.html", setup=setup, punchline=punchline)

if __name__ == "__main__":
    app.run(debug=True)