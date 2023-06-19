#from https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html
import cv2 #pra leitura da imagem
import numpy as np #redução da escrita numpy para np
#caso for usar o Google Colab com a OpenCV, usar a lib abaixo
from google.colab.patches import cv2_imshow #utilização da função cv2_imshow do google colab

img = cv2.imread('j.png',0) #função da leitura da imagem
img_opening = cv2.imread('j_ruido.png',0) #retirar pequenos ruidos da imagem, passagem da erosão pra dilatação
img_closing = cv2.imread('j_furos.png',0) #dilata a imagem para que os furos preencham o j, e erode para voltar ao j sem furos
altura, largura = img.shape #dimensões da imagem usando ".shape" e armazenamento nas variáveis
kernel = np.ones((5,5),np.uint8) #matriz do kernel 5x5 preenchido por 1 e indicação de valores inteiros sem sinal de 8 bits
print(kernel) #apresenta o kernel para visualização

erosion = cv2.erode(img,kernel,iterations = 2) #aplica a erosão usando o kernel e o "iterations" corresponde a quantidade de vezes que a erosão é utilizada. resultado armazenado na variavel "erosion"
dilation = cv2.dilate(img,kernel,iterations = 2) #mesma aplicação, apenas usando a função "dilation"

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel) #a função gradiente destaca os contornos da imagem, subtração da imagem dilatada com a erodida. nesta função ele aplica utilizando a variavel kernel e armazena na variavel "gradient"
opening = cv2.morphologyEx(img_opening, cv2.MORPH_OPEN, kernel) #função de abertura da erosão pra dilatação utilizando o kernel, armazenando na variavel "opening"
closing = cv2.morphologyEx(img_closing, cv2.MORPH_CLOSE, kernel) #função de abertura da dilatação pra erosão utilizando o kernel, armazenando na variavel "closing"

cv2_imshow(img) #exibe imagem inicial sem modificações
cv2_imshow(erosion) #exibe a imagem com efeito de erosão
cv2_imshow(dilation) #exibe a imagem com efeito da dilatação
cv2_imshow(opening) #exibe a imagem com efeito de abertura
cv2_imshow(closing) #exibe a imagem com efeito de fechamento
cv2_imshow(gradient) #exibe a imagem com efeito de gradiente
