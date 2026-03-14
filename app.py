from flask import Flask, render_template, request, jsonify
from Stock import get_stock_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_stock", methods=["POST"])
def stock():
    data = request.json

    tickers = data["tickers"]
    start_date = data["start_date"]
    end_date = data["end_date"]

    result = get_stock_data(tickers, start_date, end_date)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)