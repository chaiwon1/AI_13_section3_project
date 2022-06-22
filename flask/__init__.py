from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

# @app.errorhandler(404)
# def page_not_found(error):
# 	return render_template('404.html'), 404

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET' :
        return render_template('index.html')

    if request.method == 'POST' :

        data1 = float(request.form['a'])
        data2 = float(request.form['b'])
        data3 = float(request.form['c'])
        data4 = float(request.form['d'])
        data5 = float(request.form['e'])
        data6 = float(request.form['f'])
        data7 = float(request.form['g'])

        arr = np.array([[data1, data2, data3, data4, data5, data6, data7]])
        pred = model.predict(arr)
        pred = round(pred[0])

        return render_template('after.html', pred=pred)

if __name__ == '__main__':
    app.run(debug=True)