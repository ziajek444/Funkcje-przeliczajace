
gora = "92233720368547758070"
dol  =   "202233720368547758070"
wyn = "0."
dluzszy =  max(len(gora),len(dol))
lg= len(gora)
ld=len(dol)

if lg > ld:
	dol = (lg - ld) * '0' + dol
else:
	gora = (ld-lg) * '0' + gora

mem = 0

for it in range(dluzszy,0,-1):
  dig = int(gora[it-1])+int(dol[it-1])
  if dig>9 : 
    dig = dig -10
    wyn += chr(dig+mem+48)
    mem = 1
  else:
  	wyn += chr(dig+mem+48)
  	mem =0

if mem > 0:
	wyn += chr(mem+48)

print(wyn[::-1])


