# MLB_H_comparisson
# MLB Teams Hits Comparisson
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.espn.com.mx/beisbol/mlb/estadisticas/equipo/_/vista/batting/tabla/batting/ordenar/hits/dir/desc'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Equipos

eq = soup.find_all('a', class_='AnchorLink')

equipos = list()

for i in eq:
    equipos.append(i.text)
    

ta = list(equipos[23:83])

while '' in ta:
    ta.remove('')
    
#Variable donde estan los equipos
ta

#Encabezado

en = soup.find_all('th', class_='Table__TH')

encabezado = list()

for i in en:
    encabezado.append(i.text)
    
encabezado.remove('POS')

#Variable donde estan los encabezados
encabezado

df = pd.DataFrame({'Equipos': ta,})

