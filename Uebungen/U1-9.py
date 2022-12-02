"""
<U1 Bsp. 9>
<1 -50 Schleife der fibonacci reihe>
< Algorythmus:

    x = Durchlauf
    c(x) + n(x) = f(x)
    n(x) = c(x)
    c(x) =f(x)

<Maximilian Jonas, 52203295>
"""

currentInt = 0 # Start der Reihe
nextInt = 1 # nächster  Integer


for _ in range(0, 50):

    fibInt = nextInt + currentInt
    print(fibInt)

    nextInt = currentInt
    currentInt = fibInt










