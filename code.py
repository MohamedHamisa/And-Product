def andProduct(a, b):
    return a & ~((1<<(len(bin(a^b)) - 3)) - 1) 
