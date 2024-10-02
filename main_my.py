from flask import Flask
from datetime import datetime

app = Flask(__name__)


etf = {1:"A", 2:"B", 3:"C", 4:"D"}

@app.route("/etf_stock1")
def etf_stock1():
    return etf[1]


@app.route("/etf_stock")
def etf_stock():
    return "台股ETF類"


@app.route("/")
def index():
    today = datetime.now()
    print(today)

    return F"<h1>Hello Flask~~<br>{today}</h1>"


# debug=True → 無需中斷server
app.run(debug=True)


# if __name__ == " __main__ ":
#     app.run()