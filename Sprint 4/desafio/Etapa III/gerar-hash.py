import hashlib


while True:
    string = input("Escreva algo: ")
    
    if string == "":
        break

    hash = hashlib.sha1()    
    hash.update(string.encode('utf-8'))
    print(hash.hexdigest())
