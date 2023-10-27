#generate ANF
#run sage -python testANF.py

from sage.all import *

#F = [7,4,9,12,11,10,13,8,15,14,1,6,0,3,2,5] #S-box
F = [12,10,14,13,1,15,11,0,7,2,5,4,3,6,9,8] #inv_S-box

def Fi(Sbox, n):

    S = sage.crypto.sbox.SBox(Sbox)

    f = [0 for j in range(0, n)]

    for j in range(0, n):
        f[j] = S.component_function(1 << j).algebraic_normal_form()
        print(str(j) + ": ",end = ' ')
        print(f[j])

Fi(F, 4) #4-bit S-box

'''
S-box:
(3,2,1,0)-->(0,1,2,3)
3:  x1*x0 + x3 + 1
2:  x3*x2*x1 + x3*x2 + x3*x1 + x3*x0 + x1*x0 + x3 + x2 + 1
1:  x2*x1*x0 + x3*x2 + x2 + x1 + 1
0:  x2*x1 + x2 + x1 + x0
'''

'''
inv_Sbox:
(0,1,2,3)
x0:  y0 + y1 + y0*y1 + y1*y2 + y1*y3 + y0*y1*y3 + 1
x1:  y1 + y3 + y2*y3 + 1
x2:  y0 + y2 + y3 + y0*y3 
x3:  y0 + y1 + y0*y1 + y0*y3 + y2*y3 + y0*y2*y3
'''

