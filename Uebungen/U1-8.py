"""
<U1 Bsp. 8>
<Euro anteile eines Betrages>
<Maximilian Jonas, 52203295>
"""

# erstellen von Euroschein Variablen

fh = 500  # 500er Schein
zh = 200  # 200er Schein
hd = 100  # 100er Schein
fz = 50   # 50er Schein
zz = 20   # 20er Schein
zn = 10   # 10er Schein
ff = 5    # 5er Schein
ze = 2    # 2er Münze
ee = 1    # 1er Münze

# speichern
gesammtBetrag = int(input("Gib den Geldbetrag an: "))

# nimmt

fünfHundert = gesammtBetrag // fh
zweiHundert = (gesammtBetrag % fh) // zh
einHundert = (gesammtBetrag % fh) % zh // hd
fünfZig = (gesammtBetrag % fh) % zh % hd // fz
zwanZig = (gesammtBetrag % fh) % zh % hd % fz // zz
zehnEuro = (gesammtBetrag % fh) % zh % hd % fz % zz // zn
fünfEuro = (gesammtBetrag % fh) % zh % hd % fz % zz % zn // ff
zweiEuro = (gesammtBetrag % fh) % zh % hd % fz % zz % zn % ff // ze
einEuro = (gesammtBetrag % fh) % zh % hd % fz % zz % zn % ff % ze // ee

print(f"""
Fünfhundert Euro: {fünfHundert} Stk.
Zweihundert Euro: {zweiHundert} Stk.
Einhundert Euro:  {einHundert} Stk.
Fünfzig Euro:     {fünfZig} Stk.
Zwanzig Euro:     {zwanZig} Stk.
Zehn Euro:        {zehnEuro} Stk.
Fünf Euro:        {fünfEuro} Stk.
Zwei Euro:        {zweiEuro} Stk.
Ein Euro:         {einEuro} Stk.""")
