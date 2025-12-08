from .conftest import get_client, verify_request_count


def test_checkCapture_check_processing() -> None:
    """Test CheckProcessing endpoint with WireMock"""
    test_id = "check_capture.check_processing.0"
    client = get_client(test_id)
    client.check_capture.check_processing(
        entry_point="47abcfea12",
        front_image="/9j/4AAQSkZJRgABAQEASABIAAD...",
        rear_image="/9j/4AAQSkZJRgABAQEASABIAAD...",
        check_amount=12550,
    )
    verify_request_count(test_id, "POST", "/CheckCapture/CheckProcessing", None, 1)
