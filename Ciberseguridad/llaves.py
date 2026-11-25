import rsa 

public_key, priavate_key = rsa.newkeys(2024)
with open("public_key1.pem", "wb")as f:
    f.write(public_key.save_pkcs1(format='PEM'))
with open("private_key1.pem", "wb")as f:
    f.write(priavate_key.save_pkcs1(format='PEM'))