import hashlib


passwd = "passwort"
# Hash schaut wie folgt aus: max:7bbb60c9bbe819ea2f2759f7900689acb5f5b0615b235838d1690770aeb0357fba7b05d98d741a1d0bf5727bebfc37ececa46c34fe3d666e5b822b4dc8b7503b

print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)

# Hash - Algorithmus definieren (in übungsblatt nach schauen)

hash_alg = hashlib.sha3_224() # Create object

print(hash_alg)

# 1 Klartextpasswort in alg eintragen
print(passwd, passwd.encode('utf-8'))
sha1 = hash_alg.update(passwd.encode("utf-8")) # übergibt PW als bites

# 2 Hashverfahren gestartet
print(f"Passwort = {passwd} \nPasswort verschlüsselt = {sha1.hexdigest()}")

# einzeiler

