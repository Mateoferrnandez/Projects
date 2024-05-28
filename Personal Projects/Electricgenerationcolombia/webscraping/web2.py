import requests
from bs4 import BeautifulSoup
import csv
import time

urls = ['https://origin.cpc.ncep.noaa.gov/products/analysis_monitoring/ensostuff/ONI_v5.php']

for url in urls:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            tablas = soup.find_all('table')
            num_tablas = len(tablas)
            print(f'La página {url} contiene {num_tablas} tablas.')

           
            for i, tabla in enumerate(tablas):
                print(f'\nTabla {i + 1} - Primeras filas:')
                for fila in tabla.find_all('tr')[:5]:  # Mostrar solo las primeras 5 filas
                    celdas = [td.get_text(strip=True) for td in fila.find_all('td')]
                    print(celdas)
                print('-' * 40)

           
            tabla_index = int(input(f'Ingrese el número de la tabla que desea exportar (1-{num_tablas}): ')) - 1

            if 0 <= tabla_index < num_tablas:
                tabla = tablas[tabla_index]
                csv_file_name = f'datos_extraidos_tabla_{tabla_index + 1}_{url.split("/")[-1].replace("/", "_")}.csv'
                with open(csv_file_name, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    headers = [th.get_text(strip=True) for th in tabla.find_all('th')]
                    if headers:  # Solo escribir encabezados si existen
                        writer.writerow(headers)
                    for fila in tabla.find_all('tr'):
                        celdas = fila.find_all('td')
                        if celdas:
                            row_data = [td.get_text(strip=True) for td in celdas]
                            writer.writerow(row_data)
                    print(f'Datos de la tabla exportados correctamente a {csv_file_name}')
            else:
                print(f'Índice de tabla no válido. Debe estar entre 1 y {num_tablas}.')
        else:
            print(f'Error al acceder a {url}: Código de estado {response.status_code}')
        time.sleep(1)
    except Exception as e:
        print(f'Ocurrió un error al procesar {url}: {e}')
