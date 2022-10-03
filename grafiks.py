import matplotlib.pyplot as plt
import numpy as np

def linijas():
    ypoints = np.array(np.random.randint(100,size=(10)))
    ypoints2 = np.array(np.random.randint(100, size=(10)))
    plt.plot(ypoints, 'o-.')
    plt.plot(ypoints2, '+:r')
    plt.show()
# linijas()

a = [10,20,10,30,40,50,10,25,60]
def masivaGrafiks(masivs):
    plt.plot(masivs, 'o-.')
    plt.show()

# masivaGrafiks(a)

def kvadratfunkcija(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)

    X = -b/(2*a)
    if (X).is_integer():
        X = int(X)
    else:
        X = float(X)
    Y = (a*(X**2)+(b*X)+c)
    print('X ir',X)
    print('Y ir',Y)
    xcords = np.arange(1,20,.5)
    ycords = []
    for x in range(len(xcords)):
        x_val = xcords[x]
        y=(a*(x_val**2))+(b*x_val)+c
        ycords.append(y)
    # print(xcords)
    # print(ycords)
    plt.plot(xcords,'o-.')
    plt.plot(ycords,'o:r')
    plt.ylim([-5,15])
    plt.xlim([-5,15])
    plt.show()
    # ycords.append(Y)
    # array = np.array(xcords)
    # n = array.size
    # N = 10
    # M = n//N
    # reshaped = array.reshape((N, M))


A1 = input('Ievadiet a: ')
if A1.find(',') !=-1:
    A1 = (A1.replace(',','.'))
B1 = input('Ievadiet b: ')
if B1.find(',') !=-1:
    B1=B1.replace(',','.')
C1 = input('Ievadiet c: ')
if C1.find(',') !=-1:
    C1=C1.replace(',','.')

kvadratfunkcija(A1,B1,C1)


# Neinteresee vai ir pareizi vai nav, TAS IR PAREIZI PAT JA NAV!