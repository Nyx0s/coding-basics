
try:
    zahl = int(input("Gib eine Zahl ein: > "))
    zahl += 1

except (TypeError, ValueError) as e:
    print(f"Es können nur Zahlen um eins erhöht werde! -> {e}")

except ZeroDivisionError as e:
    print(f"es kann nicht durch 0 dividiert werden -> {e}")

def safe_cast(val, toTyp, default=None):
    try:
        return toTyp(val)
    except (ValueError, TypeError):
        return default


if safe_cast(1, int) != None:
    print("Cast ausgeführt")
else:
    print("Cast nicht ausgeführt")
