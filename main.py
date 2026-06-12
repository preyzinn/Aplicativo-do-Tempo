from weather_app.config import load_app_config
from weather_app.ui import WeatherApp


def main() -> None:
    config = load_app_config()
    app = WeatherApp(api_key=config.openweather_api_key)
    app.run()


if __name__ == "__main__":
    main()
