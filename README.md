# Proyecto Cupones de Descuento - Flask

[![Pruebas de Regresión - Cupones](https://github.com/tuusuario/cupones_descuento/actions/workflows/python-app.yml/badge.svg)](https://github.com/tuusuario/cupones_descuento/actions/workflows/python-app.yml)

## 📝 Descripción del Proyecto

Este repositorio contiene el código fuente de una aplicación web desarrollada con **Flask** que permite aplicar **descuentos mediante cupones promocionales** y calcular el precio final de un producto, incluyendo los impuestos.

El objetivo principal de este proyecto es servir como una herramienta sencilla para practicar el **desarrollo web con Python y Flask**, la **integración con tests automatizados** y el **despliegue continuo (CI/CD)**, asegurando que la lógica de negocio esté bien probada y sea robusta.

## ✨ Características Principales

* **Gestión de Cupones:** Aplicación de descuentos basados en códigos de cupón definidos.
* **Cálculo de Precio Final:** Incorporación de impuestos al precio base después de aplicar descuentos.
* **API RESTful (Opcional):** Preparado para la futura implementación de APIs si se requiere interacción programática.
* **Desarrollo Guiado por Pruebas (TDD):** Lógica principal cubierta por tests unitarios usando `pytest`.
* **Integración Continua (CI):** Automatización de pruebas con GitHub Actions en cada cambio de código.

## 🚀 Tecnologías Utilizadas

* **Python 3.10+**
* **Flask**: Micro-framework para la construcción de la aplicación web.
* **pytest**: Framework de pruebas para Python.
* **virtualenv (o venv)**: Para la gestión de entornos virtuales.
* **Git & GitHub:** Control de versiones y alojamiento del repositorio.
* **GitHub Actions:** Para la automatización de CI (pruebas).
* **Otros paquetes de Python** listados en `requirements.txt`.

## 🛠️ Estructura del Proyecto

La estructura del proyecto sigue una organización clara para facilitar el desarrollo y mantenimiento:

cupones_descuento/
├── app/
│   ├── init.py         # Inicialización de la aplicación Flask
│   ├── api.py              # (Opcional) Módulo para futuras APIs REST
│   ├── cupones.py          # Lógica principal para la aplicación de cupones y cálculo de precios
│   ├── models.py           # Definición de modelos (en caso de usar bases de datos)
│   └── routes.py           # Definición de rutas Flask y manejo de las vistas
├── tests/
│   ├── init.py
│   └── test_cupones.py     # Contiene los tests unitarios para la lógica de descuentos
├── run.py                  # Script para iniciar la aplicación Flask
├── requirements.txt        # Lista de dependencias del proyecto
├── pytest.ini              # Archivo de configuración para pytest
└── .github/
└── workflows/
└── python-app.yml  # Configuración de GitHub Actions para Integración Continua (CI)

## ⚙️ Configuración y Ejecución Local

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local.

### Prerrequisitos

Asegúrate de tener instalado:
* [Python 3.10 o superior](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads)

### Pasos

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL_DE_TU_REPOSITORIO> # Reemplaza con la URL de tu repositorio
    cd cupones_descuento              # Navega a la raíz del repositorio
    ```

2.  **Crear y activar un entorno virtual:**
    Es una buena práctica aislar las dependencias del proyecto.
    ```bash
    python -m venv venv
    source venv/bin/activate # En Linux/macOS
    # O para Windows: .\venv\Scripts\activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar Clave Secreta (Opcional, pero recomendado):**
    Para la gestión de sesiones y seguridad de Flask, se recomienda definir una clave secreta. Puedes generar una ejecutando lo siguiente en tu terminal Python:
    ```python
    import secrets
    print(secrets.token_hex(32))
    ```
    Luego, en `app/__init__.py` o donde inicialices la aplicación, configura:
    ```python
    from flask import Flask

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'TU_CLAVE_SECRETA_AQUI' # Reemplaza con la clave generada
    ```

5.  **Ejecutar la aplicación:**
    Desde la raíz del proyecto (`cupones_descuento`), ejecuta:
    ```bash
    python run.py
    ```
    La aplicación estará disponible en `http://localhost:5000/` y mostrará un mensaje simple confirmando que el proyecto está en ejecución.

## 🧪 Lógica de Cupones y Tests

### Lógica de Cupones

El archivo `app/cupones.py` contiene la función principal para aplicar descuentos y calcular el precio final con impuesto:

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

