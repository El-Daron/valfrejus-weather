"""Constants for the Val Frejus Meteo integration."""

DOMAIN = "valfrejus"
CONF_STATION = "station"
DEFAULT_STATION = "valfrejus"

SCAN_INTERVAL_HOURS = 6
BASE_URL = "https://bulletinv3.lumiplan.pro/bulletin.php"

SENSOR_TYPES = {
    "village_temp_morning": {
        "name": "Village Temperature Matin",
        "unit": "°C",
        "icon": "mdi:thermometer",
        "device_class": "temperature",
    },
    "village_temp_afternoon": {
        "name": "Village Temperature Apres-midi",
        "unit": "°C",
        "icon": "mdi:thermometer",
        "device_class": "temperature",
    },
    "village_wind_speed": {
        "name": "Village Vitesse Vent",
        "unit": "km/h",
        "icon": "mdi:weather-windy",
        "device_class": None,
    },
    "village_wind_direction": {
        "name": "Village Direction Vent",
        "unit": None,
        "icon": "mdi:compass",
        "device_class": None,
    },
    "village_snow_height": {
        "name": "Village Hauteur Neige",
        "unit": "cm",
        "icon": "mdi:snowflake",
        "device_class": None,
    },
    "village_snow_quality": {
        "name": "Village Qualite Neige",
        "unit": None,
        "icon": "mdi:snowflake-variant",
        "device_class": None,
    },
    "village_fresh_snow": {
        "name": "Village Neige Fraiche",
        "unit": "cm",
        "icon": "mdi:snowflake-alert",
        "device_class": None,
    },
    "village_last_snowfall": {
        "name": "Village Derniere Chute",
        "unit": None,
        "icon": "mdi:calendar-clock",
        "device_class": None,
    },
    "summit_temp_morning": {
        "name": "Sommet Temperature Matin",
        "unit": "°C",
        "icon": "mdi:thermometer",
        "device_class": "temperature",
    },
    "summit_temp_afternoon": {
        "name": "Sommet Temperature Apres-midi",
        "unit": "°C",
        "icon": "mdi:thermometer",
        "device_class": "temperature",
    },
    "summit_wind_speed": {
        "name": "Sommet Vitesse Vent",
        "unit": "km/h",
        "icon": "mdi:weather-windy",
        "device_class": None,
    },
    "summit_wind_direction": {
        "name": "Sommet Direction Vent",
        "unit": None,
        "icon": "mdi:compass",
        "device_class": None,
    },
    "summit_snow_height": {
        "name": "Sommet Hauteur Neige",
        "unit": "cm",
        "icon": "mdi:snowflake",
        "device_class": None,
    },
    "summit_snow_quality": {
        "name": "Sommet Qualite Neige",
        "unit": None,
        "icon": "mdi:snowflake-variant",
        "device_class": None,
    },
    "summit_fresh_snow": {
        "name": "Sommet Neige Fraiche",
        "unit": "cm",
        "icon": "mdi:snowflake-alert",
        "device_class": None,
    },
    "summit_last_snowfall": {
        "name": "Sommet Derniere Chute",
        "unit": None,
        "icon": "mdi:calendar-clock",
        "device_class": None,
    },
    "last_update": {
        "name": "Derniere Mise a Jour",
        "unit": None,
        "icon": "mdi:clock-outline",
        "device_class": None,
    },
}
