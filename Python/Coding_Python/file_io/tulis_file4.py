import csv
siswa = [
  ('Sulbit', 'C', 10),
  ('Nia', 'B', 85),
  ('Noor', 'C', 90)
]

#tentukan lokasi file, nama file dan inisialisasi csv
f = open("siswa.csv", "w")
w = csv.writer(f)
w.writerow(('Nama', 'Kelas', 'Nilai'))

#menulis file csv
for s in siswa:
  w.writerow(s)

  #menutup file csv
  f.close()