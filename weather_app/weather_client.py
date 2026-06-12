"""OpenWeather API integration."""

from dataclasses import dataclass
from typing import Any

import requests


OPENWEATHER_CURRENT_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
DEFAULT_REQUEST_TIMEOUT_SECONDS = 10


@dataclass(frozen=True)
class WeatherReport:
    city: str
    temperature_celsius: int
    description: str


class WeatherLookupError(Exception):
    """Raised when weather information cannot be fetched or parsed."""


def fetch_weather_report(city: str, api_key: str) -> WeatherReport:
    """Fetch current weather for a city using OpenWeather."""
    normalized_city = city.strip()
    if not normalized_city:
        raise WeatherLookupError("Informe uma cidade.")

    payload = request_current_weather(normalized_city, api_key)
    return parse_weather_report(payload)


def request_current_weather(city: str, api_key: str) -> dict[str, Any]:
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "pt_br",
    }

    try:
        response = requests.get(
            OPENWEATHER_CURRENT_WEATHER_URL,
            params=params,
            timeout=DEFAULT_REQUEST_TIMEOUT_SECONDS,
        )
    except requests.RequestException as exc:
        raise WeatherLookupError("Não foi possível conectar ao serviço de clima.") from exc

    if response.status_code == 404:
        raise WeatherLookupError("Local não encontrado.")

    if response.status_code == 401:
        raise WeatherLookupError("Chave da API inválida ou ausente.")

    try:
        response.raise_for_status()
    except requests.HTTPError as exc:
        raise WeatherLookupError("Erro ao consultar o serviço de clima.") from exc

    return response.json()


def parse_weather_report(payload: dict[str, Any]) -> WeatherReport:
    try:
        city = str(payload["name"])
        temperature_celsius = round(float(payload["main"]["temp"]))
        description = str(payload["weather"][0]["description"])
    except (KeyError, IndexError, TypeError, ValueError) as exc:
        raise WeatherLookupError("Resposta inválida do serviço de clima.") from exc

    return WeatherReport(
        city=city,
        temperature_celsius=temperature_celsius,
        description=description,
    )
