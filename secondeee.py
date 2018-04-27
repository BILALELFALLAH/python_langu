from math import *
a = float(input('lavaleur de a    '))
b = float(input('la valeur de b   '))
c = float(input('la valeur de c   '))
if a == 0 :
    if b == 0 :
        if c == 0 :
            print 'tout reel est une solution de cette eqution'
        else :
            print ' l ensemble des solutios est vide '
    else : 
        print 'la solution est egale a  ', -c/b
else :
    D = pow(b,2)- 4*a*c
    if D < 0 :
        print 'les racines sont complexes '
    if D == 0 :
        print  'la solution est ', -b/(2*a)
    if D > 0 :
        print 'les solutions sont :  ',(-b-sqrt(D))/2*a,'  et  :',(-b+sqrt(D))/2*a            
