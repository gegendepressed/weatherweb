from flask import Flask, render_template, request
from requests import get
import datetime

app = Flask(__name__)

def getweatherinfo(city): 
   # API_ID = insert your api id here 
    response = get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")
    data = response.json()
    weatherinfo = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "latitude": data["coord"]["lat"],
            "longitude": data["coord"]["lon"],
            "current_temperature": data["main"]["temp"], 
            "feels_like" : data["main"]["feels_like"],
            "min_temp" : data["main"]["temp_min"],
            "max_temp" : data["main"]["temp_max"],
            "humidity": data["main"]["humidity"],
            "visibility": data["visibility"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
            "wind_direction": data["wind"]["deg"],
            "timezone" : int(data['timezone']),
            "sunrise_utc" : int(data['sys']['sunrise']),
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
