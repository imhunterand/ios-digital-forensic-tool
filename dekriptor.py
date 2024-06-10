from Crypto.Cipher import AES
import base64

def dekripsi_data(data_terenkripsi, kunci, iv):
    cipher = AES.new(kunci, AES.MODE_CBC, iv)
    data_didekripsi = cipher.decrypt(base64.b64decode(data_terenkripsi))
    return data_didekripsi.rstrip(b"\0")
