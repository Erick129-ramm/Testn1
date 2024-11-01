from flask import Flask, render_template
import mysql.connector as mysqlcon

rest = Flask(__name__)

db = mysqlcon.connect(host="localhost",user="root", password="",database="restaurante_ing")


@rest.route('/')
def index():
   
    return render_template('index.html')

@rest.route('/desayunos')
def desayunos():


    return render_template('desayunos.html')

@rest.route('/comida')
def comida():
    return render_template('comida.html')

@rest.route('/postres')
def postres():
    return render_template('postres.html')

@rest.route('/bebidas')
def bebidas():
    return render_template('bebidas.html')

@rest.route('/carrito')
def carrito():
    return render_template('carrito.html')

if  __name__ == '__main__':
    rest.run()
