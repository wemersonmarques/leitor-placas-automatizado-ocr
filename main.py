import cv2
import pytesseract
from PIL import Image
import numpy as np
from os import listdir
from os.path import isdir

def suavizarImagem(img):
    ret1, th1 = cv2.threshold(img, 88, 255, cv2.THRESH_BINARY)
    ret2, th2 = cv2.threshold(th1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    blur = cv2.GaussianBlur(th2, (5, 5), 0)
    ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return th3

def tratarImagemPlaca(img):
    filtered = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 41)
    kernel = np.ones((1, 1), np.uint8)
    opening = cv2.morphologyEx(filtered, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    img = suavizarImagem(img)
    or_image = cv2.bitwise_or(img, closing)
    return or_image

def tratarImagemCompleta(imagem):
    # Tratar imagem

    ## Colocar a imagem em escala de Cinza
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('cinza', cinza)

    ## Binarizar a imagem

    _, bin = cv2.threshold(cinza, 90, 255, cv2.THRESH_BINARY)
    # cv2.imshow('bin', bin)

    return bin

def identificarContornos(imagem):
    # Identificando contornos
    contornos, hier = cv2.findContours(imagem, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    return contornos

def identificarPossiveisPlacas(contornos, imagem):
    possiveisPlacas = list()

    for contorno in contornos:
        perimetro = cv2.arcLength(contorno, True)
        aprox = cv2.approxPolyDP(contorno, 0.03 * perimetro, True)

        if (perimetro > 120):
            if len(aprox) == 4:
                (x, y, altura, largura) = cv2.boundingRect(contorno)
                cv2.rectangle(imagem, (x, y), (x + altura, y + largura), (0, 255, 0), 2)

                placa = imagem[y:y + largura, x:x + altura]
                possiveisPlacas.append(placa)

    return possiveisPlacas

def identificarPlaca(possiveisPlacas):
    placaIdentificada = ''

    for placa in possiveisPlacas:
        placaTratada = tratarImagemPlaca(placa)
        valorSaida = pytesseract.image_to_string(Image.fromarray(placaTratada))
        valorSaida = removerCaracteresIndesejados(valorSaida)

        if (len(valorSaida) > 0):
            cv2.imshow('img', placa)
            placaIdentificada = valorSaida

    if (placaIdentificada != ''):
        print('Placa identificada: {}'.format(placaIdentificada))
    else:
        print('Não foi possível identificar placa na imagem requisitada!')

def removerCaracteresIndesejados(string):
    str = "!@#%¨&*()_+:;><^^}{`?|~¬/=,.'ºª»‘\f"
    for x in str:
        string = string.replace(x, '')
    return string

if __name__ == '__main__':
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    pathPrincipal = 'imagens'

    for file in listdir(pathPrincipal):
        print('-------------')
        path = pathPrincipal + "\\" + file
        print('Arquivo: {}'.format(path))

        if isdir(path):
            continue

        imagemCompletaTratada = tratarImagemCompleta(cv2.imread(path))
        contornosImagemCompleta = identificarContornos(imagemCompletaTratada)
        possiveisPlacas = identificarPossiveisPlacas(contornosImagemCompleta, imagemCompletaTratada)

        identificarPlaca(possiveisPlacas)
        print('-------------')

        cv2.waitKey(0)
        cv2.destroyAllWindows()
