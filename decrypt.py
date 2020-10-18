import gnupg
import os

gpg=gnupg.GPG(gnupghome='/home/lol2/.gnupg')

gpg.encoding = 'utf-8'

path='/home/lol2/'
ptext='lol-gpg.txt.pgp'

stream = open(path+ptext, 'rb')
decrypt_data = gpg.decrypt_file(stream,output=path+ptext+".verified")
stream.close()

print(decrypt_data.stderr)
print(decrypt_data.status)
print(decrypt_data.valid)
print(decrypt_data.trust_text)
