from .conftest import get_client, verify_request_count


def test_hostedPaymentPages_load_page() -> None:
    """Test loadPage endpoint with WireMock"""
    test_id = "hosted_payment_pages.load_page.0"
    client = get_client(test_id)
    client.hosted_payment_pages.load_page(entry="8cfec329267", subdomain="pay-your-fees-1")
    verify_request_count(test_id, "GET", "/Paypoint/load/8cfec329267/pay-your-fees-1", None, 1)


def test_hostedPaymentPages_new_page() -> None:
    """Test newPage endpoint with WireMock"""
    test_id = "hosted_payment_pages.new_page.0"
    client = get_client(test_id)
    client.hosted_payment_pages.new_page(entry="8cfec329267", idempotency_key="6B29FC40-CA47-1067-B31D-00DD010662DA")
    verify_request_count(test_id, "POST", "/Paypoint/8cfec329267", None, 1)


def test_hostedPaymentPages_save_page() -> None:
    """Test savePage endpoint with WireMock"""
    test_id = "hosted_payment_pages.save_page.0"
    client = get_client(test_id)
    client.hosted_payment_pages.save_page(entry="8cfec329267", subdomain="pay-your-fees-1")
    verify_request_count(test_id, "PUT", "/Paypoint/8cfec329267/pay-your-fees-1", None, 1)
