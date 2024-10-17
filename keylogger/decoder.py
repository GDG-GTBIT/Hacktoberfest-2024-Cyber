import base64

def log_decrypt(content):
    with open('logfile.txt','w') as logKey:
        logKey.writelines(content)

def decode(key):
    dec = []
    with open("logfile.txt",'r') as read:
        enc = read.read()
        enc = base64.urlsafe_b64decode(enc).decode('utf-8')
        print(enc)
        for i in range(len(enc)):
            key_c = key[i % len(key)]
            dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
            dec.append(dec_c)
        content = "".join(dec)
        log_decrypt(content)