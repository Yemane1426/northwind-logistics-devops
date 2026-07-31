from unittest.mock import Mock, patch


from app import data
from app import service


def test_delivery_data_exists() -> None:
    deliveries = data.all_deliveries()

    assert isinstance(deliveries, list)
    assert len(deliveries) > 0


def test_find_existing_delivery() -> None:
    deliveries = data.all_deliveries()
    first_delivery = deliveries[0]

    result = data.find_delivery(first_delivery["id"])

    assert result is not None
    assert result["id"] == first_delivery["id"]


def test_missing_delivery_returns_none() -> None:
    result = data.find_delivery("DOES-NOT-EXIST")

    assert result is None


def test_delivery_has_required_fields() -> None:
    deliveries = data.all_deliveries()
    delivery = deliveries[0]

    assert "id" in delivery
    assert "status" in delivery
    assert "destination" in delivery


def test_main_uses_default_port() -> None:
    mock_server = Mock()
    mock_server.serve_forever.side_effect = KeyboardInterrupt

    with patch.object(
        service,
        "ThreadingHTTPServer",
        return_value=mock_server,
    ) as server_class:
        with patch.dict("os.environ", {}, clear=True):
            service.main()

    server_class.assert_called_once_with(
        ("0.0.0.0", 8000),
        service.DeliveryHandler,
    )
    mock_server.serve_forever.assert_called_once_with()
    mock_server.shutdown.assert_called_once_with()


def test_main_uses_port_environment_variable() -> None:
    mock_server = Mock()
    mock_server.serve_forever.side_effect = KeyboardInterrupt

    with patch.object(
        service,
        "ThreadingHTTPServer",
        return_value=mock_server,
    ) as server_class:
        with patch.dict("os.environ", {"PORT": "9000"}, clear=True):
            service.main()

    server_class.assert_called_once_with(
        ("0.0.0.0", 9000),
        service.DeliveryHandler,
    )
    mock_server.shutdown.assert_called_once_with()
