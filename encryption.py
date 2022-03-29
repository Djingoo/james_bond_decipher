import random

def XOR(a, b):
    assert(len(a) == len(b))
    temp = ""
    for i in xrange(len(a)):
        temp += chr(ord(a[i]) ^ ord(b[i]))
    return temp

if __name__ == "__main__":
    with open("flag.jpg", 'r') as f_in, open("flag.jpg.enc", 'w') as f_out:
        while True:
            d = f_in.read(4)
            if len(d) > 0 and len(d) < 4:
                while len(d) < 4:
                    d += chr(0)
            if d == '':
                break
            s = hex(random.getrandbits(32))[2:].replace('L', '').zfill(8).decode("hex")
            f_out.write(XOR(s, d))