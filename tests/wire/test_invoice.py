from datetime import date

from .conftest import get_client, verify_request_count


def test_invoice_add_invoice() -> None:
    """Test AddInvoice endpoint with WireMock"""
    test_id = "invoice.add_invoice.0"
    client = get_client(test_id)
    client.invoice.add_invoice(
        entry="8cfec329267",
        customer_data={"first_name": "Tamara", "last_name": "Bagratoni", "customer_number": "3"},
        invoice_data={
            "items": [
                {
                    "item_product_name": "Adventure Consult",
                    "item_description": "Consultation for Georgian tours",
                    "item_cost": 100,
                    "item_qty": 1,
                    "item_mode": 1,
                },
                {
                    "item_product_name": "Deposit ",
                    "item_description": "Deposit for trip planning",
                    "item_cost": 882.37,
                    "item_qty": 1,
                },
            ],
            "invoice_date": date.fromisoformat("2025-10-19"),
            "invoice_type": 0,
            "invoice_status": 1,
            "frequency": "one-time",
            "invoice_amount": 982.37,
            "discount": 10,
            "invoice_number": "INV-3",
        },
    )
    verify_request_count(test_id, "POST", "/Invoice/8cfec329267", None, 1)


def test_invoice_delete_attached_from_invoice() -> None:
    """Test deleteAttachedFromInvoice endpoint with WireMock"""
    test_id = "invoice.delete_attached_from_invoice.0"
    client = get_client(test_id)
    client.invoice.delete_attached_from_invoice(filename="0_Bill.pdf", id_invoice=23548884)
    verify_request_count(test_id, "DELETE", "/Invoice/attachedFileFromInvoice/23548884/0_Bill.pdf", None, 1)


def test_invoice_delete_invoice() -> None:
    """Test DeleteInvoice endpoint with WireMock"""
    test_id = "invoice.delete_invoice.0"
    client = get_client(test_id)
    client.invoice.delete_invoice(id_invoice=23548884)
    verify_request_count(test_id, "DELETE", "/Invoice/23548884", None, 1)


def test_invoice_edit_invoice() -> None:
    """Test EditInvoice endpoint with WireMock"""
    test_id = "invoice.edit_invoice.0"
    client = get_client(test_id)
    client.invoice.edit_invoice(
        id_invoice=332,
        invoice_data={
            "items": [
                {
                    "item_product_name": "Deposit",
                    "item_description": "Deposit for trip planning",
                    "item_cost": 882.37,
                    "item_qty": 1,
                }
            ],
            "invoice_date": date.fromisoformat("2025-10-19"),
            "invoice_amount": 982.37,
            "invoice_number": "INV-6",
        },
    )
    verify_request_count(test_id, "PUT", "/Invoice/332", None, 1)


def test_invoice_get_attached_file_from_invoice() -> None:
    """Test GetAttachedFileFromInvoice endpoint with WireMock"""
    test_id = "invoice.get_attached_file_from_invoice.0"
    client = get_client(test_id)
    client.invoice.get_attached_file_from_invoice(id_invoice=1, filename="filename")
    verify_request_count(test_id, "GET", "/Invoice/attachedFileFromInvoice/1/filename", None, 1)


def test_invoice_get_invoice() -> None:
    """Test GetInvoice endpoint with WireMock"""
    test_id = "invoice.get_invoice.0"
    client = get_client(test_id)
    client.invoice.get_invoice(id_invoice=23548884)
    verify_request_count(test_id, "GET", "/Invoice/23548884", None, 1)


def test_invoice_get_invoice_number() -> None:
    """Test GetInvoiceNumber endpoint with WireMock"""
    test_id = "invoice.get_invoice_number.0"
    client = get_client(test_id)
    client.invoice.get_invoice_number(entry="8cfec329267")
    verify_request_count(test_id, "GET", "/Invoice/getNumber/8cfec329267", None, 1)


def test_invoice_list_invoices() -> None:
    """Test ListInvoices endpoint with WireMock"""
    test_id = "invoice.list_invoices.0"
    client = get_client(test_id)
    client.invoice.list_invoices(entry="8cfec329267", from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/invoices/8cfec329267",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_invoice_list_invoices_org() -> None:
    """Test ListInvoicesOrg endpoint with WireMock"""
    test_id = "invoice.list_invoices_org.0"
    client = get_client(test_id)
    client.invoice.list_invoices_org(org_id=123, from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/invoices/org/123",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_invoice_send_invoice() -> None:
    """Test SendInvoice endpoint with WireMock"""
    test_id = "invoice.send_invoice.0"
    client = get_client(test_id)
    client.invoice.send_invoice(id_invoice=23548884, attachfile=True, mail_2="tamara@example.com")
    verify_request_count(
        test_id, "GET", "/Invoice/send/23548884", {"attachfile": "true", "mail2": "tamara@example.com"}, 1
    )


def test_invoice_get_invoice_pdf() -> None:
    """Test GetInvoicePDF endpoint with WireMock"""
    test_id = "invoice.get_invoice_pdf.0"
    client = get_client(test_id)
    client.invoice.get_invoice_pdf(id_invoice=23548884)
    verify_request_count(test_id, "GET", "/Export/invoicePdf/23548884", None, 1)
