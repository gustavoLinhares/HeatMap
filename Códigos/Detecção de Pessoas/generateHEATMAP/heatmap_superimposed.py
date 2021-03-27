import numpy as np
import cv2 #importa o OpenCV
import matplotlib.pyplot as plt

#Função principal HEATMAP
def main():

    img = cv2.imread("imgs/loja1.jpg")
    altura, largura, canais_de_cor = img.shape

    '''
    heatmap = np.array([
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0.3405050,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0.99919313,0,0],
        [0,0,0,0,0.10001,0,1.00000000,0,0],
        [0,1,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0.0001,0,0.5],
        [0,0,0,1,0,0.0001,0.0001,0,0]
    ])
    '''

    #Simulando dados do fluxo do heatmap
    #MATRIZ DOS VALORES DE INTENSIDADE DO HEATMAP iniciando com 0
    heatmap = np.zeros((90,135), dtype=np.float64) # tamanho aproximadamente da metade da imagem

    a = 0
    b = 0

    for i in range(0, 50):
        for j in range(0, 5):
            if i < 2:
                heatmap[(20+i) + a][(55+i) + b] = 0.1
                a = a + 2
                b = b + 1
            if (i >= 2) and (i <= 4):
                heatmap[(20+i) + a][(55+i) + b] = 0.2
                a = a + 2
                b = b + 1
            if (i > 4) and (i <= 6):
                heatmap[(20+i) + a][(55+i) + b] = 0.4
                a = a + 2
                b = b + 1
            if (i > 6) and (i <= 12):
                heatmap[(20+i) + a][(55+i) + b] = 1
                a = a + 2
                b = b + 1
            if (i > 12) and (i <= 18):
                heatmap[(20+i) + a][(55+i) + b] = 0
                a = a + 2
                b = b + 1
            if (i > 18) and (i <= 26):
                heatmap[(20+i) + a][(55+i) + b] = 0.4
                a = a + 2
                b = b + 1
            if (i > 26) and (i <= 30):
                heatmap[(20+i) + a][(55+i) + b] = 0.2
                a = a + 2
                b = b + 1
            if (i > 30) and (i <= 40):
                heatmap[(20+i) + a][(55+i) + b] = 1
                a = a + 2
                b = b + 1
            if (i > 40):
                heatmap[(20+i) + a][(55+i) + b] = 0.2
                a = a + 2
                b = b + 1

        a = 0
        b = 0

    heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0])) #REDIMENSIONA O HEATMAP PARA O TAMANHO DA IMAGEM
    cv2.imshow('Heatmap Redimensionado', heatmap) #MOSTRA O HEATMAP
    heatmap = cv2.applyColorMap(np.uint8(255 * heatmap), cv2.COLORMAP_JET) #MAPEA AS CORES DO HEATMAP NA ESCALA "COLORMAP_JET" ()
                                                                           # COM O HEATMAP COM VALORES ENTRE 0 E 1

    cv2.imshow('Heatmap Escala de COR', heatmap) #MOSTRA O HEATMAP
    altura1, largura1, canais_de_cor1 = heatmap.shape #atribui as variáveis sobre tamanho dO HEATMAP e INTENSIDADE de canais de cor BGR
    print("Dimensões da Imagem: " + str(largura1) + "x" + str(altura1))
    print("Canais de cor: ", heatmap.item(0, 0, 0), heatmap.item(0, 0, 1) ,heatmap.item(0, 0, 2)) #IMPRIME VALOR B, G e R PARA O PIXEL 0x0
                                                                                                  # B = 128 , G = 0, R = 0


    '''Varre toda a imagem do heatmap e onde o pixel é totalmente azul (B = 128 , G = 0, R = 0),
    recebe o pixel correspondente da Imagem "img"
    Onde há variação de cores no heatmap, o valor do pixel é mantido.
    Assim, a nova imagem gerada em "heatmap" é o mapa de calor sobreposto na imagem "img" '''
    for y in range(0, altura):
        for x in range(0, largura):
            if (heatmap.item(y, x, 0) == 128) and (heatmap.item(y, x, 1) == 0) and (heatmap.item(y, x, 2) == 0): #SE PIXEL TOTALMENTE AZUL
                heatmap.itemset((y,x, 0), img.item(y, x, 0))
                heatmap.itemset((y,x, 1), img.item(y, x, 1))
                heatmap.itemset((y,x, 2), img.item(y, x, 2))
            else: #SE PIXEL TEM VARIAÇÃO DE COR
                heatmap.itemset((y,x, 0), heatmap.item(y, x, 0))
                heatmap.itemset((y,x, 1), heatmap.item(y, x, 1))
                heatmap.itemset((y,x, 2), heatmap.item(y, x, 2))

    #superimposed = heatmap * 1 + img
    cv2.imshow('Superimposed', heatmap) #MOSTRA A IMAGEM COM O HEATMAP SOBREPOSTO
    cv2.imwrite("Loja_HeatMap.png", heatmap) #Salva a imagem criando uma nova com nome "Loja_HeatMap", formato ".png" e no caminho de "loja1.jpg"
    #cv2.imshow('New', superimposed)
    cv2.waitKey(0) #Mostra a janela da imagem até que uma tecla seja pressionada


main()
