# Weather App - WAPP

### About 📙
This project was created with goal of giving weather statics for anyone. You can search for a city or country and know how's the weather there.

Api Owner/Colaborator: [OpenWeather](https://openweathermap.org/)
### Project structure
#### Web
`/` - Main page, where you can search for cities and it weather's<br>
**obs.: i did implement the error pages.**
#### In code
- `./docs`: documention directory
- `./src`: source code directory
  - `./src/staticfiles`: it stores all css files
  - `./src/templates`: it have all th project templates
    - `./src/templates/pages`: there are only the main page
    - `./src/templates/error`: all the error pages is here
  - `Weather`: main app of the project
  - `WeatherApp`: the django project core

### Tools 🛠️
- Python
- Django
- HTML5/CSS3
### How to run?🏃
#### Required
- Python 3.12.1
- Django 5.0.6
### Procedure
```bash
    # In your git bash, clone the repo.
    git clone https://github.com/angelo-francisco/WAPP-WeatherAPP.git

    # Activate the enviroment
    ./venv/Scripts/Activate.ps1

    # Go to the source
    cd src

    # run the project
    python manage.py runserver
```


### License 🔑

The license of the project is [MIT](https://opensource.org/license/mit)
