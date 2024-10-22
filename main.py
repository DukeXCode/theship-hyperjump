from opcua import Client

# Step 1: Connect to the OPC UA server
url = "opc.tcp://192.168.100.11:2035"  # Replace with your OPC UA server URL
client = Client(url)

try:
    client.connect()

    # Step 2: Get the node that contains the method "JumpTo"
    # You would need the NodeId of the object and method you want to call.
    # Let's assume the object has the NodeId "ns=2;i=2" and the method has the NodeId "ns=2;i=3".
    obj_node = client.get_node("ns=0;i=20001")  # Replace with your actual object node
    method_node = client.get_node("ns=0;i=20002")  # Replace with your actual method node

    # Step 3: Call the "JumpTo" method with parameters x and y
    x = 0  # Example value for x
    y = 10  # Example value for y
    result = obj_node.call_method(method_node, x, y)

    print(f"Result of JumpTo({x}, {y}): {result}")

finally:
    client.disconnect()
