from flask import Flask, request,render_template
import joblib
import numpy as np 

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route("/")
def hello():
     return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def result():
    if request.method == 'POST':
       SQUARE_FT = request.form["SQUARE_FT"]
       BHK_NO = request.form["BHK_NO"]
       BHK_NO = int(BHK_NO)
       LONGITUDE = request.form["LONGITUDE"]
       LATITUDE = request.form["LATITUDE"]
       RESALE = request.form["RESALE"]
       RESALE = int(RESALE)
       READY_TO_MOVE = request.form["READY_TO_MOVE"]
       READY_TO_MOVE = int(READY_TO_MOVE)
       print(SQUARE_FT)
       print(BHK_NO)
       print(LONGITUDE)
       print(LATITUDE)
       print(RESALE)
       print(READY_TO_MOVE)
       price =  model.predict([[SQUARE_FT,BHK_NO,LONGITUDE,LATITUDE,RESALE,READY_TO_MOVE]])

       return render_template('index.html', prediction_text='Price in Lacs = {}'.format(price))


if __name__ == "__main__":
    app.run(debug='True')