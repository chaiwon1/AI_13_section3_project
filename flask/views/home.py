from flask import Blueprint, render_template, request
import requests
import json


home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET' :
        return render_template('home.html')
    
    if request.method == 'POST' :
        date = request.form['오늘의 날짜']
        weather_date = int(date.replace('-','').strip())

        key = 'KNuGkSNRmoO1s%2BZ%2FTn2TsXDaWhsBi8gZS5kekQhHYIdMcPWHTea1T4Vgec%2BHlj068ywy6MV55fcw1blWG7Fwbg%3D%3D'

        startDate = weather_date - 10000
        endDate =  startDate
        location = 108

        url = f'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?serviceKey={key}&pageNo=1&numOfRows=999&dataType=JSON&dataCd=ASOS&dateCd=DAY&startDt={startDate}&endDt={endDate}&stnIds={location}'

        raw_data = requests.get(url)
        parsed_data = json.loads(raw_data.text)
        weather_data = parsed_data['response']['body']['items']['item']

        return render_template('home_api.html', weather_data=weather_data), 200