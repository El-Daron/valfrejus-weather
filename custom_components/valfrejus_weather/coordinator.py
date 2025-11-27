"""Data update coordinator for Val Frejus Meteo."""
import logging
from datetime import timedelta
from typing import Any

import aiohttp
from bs4 import BeautifulSoup

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import BASE_URL, DOMAIN, SCAN_INTERVAL_HOURS

_LOGGER = logging.getLogger(__name__)


class ValFrejusDataCoordinator(DataUpdateCoordinator):
    """Class to manage fetching Val Frejus data."""

    def __init__(self, hass: HomeAssistant, station: str) -> None:
        """Initialize."""
        self.station = station
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(hours=SCAN_INTERVAL_HOURS),
        )

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch data from Lumiplan."""
        url = f"{BASE_URL}?station={self.station}&lang=fr&isSoir=false"
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=aiohttp.ClientTimeout(total=30)) as response:
                    if response.status != 200:
                        raise UpdateFailed(f"Error fetching data: {response.status}")
                    
                    html = await response.text()
                    return self._parse_data(html)
                    
        except aiohttp.ClientError as err:
            raise UpdateFailed(f"Error communicating with API: {err}")
        except Exception as err:
            raise UpdateFailed(f"Unexpected error: {err}")

    def _parse_data(self, html: str) -> dict[str, Any]:
        """Parse the HTML data."""
        soup = BeautifulSoup(html, "html.parser")
        data = {}

        try:
            maj_element = soup.find("span", class_="intro_maj")
            if maj_element:
                data["last_update"] = maj_element.text.replace("Mis a jour le ", "")

            meteo_cards = soup.find_all("div", class_="meteo_card")
            
            for card in meteo_cards:
                bloc_title = card.find("div", class_="bloc_title")
                if not bloc_title:
                    continue
                    
                location_name = bloc_title.find("h2", class_="bloc_title_text")
                if not location_name:
                    continue
                    
                location = location_name.text.strip()
                
                if "Village" in location or "1550" in card.text:
                    prefix = "village"
                elif "Punta" in location or "2737" in card.text:
                    prefix = "summit"
                else:
                    continue

                meteo_divs = card.find_all("div", class_="meteo_matin")
                
                if len(meteo_divs) >= 6:
                    temp_matin = meteo_divs[0].find("span", class_="text")
                    if temp_matin:
                        data[f"{prefix}_temp_morning"] = self._clean_temp(temp_matin.text)
                    
                    temp_aprem = meteo_divs[1].find("span", class_="text")
                    if temp_aprem:
                        data[f"{prefix}_temp_afternoon"] = self._clean_temp(temp_aprem.text)
                    
                    wind_speed = meteo_divs[2].find("span", class_="subtext")
                    if wind_speed:
                        data[f"{prefix}_wind_speed"] = self._clean_number(wind_speed.text)
                    
                    wind_dir = meteo_divs[3].find("span", class_="subtext")
                    if wind_dir:
                        data[f"{prefix}_wind_direction"] = wind_dir.text.strip()
                    
                    snow_height = meteo_divs[4].find("span", class_="text")
                    if snow_height:
                        data[f"{prefix}_snow_height"] = self._clean_number(snow_height.text)
                    
                    snow_quality = meteo_divs[4].find("span", class_="subtext")
                    if snow_quality:
                        data[f"{prefix}_snow_quality"] = snow_quality.text.strip()
                    
                    fresh_snow = meteo_divs[5].find("span", class_="text")
                    if fresh_snow:
                        data[f"{prefix}_fresh_snow"] = self._clean_number(fresh_snow.text)
                    
                    last_snowfall = meteo_divs[5].find("span", class_="text_italic")
                    if last_snowfall:
                        data[f"{prefix}_last_snowfall"] = last_snowfall.text.strip()

            _LOGGER.debug("Parsed data: %s", data)
            return data

        except Exception as err:
            _LOGGER.error("Error parsing data: %s", err)
            raise UpdateFailed(f"Error parsing data: {err}")

    @staticmethod
    def _clean_temp(value: str) -> float | None:
        """Clean temperature value."""
        try:
            return float(value.replace("°C", "").replace("C", "").strip())
        except (ValueError, AttributeError):
            return None

    @staticmethod
    def _clean_number(value: str) -> int | None:
        """Clean numeric value."""
        try:
            cleaned = "".join(c for c in value if c.isdigit() or c == "-")
            return int(cleaned) if cleaned else None
        except (ValueError, AttributeError):
            return None
