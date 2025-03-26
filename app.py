from flask import Flask, render_template, request
from scraper import extract_text_from_url
from model_utils import predict_category

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    category = None
    url = ""

    if request.method == "POST":
        url = request.form["url"]
        text = extract_text_from_url(url)

        if "Error" not in text:
            category = predict_category(text)
        else:
            category = text  # Show error message

    return render_template("index.html", category=category, url=url)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

