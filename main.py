from flask import Flask
import requests
import json

APIURL = "http://10.0.1.105/"

app = Flask(__name__)


@app.route('/')
def home():
    rtn_str = "Eunsan Company의 서비스입니다."
    return rtn_str


@app.route('/time')
def time():
    try:
        data = requests.get(APIURL + "/time", timeout=5).text
        json_data = json.loads(data)

        year = json_data.get("data").get("year")
        month = json_data.get("data").get("month")
        day = json_data.get("data").get("day")
        hour = json_data.get("data").get("hour")
        minute = json_data.get("data").get("minute")
        second = json_data.get("data").get("second")
        rtn_str = "현재시각은 {}년 {}월 {}일 {}시 {}분 {}초 입니다.".format(year, month, day, hour, minute, second)

    except:
        rtn_str = "API 서버 오류입니다."

    return rtn_str


@app.route('/rand')
def rand():
    data = requests.get(APIURL + "/rand", timeout=5).text
    json_data = json.loads(data)

    value = json_data.get("data").get("value")
    rtn_str = "Eunsan Company에서 제공하는 난수는 {} 입니다.".format(value)
    return rtn_str


app.run(host='0.0.0.0', port=80)
