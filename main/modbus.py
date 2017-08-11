from pymodbus.client.sync import ModbusTcpClient
from main.models import ModbusDevice


client = ModbusTcpClient(host='127.0.0.1', port=502)
status = client.connect()
print(status)
wresult = client.write_coil(1, 1)
rresult = client.read_coils(1, 1)
print(rresult)
client.close()