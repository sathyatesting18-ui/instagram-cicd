from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    posts = [
        {
            "username": "travel_world",
            "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
            "caption": "Beautiful beach 🌊"
        },
        {
            "username": "nature_lovers",
            "image": "https://images.unsplash.com/photo-1500534623283-312aade485b7",
            "caption": "Enjoying nature 🌲"
        },
        {
            "username": "city_life",
            "image": "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df",
            "caption": "Amazing city view 🌆"
        }
    ]

    return render_template("index.html", posts=posts)


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
