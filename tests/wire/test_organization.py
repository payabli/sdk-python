from .conftest import get_client, verify_request_count


def test_organization_add_organization() -> None:
    """Test AddOrganization endpoint with WireMock"""
    test_id = "organization.add_organization.0"
    client = get_client(test_id)
    client.organization.add_organization(
        idempotency_key="6B29FC40-CA47-1067-B31D-00DD010662DA",
        billing_info={
            "ach_account": "123123123",
            "ach_routing": "123123123",
            "billing_address": "123 Walnut Street",
            "billing_city": "Johnson City",
            "billing_country": "US",
            "billing_state": "TN",
            "billing_zip": "37615",
        },
        contacts=[
            {
                "contact_email": "herman@hermanscoatings.com",
                "contact_name": "Herman Martinez",
                "contact_phone": "3055550000",
                "contact_title": "Owner",
            }
        ],
        has_billing=True,
        has_residual=True,
        org_address="123 Walnut Street",
        org_city="Johnson City",
        org_country="US",
        org_entry_name="pilgrim-planner",
        org_id="123",
        org_logo={
            "f_content": "TXkgdGVzdCBmaWxlHJ==...",
            "filename": "my-doc.pdf",
            "ftype": "pdf",
            "furl": "https://mysite.com/my-doc.pdf",
        },
        org_name="Pilgrim Planner",
        org_parent_id=236,
        org_state="TN",
        org_timezone=-5,
        org_type=0,
        org_website="www.pilgrimageplanner.com",
        org_zip="37615",
        reply_to_email="email@example.com",
    )
    verify_request_count(test_id, "POST", "/Organization", None, 1)


def test_organization_delete_organization() -> None:
    """Test DeleteOrganization endpoint with WireMock"""
    test_id = "organization.delete_organization.0"
    client = get_client(test_id)
    client.organization.delete_organization(org_id=123)
    verify_request_count(test_id, "DELETE", "/Organization/123", None, 1)


def test_organization_edit_organization() -> None:
    """Test EditOrganization endpoint with WireMock"""
    test_id = "organization.edit_organization.0"
    client = get_client(test_id)
    client.organization.edit_organization(
        org_id=123,
        contacts=[
            {
                "contact_email": "herman@hermanscoatings.com",
                "contact_name": "Herman Martinez",
                "contact_phone": "3055550000",
                "contact_title": "Owner",
            }
        ],
        org_address="123 Walnut Street",
        org_city="Johnson City",
        org_country="US",
        org_entry_name="pilgrim-planner",
        organization_data_org_id="123",
        org_name="Pilgrim Planner",
        org_state="TN",
        org_timezone=-5,
        org_type=0,
        org_website="www.pilgrimageplanner.com",
        org_zip="37615",
    )
    verify_request_count(test_id, "PUT", "/Organization/123", None, 1)


def test_organization_get_basic_organization() -> None:
    """Test GetBasicOrganization endpoint with WireMock"""
    test_id = "organization.get_basic_organization.0"
    client = get_client(test_id)
    client.organization.get_basic_organization(entry="8cfec329267")
    verify_request_count(test_id, "GET", "/Organization/basic/8cfec329267", None, 1)


def test_organization_get_basic_organization_by_id() -> None:
    """Test GetBasicOrganizationById endpoint with WireMock"""
    test_id = "organization.get_basic_organization_by_id.0"
    client = get_client(test_id)
    client.organization.get_basic_organization_by_id(org_id=123)
    verify_request_count(test_id, "GET", "/Organization/basicById/123", None, 1)


def test_organization_get_organization() -> None:
    """Test GetOrganization endpoint with WireMock"""
    test_id = "organization.get_organization.0"
    client = get_client(test_id)
    client.organization.get_organization(org_id=123)
    verify_request_count(test_id, "GET", "/Organization/read/123", None, 1)


def test_organization_get_settings_organization() -> None:
    """Test GetSettingsOrganization endpoint with WireMock"""
    test_id = "organization.get_settings_organization.0"
    client = get_client(test_id)
    client.organization.get_settings_organization(org_id=123)
    verify_request_count(test_id, "GET", "/Organization/settings/123", None, 1)
