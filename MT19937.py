import datetime
now = datetime.datetime.now()
current_time = int(now.strftime("%Y%m%d%H%M%S"))

(w, n, m, r) = (32, 624, 397, 31)
a = 0x9908B0DF
(u, d) = (11, 0xFFFFFFFF)
(s, b) = (7, 0x9D2C5680)
(t, c) = (15, 0xEFC60000)
l = 18
f = 1812433253

MT = [0 for i in range(n)]
index = n + 1
lower_mask = 0x7FFFFFFF
upper_mask = 0x80000000

#64bit:
if False:
    (w, n, m, r) = (64, 312, 156, 31)
    a = 0xB502F5AA96619E9
    (u, d) = (29, 0x5555555555555555)
    (s, b) = (17, 0x71D67FFFEDA60000)
    (t, c) = (37, 0xFFF7EEE000000000)
    l = 43
    f = 6364136223846793005
    lower_mask = 0x7FFFFFFFFFFFFFFF
    upper_mask = 0x8000000000000000

def seed(seed):
    MT[0] = seed
    for i in range(1, n):
        temp = f * (MT[i-1] ^ (MT[i-1] >> (w-2))) + i
        MT[i] = temp & d

def twist():
    for i in range(0, n):
        x = (MT[i] & upper_mask) + (MT[(i+1) % n] & lower_mask)
        xA = x >> 1
        if (x % 2) != 0:
            xA = xA ^ a
        MT[i] = MT[(i + m) % n] ^ xA
 
def extract_number():
    global index
    if index >= n:
        twist()
        index = 0

    y = MT[index]
    y = y ^ ((y >> u) & d)
    y = y ^ ((y << s) & b)
    y = y ^ ((y << t) & c)
    y = y ^ (y >> l) #return z

    index += 1
    return y & d

seed(current_time)
#print(extract_number())

def random():
    return extract_number() / (2**w)

def randint(a, b):
    n = random()
    return int(n/(1/(b-a)) + a)

def shuffle(n):
    new = list(n)
    for i in range(10*len(n)):
        a = randint(0, len(n))
        b = randint(0, len(n))
        new[a], new[b] = new[b], new[a]
    return new

def choice(n):
    new = list(n)
    return new[randint(0, len(new))]

print(random())
print(randint(-100, 100))
print(shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
