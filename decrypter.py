import os
import pyaes

## Abrir arquivo criptografado
file_name = "teste.txt.ransomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Setando chave de descriptografia
key = b"testeransomware"
aes = pyaes.AESModesOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## Removendo o arquivo criptografado
os.remove(file_name)

## Criando novo arquivo descriptografado
new_file = "teste.txt"
new_file = open(f"{new_file}", "wb")
new_file.write(decrypt_data)
new_file.close()
