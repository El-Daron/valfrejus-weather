"""Config flow for Val Frejus Meteo integration."""
import logging
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult

from .const import CONF_STATION, DEFAULT_STATION, DOMAIN

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Optional(CONF_STATION, default=DEFAULT_STATION): str,
    }
)


class ValFrejusConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Val Frejus Meteo."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            await self.async_set_unique_id(user_input[CONF_STATION])
            self._abort_if_unique_id_configured()

            return self.async_create_entry(
                title=f"Val Frejus ({user_input[CONF_STATION]})",
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors,
        )
