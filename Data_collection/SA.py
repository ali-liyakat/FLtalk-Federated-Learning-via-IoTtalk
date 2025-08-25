import csv
from data_collector import Dummy_Control
# from inference import Dummy_Sensor, Dummy_Control



ServerURL = 'https://class.iottalk.tw' #For example: 'https://DomainName'
MQTT_broker = 'iot.iottalk.tw' # MQTT Broker address, for example: 'DomainName' or None = no MQTT support
MQTT_port = 8883
MQTT_encryption = True
MQTT_User = 'iottalk'
MQTT_PW = 'iottalk2023'
device_model = 'Dummy_Device'
IDF_list = ['Dummy_Sensor']
ODF_list = ['Dummy_Control']
device_id = 'AABB' #if None, device_id = MAC address
device_name = 'Data_Collector'
exec_interval = 1  # IDF/ODF interval


def on_register(r):
    print(f'Device name: {r["d_name"]}')    
    '''
    '''


