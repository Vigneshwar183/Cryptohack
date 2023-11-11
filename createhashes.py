import hashlib
import random
import time

SALT = "ABCDEFG"
LOW= 100000
HIGH=999999


random.seed(time.time())

number1, number2, number3 = random.randrange(LOW,HIGH),random.randrange(LOW,HIGH),random.randrange(LOW,HIGH)

hash1 = hashlib.md5(bytes(SALT+str(number1),"UTF-8")).hexdigest()
hash2 = hashlib.sha256(bytes(SALT+str(number2),"UTF-8")).hexdigest()
hash3 = hashlib.sha512(bytes(SALT+str(number3),"UTF-8")).hexdigest()

print(hash1)
print(hash2)
print(hash3)

for i in range(LOW, HIGH+1):
    if hashlib.md5(bytes(SALT+str(i),"UTF-8")).hexdigest() == hash1:
        print('number 1' + str(i))
    if hashlib.sha256(bytes(SALT+str(i),"UTF-8")).hexdigest() == hash2:
        print('number 2' + str(i))
    if hashlib.sha512(bytes(SALT+str(i),"UTF-8")).hexdigest() == hash3:
        print('number 3' + str(i))
