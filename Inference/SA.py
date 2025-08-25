import pandas as pd
import numpy as np
import json
from scipy.special import expit  # for sigmoid

ServerURL = 'https://class.iottalk.tw' #For example: 'https://DomainName'
MQTT_broker = 'iot.iottalk.tw' # MQTT Broker address, for example: 'DomainName' or None = no MQTT support
MQTT_port = 8883
MQTT_encryption = True
MQTT_User = 'iottalk'
MQTT_PW = 'iottalk2023'
device_model = 'Dummy_Device'
IDF_list = ['Dummy_Sensor']
ODF_list = ['Dummy_Control']
device_id = 'AABBCCDD' #if None, device_id = MAC address
device_name = 'Inference'
exec_interval = 1  # IDF/ODF interval



def on_register(r):
    print(f'Device name: {r["d_name"]}')    
    '''
    '''

# Load global model (received from server)
with open("../Client1/params_client1.json", "r") as f:
    model = json.load(f)
if isinstance(model, list):
    model = model[0]  # unpack the list

coef = np.array(model["coef"])
intercept = np.array(model["intercept"])

count = 1
oneData = []
datalist = []
light = 50

# This sends current light value back to GUI
def Dummy_Sensor():
    global light
    return light

# Logistic regression prediction
def prediction(inputData):
    logits = np.dot(inputData, coef.T) + intercept
    probs = expit(logits)
    result = (probs >= 0.5).astype(int)
    return result

# Receive 6D sensor input and perform inference
def Dummy_Control(data):
    global count, oneData, datalist, light

    if count % 10 != 0 and count != 0:
        print("collecting", count, "/10 data")
        oneData = [data[0][0], data[0][1], data[0][2], data[0][3], data[0][4], data[0][5]]
        datalist.append(oneData)
        count += 1
    else:
        oneData = [data[0][0], data[0][1], data[0][2], data[0][3], data[0][4], data[0][5]]
        datalist.append(oneData)
        print("collected (60 values)")
        count = 1
        oneData = []

        # Convert to DataFrame (1 row, 60 columns)
        if isinstance(datalist, list):
            datalist = pd.DataFrame(
                np.array(datalist).reshape(1, -1),
                columns=[f"{sensor}{i}-{j}" for i in range(1, 11) for sensor in ['acc', 'gyro'] for j in range(1, 4)]
            )

        # Predict using global model
        predictResult = prediction(datalist)

        print("Gesture Detection Result:")
        if predictResult == 1:
            print("ON")
            light = 100
        elif predictResult == 0:
            print("OFF")
            light = 0

        datalist = []  # reset for next round
