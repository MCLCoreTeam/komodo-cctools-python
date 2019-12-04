# -- codeng: utf-8 --
# !/usr/bin/python
import secrets
import sha3
import eth_keys
from eth_keys import keys
import os
import time

dosya1 = open("hackers_addresses.txt", "r")
i = 1
a=int(input("Sayı Giriniz ="))

start = time.time()
while (i <= a):

        zaman = time.time() - start

        private_key ="{:064x}".format(secrets.randbits(256))
        #private_key ="{064x}".format(i)
        private_key_bytes = bytes.fromhex(private_key)
        public_key_hex = keys.PrivateKey(private_key_bytes).public_key
        public_key_bytes = bytes.fromhex(str(public_key_hex)[2:])
        Keccak256_of_public_key_bytes = sha3.keccak_256(public_key_bytes).hexdigest()
        public_address = keys.PublicKey(public_key_bytes).to_address()

        dosya1.seek(0)
        aranan_varmı = dosya1.read().find(public_address)

        if aranan_varmı != -1:
            dosya2 = open("eslesme.txt", "a")
            dosya2.write(private_key + " " + public_address + "\n")
            dosya2.close()
            print("----------BULUNDU----------")
            print("Private Key    : " + private_key)
            print("Address    : " + public_address)

            time.sleep(5)
        else:
            print("Private key =",private_key+ " "+"Address =",public_address+ '\t'+ str(i))

        i = i + 1

dosya1.close()
print("Total Tİme = %s saniye " % zaman)