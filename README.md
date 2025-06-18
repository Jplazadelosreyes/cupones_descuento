¡Absolutamente! Aquí tienes el **README.md completo**, **sin interrupciones externas**, contenido desde el principio hasta el final dentro de un **único bloque de código Markdown**.

Espero que esta vez sea exactamente lo que necesitas para copiar y pegar directamente en tu archivo.

```markdown
# Proyecto Cupones de Descuento - Flask

---

## Descripción

Este proyecto es una **aplicación web** desarrollada con **Flask** que permite aplicar **descuentos mediante cupones promocionales** y calcular el precio final de un producto, incluyendo los impuestos. Es una herramienta sencilla orientada a practicar el **desarrollo web con Python y Flask**, la **integración con tests automatizados** y el **despliegue continuo (CI/CD)**.

---

## Estructura del Proyecto

La estructura del proyecto sigue una organización clara para facilitar el desarrollo y mantenimiento:

```
cupones_descuento/
├── app/
│   ├── __init__.py         # Inicialización de la aplicación Flask
│   ├── api.py              # (Opcional) Módulo para futuras APIs REST
│   ├── cupones.py          # Lógica principal para la aplicación de cupones y cálculo de precios
│   ├── models.py           # Definición de modelos (en caso de usar bases de datos)
│   └── routes.py           # Definición de rutas Flask y manejo de las vistas
├── tests/
│   ├── __init__.py
│   └── test_cupones.py     # Contiene los tests unitarios para la lógica de descuentos
├── run.py                  # Script para iniciar la aplicación Flask
├── requirements.txt        # Lista de dependencias del proyecto
├── pytest.ini              # Archivo de configuración para pytest
└── .github/
    └── workflows/
        └── python-app.yml  # Configuración de GitHub Actions para Integración Continua (CI)
```

---

## Instalación

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local.

### Clonar el Repositorio

Para empezar, clona este repositorio en tu máquina local usando `git`:

```bash
git clone <URL_DE_TU_REPOSITORIO>
cd cupones_descuento
```

**Nota:** Sustituye `<URL_DE_TU_REPOSITORIO>` por la URL real de tu repositorio.

### Crear y Activar un Entorno Virtual

Se recomienda encarecidamente usar un entorno virtual para gestionar las dependencias del proyecto de forma aislada:

```bash
python -m venv venv
source venv/bin/activate       # En Linux/macOS
# venv\Scripts\activate        # En Windows
```

### Instalar las Dependencias

Con el entorno virtual activado, instala todas las dependencias del proyecto listadas en `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## Configuración

Es una buena práctica definir una clave secreta para tu aplicación Flask, la cual es crucial para la seguridad de sesiones y otros aspectos.

### Generar Clave Secreta

Puedes generar una clave segura ejecutando el siguiente código en una terminal de Python:

```python
import secrets
print(secrets.token_hex(32))
```

### Configurar la Aplicación Flask

Luego, en tu archivo `app/__init__.py` o donde inicialices tu aplicación Flask, configura la clave secreta:

```python
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TU_CLAVE_SECRETA_AQUI' # ¡Reemplaza con la clave generada!
```

---

## Uso

Para iniciar la aplicación localmente, asegúrate de estar en el directorio raíz del proyecto y tener tu entorno virtual activado, luego ejecuta:

```bash
python run.py
```

La aplicación estará disponible en `http://localhost:5000/` y mostrará un mensaje simple confirmando que el proyecto está en ejecución.

---

## Lógica de Cupones y Cálculo

El archivo `app/cupones.py` contiene las funciones principales para aplicar descuentos y calcular el precio final con impuestos.

```python
# Contenido del archivo app/cupones.py

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
        return precio
    cupon = cupon.strip().upper()
    if cupon in DESCUENTOS:
        return round(precio * (1 - DESCUENTOS[cupon]), 2)
    return precio

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
    precio_desc = aplicar_cupon(precio_base, cupon)
    return round(precio_desc * (1 + impuesto), 2)
```

---

## Tests

Se utilizan tests con **pytest** para validar la lógica de los cupones. El archivo principal de tests es `tests/test_cupones.py`.

```python
# Contenido del archivo tests/test_cupones.py

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
```

### Ejecutar los Tests

Para ejecutar los tests, asegúrate de tener el entorno virtual activado y ejecuta:

```bash
pytest
```

---

## Integración Continua con GitHub Actions

El workflow de GitHub Actions (`.github/workflows/python-app.yml`) está configurado para:

* Ejecutar las pruebas automáticamente en cada `push` o `pull request` a la rama `main`.
* Usar Python 3.10 en un runner Ubuntu.
* Crear un entorno virtual, instalar dependencias y ejecutar `pytest`.

```yaml
# Contenido del archivo .github/workflows/python-app.yml

name: Pruebas de Regresión - Cupones

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Configurar Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Instalar dependencias
        run: |
          python -m venv venv
          source venv/bin/activate
          pip install -r requirements.txt

      - name: Ejecutar pruebas
        run: |
          source venv/bin/activate
          pytest
```

---

## Dependencias

Las dependencias del proyecto se listan en el archivo `requirements.txt`:

```
Flask==2.2.3
python-dotenv==1.0.0
pytest==7.3.1
```

---

## Contacto

Si tienes dudas o quieres aportar al proyecto, contáctame en:

* **Email**: tu.email@ejemplo.com
* **GitHub**: https://github.com/tuusuario

---

## Licencia

Este proyecto está bajo **Licencia MIT**. Consulta el archivo `LICENSE` para más detalles.
```
