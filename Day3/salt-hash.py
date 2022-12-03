import hashlib
import uuid

# max:has:salt


# String anhängen/verbinden

str1 = "12456765"
str2 = "test"

#neuer Benutzer
password1 = input("Ihr Passwort1 -> ")
password2 = input("Ihr Passwort2 -> ")

#uuid generiere ich zufällig

salt1 = uuid.uuid4().hex
print(salt1)

hashpasswd1 = hashlib.md5((salt1+password1).encode("utf-8")).hexdigest() + ":" + salt1 # generiert passwd1 hash mit salt wert

salt2 = uuid.uuid4().hex
hashpasswd2 = hashlib.md5((salt2+password2).encode("utf-8")).hexdigest() + ":" + salt2 # generiert passwd1 hash mit salt wert

print(hashpasswd1, hashpasswd2)

print("LOGIN")
print("#"*50)

hash1, salt1 = hashpasswd1.split(":")
hash2, salt2 = hashpasswd2.split(":")

print(f"Hash für PW1: {hash1}\tSalt1: {salt1}")
print(f"Hash für PW2: {hash2}\tSalt2: {salt2}")

login1 = input("Ihr Passwort1 -> ")
#login2 = input("Ihr Passwort2 -> ")

hash1_renew = hashlib.md5((salt1+login1).encode("utf-8")).hexdigest()
#hash1_renew = hashlib.md5((salt2+login2).encode("utf-8")).hexdigest()

print(f"Hash für Login1: {hash1_renew}\tSalt1: {salt1}")


if hash1 == hash1_renew:
    print("you logged in")
else:
    print("mission abbort")
