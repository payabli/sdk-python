from .conftest import get_client, verify_request_count


def test_notification_add_notification() -> None:
    """Test AddNotification endpoint with WireMock"""
    test_id = "notification.add_notification.0"
    client = get_client(test_id)
    client.notification.add_notification(
        request={
            "content": {"event_type": "CreatedApplication"},
            "frequency": "untilcancelled",
            "method": "web",
            "owner_id": "236",
            "owner_type": 0,
            "status": 1,
            "target": "https://webhook.site/2871b8f8-edc7-441a-b376-98d8c8e33275",
        }
    )
    verify_request_count(test_id, "POST", "/Notification", None, 1)


def test_notification_delete_notification() -> None:
    """Test DeleteNotification endpoint with WireMock"""
    test_id = "notification.delete_notification.0"
    client = get_client(test_id)
    client.notification.delete_notification(n_id="1717")
    verify_request_count(test_id, "DELETE", "/Notification/1717", None, 1)


def test_notification_get_notification() -> None:
    """Test GetNotification endpoint with WireMock"""
    test_id = "notification.get_notification.0"
    client = get_client(test_id)
    client.notification.get_notification(n_id="1717")
    verify_request_count(test_id, "GET", "/Notification/1717", None, 1)


def test_notification_update_notification() -> None:
    """Test UpdateNotification endpoint with WireMock"""
    test_id = "notification.update_notification.0"
    client = get_client(test_id)
    client.notification.update_notification(
        n_id="1717",
        request={
            "content": {"event_type": "ApprovedPayment"},
            "frequency": "untilcancelled",
            "method": "email",
            "owner_id": "136",
            "owner_type": 0,
            "status": 1,
            "target": "newemail@email.com",
        },
    )
    verify_request_count(test_id, "PUT", "/Notification/1717", None, 1)


def test_notification_get_report_file() -> None:
    """Test GetReportFile endpoint with WireMock"""
    test_id = "notification.get_report_file.0"
    client = get_client(test_id)
    client.notification.get_report_file(id=1000000)
    verify_request_count(test_id, "GET", "/Export/notificationReport/1000000", None, 1)
