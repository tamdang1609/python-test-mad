import websocket
import sys
import time

from datetime import datetime

count = 0
initial_time = datetime.now()
start_time = datetime.now()



def on_message(ws, message):
    print(message)
    global start_time
    global count
    print("--- %s seconds ---" % (datetime.now() - start_time))
    start_time = datetime.now()
    count = count + 1
    print("---- start at: %s" % start_time)
    print("---- count:  %d " % count)
    print("---- uptime : %s " % (datetime.now() - initial_time))




#custom_protocol = "_oauth2_proxy=IJDs4d12hGbWhVQk71lIpg=="
#protocol_str = "Cookie: " + custom_protocol
#bearer = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJRNXNCaWtrWk1ucDV0Y1NjX2NCSXNqZjIxWEdUaFpKSVc4VkJfLXV6c3drIn0.eyJleHAiOjE2Mjk1ODUyNDQsImlhdCI6MTYyOTU4NDk0NCwiYXV0aF90aW1lIjowLCJqdGkiOiIxNGQ3YjNmOS1iOGU3LTRjNzEtODgwOS1iNjFhMTE1NGNmNmYiLCJpc3MiOiJodHRwczovL2tleWNsb2FrLmVjcmlja2V0cy5vcmcvYXV0aC9yZWFsbXMvbWFya2V0IiwiYXVkIjoicHJpY2VyIiwic3ViIjoiN2NkYTJmYTMtODNlNy00NzliLWJmMWUtNWVjOTM5YzI5MmU3IiwidHlwIjoiSUQiLCJhenAiOiJwcmljZXIiLCJzZXNzaW9uX3N0YXRlIjoiMmRkOWVjYzYtNTkwNS00YWQ3LWIwZjUtZWUzYjdiNGIxODk1IiwiYXRfaGFzaCI6Inh4VjVqeFdqMnFFdUM4TW5YT05vYmciLCJhY3IiOiIxIiwic2lkIjoiMmRkOWVjYzYtNTkwNS00YWQ3LWIwZjUtZWUzYjdiNGIxODk1IiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImdyb3VwcyI6WyIvbWFya2V0Il0sInByZWZlcnJlZF91c2VybmFtZSI6InRhbS5kYW5nIiwiZW1haWwiOiJ0YW0uZGFuZ0Bwb3dlci50cmFkZSJ9.F5V7-ddYFtdWt0ph2kLYHvQuXixoZepmweWCkuONlssfQCgTDcgseYDLOSwILTknO4mWM8eEM6IomIwj_vyiDgeeMmZ0NqZ_MafRwbrxlV_X3MVw0bSO8TXbZWmHCeQkwZmcEfYLxHuH7__gR27eb7JrvVPf1lTp-Q3SbJ7Yr-xv8EmxOp4gVwd5A5ywpIxrKG0wpwAH6ueQ4avU7M84qyJdUrANNurPdJS-X9ZLSo1mZtdRxcntmnlZVZUNtD90dIHFrDbWvnWBNLK41sDRoQbayRYzW9srB8vHgvv3xouT7aXpopc1THIEmmjZOPxAP0DRPQ4NhVeP8Kpa8jlIUw"
#auth = "Authorization: Bearer " + bearer 
if __name__ == "__main__":
    #websocket.enableTrace(True)
    new_file=open("newfile.txt",mode="w",encoding="utf-8")
    while True:
        ws = websocket.WebSocketApp("ws://localhost/risk/eth/usd",
                            on_message=on_message)#,header = [protocol_str,auth])

        ws.run_forever()
        print("continue")
        new_file.write("Writing to a new file\n")
        time.sleep(10)



