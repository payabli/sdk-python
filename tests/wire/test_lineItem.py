from .conftest import get_client, verify_request_count


def test_lineItem_add_item() -> None:
    """Test AddItem endpoint with WireMock"""
    test_id = "line_item.add_item.0"
    client = get_client(test_id)
    client.line_item.add_item(
        entry="47cae3d74",
        item_product_code="M-DEPOSIT",
        item_product_name="Materials deposit",
        item_description="Deposit for materials",
        item_commodity_code="010",
        item_unit_of_measure="SqFt",
        item_cost=12.45,
        item_qty=1,
        item_mode=0,
    )
    verify_request_count(test_id, "POST", "/LineItem/47cae3d74", None, 1)


def test_lineItem_delete_item() -> None:
    """Test DeleteItem endpoint with WireMock"""
    test_id = "line_item.delete_item.0"
    client = get_client(test_id)
    client.line_item.delete_item(line_item_id=700)
    verify_request_count(test_id, "DELETE", "/LineItem/700", None, 1)


def test_lineItem_get_item() -> None:
    """Test GetItem endpoint with WireMock"""
    test_id = "line_item.get_item.0"
    client = get_client(test_id)
    client.line_item.get_item(line_item_id=700)
    verify_request_count(test_id, "GET", "/LineItem/700", None, 1)


def test_lineItem_list_line_items() -> None:
    """Test ListLineItems endpoint with WireMock"""
    test_id = "line_item.list_line_items.0"
    client = get_client(test_id)
    client.line_item.list_line_items(entry="8cfec329267", from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/lineitems/8cfec329267",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_lineItem_update_item() -> None:
    """Test UpdateItem endpoint with WireMock"""
    test_id = "line_item.update_item.0"
    client = get_client(test_id)
    client.line_item.update_item(line_item_id=700, item_cost=12.45, item_qty=1)
    verify_request_count(test_id, "PUT", "/LineItem/700", None, 1)
