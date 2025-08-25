import json
import os

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
device_name = 'Server'
exec_interval = 100  # IDF/ODF interval


def on_register(r):
    print(f'Device name: {r["d_name"]}')    
    '''
    '''


def Dummy_Sensor():
    try:
        import json
        with open("global_model.json", "r") as f:
            global_model = json.load(f)
        print("Sending global model to clients")
        return [global_model]  # must wrap in list
    except Exception as e:
        print("Global model not ready or error:", e)
        return None



received_model_params = []

def Dummy_Control(data):
    global received_model_params
    if data:
        print("Received model from client")
        print("DEBUG data:", data)
        print("Type of data[0]:", type(data[0]))

        #  unpack
        model_dict = data[0][0]  
        received_model_params.append(model_dict)

        if len(received_model_params) == 2:
            import numpy as np

            coef = np.mean([np.array(m["coef"]) for m in received_model_params], axis=0)
            intercept = np.mean([np.array(m["intercept"]) for m in received_model_params], axis=0)

            global_model = {
                "coef": coef.tolist(),
                "intercept": intercept.tolist()
            }

            with open("global_model.json", "w") as f:
                json.dump(global_model, f)
            print("Global model written and ready to send")











































'''A SIMPLE TEST'''
# received_values = []
# result_to_send = None

# def Dummy_Sensor():
#     global result_to_send
#     if result_to_send is not None:
#         print("Sending result to clients:", result_to_send)
#         value = result_to_send
#         result_to_send = None  # send only once
#         return value
#     else:
#         return None


# def Dummy_Control(data):
#     global received_values, result_to_send
#     if data:
#         received_values.append(data[0])
#         print("Got values:", data[0])
#         print("Current list:", received_values)

#         # If 2 values received, compute result
#         if len(received_values) == 2:
#             result = sum(received_values)  # or average
#             result_to_send = result
#             print("Computed result:", result)

'''A SIMPLE TEST'''