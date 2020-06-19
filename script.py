from datetime import datetime
import time
import sys
counter_compare = 0
counter_replace = 0

server_file = sys.argv[1]

handle = open(server_file, "r")
BinSearch = handle.read()
handle.close()
print(BinSearch)
BinSearch= BinSearch.split()
print(BinSearch)
a = BinSearch
for i in range(15):
    a.append(randint(1, 50))
a.sort()
print(a)
 

value = int(input())
 
 
mid = len(a) // 2
low = 0
high = len(a) - 1
 
while a[mid] != value and low <= high:
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2
 
if low > high:
    print("No value")
else:
    print("ID =", mid)
print('BinSearch', BinSearch )
print(" Lenght:", len(BinSearch))
print("Time:")
print(datetime.now() - start_time)
for i in range(0, len(BinSearch)):
   BinSearch[i] = str(BinSearch[i])
result =''.join(BinSearch)
handle = open("server_outcoming.txt", "w")
handle.write(result)
handle.close()
