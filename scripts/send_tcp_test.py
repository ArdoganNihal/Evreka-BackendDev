import socket
import json


def send_tcp_message(route, service_point, mrf, parcel, gps):
    message_dict = {
        "route": route,
        "service_point": service_point,
        "mrf": mrf,
        "parcel": parcel,
        "gps": gps
    }

    message_json = json.dumps(message_dict)
    print(message_json)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("localhost", 8888))
        s.sendall(message_json.encode())
        print("Message sent:", message_json)

send_tcp_message("route1", "service_point1", "mrf1", "parcel1", "gps_coordinates1")
