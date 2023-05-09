# import urllib library
from urllib.request import urlopen
import json
url1 = "http://dwebkit-api.tk/api/HABT"
url2 = "http://dwebkit-api.tk/api/ALZR"
url3 = "http://dwebkit-api.tk/api/BCRI"
url4 = "http://dwebkit-api.tk/api/CPFF"
url5 = "http://dwebkit-api.tk/api/CPTS"
url6 = "http://dwebkit-api.tk/api/DEVA"
# response URL
response1 = urlopen(url1)
response2 = urlopen(url2)
response3 = urlopen(url3)
response4 = urlopen(url4)
response5 = urlopen(url5)
response6 = urlopen(url6)
  
# JSON response 
data1 = json.loads(response1.read())
data3 = json.loads(response3.read())
data2 = json.loads(response2.read())
data4 = json.loads(response4.read())
data5 = json.loads(response5.read())
data6 = json.loads(response6.read())

#print(data["ultimoRendimento"]['dataBase'])
print(data2)

if (data3["valorAtual"] < data3["valorPatrimonioPCota"]):
  status3 = "COMPRAR"
else:
  status3 = "AGUARDAR"
if (data2["valorAtual"] < data2["valorPatrimonioPCota"]):
  status2 = "COMPRAR"
else:
  status2 = "AGUARDAR"
if (data1["valorAtual"] < data1["valorPatrimonioPCota"]):
  status1 = "COMPRAR"
else:
  status1 = "AGUARDAR"
if (data4["valorAtual"] < data4["valorPatrimonioPCota"]):
  status4 = "COMPRAR"
else:
  status4 = "AGUARDAR"
if (data4["valorAtual"] < data4["valorPatrimonioPCota"]):
  status4 = "COMPRAR"
else:
  status4 = "AGUARDAR"
if (data5["valorAtual"] < data5["valorPatrimonioPCota"]):
  status5 = "COMPRAR"
else:
  status5 = "AGUARDAR"
if (data6["valorAtual"] < data6["valorPatrimonioPCota"]):
  status6 = "COMPRAR"
else:
  status6 = "AGUARDAR"
f = open("fii.csv", "a")
f.write(data3["fundo"] + "," + str(data3["dividendYield"]) + "," + str(data3["valorAtual"]) + "," + str(data3["valorPatrimonioPCota"]) + "," + str(data3["ultimoRendimento"]["rendimento"]) + "," + status3 + "\n")

f.write(data1["fundo"] + "," + str(data1["dividendYield"]) + "," + str(data1["valorAtual"]) + "," + str(data1["valorPatrimonioPCota"]) + "," + str(data1["ultimoRendimento"]["rendimento"]) + "," + status1 + "\n")

f.write(data2["fundo"] + "," + str(data2["dividendYield"]) + "," + str(data2["valorAtual"]) + "," + str(data2["valorPatrimonioPCota"]) + "," + str(data2["ultimoRendimento"]["rendimento"]) + "," + status2 + "\n")

f.write(data4["fundo"] + "," + str(data4["dividendYield"]) + "," + str(data4["valorAtual"]) + "," + str(data4["valorPatrimonioPCota"]) + "," + str(data4["ultimoRendimento"]["rendimento"]) + "," + status4 + "\n")

f.write(data5["fundo"] + "," + str(data5["dividendYield"]) + "," + str(data5["valorAtual"]) + "," + str(data5["valorPatrimonioPCota"]) + "," + str(data5["ultimoRendimento"]["rendimento"]) + "," + status5 + "\n")

f.write(data6["fundo"] + "," + str(data6["dividendYield"]) + "," + str(data6["valorAtual"]) + "," + str(data6["valorPatrimonioPCota"]) + "," + str(data6["ultimoRendimento"]["rendimento"]) + "," + status6 + "\n")
f.close()