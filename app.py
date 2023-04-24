from flask import Flask, request, render_template
import requests

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/formulario', methods=['POST'])
def formulario():
    webhook = 'https://discord.com/api/webhooks/1099875025403793449/filhjPEQnSctK1jl7EFTrWyRrTxs4H1oVEFB_5pE8Il0f7NkRiPSXcYldI6eeC0BTmGL'
    
    email = request.form['correo']
    message = request.form['mensaje']
    image = request.files['imagen']
    filename = image.filename 
    image.save('uploads/' + filename) 
    
    discord_message = f"¡Llego un mensaje!\n**Email** {email}\n**Mensaje** {message}\n**Imagen**:"
    
    with open(f'uploads/{filename}', 'rb') as f:
        requests.post(webhook, data={'content': discord_message}, files={'imagen': f})
    
    return 'Datos recibidos con éxito'

if __name__ == '__main__':
    app.run(debug=True)
