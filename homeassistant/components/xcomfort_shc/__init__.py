"""The xComfort Smart Home Controller integration."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from . import xcomfort_hub

# TODO List the platforms that you want to support.
# For your initial PR, limit it to 1 platform.
# PLATFORMS: list[Platform] = [Platform.LIGHT]
PLATFORMS: list[Platform] = []

# TODO Create ConfigEntry type alias with API object
# TODO Rename type alias and update all entry annotations
type NameConfigEntry = ConfigEntry[xcomfort_hub.XcomfortHub]  # noqa: F821


# TODO Update entry annotation
async def async_setup_entry(hass: HomeAssistant, entry: NameConfigEntry) -> bool:
    """Set up xComfort Smart Home Controller from a config entry."""
    print("HENKIE - INIT - async_setup_entry")
    # TODO 1. Create API instance
    # TODO 2. Validate the API connection (and authentication)
    # TODO 3. Store an API object for your platforms to access
    # entry.runtime_data = MyAPI(...)

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    print("AFTERGGGG")

    return True


# TODO Update entry annotation
async def async_unload_entry(hass: HomeAssistant, entry: NameConfigEntry) -> bool:
    """Unload a config entry."""
    print("HENKIE - INIT - async_unload_entry")
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
