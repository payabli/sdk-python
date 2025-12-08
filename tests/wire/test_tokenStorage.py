from .conftest import get_client, verify_request_count


def test_tokenStorage_add_method() -> None:
    """Test AddMethod endpoint with WireMock"""
    test_id = "token_storage.add_method.0"
    client = get_client(test_id)
    client.token_storage.add_method(
        customer_data={"customer_id": 4440},
        entry_point="f743aed24a",
        fallback_auth=True,
        payment_method={
            "cardcvv": "123",
            "cardexp": "02/25",
            "card_holder": "John Doe",
            "cardnumber": "4111111111111111",
            "cardzip": "12345",
            "method": "card",
        },
    )
    verify_request_count(test_id, "POST", "/TokenStorage/add", None, 1)


def test_tokenStorage_get_method() -> None:
    """Test GetMethod endpoint with WireMock"""
    test_id = "token_storage.get_method.0"
    client = get_client(test_id)
    client.token_storage.get_method(
        method_id="32-8877drt00045632-678", card_expiration_format=1, include_temporary=False
    )
    verify_request_count(
        test_id,
        "GET",
        "/TokenStorage/32-8877drt00045632-678",
        {"cardExpirationFormat": "1", "includeTemporary": "false"},
        1,
    )


def test_tokenStorage_remove_method() -> None:
    """Test RemoveMethod endpoint with WireMock"""
    test_id = "token_storage.remove_method.0"
    client = get_client(test_id)
    client.token_storage.remove_method(method_id="32-8877drt00045632-678")
    verify_request_count(test_id, "DELETE", "/TokenStorage/32-8877drt00045632-678", None, 1)


def test_tokenStorage_update_method() -> None:
    """Test UpdateMethod endpoint with WireMock"""
    test_id = "token_storage.update_method.0"
    client = get_client(test_id)
    client.token_storage.update_method(
        method_id="32-8877drt00045632-678",
        customer_data={"customer_id": 4440},
        entry_point="f743aed24a",
        fallback_auth=True,
        payment_method={
            "cardcvv": "123",
            "cardexp": "02/25",
            "card_holder": "John Doe",
            "cardnumber": "4111111111111111",
            "cardzip": "12345",
            "method": "card",
        },
    )
    verify_request_count(test_id, "PUT", "/TokenStorage/32-8877drt00045632-678", None, 1)
