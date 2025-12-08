from .conftest import get_client, verify_request_count


def test_chargeBacks_add_response() -> None:
    """Test AddResponse endpoint with WireMock"""
    test_id = "charge_backs.add_response.0"
    client = get_client(test_id)
    client.charge_backs.add_response(id=1000000, idempotency_key="6B29FC40-CA47-1067-B31D-00DD010662DA")
    verify_request_count(test_id, "POST", "/ChargeBacks/response/1000000", None, 1)


def test_chargeBacks_get_chargeback() -> None:
    """Test GetChargeback endpoint with WireMock"""
    test_id = "charge_backs.get_chargeback.0"
    client = get_client(test_id)
    client.charge_backs.get_chargeback(id=1000000)
    verify_request_count(test_id, "GET", "/ChargeBacks/read/1000000", None, 1)


def test_chargeBacks_get_chargeback_attachment() -> None:
    """Test getChargebackAttachment endpoint with WireMock"""
    test_id = "charge_backs.get_chargeback_attachment.0"
    client = get_client(test_id)
    client.charge_backs.get_chargeback_attachment(id=1000000, file_name="fileName")
    verify_request_count(test_id, "GET", "/ChargeBacks/getChargebackAttachments/1000000/fileName", None, 1)
