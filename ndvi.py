import os

diretorio = 'D:/calculo_ndvi/imagens/'

b4Lista = []
b5Lista = []
#Coloca as imagens em listas 
for imagens in os.listdir(diretorio):
    if imagens[len(imagens)-5]=='4':
        b4Lista.append(imagens)
    if imagens[len(imagens)-5]=='5':
        b5Lista.append(imagens)

#Verifica se as imagens foram carregads em pares
if len(b4Lista) == 0:
    print('Arquivo de imagens vazio!')
    exit()
elif len(b4Lista) == len(b5Lista):
    print('Arquivos carregados com sucesso!')
else:
    print('Falou alguma par de imagem')

#Processa e gera as imagens
try:
    for uniao in range(len(b4Lista)):
        dirB4 = diretorio + b4Lista[uniao]
        dirB5 = diretorio + b5Lista[uniao]

        band_red = QgsRasterLayer(dirB4)
        band_nir = QgsRasterLayer(dirB5)

        saida = diretorio  + 'NDVI_'+ str(b4Lista[uniao][:len(b4Lista[uniao])-12]) +'.TIF'
        entradas = []

        red = QgsRasterCalculatorEntry()
        red.ref = 'red@1'
        red.raster = band_red
        red.bandNumber = 1
        entradas.append(red)

        nir = QgsRasterCalculatorEntry()
        nir.ref = 'nir@1'
        nir.raster = band_nir
        nir.bandNumber = 1
        entradas.append(nir)

        calc = QgsRasterCalculator("('nir@1'-'red@1')/('nir@1'+'red@1')", saida, 'GTiff',
                                band_red.extent(), band_red.width(), band_red.height(), entradas)
        calc.processCalculation()
except:
    print('ERRO')
else:
    print('Arquivos gerados com sucesso!')