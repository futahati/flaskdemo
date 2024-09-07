import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON"


def get_pm25_json():
    columns, values = scrape_pm25()

    xdata = [value[0] for value in values]
    ydata = [value[2] for value in values]

    json_data = {"site": xdata, "pm25": ydata}

    return json_data


def scrape_pm25(sort=False, ascending=True):
    try:
        datas = requests.get(url).json()["records"]
        df = pd.DataFrame(datas)
        df["pm25"] = df["pm25"].apply(lambda x: eval(x))
        # sort=False → 預設不排序
        if sort:  # =if sort=True → 要排序的話
            df = df.sort_values("pm25", ascending=ascending)  # 預設升序

        columns = df.columns
        values = df.values

        return columns, values

    except Exception as e:
        print(e)

    return None, "網址有誤。"


def scrape_stocks():
    try:
        url = "https://histock.tw/index"
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, "lxml")
        trs = soup.find(string="加權指數").find_parent("div").find_all("tr")

        datas = []
        for tr in trs:
            data = []
            for th in tr.find_all("th"):
                data.append(th.text.strip())

            for td in tr.find_all("td"):
                data.append(td.text.strip())

            datas.append(data)

        return datas
    except Exception as e:
        print(e)

    return None


if __name__ == "__main__":
    # print(scrape_stocks())
    print(get_pm25_json())
