# LectorArchivo

Este proyecto permite analizar y consultar información sobre licitaciones públicas a partir de un archivo CSV.

## Estructura del proyecto

- `app.py`: Script principal para procesar y analizar los datos.
- `Licitaciones.csv`: Archivo de datos con información de licitaciones públicas.  
  Columnas:  
  - `id`: Identificador único  
  - `entidad`: Entidad responsable  
  - `descripcion`: Descripción de la licitación  
  - `monto`: Monto adjudicado  
  - `tipo`: Tipo de licitación  
  - `fecha`: Fecha de la licitación

## Requisitos

- Python 3.x

## Uso

1. Clona este repositorio o descarga los archivos.
2. Instala las dependencias necesarias (si las hay).
3. Ejecuta el script principal:

   ```sh
   python app.py
   ```

4. Sigue las instrucciones en consola para consultar o analizar los datos.

## Personalización

Puedes modificar `app.py` para realizar análisis específicos, como:
- Filtrar licitaciones por entidad, tipo o fecha.
- Calcular montos totales por categoría.
- Buscar descripciones específicas.

## Licencia

Este proyecto es de uso libre para fines educativos y de análisis de