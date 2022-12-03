# dataei einlese


try:
    with open(file="../Uebungen/U1-6.py", mode="r", encoding="utf-8") as f:
        data = f.readlines()
        print(type(data))
        print(data)

    f.close()

    with open(file="../Uebungen/U1-6.py", mode="r", encoding="utf-8") as f:
        for idx, line in enumerate(data, start=1):

            if idx % 2 == 0:
                continue

            if idx == 10:
                break

            print(f"{idx}:{line}:{data}")

    f.close()



