# importe le module RSA
from Crypto.PublicKey import RSA

# genere une cle publique/prive avec modulos (N) de 2048 bits
cle= RSA.generate(2048)

# recupere la cle prive 
cle_prive = cle.exportKey()

#ouvre un fichier en mode d'ecriture en octets
Fichier = open("fichier_cle_prive.pem", "wb")

# ecrit le contenu de la cle prive sur fichier
Fichier.write(cle_prive)
# ferme le fichier
Fichier.close()

# recupere la cle publique 
cle_publique = cle.publickey().exportKey()


# ecrit le contenu de la cle publique sur fichier
Fichier = open("fichier_cle_publique.pem", "wb")
Fichier.write(cle_publique)
Fichier.close()

#imprime la cle publique
print(cle_publique)

#imprime la cle RSA
print(cle_prive)
