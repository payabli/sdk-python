from .conftest import get_client, verify_request_count


def test_statistic_basic_stats() -> None:
    """Test BasicStats endpoint with WireMock"""
    test_id = "statistic.basic_stats.0"
    client = get_client(test_id)
    client.statistic.basic_stats(
        entry_id=1000000, freq="m", level=1, mode="ytd", end_date="2025-11-01", start_date="2025-11-30"
    )
    verify_request_count(
        test_id, "GET", "/Statistic/basic/ytd/m/1/1000000", {"endDate": "2025-11-01", "startDate": "2025-11-30"}, 1
    )


def test_statistic_customer_basic_stats() -> None:
    """Test CustomerBasicStats endpoint with WireMock"""
    test_id = "statistic.customer_basic_stats.0"
    client = get_client(test_id)
    client.statistic.customer_basic_stats(customer_id=998, freq="m", mode="ytd")
    verify_request_count(test_id, "GET", "/Statistic/customerbasic/ytd/m/998", None, 1)


def test_statistic_sub_stats() -> None:
    """Test SubStats endpoint with WireMock"""
    test_id = "statistic.sub_stats.0"
    client = get_client(test_id)
    client.statistic.sub_stats(entry_id=1000000, interval="30", level=1)
    verify_request_count(test_id, "GET", "/Statistic/subscriptions/30/1/1000000", None, 1)


def test_statistic_vendor_basic_stats() -> None:
    """Test VendorBasicStats endpoint with WireMock"""
    test_id = "statistic.vendor_basic_stats.0"
    client = get_client(test_id)
    client.statistic.vendor_basic_stats(freq="m", id_vendor=1, mode="ytd")
    verify_request_count(test_id, "GET", "/Statistic/vendorbasic/ytd/m/1", None, 1)
