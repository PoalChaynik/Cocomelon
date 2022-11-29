from cryptography.fernet import Fernet

key = Fernet.generate_key()

print(key)

a = Fernet(key)

teksts = b'Bankas Kartes Dati' #teksts -> bytes

noHackers = a.encrypt(teksts) #datu shifreshana

print(noHackers)

print(a.decrypt(noHackers)) #datu atshifreshana