Neste código usamos as bibliotecas do cv2 para a leitura e manipulação das imagens e numpy para trabalharmos com matrizes no kernel. Este repositório trabalhou com os efeitos de manipulação de imagens do OpenCV como a abertura, fechamento, gradiente, erosão e dilatação. Começamos o código armazenando as imagens em variaveis para depois aplicarmos as funções, guardando a imagem original, com ruidos e furos nas variaveis "img", "img_opening", "img_closing" respectivamente com cada efeito que será aplicado posteriormente. Formamos a matriz do kernel 5x5 para a leitura das imagens e seguimos usando nas funções de modificações de imagens. 
  Na linha 14 e 15, aplicamos na imagem original juntamente aos efeitos o kernel 5x5 e iterations indicando a quantidade de vezes (no caso "=2") que a função será aplicada e armazenando respectivamente em "erosion" e "dilation". Seguindo para as linhas 17 à 19, as funções gradiente, abertura e fechamento sao aplicadas respectivamentes às variaveis "img", "img_opening" e "img_closing", juntamente ao kernel e guardadas nas variáveis "gradient", "opening" e "closing". Finalizando o código, da linha 21 à 26, há apresentação das váriaveis onde as imagens foram armazenadas com sua respectiva função aplicada, começando com a imagem original, seguindo com a demonstração de erosão, dilatação, abertura, fechamento e gradiente.
  O código é extremamente objetivo e indicativo com sua funções, apresentando modelos fáceis de se aplicar
