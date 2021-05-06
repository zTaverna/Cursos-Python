import requests as req

PngData = req.get("https://www.dw.com/image/19077838_303.jpg").content

Arquivo = open("C:\\Users\\lucas\\OneDrive\\Desktop\\LPII\\Aula 10\\Marx.png", "wb")
Arquivo.write(PngData)
Arquivo.close()