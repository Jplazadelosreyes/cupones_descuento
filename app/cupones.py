DESCUENTOS = {
    "OFERTA10": 0.10,
    "SUPER20": 0.20
    # "BIENVENIDA": 0.15
}

def aplicar_cupon(precio, cupon):
    if not cupon:
        return precio

    cupon = cupon.strip().upper()

    if cupon in DESCUENTOS:
        descuento = DESCUENTOS[cupon]
        return round(precio * (1 - descuento), 2)

    return precio

def calcular_precio_final(precio_base, cupon, impuesto=0.19):

    precio_desc = aplicar_cupon(precio_base, cupon)
    return round(precio_desc * (1 + impuesto), 2)
