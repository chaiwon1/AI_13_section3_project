from flask import Blueprint, render_template, request
import requests


recommand_bp = Blueprint('recommand', __name__)

@recommand_bp.route('/recommand', methods=['GET', 'POST'])
def recommand():
    if request.method == 'GET' :
        return render_template('recommand_home.html')

    if request.method == 'POST' :
        ncreds = {
                    "client_id": 'hS5xvT2ddaNb6bL4oy5J',      
                    "client_secret" : 'Kz_yIoUWcu'
                 }
        nheaders = {
                        "X-Naver-Client-Id" : ncreds.get('client_id'),
                        "X-Naver-Client-Secret" : ncreds.get('client_secret')
                    }

        naver_local_url = "https://openapi.naver.com/v1/search/local.json?"

        location = request.form['지역']
        # food = request.form['메뉴']

        recommands = []
        query = location + " " + " 맛집"
        params = "sort=comment" + "&query=" + query + "&display=" + '20'
            
        res = requests.get(naver_local_url + params, headers=nheaders)
        result_list = res.json().get('items')

        for i in range(0,5):
            recommands.append(result_list[i])

    return render_template('recommand.html', recommand=recommands)