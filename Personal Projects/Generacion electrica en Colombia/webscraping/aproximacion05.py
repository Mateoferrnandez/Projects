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
            count=0
            if num_tablas < 12:
                if count ==0:
                    tabla = tablas[0]
                    csv_file_name = f'datos_extraidos_{url.split("/")[-1].replace("/", "_")}.csv'
                    with open(csv_file_name, 'w', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        headers = [th.get_text(strip=True) for th in tabla.find_all('th')]
                        writer.writerow(headers)
                        for fila in tabla.find_all('tr'):
                            celdas = fila.find_all('td')
                            if celdas:
                                row_data = [td.get_text(strip=True) for td in celdas]
                                writer.writerow(row_data)
                                print(f'Datos de la tabla exportados correctamente a {csv_file_name}')
        else:
            print(f'Error al acceder a {url}: Código de estado {response.status_code}')
            time.sleep(1)
    except Exception as e:
        print(f'Ocurrió un error al procesar {url}: {e}')