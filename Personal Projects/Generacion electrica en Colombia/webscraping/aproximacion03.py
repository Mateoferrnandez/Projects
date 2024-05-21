import requests
from bs4 import BeautifulSoup
import time
urls = ['https://origin.cpc.ncep.noaa.gov/products/analysis_monitoring/ensostuff/ONI_v5.php']
archivo_datos = 'datos_extraidos.txt'
with open(archivo_datos, 'w', encoding='utf-8') as file:
    for url in urls:
        try:
            result = requests.get(url)
            if result.status_code == 200:
                soup = BeautifulSoup(result.text, 'lxml')
                titulo = soup.find('title').get_text(strip=True)
                file.write(titulo + '\n')
            else:
                print(f'Error al acceder a {url}: Código de estado {result.status_code}')
                time.sleep(1)
        except Exception as e:
            print(f'Ocurrió un error al procesar {url}: {e}')
print(f'Datos extraídos correctamente en {archivo_datos}')