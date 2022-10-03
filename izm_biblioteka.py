import biblioteka as bib

print(bib.a)

for v in bib.saraksts:
    print(v)

print(bib.sum(bib.a,9))

bmb = bib.Auto()

bmb.braukt()
# ////////
from biblioteka import *

print(a)
au = Auto()
au.braukt()


# 1. import x -> x.######
# 2. import x as y -> y.#######
# 3. from x import y | from x import *

from biblioteka import test,test2

print(test+' un '+test2)
