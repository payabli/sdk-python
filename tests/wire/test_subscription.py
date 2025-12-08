from .conftest import get_client, verify_request_count


def test_subscription_get_subscription() -> None:
    """Test GetSubscription endpoint with WireMock"""
    test_id = "subscription.get_subscription.0"
    client = get_client(test_id)
    client.subscription.get_subscription(sub_id=263)
    verify_request_count(test_id, "GET", "/Subscription/263", None, 1)


def test_subscription_new_subscription() -> None:
    """Test NewSubscription endpoint with WireMock"""
    test_id = "subscription.new_subscription.0"
    client = get_client(test_id)
    client.subscription.new_subscription(
        customer_data={"customer_id": 4440},
        entry_point="f743aed24a",
        payment_details={"service_fee": 0, "total_amount": 100},
        payment_method={
            "cardcvv": "123",
            "cardexp": "02/25",
            "card_holder": "John Cassian",
            "cardnumber": "4111111111111111",
            "cardzip": "37615",
            "initiator": "payor",
            "method": "card",
        },
        schedule_details={"end_date": "03-20-2025", "frequency": "weekly", "plan_id": 1, "start_date": "09-20-2024"},
    )
    verify_request_count(test_id, "POST", "/Subscription/add", None, 1)


def test_subscription_remove_subscription() -> None:
    """Test RemoveSubscription endpoint with WireMock"""
    test_id = "subscription.remove_subscription.0"
    client = get_client(test_id)
    client.subscription.remove_subscription(sub_id=396)
    verify_request_count(test_id, "DELETE", "/Subscription/396", None, 1)


def test_subscription_update_subscription() -> None:
    """Test UpdateSubscription endpoint with WireMock"""
    test_id = "subscription.update_subscription.0"
    client = get_client(test_id)
    client.subscription.update_subscription(sub_id=231, set_pause=True)
    verify_request_count(test_id, "PUT", "/Subscription/231", None, 1)
