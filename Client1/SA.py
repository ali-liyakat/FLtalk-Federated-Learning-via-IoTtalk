import json


ServerURL = 'https://class.iottalk.tw' #For example: 'https://DomainName'
MQTT_broker = 'iot.iottalk.tw' # MQTT Broker address, for example: 'DomainName' or None = no MQTT support
MQTT_port = 8883
MQTT_encryption = True
MQTT_User = 'iottalk'
MQTT_PW = 'iottalk2023'
device_model = 'Dummy_Device'
IDF_list = ['Dummy_Sensor']
ODF_list = ['Dummy_Control']
device_id = 'AABBCC01' #if None, device_id = MAC address
device_name = 'Client1'
exec_interval = 100  # IDF/ODF interval


def on_register(r):
    print(f'Device name: {r["d_name"]}')    
    '''
    '''


def Dummy_Sensor():
    with open("params_client1.json") as f:
        params = json.load(f)
    print("Sending LR model params")
    return [params]



def Dummy_Control(data):
    if data:
        global_model = data[0]  # unpack the dict
        print("Received global model from server")

        import json
        with open("global_model_received.json", "w") as f:
            json.dump(global_model, f)
        print("Saved global model to global_model_received.json")














































'''A SIMPLE TEST'''
# def Dummy_Sensor():
#     print("sending 5")
#     return 5


# def Dummy_Control(data):
#     print("Client received result from server:", data)

    #  # Save the result to file
    # with open("client_output.txt", "w") as f:
    #     f.write(str(data[0]) + "\n")

'''A SIMPLE TEST'''
