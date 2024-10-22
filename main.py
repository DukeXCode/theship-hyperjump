from opcua import Client

url = "opc.tcp://192.168.100.11:2035"
client = Client(url)

try:
    client.connect()

    obj_node = client.get_node("ns=0;i=20001")
    method_node = client.get_node("ns=0;i=20002")

    x = 0
    y = 10
    result = obj_node.call_method(method_node, x, y)

    print(f"Result of JumpTo({x}, {y}): {result}")

finally:
    client.disconnect()
