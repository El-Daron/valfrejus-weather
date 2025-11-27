"""Sensor platform for Val Frejus Meteo."""
import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, SENSOR_TYPES
from .coordinator import ValFrejusDataCoordinator

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Val Frejus sensors from config entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    
    sensors = []
    for sensor_type, sensor_info in SENSOR_TYPES.items():
        sensors.append(ValFrejusSensor(coordinator, sensor_type, sensor_info, entry))
    
    async_add_entities(sensors)


class ValFrejusSensor(CoordinatorEntity, SensorEntity):
    """Representation of a Val Frejus sensor."""

    def __init__(
        self,
        coordinator: ValFrejusDataCoordinator,
        sensor_type: str,
        sensor_info: dict,
        entry: ConfigEntry,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._sensor_type = sensor_type
        self._attr_name = f"Val Frejus {sensor_info['name']}"
        self._attr_unique_id = f"{entry.entry_id}_{sensor_type}"
        self._attr_icon = sensor_info["icon"]
        self._attr_native_unit_of_measurement = sensor_info.get("unit")
        self._attr_device_class = sensor_info.get("device_class")

    @property
    def native_value(self):
        """Return the state of the sensor."""
        return self.coordinator.data.get(self._sensor_type)

    @property
    def extra_state_attributes(self):
        """Return additional attributes."""
        return {
            "station": self.coordinator.station,
            "last_update": self.coordinator.data.get("last_update"),
        }

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return self.coordinator.last_update_success
