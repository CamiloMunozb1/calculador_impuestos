tarifa_renta = 0.35

def operacion_impuestos():
    try:

        impuesto = float(input('Ingresa el valor de la renta de este año: '))
        if not impuesto:
            print('El campo no puede estar vacio.')
            return
        calculo_renta = impuesto * tarifa_renta
        print(calculo_renta)

    except ValueError:
        print('Ingresa un valor real.')
        return
    except Exception as error:
        print(f'Error inesperado en el sistema : {error}')
        return