from app import create_app
# Si necesitas usar funciones desde cupones.py:
# from app.cupones import calcular_precio_final

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
