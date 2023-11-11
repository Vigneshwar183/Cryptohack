from Crypto.Util.number import inverse

p= [493,5564]
q= [1539,4742]
r= [4403,5202]

def calSlope(x1, y1):
    p = 9739
    if x1[0]==y1[0] and x1[1]==y1[1]:
        slope = ((y1[1]-x1[1]) * inverse(y1[0]-x1[0],1))%p
    else:
        slope = ((3*x1[0]*x1[0]+497)* inverse(2*x1[1],1))%p
    x3 = (slope*slope - x1[0] - y1[0])%p
    y3 = (slope*(x1[0]-x3) - x1[1])%p
    return [x3,y3]

final = calSlope(p, p)
final = calSlope(final, q)
final = calSlope(final, r)
print(final)