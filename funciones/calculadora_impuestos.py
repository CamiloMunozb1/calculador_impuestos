tarifa_renta = 0.35 # Tarifa de renta.

def operacion_impuestos():
    try:
        # Entrada de usuario.
        impuesto = float(input('Ingresa el valor de la renta de este año: '))
        if not impuesto: # Validacion de entrada de usuarios.
            print('El campo no puede estar vacio.')
            return
        calculo_renta = impuesto * tarifa_renta # Calculo de la renta.
        print(calculo_renta)
    # Manejo de errores.
    except ValueError:
        print('Ingresa un valor real.')
        return
    except Exception as error:
        print(f'Error inesperado en el sistema : {error}')
        return