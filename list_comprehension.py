# l1 = [a+b+c for a in 'hello' if a in 'el'
#       for b in 'HELLO' if b in ('L', "O")
#       for c in '123' if c > '1']
# print(l1)

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
dcc = [M[i][i] for i in range(len(M))]
print('DCC:', dcc)
dcp = [M[i][len(M)-1-i] for i in range(len(M))]
print('DCP:', dcp)
