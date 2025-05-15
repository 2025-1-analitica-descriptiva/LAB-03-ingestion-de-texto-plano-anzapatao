"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.
    """
    import pandas as pd
    import re
    
    # Leer el archivo como texto
    with open('files/input/clusters_report.txt', 'r') as file:
        lines = file.readlines()
    
    # Ignorar líneas iniciales hasta llegar al separador
    start_index = 0
    for i, line in enumerate(lines):
        if '-' * 10 in line:  # Buscar la línea de separación
            start_index = i + 1
            break
    
    # Preparar listas para cada columna
    clusters = []
    cantidad_palabras = []
    porcentaje_palabras = []
    palabras_clave = []
    
    # Procesar cada cluster
    i = start_index
    while i < len(lines):
        if lines[i].strip():  # Si la línea no está vacía
            # Extraer número de cluster, cantidad y porcentaje
            match = re.match(r'\s*(\d+)\s+(\d+)\s+(\d+,\d+|\d+\.\d+)\s*%\s*(.*)', lines[i].strip())
            if match:
                cluster, cantidad, porcentaje_str, palabras_inicio = match.groups()
                clusters.append(int(cluster))
                cantidad_palabras.append(int(cantidad))
                
                # Convertir porcentaje (maneja tanto comas como puntos)
                porcentaje = porcentaje_str.replace(',', '.')
                porcentaje_palabras.append(float(porcentaje))
                
                # Iniciar la colección de palabras clave
                palabras_texto = palabras_inicio.strip()
                
                # Continuar leyendo líneas para palabras clave hasta línea vacía o nuevo cluster
                j = i + 1
                while j < len(lines) and not re.match(r'\s*\d+\s+\d+', lines[j]) and lines[j].strip():
                    palabras_texto += " " + lines[j].strip()
                    j += 1
                
                # Limpiar y formatear las palabras clave
                palabras_texto = re.sub(r'\s+', ' ', palabras_texto)  # Eliminar espacios múltiples
                palabras_texto = re.sub(r'\s*,\s*', ', ', palabras_texto)  # Formatear comas
                if palabras_texto.endswith('.'):
                    palabras_texto = palabras_texto[:-1]  # Eliminar punto final si existe
                
                palabras_clave.append(palabras_texto)
                
                # Actualizar el índice para continuar desde donde terminamos
                i = j
            else:
                i += 1
        else:
            i += 1
    
    # Crear el dataframe
    df = pd.DataFrame({
        'cluster': clusters,
        'cantidad_de_palabras_clave': cantidad_palabras,
        'porcentaje_de_palabras_clave': porcentaje_palabras,
        'principales_palabras_clave': palabras_clave
    })
    
    return df

if __name__ == "__main__":
  # Test the function
  df = pregunta_01()
  print(df.head())