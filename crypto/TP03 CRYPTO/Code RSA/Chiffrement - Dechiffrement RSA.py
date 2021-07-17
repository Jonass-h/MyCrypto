from Crypto.PublicKey import RSA
from Crypto.Cipher import  PKCS1_OAEP

# importe la cle publique du fichier
contenu_clepublique = RSA.importKey(open("fichier_cle_publique.pem","rb").read())

# cree un objet a partir de la cle permetant de chiffre avec RSA
objet_cle_rsa = PKCS1_OAEP.new(contenu_clepublique)

# message claire
message=b" hello world RSA !! "
# chiffre le message avec la cle publique
message_chiffre=objet_cle_rsa.encrypt(message)

#imprime le resultat du chiffrement
print(message_chiffre)

# importe la cle prive du fichier
contenu_cleprive = RSA.importKey(open("fichier_cle_prive.pem","rb").read())
# cree un objet a partir de la cle permetant de chiffre avec RSA
objet_cle_rsa_prive = PKCS1_OAEP.new(contenu_cleprive)
#imprime le resultat du dechiffrement
print(objet_cle_rsa_prive.decrypt(message_chiffre))
