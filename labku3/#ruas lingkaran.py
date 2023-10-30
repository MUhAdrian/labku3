#ruas lingkaran
print('##  Program Python Menghitung Luas Lingkaran  ##')
print('================================================')
print()
 
def hitungLuasLingkaran(r):
  return round(3.14 * r * r, 2)
 
jari2 = float(input('Input jari-jari lingkaran:  '))
print('Luas lingkaran = ',hitungLuasLingkaran(jari2))