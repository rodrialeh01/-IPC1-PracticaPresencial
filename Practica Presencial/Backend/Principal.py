from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

#ANALISIS LEXICO
@app.route('/Analisis', methods=['POST'])
def AnalisisLexico():
    frase = request.json['frase']
    #cuenta las palabras
    palabras = len(frase.split())
    #contador de vocales
    contadorv = 0
    #contador de consonantes y signos
    contadorc = 0
    #Contador de vocales y consonantes
    for vocal in frase:
        if vocal == "a":
            contadorv +=1
        elif vocal == "e":
            contadorv +=1
        elif vocal =="i":
            contadorv +=1
        elif vocal =="o":
            contadorv +=1
        elif vocal =="u":
            contadorv +=1
        elif vocal =="A":
            contadorv +=1
        elif vocal =="E":
            contadorv +=1
        elif vocal =="I":
            contadorv +=1
        elif vocal =="O":
            contadorv +=1
        elif vocal =="U":
            contadorv +=1
        elif vocal !=" ":
            contadorc +=1
    return(jsonify({
        'palabras': palabras,
        'vocales': contadorv,
        'consonantes': contadorc
    }))

#NUMEROS PRIMOS
@app.route('/NumerosPrimos', methods=['POST'])
def NPrimos():
    inferior = int(request.json['inferior'])
    superior = int(request.json['superior'])
    contadorp = 0
    for n in range(inferior,superior):
        if Primos(n) == True:
            contadorp+=1
    return(jsonify({
        'primos': contadorp
    }))

#Funcion para numeros primos
def Primos(numero):
    if numero<2:
        return False
    for num in range(2,numero):
        if numero%num == 0:
            return False
    return True


#CALCULADORA
@app.route('/Calculadora', methods=['POST'])
def Calculadora():
    numero1 = request.json['numero1']
    numero2 = request.json['numero2']
    signo = request.json['signo']
    if(signo =="+"):
        resultado = int(numero1) + int(numero2)
        return(jsonify({
            'resultado': resultado
        }))
    elif(signo == "-"):
        resultado = int(numero1) - int(numero2)
        return(jsonify({
            'resultado': resultado
        }))
    elif(signo == "*"):
        resultado = int(numero1) * int(numero2)
        return(jsonify({
            'resultado': resultado
        }))
    elif(signo == "/"):
        if(int(numero2) == 0):
            return(jsonify({
                'resultado': 'No se puede dividir con 0'
            }))
        else:
            resultado = int(numero1) / int(numero2)
            return(jsonify({
            'resultado': resultado
        }))

#Hace que se levante la api que se esta creando
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)