# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:12:41 2020

@author: josfe
"""

import time

def cargaPalabras():
    archivo = open('words.txt', 'r')
    renglon = archivo.readline()
    archivo.close()
    palabras = renglon.split()
    print (len(palabras), 'palabras leidas')
    return palabras

def descifraSustituye(cad, llave):
    texto = ""
    alfabeto="abcdefghijklmnopqrstuvwxyz"
    for e in cad:
        if (e in alfabeto):
            pos = llave.find(e)
            if (pos>0):
                texto = texto + alfabeto[pos]
            else:
                texto = texto + "X"
        else:
            texto = texto + e
    return texto

def getAciertos(listaPalabras, diccionario):
    numAciertos = 0
    for pal in listaPalabras:
        if pal in diccionario:
            numAciertos = numAciertos + 1            
    return numAciertos

def armaLlave(alfabeto, cad, posibles):
    llave = ""
    p=0
    for i in range(len(alfabeto)):
        if (alfabeto[i] in posibles):
            pos = posibles.index(alfabeto[i])
            llave = llave + cad[pos]
            p = p + 1
        else:
            llave = llave + "X"
    return llave


arch = open("cifrado.txt", "r")
texto = arch.read()
arch.close()
dic1 = cargaPalabras()
alfabeto="abcdefghijklmnopqrstuvwxyz"
inicio = time.time()
masUsadasEng = "etaonihsrlducmw"
mejorCad="lxczdkvwbt"
aciertos = 0
maxAciertos = 0
c = 0
for c1 in "e":    
    for c2 in (set(masUsadasEng[1:4])-set(c1)):        
        for c3 in (set(masUsadasEng[1:5])-set([c1, c2])):            
            for c4 in (set(masUsadasEng[1:6])-set([c1, c2, c3])):
                fin = time.time()
                print(fin-inicio, "segundos")
                print("llevamos "+str((c*100)/(26))+"%  del problema")
                c = c + 1
                for c5 in (set(masUsadasEng[2:8])-set([c1, c2, c3, c4])):
                    for c6 in (set(masUsadasEng[3:9])-set([c1, c2, c3, c4, c5])):
                        for c7 in (set(masUsadasEng[4:10])-set([c1, c2, c3,c4,c5,c6])):
                            for c8 in (set(masUsadasEng[5:11])-set([c1, c2, c3,c4,c5,c6,c7])):
                                for c9 in (set(masUsadasEng[6:12])-set([c1,c2,c3,c4,c5,c6,c7,c8])):
                                    for c10 in (set(masUsadasEng[6:12])-set([c1,c2,c3,c4,c5,c6,c7,c8,c9])):
                                        posibles = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]                            
                                        llave = armaLlave(alfabeto, mejorCad, posibles)
                                        claro = descifraSustituye(texto, llave)
                                        claro2 = claro.split()
                                        aciertos = getAciertos(claro2, dic1)
                                        if (aciertos>maxAciertos):
                                            maxAciertos = aciertos
                                            mejorLlave = llave
                                            print("aciertos", aciertos)
                                            print("llave: ", llave)
                                            print (claro)
fin = time.time()
print(fin-inicio)




