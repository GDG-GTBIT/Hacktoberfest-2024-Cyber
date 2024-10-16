import base64

def log_encrypt(content):
    with open("logfile.txt",'w') as logKey:
        logKey.write(content.decode())
def encode(key):
    encrypt = []
    with open("logfile.txt", 'r') as read:
        log_read = read.read()
        for i in range(len(log_read)):
            encrypt_key = key[i % len(key)]
            encrypt_log = chr((ord(log_read[i]) + ord(encrypt_key))%256)
            encrypt.append(encrypt_log)
        content = base64.urlsafe_b64encode("".join(encrypt).encode())
        log_encrypt(content)