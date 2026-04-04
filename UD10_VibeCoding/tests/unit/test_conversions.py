"""Unit tests for src/core/conversions.py.

Achieves 100% coverage on all pure conversion functions.
Tests normal values, zero inputs, and negative temperatures.
"""

import pytest

from src.core.conversions import celsius_to_fahrenheit, kmh_to_ms


class TestCelsiusToFahrenheit:
    """Tests for the celsius_to_fahrenheit conversion function."""

    def test_boiling_point(self) -> None:
        """100°C should convert to 212°F (boiling point of water)."""
        assert celsius_to_fahrenheit(100.0) == pytest.approx(212.0)

    def test_freezing_point(self) -> None:
        """0°C should convert to 32°F (freezing point of water)."""
        assert celsius_to_fahrenheit(0.0) == pytest.approx(32.0)

    def test_body_temperature(self) -> None:
        """37°C should convert to 98.6°F (human body temperature)."""
        assert celsius_to_fahrenheit(37.0) == pytest.approx(98.6)

    def test_negative_temperature(self) -> None:
        """-40°C should convert to -40°F (intersection point)."""
        assert celsius_to_fahrenheit(-40.0) == pytest.approx(-40.0)

    def test_negative_temperature_mild(self) -> None:
        """-10°C should convert to 14°F."""
        assert celsius_to_fahrenheit(-10.0) == pytest.approx(14.0)

    def test_fractional_temperature(self) -> None:
        """22.5°C should convert to 72.5°F."""
        assert celsius_to_fahrenheit(22.5) == pytest.approx(72.5)

    def test_large_positive_temperature(self) -> None:
        """1000°C should convert to 1832°F."""
        assert celsius_to_fahrenheit(1000.0) == pytest.approx(1832.0)

    def test_large_negative_temperature(self) -> None:
        """-273.15°C (absolute zero) should convert to -459.67°F."""
        assert celsius_to_fahrenheit(-273.15) == pytest.approx(-459.67)


class TestKmhToMs:
    """Tests for the kmh_to_ms conversion function."""

    def test_standard_conversion(self) -> None:
        """36 km/h should convert to 10 m/s."""
        assert kmh_to_ms(36.0) == pytest.approx(10.0)

    def test_zero_speed(self) -> None:
        """0 km/h should convert to 0 m/s."""
        assert kmh_to_ms(0.0) == pytest.approx(0.0)

    def test_one_kmh(self) -> None:
        """1 km/h should convert to approximately 0.27778 m/s."""
        assert kmh_to_ms(1.0) == pytest.approx(0.27778, rel=1e-3)

    def test_common_wind_speed(self) -> None:
        """15 km/h should convert to approximately 4.167 m/s."""
        assert kmh_to_ms(15.0) == pytest.approx(4.1667, rel=1e-3)

    def test_high_wind_speed(self) -> None:
        """100 km/h should convert to approximately 27.778 m/s."""
        assert kmh_to_ms(100.0) == pytest.approx(27.778, rel=1e-3)

    def test_fractional_speed(self) -> None:
        """3.6 km/h should convert to exactly 1 m/s."""
        assert kmh_to_ms(3.6) == pytest.approx(1.0)

    def test_hurricane_speed(self) -> None:
        """200 km/h should convert to approximately 55.556 m/s."""
        assert kmh_to_ms(200.0) == pytest.approx(55.556, rel=1e-3)
