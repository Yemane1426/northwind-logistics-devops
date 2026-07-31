"""A minimal delivery-tracking web service for Northwind Logistics.

It is built on the Python standard library only, so it can be containerised
and deployed without pinning a web framework. It exposes:

    GET /                  service information
    GET /health            health check, always returns HTTP 200
    GET /deliveries        all deliveries, as JSON
    GET /deliveries/{id}   one delivery as JSON, or HTTP 404 if unknown

Unsupported HTTP methods return HTTP 405 with a JSON error response.

The ``/health`` endpoint is deliberately simple and dependency-free so it can
back a container health check and Kubernetes readiness and liveness probes.

The listening port is read from the ``PORT`` environment variable and defaults
to 8000. The service binds to 0.0.0.0 so it is reachable from outside a
container.

Run it locally with:
    python -m app
"""

from __future__ import annotations

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from app import data

DELIVERIES_PREFIX = "/deliveries/"


class DeliveryHandler(BaseHTTPRequestHandler):
    """Handle requests for the delivery-tracking endpoints."""

    server_version = "NorthwindDelivery/1.0"

    def _send_json(self, status: int, payload: dict | list) -> None:
        """Send a JSON response with the supplied status code."""
        body = json.dumps(payload).encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        """Handle supported GET endpoints."""
        path = self.path.split("?", 1)[0]

        if len(path) > 1:
            path = path.rstrip("/")

        if path == "/":
            self._send_json(
                200,
                {
                    "service": "Northwind Logistics delivery tracking",
                    "endpoints": [
                        "/health",
                        "/deliveries",
                        "/deliveries/{id}",
                    ],
                },
            )

        elif path == "/health":
            self._send_json(
                200,
                {"status": "ok"},
            )

        elif path == "/deliveries":
            self._send_json(
                200,
                data.all_deliveries(),
            )

        elif path.startswith(DELIVERIES_PREFIX):
            delivery_id = path[len(DELIVERIES_PREFIX):]
            delivery = data.find_delivery(delivery_id)

            if delivery is None:
                self._send_json(
                    404,
                    {"error": f"No delivery with id {delivery_id}"},
                )
            else:
                self._send_json(
                    200,
                    delivery,
                )

        else:
            self._send_json(
                404,
                {"error": "Not found"},
            )

    def _method_not_allowed(self) -> None:
        """Return a JSON response for unsupported HTTP methods."""
        self._send_json(
            405,
            {"error": "Method not allowed"},
        )

    def do_POST(self) -> None:  # noqa: N802
        """Reject unsupported POST requests."""
        self._method_not_allowed()

    def do_PUT(self) -> None:  # noqa: N802
        """Reject unsupported PUT requests."""
        self._method_not_allowed()

    def do_PATCH(self) -> None:  # noqa: N802
        """Reject unsupported PATCH requests."""
        self._method_not_allowed()

    def do_DELETE(self) -> None:  # noqa: N802
        """Reject unsupported DELETE requests."""
        self._method_not_allowed()

    def log_message(
        self,
        *args: object,
    ) -> None:  # noqa: D401
        """Suppress the default per-request logging to keep output clean."""
        return


def main() -> None:
    """Start the Northwind delivery-tracking HTTP server."""
    port = int(os.environ.get("PORT", "8000"))

    server = ThreadingHTTPServer(
        ("0.0.0.0", port),  # nosec B104
        DeliveryHandler,
    )

    print(f"Northwind delivery tracking listening on port {port}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
