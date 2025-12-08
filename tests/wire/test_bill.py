from datetime import date

from .conftest import get_client, verify_request_count


def test_bill_add_bill() -> None:
    """Test AddBill endpoint with WireMock"""
    test_id = "bill.add_bill.0"
    client = get_client(test_id)
    client.bill.add_bill(
        entry="8cfec329267",
        bill_number="ABC-123",
        net_amount=3762.87,
        bill_date=date.fromisoformat("2024-07-01"),
        due_date=date.fromisoformat("2024-07-01"),
        comments="Deposit for materials",
        bill_items=[
            {
                "item_product_code": "M-DEPOSIT",
                "item_product_name": "Materials deposit",
                "item_description": "Deposit for materials",
                "item_commodity_code": "010",
                "item_unit_of_measure": "SqFt",
                "item_cost": 5,
                "item_qty": 1,
                "item_mode": 0,
                "item_categories": ["deposits"],
                "item_total_amount": 123,
                "item_tax_amount": 7,
                "item_tax_rate": 0.075,
            }
        ],
        mode=0,
        accounting_field_1="MyInternalId",
        vendor={"vendor_number": "1234-A"},
        end_date=date.fromisoformat("2024-07-01"),
        frequency="monthly",
        terms="NET30",
        status=-99,
        attachments=[{"ftype": "pdf", "filename": "my-doc.pdf", "furl": "https://mysite.com/my-doc.pdf"}],
    )
    verify_request_count(test_id, "POST", "/Bill/single/8cfec329267", None, 1)


def test_bill_delete_attached_from_bill() -> None:
    """Test deleteAttachedFromBill endpoint with WireMock"""
    test_id = "bill.delete_attached_from_bill.0"
    client = get_client(test_id)
    client.bill.delete_attached_from_bill(filename="0_Bill.pdf", id_bill=285)
    verify_request_count(test_id, "DELETE", "/Bill/attachedFileFromBill/285/0_Bill.pdf", None, 1)


def test_bill_delete_bill() -> None:
    """Test DeleteBill endpoint with WireMock"""
    test_id = "bill.delete_bill.0"
    client = get_client(test_id)
    client.bill.delete_bill(id_bill=285)
    verify_request_count(test_id, "DELETE", "/Bill/285", None, 1)


def test_bill_edit_bill() -> None:
    """Test EditBill endpoint with WireMock"""
    test_id = "bill.edit_bill.0"
    client = get_client(test_id)
    client.bill.edit_bill(id_bill=285, net_amount=3762.87, bill_date=date.fromisoformat("2025-07-01"))
    verify_request_count(test_id, "PUT", "/Bill/285", None, 1)


def test_bill_get_attached_from_bill() -> None:
    """Test getAttachedFromBill endpoint with WireMock"""
    test_id = "bill.get_attached_from_bill.0"
    client = get_client(test_id)
    client.bill.get_attached_from_bill(filename="0_Bill.pdf", id_bill=285, return_object=True)
    verify_request_count(test_id, "GET", "/Bill/attachedFileFromBill/285/0_Bill.pdf", {"returnObject": "true"}, 1)


def test_bill_get_bill() -> None:
    """Test GetBill endpoint with WireMock"""
    test_id = "bill.get_bill.0"
    client = get_client(test_id)
    client.bill.get_bill(id_bill=285)
    verify_request_count(test_id, "GET", "/Bill/285", None, 1)


def test_bill_list_bills() -> None:
    """Test ListBills endpoint with WireMock"""
    test_id = "bill.list_bills.0"
    client = get_client(test_id)
    client.bill.list_bills(entry="8cfec329267", from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/bills/8cfec329267",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_bill_list_bills_org() -> None:
    """Test ListBillsOrg endpoint with WireMock"""
    test_id = "bill.list_bills_org.0"
    client = get_client(test_id)
    client.bill.list_bills_org(org_id=123, from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/bills/org/123",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_bill_modify_approval_bill() -> None:
    """Test ModifyApprovalBill endpoint with WireMock"""
    test_id = "bill.modify_approval_bill.0"
    client = get_client(test_id)
    client.bill.modify_approval_bill(id_bill=285, request=["string"])
    verify_request_count(test_id, "PUT", "/Bill/approval/285", None, 1)


def test_bill_send_to_approval_bill() -> None:
    """Test SendToApprovalBill endpoint with WireMock"""
    test_id = "bill.send_to_approval_bill.0"
    client = get_client(test_id)
    client.bill.send_to_approval_bill(
        id_bill=285, idempotency_key="6B29FC40-CA47-1067-B31D-00DD010662DA", request=["string"]
    )
    verify_request_count(test_id, "POST", "/Bill/approval/285", None, 1)


def test_bill_set_approved_bill() -> None:
    """Test SetApprovedBill endpoint with WireMock"""
    test_id = "bill.set_approved_bill.0"
    client = get_client(test_id)
    client.bill.set_approved_bill(approved="true", id_bill=285)
    verify_request_count(test_id, "GET", "/Bill/approval/285/true", None, 1)
