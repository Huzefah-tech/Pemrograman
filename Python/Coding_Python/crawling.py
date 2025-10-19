import requests
from bs4 import BeautifulSoup
import pandas as pd

#URL target (misalnya detik news)
url = 'https://books.toscrape.com/catalogue/page-1.html'

#Ambil konten HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#Cari elemen berita
berita_list = soup.find_all('article')

data = []
for berita in berita_list:
  #ambil judul
    judul = berita.get_text(strip=True)
    #ambil link
    link = berita.find('a')['href'] if berita.find('a') else None
    #print(judul, link
    data.append({'Judul': judul, 'Link': link})

# Simpan ke DataFrame
df = pd.DataFrame(data)

# Tampilkan hasil
print(df.head())

# Simpan ke CSV
df.to_csv('hasil_crawling.csv', index=False, encoding="utf-8-sig")

# Simpan ke Excel
df.to_excel('hasil_crawling.xlsx', index=False, engine='openpyxl')

print('Data berhasil disimpan ke hasil_crawling.csv dan hasil_crawling.xlsx')