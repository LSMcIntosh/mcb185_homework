
def oligoMT(A, T, C, G):
	nt = A + T + C + G
	if nt <= 13: Tm = (A+T)+2 + (G+C)*4
	else: Tm = 64.9 + 41*((G+C-16.4)/nt) 
	if type(Tm) == float:
		round(Tm, ndigits=2)
	return Tm
	
print (oligoMT(5, 7, 3, 4))
print (oligoMT(4, 2, 3, 4))
print (oligoMT(24, 27, 35, 32))

