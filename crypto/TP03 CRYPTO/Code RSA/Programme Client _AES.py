import socket 
from Crypto.PublicKey import RSA
from Crypto.Cipher import  PKCS1_OAEP
import os
from Crypto.Cipher import AES
import Padding
from Crypto.Util.Padding import pad, unpad



SocketClient = socket.socket()
host = socket.gethostname() 
port = 9501
SocketClient.connect(("127.0.0.1", port)) 

Cle_publique=b""
while True:
        recu=SocketClient.recv(1024)
        Cle_publique+=recu
        if b'-----END PUBLIC KEY-----' in Cle_publique:
                clepublique = RSA.importKey(Cle_publique)
                objet_cle_rsa_publique = PKCS1_OAEP.new(clepublique)
                ###################################################################################################

                cle_16_octet =os.urandom(16)
                #cree une instance AES avec une cle= "cle16 octets AES"
                #la taille de la cle == (16octets)
                objet_de_chiffrement=AES.new(cle_16_octet, AES. MODE_ECB)
                #chiffre cle AES + send
                resultat_chiffre=objet_cle_rsa_publique.encrypt(cle_16_octet)
                SocketClient.send(resultat_chiffre)
                
                break

# Importez la cle a partir du contenu recu Cle_publique
# Utilisez la methode importKey de RSA pour importer la cle
# Mettez le resultat dans clepublique 
# Creez un objet objet_cle_rsa_publique a partir de clepublique (objet de cle publique)
# Utilisez PKCS1_OAEP.new pour faire ceci
# (A FAIRE 1) ajoutez deux instructions dans les deux lignes suivantes



################################# debut communication avec AES ####################################




print("Lancement serveur (using AES)")
while True:  
   MessageATransmettre=input().encode()
   # Chiffre le message lu du clavier (MessageATransmettre)
   # Utilisez la methode encrypt de objet_cle_rsa_publique
   # Mettez le resultat dans resultat_chiffre
   # (A FAIRE 2) ajoutez l'instruction dans cette ligne
   #resultat_chiffre=objet_cle_rsa_publique.encrypt(MessageATransmettre)
   data=objet_de_chiffrement.encrypt(pad(MessageATransmettre, AES.block_size))
   
   SocketClient.send(data)
   if(MessageATransmettre==b"Fin"):
      break
      print( "Deconnexion de :",addrclient)
SocketClient.close()
