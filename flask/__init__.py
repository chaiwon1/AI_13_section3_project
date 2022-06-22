from flask import Flask, render_template, request
import requests
import json

# app = Flask(__name__)

# @app.errorhandler(404)
# def page_not_found(error):
# 	return render_template('404.html'), 404


# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'GET' :
#         return render_template('home.html')
    
#     if request.method == 'POST' :
#         date = request.form['오늘의 날짜']
#         weather_date = int(date.replace('-','').strip())

#         key = 'KNuGkSNRmoO1s%2BZ%2FTn2TsXDaWhsBi8gZS5kekQhHYIdMcPWHTea1T4Vgec%2BHlj068ywy6MV55fcw1blWG7Fwbg%3D%3D'

#         startDate = weather_date - 10000
#         endDate =  startDate
#         location = 108

#         url = f'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?serviceKey={key}&pageNo=1&numOfRows=999&dataType=JSON&dataCd=ASOS&dateCd=DAY&startDt={startDate}&endDt={endDate}&stnIds={location}'

#         raw_data = requests.get(url)
#         parsed_data = json.loads(raw_data.text)
#         weather_data = parsed_data['response']['body']['items']['item']

#         return render_template('home_api.html', weather_data=weather_data), 200


# @app.route('/predict', methods=['GET', 'POST'])
# def predict():
#     if request.method == 'GET' :

#         return render_template('predict.html')

#     if request.method == 'POST' :

#         data1 = float(request.form['평균기온'])
#         data2 = float(request.form['최저기온'])
#         data3 = float(request.form['최고기온'])
#         data4 = float(request.form['합계일조시간'])
#         data5 = float(request.form['평균풍속'])
#         data6 = float(request.form['일강수량'])
#         data7 = float(request.form['평균상대습도'])

#         arr = np.array([[data1, data2, data3, data4, data5, data6, data7]])
#         pred = model.predict(arr)
#         pred = round(pred[0])

#         return render_template('predict_result.html', pred=pred)


# @app.route('/recommand', methods=['GET', 'POST'])
# def recommand():
#     if request.method == 'GET' :
#         return render_template('recommand_home.html')

#     if request.method == 'POST' :
#         ncreds = {
#                     "client_id": 'hS5xvT2ddaNb6bL4oy5J',      
#                     "client_secret" : 'Kz_yIoUWcu'
#                  }
#         nheaders = {
#                         "X-Naver-Client-Id" : ncreds.get('client_id'),
#                         "X-Naver-Client-Secret" : ncreds.get('client_secret')
#                     }

#         naver_local_url = "https://openapi.naver.com/v1/search/local.json?"

#         location = request.form['지역']
#         # food = request.form['메뉴']

#         recommands = []
#         query = location + " " + " 맛집"
#         params = "sort=comment" + "&query=" + query + "&display=" + '20'
            
#         # headers : 네이버 인증 정보
#         res = requests.get(naver_local_url + params, headers=nheaders)
#         result_list = res.json().get('items')

#         for i in range(0,5):
#             recommands.append(result_list[i])

#     return render_template('recommand.html', recommand=recommands)

# if __name__ == '__main__':
#     app.run(debug=True)


def create_app(config=None):
    """
    create_app 은 애플리케이션 팩토리 패턴에 따른 함수입니다.

    config 파라미터는 테스트에 필요하니 변경하지는 말아주세요!
    """
    app = Flask(__name__)
    
    # 여기에서 주어진 config 에 따라 추가 설정을 합니다.
    if config is not None:
        app.config.update(config)
    
    # 왜 여기에서 import 를 하고 있을까요?
    # 맨 위로 옮기게 되면 어떻게 되나요? 어떤 잠재적 문제들이 있나요?
    from views.home import home_bp
    from views.predict import predict_bp
    from views.recommand import recommand_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(predict_bp)
    app.register_blueprint(recommand_bp)


    return app


if __name__ == "__main__":
  app = create_app()
  app.run()