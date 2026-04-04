"""Pure conversion functions for weather unit transformations.

All functions in this module are pure — zero side effects, no I/O,
no external dependencies. Designed for isolated unit testing.
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit.

    Uses the standard conversion formula:
        F = (C × 9/5) + 32

    Args:
        celsius: Temperature value in degrees Celsius.

    Returns:
        Temperature value in degrees Fahrenheit.
    """
    # Formula: F = (C × 9/5) + 32
    return (celsius * 9 / 5) + 32


def kmh_to_ms(kmh: float) -> float:
    """Convert wind speed from kilometers per hour to meters per second.

    Uses the standard conversion formula:
        V_ms = V_kmh ÷ 3.6

    Args:
        kmh: Wind speed value in kilometers per hour.

    Returns:
        Wind speed value in meters per second.
    """
    # Formula: V_ms = V_kmh ÷ 3.6
    return kmh / 3.6
