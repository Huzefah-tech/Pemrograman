#Membuat Dictionary
my_dict = {
  'nama': 'Huzefah',
  'umur': 20,
  'pekerjaan': 'Programmer',
  'kota': 'Jakarta',
}

#Mengakses nilai dari Dictionary
print("Nama:", my_dict['nama'])

#Menambah elemen ke Dictionary
my_dict['kota'] = 'Jakarta'

my_dict['nim1'] ='2513000020'
my_dict['nama1'] = 'Raja'
my_dict['alamat1'] = 'batang kuis'
my_dict['umur1'] = 20

my_dict['nim2'] ='2513000032'
my_dict['nama2'] = 'Najwa'
my_dict['alamat2'] = 'Martubung'
my_dict['umur2'] = 19

my_dict['nim3'] ='2513000010'
my_dict['nama3'] = 'Hafiz'
my_dict['alamat3'] = 'Mabar psr 3'
my_dict['umur3'] = 18

my_dict['nim4'] ='2513000046'
my_dict['nama4'] = 'Razzaq'
my_dict['alamat4'] = 'Marelan psr 3 barat'
my_dict['umur4'] = 18

my_dict['nim5'] ='2513000001'
my_dict['nama5'] = 'Adel'
my_dict['alamat5'] = 'Marelan'
my_dict['umur5'] = 18

my_dict['nim6'] ='2513000146'
my_dict['nama6'] = 'Krispinus'
my_dict['alamat6'] = 'Belawan'
my_dict['umur6'] = 18

my_dict['nim7'] ='2513000043'
my_dict['nama7'] = 'Bila'
my_dict['alamat7'] = 'Tj. Mulia'
my_dict['umur7'] = 19

my_dict['nim8'] ='2513000141'
my_dict['nama8'] = 'Nazwa'
my_dict['alamat8'] = 'Gg. Paniters'
my_dict['umur8'] = 18

my_dict['nim9'] ='2513000048'
my_dict['nama9'] = 'Wirda'
my_dict['alamat9'] = 'Marelan'
my_dict['umur9'] = 19

my_dict['nim10'] ='2513000015'
my_dict['nama10'] = 'Dinda'
my_dict['alamat10'] = 'Mabar'
my_dict['umur10'] = 18

print("Dictionary setelah penambahan:", my_dict)

#Menghapus elemen dari Dictionary
del my_dict['pekerjaan']
print("Dictionary setelah penghapusan:", my_dict)

#Mengakses semua kunci dan nilai
for key, value in my_dict.items():
  print(f"{key}: {value}")