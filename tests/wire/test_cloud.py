from .conftest import get_client, verify_request_count


def test_cloud_add_device() -> None:
    """Test addDevice endpoint with WireMock"""
    test_id = "cloud.add_device.0"
    client = get_client(test_id)
    client.cloud.add_device(entry="8cfec329267", registration_code="YS7DS5", description="Front Desk POS")
    verify_request_count(test_id, "POST", "/Cloud/register/8cfec329267", None, 1)


def test_cloud_history_device() -> None:
    """Test HistoryDevice endpoint with WireMock"""
    test_id = "cloud.history_device.0"
    client = get_client(test_id)
    client.cloud.history_device(device_id="WXGDWB", entry="8cfec329267")
    verify_request_count(test_id, "GET", "/Cloud/history/8cfec329267/WXGDWB", None, 1)


def test_cloud_list_device() -> None:
    """Test ListDevice endpoint with WireMock"""
    test_id = "cloud.list_device.0"
    client = get_client(test_id)
    client.cloud.list_device(entry="8cfec329267")
    verify_request_count(test_id, "GET", "/Cloud/list/8cfec329267", None, 1)


def test_cloud_remove_device() -> None:
    """Test RemoveDevice endpoint with WireMock"""
    test_id = "cloud.remove_device.0"
    client = get_client(test_id)
    client.cloud.remove_device(device_id="6c361c7d-674c-44cc-b790-382b75d1xxx", entry="8cfec329267")
    verify_request_count(test_id, "DELETE", "/Cloud/register/8cfec329267/6c361c7d-674c-44cc-b790-382b75d1xxx", None, 1)
