from .conftest import get_client, verify_request_count


def test_customer_add_customer() -> None:
    """Test AddCustomer endpoint with WireMock"""
    test_id = "customer.add_customer.0"
    client = get_client(test_id)
    client.customer.add_customer(
        entry="8cfec329267",
        customer_number="12356ACB",
        firstname="Irene",
        lastname="Canizales",
        address_1="123 Bishop's Trail",
        city="Mountain City",
        state="TN",
        zip="37612",
        country="US",
        email="irene@canizalesconcrete.com",
        identifier_fields=["email"],
        time_zone=-5,
    )
    verify_request_count(test_id, "POST", "/Customer/single/8cfec329267", None, 1)


def test_customer_delete_customer() -> None:
    """Test DeleteCustomer endpoint with WireMock"""
    test_id = "customer.delete_customer.0"
    client = get_client(test_id)
    client.customer.delete_customer(customer_id=998)
    verify_request_count(test_id, "DELETE", "/Customer/998", None, 1)


def test_customer_get_customer() -> None:
    """Test GetCustomer endpoint with WireMock"""
    test_id = "customer.get_customer.0"
    client = get_client(test_id)
    client.customer.get_customer(customer_id=998)
    verify_request_count(test_id, "GET", "/Customer/998", None, 1)


def test_customer_link_customer_transaction() -> None:
    """Test LinkCustomerTransaction endpoint with WireMock"""
    test_id = "customer.link_customer_transaction.0"
    client = get_client(test_id)
    client.customer.link_customer_transaction(customer_id=998, trans_id="45-as456777hhhhhhhhhh77777777-324")
    verify_request_count(test_id, "GET", "/Customer/link/998/45-as456777hhhhhhhhhh77777777-324", None, 1)


def test_customer_request_consent() -> None:
    """Test RequestConsent endpoint with WireMock"""
    test_id = "customer.request_consent.0"
    client = get_client(test_id)
    client.customer.request_consent(customer_id=998)
    verify_request_count(test_id, "POST", "/Customer/998/consent", None, 1)


def test_customer_update_customer() -> None:
    """Test UpdateCustomer endpoint with WireMock"""
    test_id = "customer.update_customer.0"
    client = get_client(test_id)
    client.customer.update_customer(
        customer_id=998,
        firstname="Irene",
        lastname="Canizales",
        address_1="145 Bishop's Trail",
        city="Mountain City",
        state="TN",
        zip="37612",
        country="US",
    )
    verify_request_count(test_id, "PUT", "/Customer/998", None, 1)
