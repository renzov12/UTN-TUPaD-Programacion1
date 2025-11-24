def es_palindromo(palabra):
    if len(palabra) <= 1 :
        return True
    

    #buscamos los inicios 
    if palabra[0] != palabra[-1]:
        return False
    

    #revisamos los medios
    return es_palindromo(palabra[1:-1])
    

    
print(es_palindromo("ana"))       
print(es_palindromo("reconocer"))  
print(es_palindromo("python")) 

