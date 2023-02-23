def sumar(x, y):
    return x + y
    

def es_primo(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
    
print("pruebas")    