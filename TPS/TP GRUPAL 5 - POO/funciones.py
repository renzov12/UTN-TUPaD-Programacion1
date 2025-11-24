def pedir_int_rango(mensaje, limite_inf = -float("inf"), limite_sup = float("inf")):
    """
    Pide un numero entero y valida que este dentro dentro del rango solicitado\n
    mensaje = mensaje a mostrar en input\n
    limite_inf = limite inferior del rango\n
    limite_sup = limite superior del rango\n
    retorna int
    """
    while True:
        n = input(mensaje)
        try: n = int(n)
        except: 
            print("ERROR: Ingresa un numero entero")
            continue
        if not limite_inf<=n<=limite_sup:
            print(f"ERROR: El numero ingresado no esta entre {limite_inf} y {limite_sup}")
            continue
        return n

def pedir_float_rango(mensaje, limite_inf = -float("inf"), limite_sup = float("inf")):
    """Pide un numero flotante y valida que este dentro dentro del rango solicitado"""
    while True:
        n = input(mensaje)
        try: n = float(n)
        except: 
            print("ERROR: Ingresa un numero")
            continue
        if not limite_inf<=n<=limite_sup:
            print(f"ERROR: El numero ingresado no esta entre {limite_inf} y {limite_sup}")
            continue
        return n
