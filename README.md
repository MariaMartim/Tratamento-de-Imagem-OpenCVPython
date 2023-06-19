Neste código usamos as bibliotecas do cv2 para a leitura e manipulação das imagens e numpy para trabalharmos com matrizes no kernel. Este repositório trabalhou com os efeitos de manipulação de imagens do OpenCV como a abertura, fechamento, gradiente, erosão e dilatação. Com isso, usamos a imagem de um "J" para reformá-la, com exemplos de furos e ruídos, arrumando elas com os efeitos de fechamento e abertura respectivamente. Logo após resolver os erros nas imagens, formamos a matriz do kernel 5x5 para a leitura das imagens e seguimos usando nas funções de modificações de imagens, porém agora usando erosão e dilatação. Na linha 14 e 15, aplicamos juntamente aos efeitos o kernel 5x5 e iterations indicando a quantidade de vezes que a função será aplicada e armazenando respectivamente em "erosion" e "dilation". Seguindo para as linhas 17 à 19, as funções gradiente, abertura e fechamento sao aplicadas respectivamentes juntamente ao kernel e guardadas nas variáveis "gradient", "opening" e "closing", como feito anteriormente. Finalizando o código, da linha 21 à 26, há apresentação das imagens com sua respectiva função aplicada, começando com a imagem original, seguindo com os exemplos de erosão, dilatação, abertura, fechamento e gradiente.
