# Simulaciones de Stir/Shaken en Python

Este repositorio contiene simulaciones en Python que explican el funcionamiento del protocolo Stir/Shaken en el contexto de las telecomunicaciones.

## Stir/Shaken

Stir/Shaken es un conjunto de estándares y protocolos diseñados para combatir el fraude de llamadas telefónicas y la suplantación de identidad (spoofing) en redes telefónicas.

## Simulaciones

Las simulaciones incluidas en este repositorio demuestran los siguientes aspectos clave de Stir/Shaken:

1. **Creación y Codificación de un Pasaporte:** Se crea un pasaporte Stir/Shaken que consta de un encabezado, una carga útil y una firma.

2. **Codificación a JSON y Decodificación:** El pasaporte se codifica en formato JSON para su fácil transporte y almacenamiento, y luego se decodifica para su procesamiento.

3. **Firma y Verificación de la Firma:** Se simula el proceso de firma del pasaporte y su posterior verificación para garantizar la autenticidad de la llamada.

## Ejecución de las Simulaciones

Para ejecutar las simulaciones, simplemente sigue estos pasos:

1. Clona este repositorio a tu máquina local.
```bash
git clone https://github.com/IvonneDuarte/SimulacionLibStir-Shaken.git
```
2. Ejecuta el script principal.
```bash
python stir_shaken_simulaciones.py
```
## Requisitos

Python 3.x
Biblioteca cryptography (puedes instalarla usando pip install cryptography)

## Contribuciones
¡Las contribuciones son bienvenidas! Si encuentras errores o tienes sugerencias de mejora, no dudes en abrir un problema o enviar una solicitud de extracción.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.
