from .conftest import get_client, verify_request_count


def test_vendor_add_vendor() -> None:
    """Test AddVendor endpoint with WireMock"""
    test_id = "vendor.add_vendor.0"
    client = get_client(test_id)
    client.vendor.add_vendor(
        entry="8cfec329267",
        vendor_number="1234",
        name_1="Herman's Coatings and Masonry",
        name_2="<string>",
        ein="12-3456789",
        phone="5555555555",
        email="example@email.com",
        address_1="123 Ocean Drive",
        address_2="Suite 400",
        city="Miami",
        state="FL",
        zip="33139",
        country="US",
        mcc="7777",
        location_code="MIA123",
        contacts=[
            {
                "contact_name": "Herman Martinez",
                "contact_email": "example@email.com",
                "contact_title": "Owner",
                "contact_phone": "3055550000",
            }
        ],
        billing_data={
            "id": 123,
            "bank_name": "Country Bank",
            "routing_account": "123123123",
            "account_number": "123123123",
            "type_account": "Checking",
            "bank_account_holder_name": "Gruzya Adventure Outfitters LLC",
            "bank_account_holder_type": "Business",
            "bank_account_function": 0,
        },
        payment_method="managed",
        vendor_status=1,
        remit_address_1="123 Walnut Street",
        remit_address_2="Suite 900",
        remit_city="Miami",
        remit_state="FL",
        remit_zip="31113",
        remit_country="US",
        payee_name_1="<string>",
        payee_name_2="<string>",
        customer_vendor_account="A-37622",
        internal_reference_id=123,
    )
    verify_request_count(test_id, "POST", "/Vendor/single/8cfec329267", None, 1)


def test_vendor_delete_vendor() -> None:
    """Test DeleteVendor endpoint with WireMock"""
    test_id = "vendor.delete_vendor.0"
    client = get_client(test_id)
    client.vendor.delete_vendor(id_vendor=1)
    verify_request_count(test_id, "DELETE", "/Vendor/1", None, 1)


def test_vendor_edit_vendor() -> None:
    """Test EditVendor endpoint with WireMock"""
    test_id = "vendor.edit_vendor.0"
    client = get_client(test_id)
    client.vendor.edit_vendor(id_vendor=1, name_1="Theodore's Janitorial")
    verify_request_count(test_id, "PUT", "/Vendor/1", None, 1)


def test_vendor_get_vendor() -> None:
    """Test GetVendor endpoint with WireMock"""
    test_id = "vendor.get_vendor.0"
    client = get_client(test_id)
    client.vendor.get_vendor(id_vendor=1)
    verify_request_count(test_id, "GET", "/Vendor/1", None, 1)
