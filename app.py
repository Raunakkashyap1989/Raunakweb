from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head><title>Raunak Web</title>
    <style>
        body{font-family:Arial; text-align:center; padding:50px; background:#f0f8ff}
        h1{color:#4a00e0}
        .box{background:white; padding:30px; border-radius:15px; box-shadow:0 5px 15px rgba(0,0,0,0.1); display:inline-block}
    </style>
    </head>
    <body>
        <div class="box">
            <h1>🚀 Raunakweb Live Hai!</h1>
            <p>Namaste, main Raunak Kashyap!</p>
            <p>Website successfully deployed on Render.</p>
            <p><b>Lucknow, UP</b></p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run()
