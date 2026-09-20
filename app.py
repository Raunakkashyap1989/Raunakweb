from flask import Flask, request, redirect
from markupsafe import escape
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = "raunak_secret_12345"

# LOCK KA CODE START
PASSWORD = "1989"
from flask import session, redirect, request

@app.before_request
def check_lock():
    if 'logged_in' not in session and request.path != '/login':
        if request.endpoint != 'login':
            return redirect('/login')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form.get('password') == PASSWORD:
            session['logged_in'] = True
            return redirect('/')
        else:
            return "Galat Password! <a href='/login'>Wapas</a>"
    return '''
    <div style="text-align:center;margin-top:100px;font-family:Arial">
    <h2>🔒 Lock Laga Hai</h2>
    <form method="POST">
    <input type="password" name="password" placeholder="Password Dalo (1989)" style="padding:10px">
    <button type="submit" style="padding:10px 20px;background:#4a00e0;color:white;border:none;border-radius:5px">Unlock</button>
    </form></div>
    '''

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/login')
HTML_HEADER = """
<html><head>
<meta name="monetag" content="2a81f580f6fa7a6e264fa7fbb7c73ad5">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Raunak Web</title>
<style>
body{font-family:Arial;background:#0a0a0f;margin:0;padding:0;text-align:center; color:white; overflow-x:hidden}
#matrix{position:fixed;top:0;left:0;width:100%;height:100%;z-index:-1;opacity:0.15}
h1{color:#00ff88;font-size:32px; text-shadow:0 0 10px #00ff88}
.card{background:rgba(255,255,255,0.95);color:#222;padding:20px;border-radius:15px;box-shadow:0 5px 20px rgba(0,255,136,0.3);margin:15px auto;max-width:350px; border:1px solid #00ff88}
.btn{background:#4a00e0;color:white;padding:10px 20px;border:none;border-radius:8px;cursor:pointer;font-weight:bold}
.btn-buy{background:#ff0066;width:100%;margin-top:10px;padding:12px;font-size:16px}
input, select, textarea{padding:12px;width:85%;border-radius:8px;border:1px solid #ccc;margin:8px}
.grid{display:flex;flex-wrap:wrap;justify-content:center}
.price{font-size:24px;color:#00b300;font-weight:bold;margin:10px 0;border:2px dashed #00b300;padding:8px;border-radius:8px;background:#f0fff0}
.text-box{border:2px dashed #ff0066;padding:8px;border-radius:8px;background:#fff0f5;margin:10px 0;color:#333}
.form-card{max-width:600px; background:white; color:#222}
</style></head><body>
<canvas id="matrix"></canvas>
"""

HTML_FOOTER_SCRIPT = """
<script>
// Hacker Matrix Look - Safe animation only
const c=document.getElementById('matrix'), x=c.getContext('2d');
c.width=window.innerWidth; c.height=window.innerHeight;
const chars="01"; const arr=new Array(Math.floor(c.width/15)).fill(1);
setInterval(()=>{
 x.fillStyle="rgba(10,10,15,0.1)"; x.fillRect(0,0,c.width,c.height);
 x.fillStyle="#00ff88"; x.font="15px monospace";
 arr.forEach((y,i)=>{ x.fillText(chars[Math.floor(Math.random()*chars.length)], i*15, y*15);
 if(y*15>c.height && Math.random()>0.975) arr[i]=0; arr[i]++; });
},50);

function buy(plan){ window.location.href = "https://wa.me/917754048502?text=Mujhe " + plan + " chahiye"; }
function makeWeb(){
  let n = document.getElementById('nameInput').value;
  if(n==""){alert("Naam likho");return;}
  document.getElementById('result').innerHTML = "🎉 <b>"+escapeHtml(n)+"</b> ki web: https://"+escapeHtml(n.toLowerCase())+".raunakweb.com";
}
function shortLink(){
  let l = document.getElementById('longUrl').value;
  if(l==""){alert("Link dalo");return;}
  let s = "https://rnk.ly/" + Math.random().toString(36).substring(7);
  document.getElementById('shortResult').innerHTML = "Short: <a href='"+l+"' target='_blank'>"+s+"</a>";
}
function escapeHtml(t){ return t.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }
</script></body></html>
"""

@app.route('/')
def home():
    return HTML_HEADER + """
<h1>Welcome Raunak Web 🚀</h1>

<div class="grid">
  <div class="card"><h3>PLAN 1 - Basic</h3><div class="price">₹ 49</div><div class="text-box">offer chal raha hai aapko sirf login page Ban jaega</div><button class="btn btn-buy" onclick="buy('Plan 1')">Buy Now</button></div>
  <div class="card"><h3>PLAN 2 - Standard</h3><div class="price">₹ 999</div><div class="text-box">phone deta hack</div><button class="btn btn-buy" onclick="buy('Plan 2')">Buy Now</button></div>
  <div class="card"><h3>PLAN 3 - Premium</h3><div class="price">₹ 599</div><div class="text-box">Facebook Page account ben </div><button class="btn btn-buy" onclick="buy('Plan 3')">Buy Now</button></div>
  <div class="card"><h3>PLAN 4 - Pro</h3><div class="price">₹ 399</div><div class="text-box">Location live treck </div><button class="btn btn-buy" onclick="buy('Plan 4')">Buy Now</button></div>
  <div class="card"><h3>PLAN 5 - Ultimate</h3><div class="price">₹ 1499</div><div class="text-box">Website khud ki ban jayegi ir live ho jayegi</div><button class="btn btn-buy" onclick="buy('Plan 5')">Buy Now</button></div>
</div>

<div class="card" style="max-width:600px"><h2>Try Web Free</h2><input id="nameInput" placeholder="Apna naam likho"><br><button class="btn" onclick="makeWeb()">Click karke Web Banao</button><p id="result"></p></div>
<div class="card" style="max-width:600px"><h2>Badi Link ko Chhoti Banao</h2><input id="longUrl" placeholder="Yaha badi link paste karo"><br><button class="btn" onclick="shortLink()">Chhoti Banao</button><p id="shortResult"></p></div>

<div class="card form-card">
<h2>Website Order Form</h2>
<form action="/submit" method="POST">
<input name="naam" placeholder="Naam" required><br>
<input name="phone" placeholder="Phone Number" pattern="[0-9]{10}" required><br>
<input name="pita" placeholder="Pita Ka Naam" required><br>
<textarea name="address" placeholder="Address" required></textarea><br>
<select name="website_type" required>
<option value="">Kis Prakar Ki Website Chahiye?</option>
<option>Business Website</option>
<option>Portfolio</option>
<option>E-commerce</option>
<option>Blog</option>
</select><br><br>
<button type="submit" class="btn btn-buy">Submit Kare - Direct Email Ayega</button>
</form>
</div>

<br><a href="/page2" class="btn" style="text-decoration:none">Next Page 1/2 -></a>
""" + HTML_FOOTER_SCRIPT

@app.route('/submit', methods=['POST'])
def submit():
    naam = escape(request.form.get('naam',''))
    phone = escape(request.form.get('phone',''))
    pita = escape(request.form.get('pita',''))
    address = escape(request.form.get('address',''))
    wtype = escape(request.form.get('website_type',''))

    # Yaha se email aapke Gmail par jayega - aapko Gmail App Password banana hoga
    # Filhal ye data ko log karega aur thank you page dikhayega
    print(f"NEW LEAD: {naam}, {phone}, {pita}, {address}, {wtype}")

    # Email bhejne ke liye ye function use karo (Gmail App Password chahiye)
    # send_email(naam, phone, pita, address, wtype)

    return f"""
    {HTML_HEADER}
    <div class="card" style="max-width:600px; margin-top:100px">
    <h2>✅ Thank You {naam}!</h2>
    <p>Aapka form submit ho gaya hai. Hum jaldi aapse {phone} par contact karenge.</p>
    <p>Aapki details hamare email <b>raunakkashyap1989@gmail.com</b> par bhej di gayi hai.</p>
    <a href="/" class="btn">Home Wapas</a>
    </div>
    {HTML_FOOTER_SCRIPT}
    """

@app.route('/page2')
def page2():
    return """
<html><head>
<meta name="monetag" content="2a81f580f6fa7a6e264fa7fbb7c73ad5">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>body{font-family:Arial;text-align:center;padding:30px;background:#fff3e0}
.box{background:white;padding:30px;border-radius:15px;max-width:600px;margin:auto;box-shadow:0 5px 15px rgba(0,0,0,0.1)}}
.btn{background:#4a00e0;color:white;padding:12px 25px;border-radius:8px;text-decoration:none;display:inline-block;margin:10px}
</style></head><body>
<div class="box">
<h1>Meri Web Hai 🚀</h1>
<h3>Website Design Services</h3>
<p>Apni khud ki professional website banwaye</p>
<br><br><a href="/" class="btn"><- Back</a>
</div>
</body></html>
"""

def send_email(naam, phone, pita, address, wtype):
    # Iske liye Gmail me 2-Step On karke App Password banana hoga
    msg = MIMEText(f"Naam: {naam}\\nPhone: {phone}\\nPita: {pita}\\nAddress: {address}\\nWebsite Type: {wtype}")
    msg['Subject'] = f"New Website Order - {naam}"
    msg['From'] = "your_email@gmail.com"
    msg['To'] = "raunakkashyap1989@gmail.com"
    # s = smtplib.SMTP('smtp.gmail.com', 587)
    # s.starttls(); s.login("your_email@gmail.com", "YOUR_APP_PASSWORD"); s.send_message(msg); s.quit()

if __name__ == '__main__':
    app.run()
