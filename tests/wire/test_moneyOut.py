from .conftest import get_client, verify_request_count


def test_moneyOut_authorize_out() -> None:
    """Test AuthorizeOut endpoint with WireMock"""
    test_id = "money_out.authorize_out.0"
    client = get_client(test_id)
    client.money_out.authorize_out(
        entry_point="48acde49",
        invoice_data=[{"bill_id": 54323}],
        order_description="Window Painting",
        payment_details={"total_amount": 47, "unbundled": False},
        payment_method={"method": "managed"},
        vendor_data={"vendor_number": "7895433"},
    )
    verify_request_count(test_id, "POST", "/MoneyOut/authorize", None, 1)


def test_moneyOut_cancel_all_out() -> None:
    """Test CancelAllOut endpoint with WireMock"""
    test_id = "money_out.cancel_all_out.0"
    client = get_client(test_id)
    client.money_out.cancel_all_out(request=["2-29", "2-28", "2-27"])
    verify_request_count(test_id, "POST", "/MoneyOut/cancelAll", None, 1)


def test_moneyOut_cancel_out_get() -> None:
    """Test CancelOutGet endpoint with WireMock"""
    test_id = "money_out.cancel_out_get.0"
    client = get_client(test_id)
    client.money_out.cancel_out_get(reference_id="129-219")
    verify_request_count(test_id, "GET", "/MoneyOut/cancel/129-219", None, 1)


def test_moneyOut_cancel_out_delete() -> None:
    """Test CancelOutDelete endpoint with WireMock"""
    test_id = "money_out.cancel_out_delete.0"
    client = get_client(test_id)
    client.money_out.cancel_out_delete(reference_id="129-219")
    verify_request_count(test_id, "DELETE", "/MoneyOut/cancel/129-219", None, 1)


def test_moneyOut_capture_all_out() -> None:
    """Test CaptureAllOut endpoint with WireMock"""
    test_id = "money_out.capture_all_out.0"
    client = get_client(test_id)
    client.money_out.capture_all_out(request=["2-29", "2-28", "2-27"])
    verify_request_count(test_id, "POST", "/MoneyOut/captureAll", None, 1)


def test_moneyOut_capture_out() -> None:
    """Test CaptureOut endpoint with WireMock"""
    test_id = "money_out.capture_out.0"
    client = get_client(test_id)
    client.money_out.capture_out(reference_id="129-219")
    verify_request_count(test_id, "GET", "/MoneyOut/capture/129-219", None, 1)


def test_moneyOut_payout_details() -> None:
    """Test PayoutDetails endpoint with WireMock"""
    test_id = "money_out.payout_details.0"
    client = get_client(test_id)
    client.money_out.payout_details(trans_id="45-as456777hhhhhhhhhh77777777-324")
    verify_request_count(test_id, "GET", "/MoneyOut/details/45-as456777hhhhhhhhhh77777777-324", None, 1)


def test_moneyOut_v_card_get() -> None:
    """Test VCardGet endpoint with WireMock"""
    test_id = "money_out.v_card_get.0"
    client = get_client(test_id)
    client.money_out.v_card_get(card_token="20230403315245421165")
    verify_request_count(test_id, "GET", "/MoneyOut/vcard/20230403315245421165", None, 1)


def test_moneyOut_send_v_card_link() -> None:
    """Test SendVCardLink endpoint with WireMock"""
    test_id = "money_out.send_v_card_link.0"
    client = get_client(test_id)
    client.money_out.send_v_card_link(trans_id="01K33Z6YQZ6GD5QVKZ856MJBSC")
    verify_request_count(test_id, "POST", "/vcard/send-card-link", None, 1)


def test_moneyOut_get_check_image() -> None:
    """Test GetCheckImage endpoint with WireMock"""
    test_id = "money_out.get_check_image.0"
    client = get_client(test_id)
    client.money_out.get_check_image(asset_name="check133832686289732320_01JKBNZ5P32JPTZY8XXXX000000.pdf")
    verify_request_count(
        test_id, "GET", "/MoneyOut/checkimage/check133832686289732320_01JKBNZ5P32JPTZY8XXXX000000.pdf", None, 1
    )
