from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)







@app.route("/bmi/name=<name>&hei=<h>&wei=<w>")
def get_bmi(name, h, w):
    try:
        bmi = round(eval(w)/(eval(h)/100)**2, 2)
        return F"<h1><span style='color:blue'>姓名：{name}</span><p>BMI:{bmi}</p></h1>"
    except Exception as e:
        print(e)

    return F"<h2>參數不正確！</h2>"


@app.route("/sum/x=<x>&y=<y>")
def my_sum(x, y):
    # 參數不正確，請輸出參數錯誤( try + except )
    try:
        total = eval(x) + eval(y)
        return F"{x}+{y}={total}"
    except Exception as E:
        print(e) # ←這是給程式員看的

    return "<h1>參數錯誤。</h1>" # ←這是給使用者看的。


etf = {1:"A", 2:"B", 3:"C", 4:"D"}

@app.route("/etf_stock1")
def etf_stock1():
    return etf[1]


@app.route("/etf_stock")
def etf_stock():
    return "台股/上市類股/ETF即時行情"


@app.route("/")
def index():
    today = datetime.now()
    print(today)

    # return F"<h1>Hello Flask~~<br>{today}</h1>"
    return render_template("index.html")


# debug=True → 無需中斷server
app.run(debug=True)


# if __name__ == " __main__ ":
#     app.run()