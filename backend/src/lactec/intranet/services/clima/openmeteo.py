from lactec.intranet import logger
from plone.memoize.ram import cache
from time import time

import requests


BASE_URL: str = "https://api.open-meteo.com/v1/forecast"


def time_30m_key(*args, **kwargs):
    """Chave de cache para manter o valor em cache por 30 minutos."""
    return time() // (60 * 30)


def formata_weather_code(code: int) -> str:
    WMO = {
        0: "sun",
        1: "sun",
        2: "sun",
        3: "sun",
        45: "sun",
        48: "sun",
        51: "cloud",
        53: "cloud",
        55: "cloud",
        56: "cloud",
        57: "cloud",
        61: "cloud",
        63: "cloud",
        65: "cloud",
        66: "cloud",
        67: "cloud",
    }
    return WMO.get(code, "sun")


def formata_hora(valor: str) -> str:
    """Formata valores de hora a partir de uma data."""
    return valor[-5:]


def _formatar_resposta(data: dict) -> dict:
    """Parseia os dados obtidos da OpenMeteo.

    retorna um dicionários com informações meteorológicas.
    """
    dados_diarios = data["daily"]
    dados_hora = data["hourly"]
    dados_agora = data["current"]
    sunrise = dados_diarios["sunrise"]
    sunset = dados_diarios["sunset"]
    horarios = dados_hora["time"]
    sequencia = dados_hora["temperature_2m"]
    temperaturas = {
        formata_hora(hora): temp for hora, temp in zip(horarios, sequencia, strict=True)
    }
    temperatura = dados_agora["temperature_2m"]
    weather_code = dados_agora["weather_code"]
    return {
        "events": {
            "sunrise": formata_hora(sunrise[0]),
            "sunset": formata_hora(sunset[0]),
        },
        "temperature": {"now": temperatura, "hourly": temperaturas},
        "weather": formata_weather_code(weather_code),
    }


def _obtem_dados_open_meteo(params: dict[str, str]) -> dict:
    """Realiza chamada ao serviço Open Meteo.

    Esse método existe para facilitar o mock em testes.
    """
    # Parametros da chamada
    response = requests.get(BASE_URL, params=params, timeout=5)
    return response.json()


@cache(time_30m_key)
def dados_clima(latitude: str, longitude: str, timezone: str) -> dict:
    """Chama o serviço Open Meteo e retorna os dados de clima."""
    # Parametros da chamada
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "timezone": timezone,
        "current": "weather_code,temperature_2m",
        "hourly": "temperature_2m",
        "daily": "sunrise,sunset",
        "forecast_days": 1,
    }
    # Realiza a requisição
    logger.info("Acesso ao OpenMeteo")
    raw_data = _obtem_dados_open_meteo(params)
    logger.info("Parseia dados recebidos")
    data = _formatar_resposta(raw_data)
    return data
