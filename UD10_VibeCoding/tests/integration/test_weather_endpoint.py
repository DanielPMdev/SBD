"""Integration tests for the GET /weather endpoint.

All external HTTP calls are mocked — no real network traffic.
Tests both success (200) and error (502) paths.
"""

import httpx
import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture()
def client() -> TestClient:
    """Create a test client for the FastAPI application."""
    return TestClient(app)


def _build_mock_response(
    json_data: dict,
    status_code: int = 200,
) -> httpx.Response:
    """Build a mock httpx.Response with the given JSON data.

    Args:
        json_data: The JSON payload to include in the response.
        status_code: HTTP status code for the response.

    Returns:
        A fully-formed httpx.Response object.
    """
    return httpx.Response(
        status_code=status_code,
        json=json_data,
        request=httpx.Request('GET', 'https://api.open-meteo.com/v1/forecast'),
    )


class TestWeatherEndpointSuccess:
    """Tests for the successful (200) path of GET /weather."""

    def test_success_response_status(self, client: TestClient, mocker) -> None:
        """GET /weather should return 200 with valid Open-Meteo data."""
        mock_response = _build_mock_response({
            'current_weather': {
                'temperature': 22.5,
                'windspeed': 15.0,
            }
        })

        mocker.patch(
            'src.services.weather_service.httpx.AsyncClient.get',
            return_value=mock_response,
        )

        response = client.get('/weather')

        assert response.status_code == 200

    def test_success_response_shape(self, client: TestClient, mocker) -> None:
        """Response body should contain temperature and wind_speed objects."""
        mock_response = _build_mock_response({
            'current_weather': {
                'temperature': 22.5,
                'windspeed': 15.0,
            }
        })

        mocker.patch(
            'src.services.weather_service.httpx.AsyncClient.get',
            return_value=mock_response,
        )

        response = client.get('/weather')
        data = response.json()

        assert 'temperature' in data
        assert 'wind_speed' in data

    def test_success_temperature_values(self, client: TestClient, mocker) -> None:
        """Temperature should include both celsius and fahrenheit values."""
        mock_response = _build_mock_response({
            'current_weather': {
                'temperature': 22.5,
                'windspeed': 15.0,
            }
        })

        mocker.patch(
            'src.services.weather_service.httpx.AsyncClient.get',
            return_value=mock_response,
        )

        response = client.get('/weather')
        temp = response.json()['temperature']

        assert temp['celsius'] == pytest.approx(22.5)
        # F = (22.5 × 9/5) + 32 = 72.5
        assert temp['fahrenheit'] == pytest.approx(72.5)

    def test_success_wind_speed_values(self, client: TestClient, mocker) -> None:
        """Wind speed should include both kmh and ms values."""
        mock_response = _build_mock_response({
            'current_weather': {
                'temperature': 22.5,
                'windspeed': 15.0,
            }
        })

        mocker.patch(
            'src.services.weather_service.httpx.AsyncClient.get',
            return_value=mock_response,
        )

        response = client.get('/weather')
        wind = response.json()['wind_speed']

        assert wind['kmh'] == pytest.approx(15.0)
        # V_ms = 15 ÷ 3.6 ≈ 4.167
        assert wind['ms'] == pytest.approx(4.167, rel=1e-2)

    def test_success_does_not_leak_raw_data(self, client: TestClient, mocker) -> None:
        """Response should not contain raw Open-Meteo fields."""
        mock_response = _build_mock_response({
            'current_weather': {
                'temperature': 22.5,
                'windspeed': 15.0,
                'weathercode': 0,
                'winddirection': 180,
            }
        })

        mocker.patch(
            'src.services.weather_service.httpx.AsyncClient.get',
            return_value=mock_response,
        )

        response = client.get('/weather')
        data = response.json()

        assert 'current_weather' not in data
        assert 'weathercode' not in data
        assert 'winddirection' not in data


class TestWeatherEndpointErrors:
    """Tests for the error (502) paths of GET /weather."""

    def test_502_on_connection_error(self, client: TestClient, mocker) -> None:
        """Should return 502 when Open-Meteo is unreachable."""
        mocker.patch(
            'src.services.weather_service.httpx.AsyncClient.get',
            side_effect=httpx.ConnectError('Connection refused'),
        )

        response = client.get('/weather')

        assert response.status_code == 502
        data = response.json()
        assert data['error'] == 'bad_gateway'
        assert 'message' in data

    def test_502_on_timeout(self, client: TestClient, mocker) -> None:
        """Should return 502 when Open-Meteo times out."""
        mocker.patch(
            'src.services.weather_service.httpx.AsyncClient.get',
            side_effect=httpx.ReadTimeout('Read timed out'),
        )

        response = client.get('/weather')

        assert response.status_code == 502

    def test_502_on_missing_temperature(self, client: TestClient, mocker) -> None:
        """Should return 502 when temperature field is missing."""
        mock_response = _build_mock_response({
            'current_weather': {
                'windspeed': 15.0,
            }
        })

        mocker.patch(
            'src.services.weather_service.httpx.AsyncClient.get',
            return_value=mock_response,
        )

        response = client.get('/weather')

        assert response.status_code == 502
        data = response.json()
        assert data['error'] == 'bad_gateway'

    def test_502_on_missing_windspeed(self, client: TestClient, mocker) -> None:
        """Should return 502 when windspeed field is missing."""
        mock_response = _build_mock_response({
            'current_weather': {
                'temperature': 22.5,
            }
        })

        mocker.patch(
            'src.services.weather_service.httpx.AsyncClient.get',
            return_value=mock_response,
        )

        response = client.get('/weather')

        assert response.status_code == 502
        data = response.json()
        assert data['error'] == 'bad_gateway'

    def test_502_on_empty_current_weather(self, client: TestClient, mocker) -> None:
        """Should return 502 when current_weather is empty."""
        mock_response = _build_mock_response({
            'current_weather': {}
        })

        mocker.patch(
            'src.services.weather_service.httpx.AsyncClient.get',
            return_value=mock_response,
        )

        response = client.get('/weather')

        assert response.status_code == 502

    def test_502_on_missing_current_weather_key(self, client: TestClient, mocker) -> None:
        """Should return 502 when current_weather key is absent entirely."""
        mock_response = _build_mock_response({
            'some_other_key': 'value'
        })

        mocker.patch(
            'src.services.weather_service.httpx.AsyncClient.get',
            return_value=mock_response,
        )

        response = client.get('/weather')

        assert response.status_code == 502

    def test_502_on_server_error(self, client: TestClient, mocker) -> None:
        """Should return 502 when Open-Meteo returns a 500 error."""
        mock_response = _build_mock_response(
            json_data={'error': 'internal server error'},
            status_code=500,
        )

        mocker.patch(
            'src.services.weather_service.httpx.AsyncClient.get',
            return_value=mock_response,
        )

        response = client.get('/weather')

        assert response.status_code == 502

    def test_error_response_envelope_shape(self, client: TestClient, mocker) -> None:
        """Error responses should always have 'error' and 'message' keys."""
        mocker.patch(
            'src.services.weather_service.httpx.AsyncClient.get',
            side_effect=httpx.ConnectError('Connection refused'),
        )

        response = client.get('/weather')
        data = response.json()

        assert 'error' in data
        assert 'message' in data
        assert isinstance(data['error'], str)
        assert isinstance(data['message'], str)
