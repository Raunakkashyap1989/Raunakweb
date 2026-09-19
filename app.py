from flask import Flask
app = Flask(__name__)



@app.route('/')
def home():
    return f"""
<html><head>
<meta name="monetag" content="2a81f580f6fa7a6e264fa7fbb7c73ad5">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Raunak Web</title>
<style>
body{{font-family:Arial;background:#f5f7ff;margin:0;padding:20px;text-align:center}}
h1{{color:#4a00e0;font-size:32px}}
.card{{background:white;padding:20px;border-radius:15px;box-shadow:0 5px 15px rgba(0,0,0,0.1);margin:15px auto;max-width:350px}}
.btn{{background:#4a00e0;color:white;padding:10px 20px;border:none;border-radius:8px;cursor:pointer;font-weight:bold}}
.btn-buy{{background:#ff0066;width:100%;margin-top:10px;padding:12px;font-size:16px}}
input{{padding:12px;width:80%;border-radius:8px;border:1px solid #ccc;margin:10px}}
.grid{{display:flex;flex-wrap:wrap;justify-content:center}}
.price{{font-size:24px;color:#00b300;font-weight:bold;margin:10px 0;border:2px dashed #00b300;padding:8px;border-radius:8px;background:#f0fff0}}
.text-box{{border:2px dashed #ff0066;padding:8px;border-radius:8px;background:#fff0f5;margin:10px 0}}
</style></head><body>

<h1>Welcome Raunak Web 🚀</h1>

<div class="grid">
  <div class="card">
    <h3>PLAN 1 - Basic</h3>
    <div class="price">₹ 199</div>
    <div class="text-box">website ban jayegi no live </div>
    <button class="btn btn-buy" onclick="buy('Plan 1')">Buy Now</button>
  </div>
  <div class="card">
    <h3>PLAN 2 - Standard</h3>
    <div class="price">₹ 999</div>
    <div class="text-box">phone ka sara deta hack </div>
    <button class="btn btn-buy" onclick="buy('Plan 2')">Buy Now</button>
  </div>
  <div class="card">
    <h3>PLAN 3 - Premium</h3>
    <div class="price">₹ 599</div>
    <div class="text-box">Social facebook account ben</div>
    <button class="btn btn-buy" onclick="buy('Plan 3')">Buy Now</button>
  </div>
  <div class="card">
    <h3>PLAN 4 - Pro</h3>
    <div class="price">₹ 399</div>
    <div class="text-box">Location pta karna number se ho jayega </div>
    <button class="btn btn-buy" onclick="buy('Plan 4')">Buy Now</button>
  </div>
  <div class="card">
    <h3>PLAN 5 - Ultimate</h3>
    <div class="price">₹ 1499</div>
    <div class="text-box">website ban jaygi live bhi kar duga </div>
    <button class="btn btn-buy" onclick="buy('Plan 5')">Buy Now</button>
  </div>
</div>

<div class="card" style="max-width:600px">
<h2>Try Web Free</h2>
<input id="nameInput" placeholder="Apna naam likho">
<br><button class="btn" onclick="makeWeb()">Click karke Web Banao</button>
<p id="result"></p>
</div>

<div class="card" style="max-width:600px">
<h2>Badi Link ko Chhoti Banao</h2>
<input id="longUrl" placeholder="Yaha badi link paste karo">
<br><button class="btn" onclick="shortLink()">Chhoti Banao</button>
<p id="shortResult"></p>
</div>

<br><a href="/page2" class="btn" style="text-decoration:none">Next Page 1/2 -></a>

<script>
function buy(plan){{
  // Pehle ad khulega, fir WhatsApp
  window.open("{DIRECT_LINK}", "_blank");
  setTimeout(function(){{
    window.open("https://wa.me/917754048502?text=Mujhe "+plan+" chahiye","_blank");
  }}, 1000);
}}
function makeWeb(){{
  let n = document.getElementById('nameInput').value;
  if(n==""){{alert("Naam likho");return;}}
  window.open("{DIRECT_LINK}", "_blank");
  document.getElementById('result').innerHTML = "🎉 <b>"+n+"</b> ki web: https://"+n.toLowerCase()+".raunakweb.com";
}}
function shortLink(){{
  let l = document.getElementById('longUrl').value;
  if(l==""){{alert("Link dalo");return;}}
  window.open("{DIRECT_LINK}", "_blank");
  let s = "https://rnk.ly/" + Math.random().toString(36).substring(7);
  document.getElementById('shortResult').innerHTML = "Short: <a href='"+l+"' target='_blank'>"+s+"</a>";
}}
</script>
</body></html>
"""

@app.route('/page2')
def page2():
    return f"""
<html><head>
<meta name="monetag" content="2a81f580f6fa7a6e264fa7fbb7c73ad5">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>body{{font-family:Arial;text-align:center;padding:30px;background:#fff3e0}}
.box{{background:white;padding:30px;border-radius:15px;max-width:600px;margin:auto;box-shadow:0 5px 15px rgba(0,0,0,0.1)}}
a{{word-break:break-all;color:#4a00e0;font-weight:bold}}
.btn{{background:#4a00e0;color:white;padding:12px 25px;border-radius:8px;text-decoration:none;display:inline-block;margin:10px}}
</style></head><body>
<div class="box">
<h1>Meri Web Hai 🚀</h1>
<h3>Website Design Services</h3>
<p>Apni khud ki professional website banwaye</p>
<a href="{DIRECT_LINK}" target="_blank" class="btn">Visit Demo Website</a>
<br><br><a href="/" class="btn"><- Back</a>
</div>
</body></html>
"""

if __name__ == '__main__':
    app.run()
