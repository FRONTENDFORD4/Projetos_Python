from ftplib import *

ftp = FTP("ftp.ibge.gov.br")

print(ftp.getwelcome())

print("Pasta atual: ", ftp.pwd())