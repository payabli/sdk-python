from .conftest import get_client, verify_request_count


def test_paymentLink_add_pay_link_from_invoice() -> None:
    """Test AddPayLinkFromInvoice endpoint with WireMock"""
    test_id = "payment_link.add_pay_link_from_invoice.0"
    client = get_client(test_id)
    client.payment_link.add_pay_link_from_invoice(
        id_invoice=23548884,
        mail_2="jo@example.com; ceo@example.com",
        contact_us={
            "email_label": "Email",
            "enabled": True,
            "header": "Contact Us",
            "order": 0,
            "payment_icons": True,
            "phone_label": "Phone",
        },
        invoices={
            "enabled": True,
            "invoice_link": {"enabled": True, "label": "View Invoice", "order": 0},
            "order": 0,
            "view_invoice_details": {"enabled": True, "label": "Invoice Details", "order": 0},
        },
        logo={"enabled": True, "order": 0},
        message_before_paying={"enabled": True, "label": "Please review your payment details", "order": 0},
        notes={
            "enabled": True,
            "header": "Additional Notes",
            "order": 0,
            "placeholder": "Enter any additional notes here",
            "value": "",
        },
        page={"description": "Complete your payment securely", "enabled": True, "header": "Payment Page", "order": 0},
        payment_button={"enabled": True, "label": "Pay Now", "order": 0},
        payment_methods={
            "all_methods_checked": True,
            "enabled": True,
            "header": "Payment Methods",
            "methods": {
                "amex": True,
                "apple_pay": True,
                "discover": True,
                "e_check": True,
                "mastercard": True,
                "visa": True,
            },
            "order": 0,
            "settings": {"apple_pay": {"button_style": "black", "button_type": "pay", "language": "en-US"}},
        },
        payor={
            "enabled": True,
            "fields": [
                {
                    "display": True,
                    "fixed": True,
                    "identifier": True,
                    "label": "Full Name",
                    "name": "fullName",
                    "order": 0,
                    "required": True,
                    "validation": "^[a-zA-Z ]+$",
                    "value": "",
                    "width": 0,
                }
            ],
            "header": "Payor Information",
            "order": 0,
        },
        review={"enabled": True, "header": "Review Payment", "order": 0},
        settings={
            "color": "#000000",
            "custom_css_url": "https://example.com/custom.css",
            "language": "en",
            "page_logo": {
                "f_content": "PHN2ZyB2aWV3Qm94PSIwIDAgODAwIDEwMDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPCEtLSBCYWNrZ3JvdW5kIC0tPgogIDxyZWN0IHdpZHRoPSI4MDAiIGhlaWdodD0iMTAwMCIgZmlsbD0id2hpdGUiLz4KICAKICA8IS0tIENvbXBhbnkgSGVhZGVyIC0tPgogIDx0ZXh0IHg9IjQwIiB5PSI2MCIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjI0IiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0iIzJjM2U1MCI+R3J1enlhIEFkdmVudHVyZSBPdXRmaXR0ZXJzPC90ZXh0PgogIDxsaW5lIHgxPSI0MCIgeTE9IjgwIiB4Mj0iNzYwIiB5Mj0iODAiIHN0cm9rZT0iIzJjM2U1MCIgc3Ryb2tlLXdpZHRoPSIyIi8+CiAgCiAgPCEtLSBDb21wYW55IERldGFpbHMgLS0+CiAgPHRleHQgeD0iNDAiIHk9IjExMCIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjE0IiBmaWxsPSIjMzQ0OTVlIj4xMjMgTW91bnRhaW4gVmlldyBSb2FkPC90ZXh0PgogIDx0ZXh0IHg9IjQwIiB5PSIxMzAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzM0NDk1ZSI+VGJpbGlzaSwgR2VvcmdpYSAwMTA1PC90ZXh0PgogIDx0ZXh0IHg9IjQwIiB5PSIxNTAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzM0NDk1ZSI+VGVsOiArOTk1IDMyIDEyMyA0NTY3PC90ZXh0PgogIDx0ZXh0IHg9IjQwIiB5PSIxNzAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzM0NDk1ZSI+RW1haWw6IGluZm9AZ3J1enlhYWR2ZW50dXJlcy5jb208L3RleHQ+CgogIDwhLS0gSW52b2ljZSBUaXRsZSAtLT4KICA8dGV4dCB4PSI2MDAiIHk9IjExMCIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjI0IiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0iIzJjM2U1MCI+SU5WT0lDRTwvdGV4dD4KICA8dGV4dCB4PSI2MDAiIHk9IjE0MCIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjE0IiBmaWxsPSIjMzQ0OTVlIj5EYXRlOiAxMi8xMS8yMDI0PC90ZXh0PgogIDx0ZXh0IHg9IjYwMCIgeT0iMTYwIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTQiIGZpbGw9IiMzNDQ5NWUiPkludm9pY2UgIzogR1JaLTIwMjQtMTEyMzwvdGV4dD4KCiAgPCEtLSBCaWxsIFRvIFNlY3Rpb24gLS0+CiAgPHRleHQgeD0iNDAiIHk9IjIyMCIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjE2IiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0iIzJjM2U1MCI+QklMTCBUTzo8L3RleHQ+CiAgPHJlY3QgeD0iNDAiIHk9IjIzNSIgd2lkdGg9IjMwMCIgaGVpZ2h0PSI4MCIgZmlsbD0iI2Y3ZjlmYSIvPgogIDx0ZXh0IHg9IjUwIiB5PSIyNjAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzM0NDk1ZSI+W0N1c3RvbWVyIE5hbWVdPC90ZXh0PgogIDx0ZXh0IHg9IjUwIiB5PSIyODAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzM0NDk1ZSI+W0FkZHJlc3MgTGluZSAxXTwvdGV4dD4KICA8dGV4dCB4PSI1MCIgeT0iMzAwIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTQiIGZpbGw9IiMzNDQ5NWUiPltDaXR5LCBDb3VudHJ5XTwvdGV4dD4KCiAgPCEtLSBUYWJsZSBIZWFkZXJzIC0tPgogIDxyZWN0IHg9IjQwIiB5PSIzNDAiIHdpZHRoPSI3MjAiIGhlaWdodD0iMzAiIGZpbGw9IiMyYzNlNTAiLz4KICA8dGV4dCB4PSI1MCIgeT0iMzYwIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTQiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSJ3aGl0ZSI+RGVzY3JpcHRpb248L3RleHQ+CiAgPHRleHQgeD0iNDUwIiB5PSIzNjAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9IndoaXRlIj5RdWFudGl0eTwvdGV4dD4KICA8dGV4dCB4PSI1NTAiIHk9IjM2MCIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjE0IiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0id2hpdGUiPlJhdGU8L3RleHQ+CiAgPHRleHQgeD0iNjgwIiB5PSIzNjAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9IndoaXRlIj5BbW91bnQ8L3RleHQ+CgogIDwhLS0gVGFibGUgUm93cyAtLT4KICA8cmVjdCB4PSI0MCIgeT0iMzcwIiB3aWR0aD0iNzIwIiBoZWlnaHQ9IjMwIiBmaWxsPSIjZjdmOWZhIi8+CiAgPHRleHQgeD0iNTAiIHk9IjM5MCIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjE0IiBmaWxsPSIjMzQ0OTVlIj5Nb3VudGFpbiBDbGltYmluZyBFcXVpcG1lbnQgUmVudGFsPC90ZXh0PgogIDx0ZXh0IHg9IjQ1MCIgeT0iMzkwIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTQiIGZpbGw9IiMzNDQ5NWUiPjE8L3RleHQ+CiAgPHRleHQgeD0iNTUwIiB5PSIzOTAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzM0NDk1ZSI+JDI1MC4wMDwvdGV4dD4KICA8dGV4dCB4PSI2ODAiIHk9IjM5MCIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjE0IiBmaWxsPSIjMzQ0OTVlIj4kMjUwLjAwPC90ZXh0PgoKICA8cmVjdCB4PSI0MCIgeT0iNDAwIiB3aWR0aD0iNzIwIiBoZWlnaHQ9IjMwIiBmaWxsPSJ3aGl0ZSIvPgogIDx0ZXh0IHg9IjUwIiB5PSI0MjAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzM0NDk1ZSI+R3VpZGVkIFRyZWsgUGFja2FnZSAtIDIgRGF5czwvdGV4dD4KICA8dGV4dCB4PSI0NTAiIHk9IjQyMCIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjE0IiBmaWxsPSIjMzQ0OTVlIj4xPC90ZXh0PgogIDx0ZXh0IHg9IjU1MCIgeT0iNDIwIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTQiIGZpbGw9IiMzNDQ5NWUiPiQ0MDAuMDA8L3RleHQ+CiAgPHRleHQgeD0iNjgwIiB5PSI0MjAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzM0NDk1ZSI+JDQwMC4wMDwvdGV4dD4KCiAgPHJlY3QgeD0iNDAiIHk9IjQzMCIgd2lkdGg9IjcyMCIgaGVpZ2h0PSIzMCIgZmlsbD0iI2Y3ZjlmYSIvPgogIDx0ZXh0IHg9IjUwIiB5PSI0NTAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzM0NDk1ZSI+U2FmZXR5IEVxdWlwbWVudCBQYWNrYWdlPC90ZXh0PgogIDx0ZXh0IHg9IjQ1MCIgeT0iNDUwIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTQiIGZpbGw9IiMzNDQ5NWUiPjE8L3RleHQ+CiAgPHRleHQgeD0iNTUwIiB5PSI0NTAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzM0NDk1ZSI+JDE1MC4wMDwvdGV4dD4KICA8dGV4dCB4PSI2ODAiIHk9IjQ1MCIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjE0IiBmaWxsPSIjMzQ0OTVlIj4kMTUwLjAwPC90ZXh0PgoKICA8IS0tIFRvdGFscyAtLT4KICA8bGluZSB4MT0iNDAiIHkxPSI0ODAiIHgyPSI3NjAiIHkyPSI0ODAiIHN0cm9rZT0iIzJjM2U1MCIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgPHRleHQgeD0iNTUwIiB5PSI1MTAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9IiMzNDQ5NWUiPlN1YnRvdGFsOjwvdGV4dD4KICA8dGV4dCB4PSI2ODAiIHk9IjUxMCIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjE0IiBmaWxsPSIjMzQ0OTVlIj4kODAwLjAwPC90ZXh0PgogIDx0ZXh0IHg9IjU1MCIgeT0iNTM1IiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTQiIGZvbnQtd2VpZ2h0PSJib2xkIiBmaWxsPSIjMzQ0OTVlIj5UYXggKDE4JSk6PC90ZXh0PgogIDx0ZXh0IHg9IjY4MCIgeT0iNTM1IiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTQiIGZpbGw9IiMzNDQ5NWUiPiQxNDQuMDA8L3RleHQ+CiAgPHRleHQgeD0iNTUwIiB5PSI1NzAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNiIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9IiMyYzNlNTAiPlRvdGFsOjwvdGV4dD4KICA8dGV4dCB4PSI2ODAiIHk9IjU3MCIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjE2IiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0iIzJjM2U1MCI+JDk0NC4wMDwvdGV4dD4KCiAgPCEtLSBQYXltZW50IFRlcm1zIC0tPgogIDx0ZXh0IHg9IjQwIiB5PSI2NDAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNiIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9IiMyYzNlNTAiPlBheW1lbnQgVGVybXM8L3RleHQ+CiAgPHRleHQgeD0iNDAiIHk9IjY3MCIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjE0IiBmaWxsPSIjMzQ0OTVlIj5QYXltZW50IGlzIGR1ZSB3aXRoaW4gMzAgZGF5czwvdGV4dD4KICA8dGV4dCB4PSI0MCIgeT0iNjkwIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTQiIGZpbGw9IiMzNDQ5NWUiPlBsZWFzZSBpbmNsdWRlIGludm9pY2UgbnVtYmVyIG9uIHBheW1lbnQ8L3RleHQ+CgogIDwhLS0gQmFuayBEZXRhaWxzIC0tPgogIDx0ZXh0IHg9IjQwIiB5PSI3MzAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNiIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9IiMyYzNlNTAiPkJhbmsgRGV0YWlsczwvdGV4dD4KICA8dGV4dCB4PSI0MCIgeT0iNzYwIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTQiIGZpbGw9IiMzNDQ5NWUiPkJhbms6IEJhbmsgb2YgR2VvcmdpYTwvdGV4dD4KICA8dGV4dCB4PSI0MCIgeT0iNzgwIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTQiIGZpbGw9IiMzNDQ5NWUiPklCQU46IEdFMTIzNDU2Nzg5MDEyMzQ1Njc4PC90ZXh0PgogIDx0ZXh0IHg9IjQwIiB5PSI4MDAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzM0NDk1ZSI+U1dJRlQ6IEJBR0FHRTIyPC90ZXh0PgoKICA8IS0tIEZvb3RlciAtLT4KICA8bGluZSB4MT0iNDAiIHkxPSI5MDAiIHgyPSI3NjAiIHkyPSI5MDAiIHN0cm9rZT0iIzJjM2U1MCIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgPHRleHQgeD0iNDAiIHk9IjkzMCIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjEyIiBmaWxsPSIjN2Y4YzhkIj5UaGFuayB5b3UgZm9yIGNob29zaW5nIEdydXp5YSBBZHZlbnR1cmUgT3V0Zml0dGVyczwvdGV4dD4KICA8dGV4dCB4PSI0MCIgeT0iOTUwIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMTIiIGZpbGw9IiM3ZjhjOGQiPnd3dy5ncnV6eWFhZHZlbnR1cmVzLmNvbTwvdGV4dD4KPC9zdmc+Cg==",
                "filename": "logo.jpg",
                "ftype": "jpg",
                "furl": "",
            },
            "redirect_after_approve": True,
            "redirect_after_approve_url": "https://example.com/success",
        },
    )
    verify_request_count(test_id, "POST", "/PaymentLink/23548884", {"mail2": "jo@example.com; ceo@example.com"}, 1)


def test_paymentLink_add_pay_link_from_bill() -> None:
    """Test AddPayLinkFromBill endpoint with WireMock"""
    test_id = "payment_link.add_pay_link_from_bill.0"
    client = get_client(test_id)
    client.payment_link.add_pay_link_from_bill(
        bill_id=23548884,
        mail_2="jo@example.com; ceo@example.com",
        contact_us={
            "email_label": "Email",
            "enabled": True,
            "header": "Contact Us",
            "order": 0,
            "payment_icons": True,
            "phone_label": "Phone",
        },
        logo={"enabled": True, "order": 0},
        message_before_paying={"enabled": True, "label": "Please review your payment details", "order": 0},
        notes={
            "enabled": True,
            "header": "Additional Notes",
            "order": 0,
            "placeholder": "Enter any additional notes here",
            "value": "",
        },
        page={"description": "Get paid securely", "enabled": True, "header": "Payment Page", "order": 0},
        payment_button={"enabled": True, "label": "Pay Now", "order": 0},
        payment_methods={
            "all_methods_checked": True,
            "enabled": True,
            "header": "Payment Methods",
            "methods": {
                "amex": True,
                "apple_pay": True,
                "discover": True,
                "e_check": True,
                "mastercard": True,
                "visa": True,
            },
            "order": 0,
        },
        payor={
            "enabled": True,
            "fields": [
                {
                    "display": True,
                    "fixed": True,
                    "identifier": True,
                    "label": "Full Name",
                    "name": "fullName",
                    "order": 0,
                    "required": True,
                    "validation": "^[a-zA-Z ]+$",
                    "value": "",
                    "width": 0,
                }
            ],
            "header": "Payor Information",
            "order": 0,
        },
        review={"enabled": True, "header": "Review Payment", "order": 0},
        settings={"color": "#000000", "language": "en"},
    )
    verify_request_count(test_id, "POST", "/PaymentLink/bill/23548884", {"mail2": "jo@example.com; ceo@example.com"}, 1)


def test_paymentLink_delete_pay_link_from_id() -> None:
    """Test deletePayLinkFromId endpoint with WireMock"""
    test_id = "payment_link.delete_pay_link_from_id.0"
    client = get_client(test_id)
    client.payment_link.delete_pay_link_from_id(pay_link_id="payLinkId")
    verify_request_count(test_id, "DELETE", "/PaymentLink/payLinkId", None, 1)


def test_paymentLink_get_pay_link_from_id() -> None:
    """Test getPayLinkFromId endpoint with WireMock"""
    test_id = "payment_link.get_pay_link_from_id.0"
    client = get_client(test_id)
    client.payment_link.get_pay_link_from_id(paylink_id="paylinkId")
    verify_request_count(test_id, "GET", "/PaymentLink/load/paylinkId", None, 1)


def test_paymentLink_push_pay_link_from_id() -> None:
    """Test pushPayLinkFromId endpoint with WireMock"""
    test_id = "payment_link.push_pay_link_from_id.0"
    client = get_client(test_id)
    client.payment_link.push_pay_link_from_id(pay_link_id="payLinkId", request={"channel": "sms"})
    verify_request_count(test_id, "POST", "/PaymentLink/push/payLinkId", None, 1)


def test_paymentLink_refresh_pay_link_from_id() -> None:
    """Test refreshPayLinkFromId endpoint with WireMock"""
    test_id = "payment_link.refresh_pay_link_from_id.0"
    client = get_client(test_id)
    client.payment_link.refresh_pay_link_from_id(pay_link_id="payLinkId")
    verify_request_count(test_id, "GET", "/PaymentLink/refresh/payLinkId", None, 1)


def test_paymentLink_send_pay_link_from_id() -> None:
    """Test sendPayLinkFromId endpoint with WireMock"""
    test_id = "payment_link.send_pay_link_from_id.0"
    client = get_client(test_id)
    client.payment_link.send_pay_link_from_id(pay_link_id="payLinkId", mail_2="jo@example.com; ceo@example.com")
    verify_request_count(test_id, "GET", "/PaymentLink/send/payLinkId", {"mail2": "jo@example.com; ceo@example.com"}, 1)


def test_paymentLink_update_pay_link_from_id() -> None:
    """Test updatePayLinkFromId endpoint with WireMock"""
    test_id = "payment_link.update_pay_link_from_id.0"
    client = get_client(test_id)
    client.payment_link.update_pay_link_from_id(
        pay_link_id="332-c277b704-1301",
        notes={
            "enabled": True,
            "header": "Additional Notes",
            "order": 0,
            "placeholder": "Enter any additional notes here",
            "value": "",
        },
        payment_button={"enabled": True, "label": "Pay Now", "order": 0},
    )
    verify_request_count(test_id, "PUT", "/PaymentLink/update/332-c277b704-1301", None, 1)


def test_paymentLink_add_pay_link_from_bill_lot_number() -> None:
    """Test AddPayLinkFromBillLotNumber endpoint with WireMock"""
    test_id = "payment_link.add_pay_link_from_bill_lot_number.0"
    client = get_client(test_id)
    client.payment_link.add_pay_link_from_bill_lot_number(
        lot_number="LOT-2024-001",
        entry_point="billing",
        vendor_number="VENDOR-123",
        mail_2="customer@example.com; billing@example.com",
        amount_fixed="true",
        contact_us={
            "email_label": "Email",
            "enabled": True,
            "header": "Contact Us",
            "order": 0,
            "payment_icons": True,
            "phone_label": "Phone",
        },
        logo={"enabled": True, "order": 0},
        message_before_paying={"enabled": True, "label": "Please review your payment details", "order": 0},
        notes={
            "enabled": True,
            "header": "Additional Notes",
            "order": 0,
            "placeholder": "Enter any additional notes here",
            "value": "",
        },
        page={"description": "Get paid securely", "enabled": True, "header": "Payment Page", "order": 0},
        payment_button={"enabled": True, "label": "Pay Now", "order": 0},
        payment_methods={
            "all_methods_checked": True,
            "enabled": True,
            "header": "Payment Methods",
            "methods": {
                "amex": True,
                "apple_pay": True,
                "discover": True,
                "e_check": True,
                "mastercard": True,
                "visa": True,
            },
            "order": 0,
        },
        payor={
            "enabled": True,
            "fields": [
                {
                    "display": True,
                    "fixed": True,
                    "identifier": True,
                    "label": "Full Name",
                    "name": "fullName",
                    "order": 0,
                    "required": True,
                    "validation": "^[a-zA-Z ]+$",
                    "value": "",
                    "width": 0,
                }
            ],
            "header": "Payor Information",
            "order": 0,
        },
        review={"enabled": True, "header": "Review Payment", "order": 0},
        settings={"color": "#000000", "language": "en"},
    )
    verify_request_count(
        test_id,
        "POST",
        "/PaymentLink/bill/lotNumber/LOT-2024-001",
        {
            "entryPoint": "billing",
            "vendorNumber": "VENDOR-123",
            "mail2": "customer@example.com; billing@example.com",
            "amountFixed": "true",
        },
        1,
    )
