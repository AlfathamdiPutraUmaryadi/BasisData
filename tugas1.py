#pengimportan module
import pandas as pd
import io
from google.colab import files

#import data json dari github
!wget -O file.json https://raw.githubusercontent.com/AlfathamdiPutraUmaryadi/BasisData/main/dataTest.json

# Membuat variable global untuk data json yang ingin diproses
file_path = 'file.json' 

# mengambil data jsonnya
with open(file_path, 'r') as file:
    data_tugas1 = json.load(file) #membuat nama variabel gobalnya menjadi data_tugas1

#gambaran datanya
data_tugas1 

#cara pertama
def see_cordinates(border_name):
  for i in range(len(data_tugas1)):
    if border_name == data_tugas1[i]["name"]:
      for j in range(len(data_tugas1[i]["coordinates"])):
        print(" ".join(map(str, data_tugas1[i]["coordinates"][j])),end=", ")
  return None

see_cordinates("border_2")

#cara kedua
def see_cordinates2(border_name):
  for i in range(len(data_tugas1)):
    if border_name == data_tugas1[i]["name"]:
       b = int(len(data_tugas1[i]["coordinates"]))
       c = data_tugas1[i]["coordinates"]
       for j in range(b):
         for k in range(2):
           print(c[j][k], end= " ")
         print(",",end= " ")

see_cordinates2("border_2")
