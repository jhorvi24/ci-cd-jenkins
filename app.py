#Portafolio que sirve para mostrar los proyecto realizados por un desarrollador software

from flask import Flask, render_template, request
import boto3

app = Flask(__name__)  
app._static_folder = 'static'
ec2 = boto3.resource('ec2')



def get_IP():
    instance_id='i-02a36dea2d0481431'
    instance = ec2.Instance(instance_id)
    public_ip = instance.public_ip_address
    hostname = instance.public_dns_name
    return public_ip, hostname

@app.route('/')
def index():
    ip, hostname  = get_IP()
    return render_template('index.html', IP=ip, HOSTNAME=hostname)

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)