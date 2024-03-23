from flask import Flask, render_template, request
from requests import get
import datetime

app = Flask(__name__)

def getweatherinfo(city): 
    
    response = get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=46cb5a7600879c70efa657aa740287ff&units=metric")
    data = response.json()
    weatherinfo = {
            "city": data["name"],
            "latitude": data["coord"]["lat"],
            "longitude": data["coord"]["lon"],
            "current_temperature": data["main"]["temp"], 
            "humidity": data["main"]["humidity"],
            "visibility": data["visibility"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
            "wind_direction": data["wind"]["deg"],
            "timezone" : int(data['timezone']),
            "sunrise_utc" : int(data['sys']['sunrise']),
            "sunrise_local" : datetime.utcfromtimestamp("sunrise_utc" + "timezone").strftime('%H-%M-%S')
        }
    return weatherinfo
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/weather.html')
def form():
    return render_template('weather.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    weatherinfo = getweatherinfo(name)
    return render_template('submit.html',name=name, weatherinfo=weatherinfo)

if __name__ == '__main__':
    app.run(debug=True)
