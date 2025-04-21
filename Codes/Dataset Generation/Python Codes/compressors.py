def FA(a,b,c):
    sum = a^b^c
    carry = (a & b) | (b & c) | (c & a)

    return [carry,sum]
def HA(a,b):
    sum = a^b
    carry = a&b

    return [sum,carry]

def exact_42(a,b,c,d,cin):
    [cout,sum1]=FA(d,c,b)
    [carry,sum]=FA(a,cin,sum1)

    return [sum,carry,cout]

def exact_52(a,b,c,d,e,cin1,cin2):
    [cout1,sum1]=FA(d,c,e)
    [cout2,sum2]=FA(b,cin1,sum1)
    [carry,sum]=FA(a,cin2,sum2)

    return [sum,carry,cout1,cout2]


def pos_42(a,b,c,d):
    sum = a|b|c|d
    carry = (a&b)|(b&c)|(d&b)|(c&d)

    return [sum,carry]

def neg_42(a,b,c,d):
    sum = a|b|c|d
    carry = (a&b)|(c&d)

    return [sum,carry]

# chatgpt
def neg1_42(a, b, c, d):
    sum_out = a ^ b ^ c ^ d
    carry_out = (a & b) | (c & (a ^ b))
    return [sum_out, carry_out]

def pos1_42(a, b, c, d):
    sum_out = a ^ b ^ c ^ d
    carry_out = (a & b) | (c & (a ^ b))
    return [sum_out, carry_out]


# Approximate Multiplier Design Using Novel Dual-Stage 4:2 Compressors
def comp1_42(a,b,c,d):
    sum =((a^b)&(c&d))|((~(a^b))&(c|d))
    carry = a|b

    return [sum,carry]

# novel compressor

def comp2_42(a,b,c,d):
    sum =((a^b^c^d)|(a & b & c ))
    carry = ((a&b)|(a&c)|(a&d)|(b&c)|(b&d)|(c&d))

    return [sum,carry]


def approx_pro1_42(a,b,c,d):
    t1 = a^b
    t2 = c^d
    sum = ((~t1)&(t2) | ((t1)&(~t2)) | (a&b&c&d))
    carry = ~((~(a|b)&(~(c&d))) | (~(c|d)&(~(a&b))))
    return [sum,carry]


def approx_pro2_42(a,b,c,d):
    t1 = a^b
    t2 = c^d
    sum = (~t1)&(t2) | ((t1)&(~t2)) 
    carry = ~((~(a|b)&(~(c&d))) | (~(c|d)&(~(a&b))))
    return [sum,carry]


def approx_pro3_42(a,b,c,d):
    t1 = a^b
    t2 = c^d
    sum = ((~t1)&(c|d) | (t1)&(~t2)) 
    carry = ~(((~(a|b))&(~(c&d))) | (~(c|d)&(~(a&b))))
    return [sum,carry]

def approx_pro5_42(a,b,c,d):
    d1 = ~(a|b)
    d2 = ~(c|d)
    d3 = ~(a&b)
    d4 = ~(c&d)
    O4 = d1 & d2
    O3 = (d1 | d2) & (d3 & d4)
    O2 = (d1 | d2) | (d3 & d4)
    carry = ~(O3)                   
    sum = (O3&(~O4)) | (~O2)

    return [sum,carry]

def approx_pro4_42(a,b,c,d):
    t1 = a^b
    t2 = c^d
    sum = ~((~t1)&(c|d) | (t1)&(~t2))
    carry = ~((~(a|b))&(~(c&d))) | (~(c|d)&(~(a&b)))
    return [sum,carry]


def compressors_42(a,b,c,d,pos):
    if pos==1:
        [sum42,carry42]= pos1_42(a,b,c,d)
    elif pos==2:
        [sum42,carry42]= comp1_42(a,b,c,d)
    elif pos==3:
        [sum42,carry42]= pos_42(a,b,c,d)
    elif pos==4:
        [sum42,carry42]= neg_42(a,b,c,d)
    elif pos==5:
        [sum42,carry42]= comp2_42(a,b,c,d)
    elif pos==6:
        [sum42,carry42]= approx_pro1_42(a,b,c,d)
    elif pos==7:
        [sum42,carry42]= approx_pro2_42(a,b,c,d)
    elif pos==8:
        [sum42,carry42]= approx_pro3_42(a,b,c,d)
    elif pos==9:
        [sum42,carry42]= approx_pro5_42(a,b,c,d)

    return [sum42,carry42]
