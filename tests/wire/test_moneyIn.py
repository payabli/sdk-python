from .conftest import get_client, verify_request_count


def test_moneyIn_authorize() -> None:
    """Test Authorize endpoint with WireMock"""
    test_id = "money_in.authorize.0"
    client = get_client(test_id)
    client.money_in.authorize(
        customer_data={"customer_id": 4440},
        entry_point="f743aed24a",
        ipaddress="255.255.255.255",
        payment_details={"service_fee": 0, "total_amount": 100},
        payment_method={
            "cardcvv": "999",
            "cardexp": "02/27",
            "card_holder": "John Cassian",
            "cardnumber": "4111111111111111",
            "cardzip": "12345",
            "initiator": "payor",
            "method": "card",
        },
    )
    verify_request_count(test_id, "POST", "/MoneyIn/authorize", None, 1)


def test_moneyIn_capture() -> None:
    """Test Capture endpoint with WireMock"""
    test_id = "money_in.capture.0"
    client = get_client(test_id)
    client.money_in.capture(trans_id="10-7d9cd67d-2d5d-4cd7-a1b7-72b8b201ec13", amount=0)
    verify_request_count(test_id, "GET", "/MoneyIn/capture/10-7d9cd67d-2d5d-4cd7-a1b7-72b8b201ec13/0", None, 1)


def test_moneyIn_capture_auth() -> None:
    """Test CaptureAuth endpoint with WireMock"""
    test_id = "money_in.capture_auth.0"
    client = get_client(test_id)
    client.money_in.capture_auth(
        trans_id="10-7d9cd67d-2d5d-4cd7-a1b7-72b8b201ec13", payment_details={"total_amount": 105, "service_fee": 5}
    )
    verify_request_count(test_id, "POST", "/MoneyIn/capture/10-7d9cd67d-2d5d-4cd7-a1b7-72b8b201ec13", None, 1)


def test_moneyIn_credit() -> None:
    """Test Credit endpoint with WireMock"""
    test_id = "money_in.credit.0"
    client = get_client(test_id)
    client.money_in.credit(
        idempotency_key="6B29FC40-CA47-1067-B31D-00DD010662DA",
        customer_data={"billing_address_1": "5127 Linkwood ave", "customer_number": "100"},
        entrypoint="my-entrypoint",
        payment_details={"service_fee": 0, "total_amount": 1},
        payment_method={
            "ach_account": "88354454",
            "ach_account_type": "Checking",
            "ach_holder": "John Smith",
            "ach_routing": "021000021",
            "method": "ach",
        },
    )
    verify_request_count(test_id, "POST", "/MoneyIn/makecredit", None, 1)


def test_moneyIn_details() -> None:
    """Test Details endpoint with WireMock"""
    test_id = "money_in.details.0"
    client = get_client(test_id)
    client.money_in.details(trans_id="45-as456777hhhhhhhhhh77777777-324")
    verify_request_count(test_id, "GET", "/MoneyIn/details/45-as456777hhhhhhhhhh77777777-324", None, 1)


def test_moneyIn_getpaid() -> None:
    """Test getpaid endpoint with WireMock"""
    test_id = "money_in.getpaid.0"
    client = get_client(test_id)
    client.money_in.getpaid(
        customer_data={"customer_id": 4440},
        entry_point="f743aed24a",
        ipaddress="255.255.255.255",
        payment_details={"service_fee": 0, "total_amount": 100},
        payment_method={
            "cardcvv": "999",
            "cardexp": "02/27",
            "card_holder": "John Cassian",
            "cardnumber": "4111111111111111",
            "cardzip": "12345",
            "initiator": "payor",
            "method": "card",
        },
    )
    verify_request_count(test_id, "POST", "/MoneyIn/getpaid", None, 1)


def test_moneyIn_reverse() -> None:
    """Test Reverse endpoint with WireMock"""
    test_id = "money_in.reverse.0"
    client = get_client(test_id)
    client.money_in.reverse(amount=0, trans_id="10-3ffa27df-b171-44e0-b251-e95fbfc7a723")
    verify_request_count(test_id, "GET", "/MoneyIn/reverse/10-3ffa27df-b171-44e0-b251-e95fbfc7a723/0", None, 1)


def test_moneyIn_refund() -> None:
    """Test Refund endpoint with WireMock"""
    test_id = "money_in.refund.0"
    client = get_client(test_id)
    client.money_in.refund(amount=0, trans_id="10-3ffa27df-b171-44e0-b251-e95fbfc7a723")
    verify_request_count(test_id, "GET", "/MoneyIn/refund/10-3ffa27df-b171-44e0-b251-e95fbfc7a723/0", None, 1)


def test_moneyIn_refund_with_instructions() -> None:
    """Test RefundWithInstructions endpoint with WireMock"""
    test_id = "money_in.refund_with_instructions.0"
    client = get_client(test_id)
    client.money_in.refund_with_instructions(
        trans_id="10-3ffa27df-b171-44e0-b251-e95fbfc7a723",
        idempotency_key="8A29FC40-CA47-1067-B31D-00DD010662DB",
        source="api",
        order_description="Materials deposit",
        amount=100,
        refund_details={
            "split_refunding": [
                {
                    "origination_entry_point": "7f1a381696",
                    "account_id": "187-342",
                    "description": "Refunding undelivered materials",
                    "amount": 60,
                },
                {
                    "origination_entry_point": "7f1a381696",
                    "account_id": "187-343",
                    "description": "Refunding deposit for undelivered materials",
                    "amount": 40,
                },
            ]
        },
    )
    verify_request_count(test_id, "POST", "/MoneyIn/refund/10-3ffa27df-b171-44e0-b251-e95fbfc7a723", None, 1)


def test_moneyIn_reverse_credit() -> None:
    """Test ReverseCredit endpoint with WireMock"""
    test_id = "money_in.reverse_credit.0"
    client = get_client(test_id)
    client.money_in.reverse_credit(trans_id="45-as456777hhhhhhhhhh77777777-324")
    verify_request_count(test_id, "GET", "/MoneyIn/reverseCredit/45-as456777hhhhhhhhhh77777777-324", None, 1)


def test_moneyIn_send_receipt_2_trans() -> None:
    """Test SendReceipt2Trans endpoint with WireMock"""
    test_id = "money_in.send_receipt_2_trans.0"
    client = get_client(test_id)
    client.money_in.send_receipt_2_trans(trans_id="45-as456777hhhhhhhhhh77777777-324", email="example@email.com")
    verify_request_count(
        test_id, "GET", "/MoneyIn/sendreceipt/45-as456777hhhhhhhhhh77777777-324", {"email": "example@email.com"}, 1
    )


def test_moneyIn_validate() -> None:
    """Test Validate endpoint with WireMock"""
    test_id = "money_in.validate.0"
    client = get_client(test_id)
    client.money_in.validate(
        idempotency_key="6B29FC40-CA47-1067-B31D-00DD010662DA",
        entry_point="entry132",
        payment_method={
            "method": "card",
            "cardnumber": "4360000001000005",
            "cardexp": "12/29",
            "cardzip": "14602-8328",
            "card_holder": "Dianne Becker-Smith",
        },
    )
    verify_request_count(test_id, "POST", "/MoneyIn/validate", None, 1)


def test_moneyIn_void() -> None:
    """Test Void endpoint with WireMock"""
    test_id = "money_in.void.0"
    client = get_client(test_id)
    client.money_in.void(trans_id="10-3ffa27df-b171-44e0-b251-e95fbfc7a723")
    verify_request_count(test_id, "GET", "/MoneyIn/void/10-3ffa27df-b171-44e0-b251-e95fbfc7a723", None, 1)
