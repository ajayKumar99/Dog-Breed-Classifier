import random

def initializer():
    i = random.randint(0 , 119)
    while True:
        j = random.randint(0 , 119)
        if i != j:
            break
    while True:
        z = random.randint(0 , 119)
        if z != i and z != j:
            break
    k = random.randint(0 ,2)
    while True:
        l = random.randint(0 , 2)
        if l != k:
            break
    while True:
        m = random.randint(0 , 2)
        if m != k and m != l:
            break
    return i , j , z , k , l , m
