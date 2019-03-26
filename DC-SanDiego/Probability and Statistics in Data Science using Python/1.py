
def gen_c(k=1000, n=100):
    X = 2 * (random.rand(k,n)>0.5)-1 
    S = sum (X,axis=0)
    return S

print(gen_c)