from datetime import datetime
from uuid import UUID

from .conftest import get_client, verify_request_count


def test_notificationlogs_search_notification_logs() -> None:
    """Test searchNotificationLogs endpoint with WireMock"""
    test_id = "notificationlogs.search_notification_logs.0"
    client = get_client(test_id)
    client.notificationlogs.search_notification_logs(
        page_size=20,
        start_date=datetime.fromisoformat("2024-01-01T00:00:00Z"),
        end_date=datetime.fromisoformat("2024-01-31T23:59:59Z"),
        org_id=12345,
        notification_event="ActivatedMerchant",
        succeeded=True,
    )
    verify_request_count(test_id, "POST", "/v2/notificationlogs", {"PageSize": "20"}, 1)


def test_notificationlogs_get_notification_log() -> None:
    """Test getNotificationLog endpoint with WireMock"""
    test_id = "notificationlogs.get_notification_log.0"
    client = get_client(test_id)
    client.notificationlogs.get_notification_log(uuid_=UUID("550e8400-e29b-41d4-a716-446655440000"))
    verify_request_count(test_id, "GET", "/v2/notificationlogs/550e8400-e29b-41d4-a716-446655440000", None, 1)


def test_notificationlogs_retry_notification_log() -> None:
    """Test retryNotificationLog endpoint with WireMock"""
    test_id = "notificationlogs.retry_notification_log.0"
    client = get_client(test_id)
    client.notificationlogs.retry_notification_log(uuid_=UUID("550e8400-e29b-41d4-a716-446655440000"))
    verify_request_count(test_id, "GET", "/v2/notificationlogs/550e8400-e29b-41d4-a716-446655440000/retry", None, 1)


def test_notificationlogs_bulk_retry_notification_logs() -> None:
    """Test bulkRetryNotificationLogs endpoint with WireMock"""
    test_id = "notificationlogs.bulk_retry_notification_logs.0"
    client = get_client(test_id)
    client.notificationlogs.bulk_retry_notification_logs(
        request=[
            UUID("550e8400-e29b-41d4-a716-446655440000"),
            UUID("550e8400-e29b-41d4-a716-446655440001"),
            UUID("550e8400-e29b-41d4-a716-446655440002"),
        ]
    )
    verify_request_count(test_id, "POST", "/v2/notificationlogs/retry", None, 1)
