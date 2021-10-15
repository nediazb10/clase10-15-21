from flask import Flask, render_template, request, jsonify
import db
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def validar():
    usuario=request.form['usuario']
    password=request.form['contraseña']
    if validarUserPass(usuario,password):
        return jsonify({'mensaje': 'Usuario registrado'})
    else:
        return jsonify({'mensaje': 'Usuario no valido'})

def validarUserPass(usuario,contraseña):
    conexion=db.get_db()
    strsql="SELECT * FROM usuario WHERE usuario = '{}' and contraseña = '{}'".format(usuario, contraseña)
    # strsql="SELECT * FROM usuario WHERE usuario = '"+usuario+"' and contraseña = '"+contraseña+"'
    cursor=conexion.cursor()
    cursor.execute(strsql)
    datos=cursor.fetchall()
    if datos:
        return True
    else:
        return False
