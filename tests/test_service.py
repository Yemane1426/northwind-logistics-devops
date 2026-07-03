from app import data


def test_delivery_data_exists():
    deliveries = data.all_deliveries()
    assert isinstance(deliveries, list)
    assert len(deliveries) > 0


def test_find_existing_delivery():
    deliveries = data.all_deliveries()
    first_delivery = deliveries[0]

    result = data.find_delivery(first_delivery["id"])

    assert result is not None
    assert result["id"] == first_delivery["id"]


def test_missing_delivery_returns_none():
    result = data.find_delivery("DOES-NOT-EXIST")
    assert result is None


def test_delivery_has_required_fields():
    deliveries = data.all_deliveries()
    delivery = deliveries[0]

    assert "id" in delivery
    assert "status" in delivery
    assert "destination" in delivery
