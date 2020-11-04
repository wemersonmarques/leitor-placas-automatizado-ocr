# Leitor de Placas Veiculares Automatizado

O Leitor de Placas Veiculares Automatizado (ANPR) é um software responsável por fazer a leitura imagens de veículos, identificar a sua placa e traduzir seus caracteres (imagem) para a caracteres de linguagem de máquina (char).

## Tecnologias
1. OpenCV2 -> Provê as funções necessárias para realizar operações com imagens. Foi utilizado principalmente no processo de Tratamento de Imagens, que está listado a seguir. 
2. Tesseract OCR -> Provê a tecnologia necessária, baseada em Inteligência Artificial, para a conversão de uma imagem que contém caracteres para caracteres entendíveis em linguagem de máquinas. Assim, é feita a conversão de uma imagem (no caso do exemplo, com extensão .JPG) para uma String, contendo todos os caracteres das placas dos veículos.

### Tratamentos das imagens

Para aumentar a acurácia da leitura dos caracteres de imagem e transformação para linguagem de máquinas, através da ferramenta Tesseract OCR, foi necessário realizar um pré-processamento das imagens. Os principais processos deste pré-processamento são:
1. Conversão da imagem para escala de cinza
2. Binarização da imagem para reforçar os traços
3. Aplicação de *Gaussian Blur*

## Identificadores

Trabalho desenvolvido para a disciplina de Tópicos Especiais em Inteligência Artificial do Instituto Federal de Goiás (IFG), no segundo semestre de 2020.

Professor: Eduardo Noronha

Aluno: Wemerson da Silva Marques

Matrícula: 20171011090140

## Como executar?

Após clonar o repositório, deve ser executado o arquivo *main.py*. Assim, serão exibidos os resultados do processamento das imagens que estão na pasta /imagens no console. 
