import gnupg
import os

gpg=gnupg.GPG(gnupghome='/home/lol/.gnupg')

gpg.encoding = 'utf-8'

path='/path_to_file'
ptext='/lol-gpg.txt'

stream = open(path+ptext, 'rb')

fp = gpg.list_keys(True).fingerprints[0]

edata = gpg.encrypt_file(stream, recipients='lol@gmail.com',sign=fp,always_trust=True,output=path+ptext+".pgp")
stream.close()

print(edata.stderr)
