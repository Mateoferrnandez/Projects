import requests
from bs4 import BeautifulSoup
response = requests.get('https://origin.cpc.ncep.noaa.gov/products/analysis_monitoring/ensostuff/ONI_v5.php')
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    titulo = soup.find('title')
    if titulo:
        titulo_texto = titulo.get_text()
        print('El título de la página es:', titulo_texto)
    else:
        print('No se encontró ningún título en la página.')
else:
    print('No se pudo acceder a la página. Código de estado:', response.status_code)