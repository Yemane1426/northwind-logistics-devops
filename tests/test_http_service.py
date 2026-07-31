"""Integration tests for the Northwind HTTP service."""

from __future__ import annotations

import json
import threading
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer
from typing import Generator

import pytest

from app import data
from app.service import DeliveryHandler


@pytest.fixture(scope="module")
def running_server() -> Generator[tuple[str, int], None, None]:
    """Run the real HTTP handler on a temporary local port."""

    server = ThreadingHTTPServer(("127.0.0.1", 0), DeliveryHandler)
    host, port = server.server_address

    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    try:
        yield host, port
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


def make_request(
    server_address: tuple[str, int],
    path: str,
    method: str = "GET",
) -> tuple[int, dict | list, str]:
    """Send a GET request and return status, JSON body, and content type."""

    host, port = server_address
    connection = HTTPConnection(host, port, timeout=5)

    try:
        connection.request(method, path)
        response = connection.getresponse()
        raw_body = response.read().decode("utf-8")
        payload = json.loads(raw_body)

        return (
            response.status,
            payload,
            response.getheader("Content-Type", ""),
        )
    finally:
        connection.close()


def test_root_returns_service_information(
    running_server: tuple[str, int],
) -> None:
    status, payload, content_type = make_request(running_server, "/")

    assert status == 200
    assert content_type == "application/json"
    assert payload["service"] == "Northwind Logistics delivery tracking"
    assert "/health" in payload["endpoints"]
    assert "/deliveries" in payload["endpoints"]


def test_health_endpoint_returns_ok(
    running_server: tuple[str, int],
) -> None:
    status, payload, content_type = make_request(running_server, "/health")

    assert status == 200
    assert content_type == "application/json"
    assert payload == {"status": "ok"}


def test_deliveries_endpoint_returns_all_records(
    running_server: tuple[str, int],
) -> None:
    status, payload, content_type = make_request(
        running_server,
        "/deliveries",
    )

    assert status == 200
    assert content_type == "application/json"
    assert isinstance(payload, list)
    assert payload == data.all_deliveries()


def test_existing_delivery_returns_expected_record(
    running_server: tuple[str, int],
) -> None:
    expected = data.all_deliveries()[0]

    status, payload, content_type = make_request(
        running_server,
        f"/deliveries/{expected['id']}",
    )

    assert status == 200
    assert content_type == "application/json"
    assert payload == expected


@pytest.mark.parametrize(
    "path",
    [
        "/deliveries/DOES-NOT-EXIST",
        "/deliveries/unknown-id",
    ],
)
def test_unknown_delivery_returns_404(
    running_server: tuple[str, int],
    path: str,
) -> None:
    status, payload, content_type = make_request(running_server, path)

    assert status == 404
    assert content_type == "application/json"
    assert "error" in payload
    assert "No delivery with id" in payload["error"]


@pytest.mark.parametrize(
    "path",
    [
        "/not-a-real-route",
        "/admin",
        "/api",
    ],
)
def test_unknown_route_returns_404(
    running_server: tuple[str, int],
    path: str,
) -> None:
    status, payload, content_type = make_request(running_server, path)

    assert status == 404
    assert content_type == "application/json"
    assert payload == {"error": "Not found"}


@pytest.mark.parametrize(
    ("path", "expected_status"),
    [
        ("/health/", 200),
        ("/deliveries/", 200),
        ("/health?source=probe", 200),
    ],
)
def test_trailing_slashes_and_query_strings_are_handled(
    running_server: tuple[str, int],
    path: str,
    expected_status: int,
) -> None:
    status, _, _ = make_request(running_server, path)

    assert status == expected_status


@pytest.mark.parametrize(
    "method",
    ["POST", "PUT", "PATCH", "DELETE"],
)
def test_unsupported_http_methods_do_not_modify_data(
    running_server: tuple[str, int],
    method: str,
) -> None:
    before = data.all_deliveries()

    status, payload, content_type = make_request(
        running_server,
        "/deliveries",
        method=method,
    )

    assert status == 405
    assert content_type == "application/json"
    assert payload == {"error": "Method not allowed"}
    assert data.all_deliveries() == before


@pytest.mark.parametrize(
    "path",
    [
        "/health",
        "/deliveries",
        "/deliveries/DOES-NOT-EXIST",
        "/not-a-real-route",
    ],
)
def test_json_responses_have_correct_content_type(
    running_server: tuple[str, int],
    path: str,
) -> None:
    _, _, content_type = make_request(running_server, path)

    assert content_type == "application/json"


@pytest.mark.parametrize(
    "path",
    [
        "/health?source=kubernetes",
        "/deliveries?source=test",
        "/deliveries/?page=1",
    ],
)
def test_supported_routes_ignore_query_parameters(
    running_server: tuple[str, int],
    path: str,
) -> None:
    status, _, _ = make_request(running_server, path)

    assert status == 200


def test_delivery_list_returns_independent_data_structure() -> None:
    first_result = data.all_deliveries()
    second_result = data.all_deliveries()

    assert first_result == second_result
    assert first_result is not second_result
