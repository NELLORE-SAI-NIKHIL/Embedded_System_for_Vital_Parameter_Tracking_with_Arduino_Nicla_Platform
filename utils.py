import numpy as np
import joblib

def preprocessdata(AccX, AccY, AccZ, GyroX, GyroY, GyroZ, Temp, Gas, RotX, RotY, RotZ, RotW, RotAcc, Pressure, HeartRate, AQI):
    test_data = np.array([[AccX, AccY, AccZ, GyroX, GyroY, GyroZ, Temp, Gas, RotX, RotY, RotZ, RotW, RotAcc, Pressure, HeartRate, AQI]])

    trained_model = joblib.load(r"C:\Users\sheks\PycharmProjects\Ecsproject\model\logistic_regression_model.pkl")
    standard_scaler = joblib.load(r"C:\Users\sheks\PycharmProjects\Ecsproject\model\scaler.pkl")

    scaled_numerical_features = standard_scaler.transform([[AccX, AccY, AccZ, GyroX, GyroY, GyroZ, Temp, Gas, RotX, RotY, RotZ, RotW, RotAcc, Pressure, HeartRate, AQI]])

    result = trained_model.predict(scaled_numerical_features)

    return result