# Names: Ankit Gulekar
#        Erick Shaffer

import time
from socket import *
import datetime

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1.00)

message = ''
times_passed = []
lost_packets = 0
array_size = 0

estRTT = 0
for x in range(0, 10):
    try:
        currentDT = datetime.datetime.now()
        message = 'Ping ' + str(x) + ' ' + str(currentDT)
        start_time = time.time()
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        times_passed.append(time.time() - start_time)
        print('Server message: ' + modifiedMessage)
        print('Round Trip Time for packet ' + str(x) + ': ' + str(times_passed[array_size]))
        estRTT = (1 - 0.125) * estRTT + 0.125 * times_passed[array_size]
        array_size = array_size + 1
    except timeout:
        print('Request timed out')
        lost_packets = lost_packets + 1

packet_loss = lost_packets / float(10)

print('Packet Loss: ' + str(packet_loss))
print('Max Round Trip Time: ' + str(max(times_passed)))
print('Min Round Trip Time: ' + str(min(times_passed)))
print('Average Round Trip Time: ' + str(reduce(lambda z, y: z + y, times_passed) / len(times_passed)))
print('Estimated Round Trip Time: ' + str(estRTT))
clientSocket.close()
