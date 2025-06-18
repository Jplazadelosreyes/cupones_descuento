Proyecto Cupones de Descuento - Flask
Descripción
Este proyecto es una aplicación web desarrollada con Flask que permite aplicar descuentos mediante cupones promocionales y calcular el precio final de un producto incluyendo impuestos. Es una herramienta sencilla orientada a practicar desarrollo web con Python y Flask, integración con tests automatizados y despliegue continuo.

Estructura del Proyecto
cupones_descuento/
├── app/
│   ├── __init__.py         # Inicialización de la aplicación Flask
│   ├── api.py              # (Opcional) APIs REST si se agregan
│   ├── cupones.py          # Lógica para aplicar cupones y calcular precios
│   ├── models.py           # Definición de modelos (si se usan bases de datos)
│   └── routes.py           # Definición de rutas Flask y vistas
├── tests/
│   ├── __init__.py
│   └── test_cupones.py     # Tests para la lógica de descuentos
├── run.py                  # Script para correr la aplicación
├── requirements.txt        # Dependencias del proyecto
├── pytest.ini              # Configuración para pytest
└── .github/
    └── workflows/
        └── python-app.yml  # Configuración de GitHub Actions para CI

Instalación
Clonar el repositorio

git clone <URL_DE_TU_REPOSITORIO>
cd cupones_descuento

Crear y activar un entorno virtual

python -m venv venv
source venv/bin/activate    # En Linux/macOS
venv\Scripts\activate       # En Windows

Instalar las dependencias

pip install -r requirements.txt

Configuración
Se recomienda definir una clave secreta para la aplicación Flask, utilizada para la gestión de sesiones y seguridad. Puedes generar una ejecutando lo siguiente en tu terminal Python:

import secrets
print(secrets.token_hex(32))

Luego, en app/__init__.py o donde inicialices la aplicación, configura:

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TU_CLAVE_SECRETA_AQUI' # Reemplaza con la clave generada

Uso
Para iniciar la aplicación, ejecuta:

python run.py

La aplicación estará disponible en http://localhost:5000/ y mostrará un mensaje simple confirmando que el proyecto está en ejecución.

Lógica de Cupones y Cálculo
El archivo app/cupones.py contiene la función principal para aplicar descuentos y calcular el precio final con impuesto:

# Diccionario de descuentos, mapea el nombre del cupón a su porcentaje de descuento.
DESCUENTOS = {
    "OFERTA10": 0.10,
    "SUPER20": 0.20,
    "BIENVENIDA": 0.15
}

def aplicar_cupon(precio, cupon):
    """
    Aplica un descuento al precio dado si el cupón es válido.

    Args:
        precio (float): El precio base al que se aplicará el descuento.
        cupon (str): El código del cupón a aplicar.

    Returns:
        float: El precio con el descuento aplicado, o el precio original si el cupón no es válido.
    """
    if not cupon:
        return precio # Si no hay cupón, retorna el precio sin cambios
    cupon = cupon.strip().upper() # Limpia espacios y convierte a mayúsculas para la comparación
    if cupon in DESCUENTOS:
        # Calcula el precio con descuento y lo redondea a 2 decimales
        return round(precio * (1 - DESCUENTOS[cupon]), 2)
    return precio # Si el cupón no existe, retorna el precio original

def calcular_precio_final(precio_base, cupon, impuesto=0.19):
    """
    Calcula el precio final de un producto después de aplicar un cupón y un impuesto.

    Args:
        precio_base (float): El precio base del producto.
        cupon (str): El código del cupón a aplicar.
        impuesto (float, optional): La tasa de impuesto a aplicar. Por defecto es 0.19 (19%).

    Returns:
        float: El precio final del producto con descuento e impuesto aplicados.
    """
    precio_desc = aplicar_cupon(precio_base, cupon) # Primero aplica el descuento
    # Luego aplica el impuesto y redondea a 2 decimales
    return round(precio_desc * (1 + impuesto), 2)

Tests
Se utilizan tests con pytest para validar la lógica de los cupones. El archivo principal de tests es tests/test_cupones.py:

from app.cupones import aplicar_cupon, calcular_precio_final

def test_descuento_oferta10():
    """Verifica que el cupón 'OFERTA10' aplica un 10% de descuento correctamente."""
    assert aplicar_cupon(100, "OFERTA10") == 90.0

def test_descuento_super20():
    """Verifica que el cupón 'SUPER20' aplica un 20% de descuento correctamente."""
    assert aplicar_cupon(200, "SUPER20") == 160.0

def test_descuento_bienvenida():
    """Verifica que el cupón 'BIENVENIDA' aplica un 15% de descuento correctamente."""
    assert aplicar_cupon(100, "BIENVENIDA") == 85.0

def test_cupon_no_valido():
    """Verifica que un cupón no válido no aplica ningún descuento."""
    assert aplicar_cupon(100, "INVALIDO") == 100

def test_precio_final_con_cupon():
    """
    Verifica el cálculo del precio final con un cupón aplicado (OFERTA10)
    y el impuesto del 19%. (100 * 0.9) * 1.19 = 107.1
    """
    assert calcular_precio_final(100, "OFERTA10") == 107.1

def test_precio_final_sin_cupon():
    """
    Verifica el cálculo del precio final sin cupón aplicado, solo con el
    impuesto del 19%. 100 * 1.19 = 119.0
    """
    assert calcular_precio_final(100, "") == 119.0

Para ejecutar los tests:

pytest

Integración Continua con GitHub Actions
El workflow de GitHub Actions (.github/workflows/python-app.yml) está configurado para:

Ejecutar las pruebas automáticamente en cada push o pull request a la rama main.

Usar Python 3.10 en un runner Ubuntu.

Crear un entorno virtual, instalar dependencias y ejecutar pytest.

Ejemplo básico del workflow:

name: Pruebas de Regresión - Cupones # Nombre del workflow

on:
  push: # Se dispara en cada push
    branches: [main] # A la rama main
  pull_request: # Se dispara en cada pull request
    branches: [main] # A la rama main

jobs:
  test: # Define un job llamado 'test'
    runs-on: ubuntu-latest # Ejecuta el job en un ambiente Ubuntu
    steps:
      - uses: actions/checkout@v3 # Paso para clonar el repositorio

      - name: Configurar Python # Nombre del paso para configurar Python
        uses: actions/setup-python@v4 # Usa la acción oficial para configurar Python
        with:
          python-version: '3.10' # Especifica la versión de Python a usar

      - name: Instalar dependencias # Nombre del paso para instalar dependencias
        run: | # Ejecuta múltiples comandos en shell
          python -m venv venv # Crea un entorno virtual
          source venv/bin/activate # Activa el entorno virtual (Linux/macOS)
          pip install -r requirements.txt # Instala las dependencias desde requirements.txt

      - name: Ejecutar pruebas # Nombre del paso para ejecutar las pruebas
        run: | # Ejecuta múltiples comandos en shell
          source venv/bin/activate # Asegura que el entorno virtual esté activado
          pytest # Ejecuta pytest para correr las pruebas

Dependencias
Las dependencias del proyecto se listan en el archivo requirements.txt:

Flask==2.2.3
python-dotenv==1.0.0
pytest==7.3.1

Contacto
Si tienes dudas o quieres aportar al proyecto, contáctame en:

Email: tu.email@ejemplo.com

GitHub: https://github.com/tuusuario

Licencia
Este proyecto está bajo licencia MIT. Consulta el archivo LICENSE para más detalles.
