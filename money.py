from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
    return"""
    <!DOCTYPE html>
    <h1>welcome to Auto hub 🏎️💨</h1>
<h2>we provide you with the best car trends and updates</h2>
<h3>Also remember to subscribe to our youtube channel</h3> <a href="https://youtu.be/cG1hr3uat0c?si=E7FxqjQM1d8D_i4H"> click here to subscribe</a>
<h4> Today we will discuss about the mercesdes benz CLA</h4>
<b>The mercedes benz CLA is a car that combines luxury and speed </b>
<p>The mercedes benz CLA was introduced in 2013 </p>
<img src=" https://www.motortrend.com/uploads/sites/5/2020/11/2020-Mercedes-AMG-CLA-45-4Matic-3-1.jpg">2024 Mercedes CLA
<p> The car has a 2.0-liter four-cylinder engine fitted with a turbocharger as well as a belt-driven starter-generator. </p>


<p>The price of the 2024 Mercedes-Benz CLA-class starts at $44,350 and goes up to $53,400 depending on the trim and options.</p>

<img src="https://www.topgear.com/sites/default/files/2023/10/Medium-44249-CLA250e.jpg?w=1784&h=1004">contains an updated infotainment system 
<p>The mercedes benz CLA can max out 221 horsepower and 258 pound-feet of torque</p>
<img src="https://www.topgear.com/sites/default/files/2023/10/Medium-44235-CLA250e.jpg?w=1784&h=1004"> can reach 60 miles per hour in 4.4 seconds

<p>The  2024 Mercedes Benz CLA Class Reveiw is wriiten by james bright</p>

<img src=" https://wallpapers.com/images/high/dark-web-pictures-c1qyvik4gxu4n6zp.webp"> wriiten by james bright
"""
if __name__ =='__main__':
    app.run(debug=True)



























