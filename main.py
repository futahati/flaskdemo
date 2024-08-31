from flask import Flask, render_template
from datetime import datetime
from scrape import scrape_stocks, scrape_pm25

# print(__name__)

app = Flask(__name__)

books = {
    1: {
        "name": "Python book",
        "price": 299,
        "image_url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/CN1/136/11/CN11361197.jpg&v=58096f9ck&w=348&h=348",
    },
    2: {
        "name": "Java book",
        "price": 399,
        "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/087/31/0010873110.jpg&v=5f7c475bk&w=348&h=348",
    },
    3: {
        "name": "C# book",
        "price": 499,
        "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/036/04/0010360466.jpg&v=62d695bak&w=348&h=348",
    },
}


# PM25
@app.route("/pm25")
def get_pm25():
    today = datetime.now()
    columns, values = scrape_pm25()
    data = {
        "columns": columns,
        "values": values,
        "today": today.strftime("%Y/%m/%d %M:%H:%S"),
    }
    return render_template("pm25.html", data=data)


# 股市
@app.route("/stocks")
def get_stocks():
    datas = scrape_stocks()
    return render_template("stocks.html", stocks=datas)


# 程式練習 BMI
@app.route("/bmi/name=<name>&height=<h>&weight=<w>")
def get_bmi(name, h, w):
    try:
        bmi = round(eval(w) / (eval(h) / 100) ** 2, 2)
        return f"<h1><span style='color:blue'>{name}</span> <br>BMI:{bmi}</h1>"

    except Exception as e:
        print(e)
    return "<h1>參數不正確！</h1>"


@app.route("/sum/x=<x>&y=<y>")
def my_sum(x, y):
    # 參數不正確，請輸出參數錯誤 (try + except)
    try:
        total = eval(x) + eval(y)
        return f"<h1>{x}+{y}={total}</h1>"
    except Exception as e:
        print(e)
    return "<h1>參數不正確！</h1>"


@app.route("/book/<int:id>")  # ---參數<int:id>
def show_book(id):
    # 輸出有書 <h1>第一本書：xxx</h1> 或 無此編號
    if id not in books:
        return f"<h2 style='color:red'>無此編號：{id}</h2>"

    return f"<h1>第{id}本書：{books[id]}</h1>"


@app.route("/books")
def show_books():
    print(books)

    for key in books:
        print(books[key])

    # return books
    return render_template("books.html", books=books)


@app.route("/")
def index():
    today = datetime.now()
    print(today)
    name = "uiui"
    # return f"<h1>Hello Flask!<br>{today}</h1>"
    return render_template("index.html", date=today, name=name)


app.run(debug=True)
