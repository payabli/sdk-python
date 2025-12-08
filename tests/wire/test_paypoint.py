from .conftest import get_client, verify_request_count


def test_paypoint_get_basic_entry() -> None:
    """Test getBasicEntry endpoint with WireMock"""
    test_id = "paypoint.get_basic_entry.0"
    client = get_client(test_id)
    client.paypoint.get_basic_entry(entry="8cfec329267")
    verify_request_count(test_id, "GET", "/Paypoint/basic/8cfec329267", None, 1)


def test_paypoint_get_basic_entry_by_id() -> None:
    """Test getBasicEntryById endpoint with WireMock"""
    test_id = "paypoint.get_basic_entry_by_id.0"
    client = get_client(test_id)
    client.paypoint.get_basic_entry_by_id(id_paypoint="198")
    verify_request_count(test_id, "GET", "/Paypoint/basicById/198", None, 1)


def test_paypoint_get_entry_config() -> None:
    """Test getEntryConfig endpoint with WireMock"""
    test_id = "paypoint.get_entry_config.0"
    client = get_client(test_id)
    client.paypoint.get_entry_config(entry="8cfec329267")
    verify_request_count(test_id, "GET", "/Paypoint/8cfec329267", None, 1)


def test_paypoint_get_page() -> None:
    """Test getPage endpoint with WireMock"""
    test_id = "paypoint.get_page.0"
    client = get_client(test_id)
    client.paypoint.get_page(entry="8cfec329267", subdomain="pay-your-fees-1")
    verify_request_count(test_id, "GET", "/Paypoint/8cfec329267/pay-your-fees-1", None, 1)


def test_paypoint_remove_page() -> None:
    """Test removePage endpoint with WireMock"""
    test_id = "paypoint.remove_page.0"
    client = get_client(test_id)
    client.paypoint.remove_page(entry="8cfec329267", subdomain="pay-your-fees-1")
    verify_request_count(test_id, "DELETE", "/Paypoint/8cfec329267/pay-your-fees-1", None, 1)


def test_paypoint_save_logo() -> None:
    """Test saveLogo endpoint with WireMock"""
    test_id = "paypoint.save_logo.0"
    client = get_client(test_id)
    client.paypoint.save_logo(entry="8cfec329267")
    verify_request_count(test_id, "PUT", "/Paypoint/logo/8cfec329267", None, 1)


def test_paypoint_settings_page() -> None:
    """Test settingsPage endpoint with WireMock"""
    test_id = "paypoint.settings_page.0"
    client = get_client(test_id)
    client.paypoint.settings_page(entry="8cfec329267")
    verify_request_count(test_id, "GET", "/Paypoint/settings/8cfec329267", None, 1)


def test_paypoint_migrate() -> None:
    """Test migrate endpoint with WireMock"""
    test_id = "paypoint.migrate.0"
    client = get_client(test_id)
    client.paypoint.migrate(
        entry_point="473abc123def",
        new_parent_organization_id=123,
        notification_request={
            "notification_url": "https://webhook-test.yoursie.com",
            "web_header_parameters": [{"key": "testheader", "value": "1234567890"}],
        },
    )
    verify_request_count(test_id, "POST", "/Paypoint/migrate", None, 1)
