from flask import Flask, render_template, request
import numpy as np
import joblib

import utils

app = Flask(__name__)

# Load the trained model and scaler
# model = joblib.load(r'C:\Users\sheks\PycharmProjects\Ecsproject\model\logistic_regression_model.pkl')
# scaler = joblib.load(r'C:\Users\sheks\PycharmProjects\Ecsproject\model\scaler.pkl')

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # if request.method == 'POST':
#     #     input_data = request.form.get('input_data')
#     #     input_list = [float(i) for i in input_data.split(',')]
#     #     input_array = np.array(input_list).reshape(1, -1)
#     #     scaled_data = scaler.transform(input_array)
#     #     prediction = model.predict(scaled_data)[0]
#     #     result = "Normal" if prediction == 0 else "Break"
#     # return render_template('result.html', prediction=result)
#
#     if request.method == 'POST':
#         AccX = request.form.get('AccX')
#         AccY = request.form.get('AccY')
#         AccZ = request.form.get('AccZ')
#         GyroX = request.form.get('GyroX')
#         GyroY = request.form.get('GyroY')
#         GyroZ = request.form.get('GyroZ')
#         Temp = request.form.get('Temp')
#         Gas = request.form.get('Gas')
#         RotX = request.form.get('RotX')
#         RotY = request.form.get('RotY')
#         RotZ = request.form.get('RotZ')
#         RotW = request.form.get('RotW')
#         RotAcc = request.form.get('RotAcc')
#         Pressure = request.form.get('Pressure')
#         HeartRate = request.form.get('HeartRate')
#         AQI = request.form.get('AQI')
#
#     result = utils.preprocessdata(AccX, AccY, AccZ, GyroX, GyroY, GyroZ, Temp, Gas, RotX, RotY, RotZ, RotW, RotAcc, Pressure, HeartRate, AQI)
#
#     return render_template('result.html', prediction=result)


@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        AccX = float(request.form.get('accx'))
        AccY = float(request.form.get('accy'))
        AccZ = float(request.form.get('accz'))
        GyroX = float(request.form.get('gyrox'))
        GyroY = float(request.form.get('gyroy'))
        GyroZ = float(request.form.get('gyroz'))
        Temp = float(request.form.get('temp'))
        Gas = float(request.form.get('gas'))
        RotX = float(request.form.get('rotx'))
        RotY = float(request.form.get('roty'))
        RotZ = float(request.form.get('rotz'))
        RotW = float(request.form.get('rotw'))
        RotAcc = float(request.form.get('rotacc'))
        Pressure = float(request.form.get('pressure'))
        HeartRate = float(request.form.get('heartrate'))
        AQI = float(request.form.get('aqi'))
    # Code to preprocess data and get the result
    result = utils.preprocessdata(AccX, AccY, AccZ, GyroX, GyroY, GyroZ, Temp, Gas, RotX, RotY, RotZ, RotW, RotAcc,
                                  Pressure, HeartRate, AQI)

    # Pass the result to the template
    return render_template('result.html', prediction=result)



if __name__ == '__main__':
    app.run(debug=True)
