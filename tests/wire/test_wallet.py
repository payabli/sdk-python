from .conftest import get_client, verify_request_count


def test_wallet_configure_apple_pay_organization() -> None:
    """Test ConfigureApplePayOrganization endpoint with WireMock"""
    test_id = "wallet.configure_apple_pay_organization.0"
    client = get_client(test_id)
    client.wallet.configure_apple_pay_organization(cascade=True, is_enabled=True, org_id=901)
    verify_request_count(test_id, "POST", "/Wallet/applepay/configure-organization", None, 1)


def test_wallet_configure_apple_pay_paypoint() -> None:
    """Test ConfigureApplePayPaypoint endpoint with WireMock"""
    test_id = "wallet.configure_apple_pay_paypoint.0"
    client = get_client(test_id)
    client.wallet.configure_apple_pay_paypoint(entry="8cfec329267", is_enabled=True)
    verify_request_count(test_id, "POST", "/Wallet/applepay/configure-paypoint", None, 1)


def test_wallet_configure_google_pay_organization() -> None:
    """Test ConfigureGooglePayOrganization endpoint with WireMock"""
    test_id = "wallet.configure_google_pay_organization.0"
    client = get_client(test_id)
    client.wallet.configure_google_pay_organization(cascade=True, is_enabled=True, org_id=901)
    verify_request_count(test_id, "POST", "/Wallet/googlepay/configure-organization", None, 1)


def test_wallet_configure_google_pay_paypoint() -> None:
    """Test ConfigureGooglePayPaypoint endpoint with WireMock"""
    test_id = "wallet.configure_google_pay_paypoint.0"
    client = get_client(test_id)
    client.wallet.configure_google_pay_paypoint(entry="8cfec329267", is_enabled=True)
    verify_request_count(test_id, "POST", "/Wallet/googlepay/configure-paypoint", None, 1)
