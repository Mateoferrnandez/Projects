import requests
url = 'https://origin.cpc.ncep.noaa.gov/products/analysis_monitoring/ensostuff/ONI_v5.php'
response = requests.get(url)
if response.status_code == 200:
    with open('pagina_descargada.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
    print('HTML guardado en: "pagina_descargada.html"')
else:
    print('Error al hacer la solicitud:', response.status_code)