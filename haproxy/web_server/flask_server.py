from flask import Flask, render_template_string, request
import socket

app = Flask(__name__)

@app.route('/')
def home():
    user_name = request.remote_addr  # IP-адрес пользователя
    server_ip = socket.gethostbyname(socket.gethostname())  # IP-адрес сервера
    html = f"""
    <html>
        <head>
            <title>Web Server</title>
        </head>
        <body>
            <h1>Web server {user_name} IP ({server_ip})</h1>
        </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

