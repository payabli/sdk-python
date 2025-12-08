from .conftest import get_client, verify_request_count


def test_import_import_bills() -> None:
    """Test ImportBills endpoint with WireMock"""
    test_id = "import_.import_bills.0"
    client = get_client(test_id)
    client.import_.import_bills(entry="8cfec329267", file="example_file")
    verify_request_count(test_id, "POST", "/Import/billsForm/8cfec329267", None, 1)


def test_import_import_customer() -> None:
    """Test ImportCustomer endpoint with WireMock"""
    test_id = "import_.import_customer.0"
    client = get_client(test_id)
    client.import_.import_customer(entry="8cfec329267", file="example_file")
    verify_request_count(test_id, "POST", "/Import/customersForm/8cfec329267", None, 1)


def test_import_import_vendor() -> None:
    """Test ImportVendor endpoint with WireMock"""
    test_id = "import_.import_vendor.0"
    client = get_client(test_id)
    client.import_.import_vendor(entry="8cfec329267", file="example_file")
    verify_request_count(test_id, "POST", "/Import/vendorsForm/8cfec329267", None, 1)
