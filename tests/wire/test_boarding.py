from .conftest import get_client, verify_request_count


def test_boarding_add_application() -> None:
    """Test AddApplication endpoint with WireMock"""
    test_id = "boarding.add_application.0"
    client = get_client(test_id)
    client.boarding.add_application(
        request={
            "services": {
                "ach": {},
                "card": {"accept_amex": True, "accept_discover": True, "accept_mastercard": True, "accept_visa": True},
            },
            "annual_revenue": 1000,
            "average_bill_size": "500",
            "average_monthly_bill": "5650",
            "avgmonthly": 1000,
            "baddress": "123 Walnut Street",
            "baddress_1": "Suite 103",
            "bank_data": {},
            "bcity": "New Vegas",
            "bcountry": "US",
            "binperson": 60,
            "binphone": 20,
            "binweb": 20,
            "bstate": "FL",
            "bsummary": "Brick and mortar store that sells office supplies",
            "btype": "Limited Liability Company",
            "bzip": "33000",
            "contacts": [
                {
                    "contact_email": "herman@hermanscoatings.com",
                    "contact_name": "Herman Martinez",
                    "contact_phone": "3055550000",
                    "contact_title": "Owner",
                }
            ],
            "credit_limit": "creditLimit",
            "dba_name": "Sunshine Gutters",
            "ein": "123456789",
            "faxnumber": "1234567890",
            "highticketamt": 1000,
            "legal_name": "Sunshine Services, LLC",
            "license": "2222222FFG",
            "licstate": "CA",
            "maddress": "123 Walnut Street",
            "maddress_1": "STE 900",
            "mcc": "7777",
            "mcity": "Johnson City",
            "mcountry": "US",
            "mstate": "TN",
            "mzip": "37615",
            "org_id": 123,
            "ownership": [
                {
                    "oaddress": "33 North St",
                    "ocity": "Any City",
                    "ocountry": "US",
                    "odriverstate": "CA",
                    "ostate": "CA",
                    "ownerdob": "01/01/1990",
                    "ownerdriver": "CA6677778",
                    "owneremail": "test@email.com",
                    "ownername": "John Smith",
                    "ownerpercent": 100,
                    "ownerphone_1": "555888111",
                    "ownerphone_2": "555888111",
                    "ownerssn": "123456789",
                    "ownertitle": "CEO",
                    "ozip": "55555",
                }
            ],
            "phonenumber": "1234567890",
            "processing_region": "US",
            "recipient_email": "josephray@example.com",
            "recipient_email_notification": True,
            "resumable": True,
            "signer": {
                "address": "33 North St",
                "address_1": "STE 900",
                "city": "Bristol",
                "country": "US",
                "dob": "01/01/1976",
                "email": "test@email.com",
                "name": "John Smith",
                "phone": "555888111",
                "ssn": "123456789",
                "state": "TN",
                "zip": "55555",
                "pci_attestation": True,
                "signed_document_reference": "https://example.com/signed-document.pdf",
                "attestation_date": "04/20/2025",
                "sign_date": "04/20/2025",
                "additional_data": '{"deviceId":"499585-389fj484-3jcj8hj3","session":"fifji4-fiu443-fn4843","timeWithCompany":"6 Years"}',
            },
            "startdate": "01/01/1990",
            "tax_fill_name": "Sunshine LLC",
            "template_id": 22,
            "ticketamt": 1000,
            "website": "www.example.com",
            "when_charged": "When Service Provided",
            "when_delivered": "Over 30 Days",
            "when_provided": "30 Days or Less",
            "when_refunded": "30 Days or Less",
        }
    )
    verify_request_count(test_id, "POST", "/Boarding/app", None, 1)


def test_boarding_delete_application() -> None:
    """Test DeleteApplication endpoint with WireMock"""
    test_id = "boarding.delete_application.0"
    client = get_client(test_id)
    client.boarding.delete_application(app_id=352)
    verify_request_count(test_id, "DELETE", "/Boarding/app/352", None, 1)


def test_boarding_get_application() -> None:
    """Test GetApplication endpoint with WireMock"""
    test_id = "boarding.get_application.0"
    client = get_client(test_id)
    client.boarding.get_application(app_id=352)
    verify_request_count(test_id, "GET", "/Boarding/read/352", None, 1)


def test_boarding_get_application_by_auth() -> None:
    """Test GetApplicationByAuth endpoint with WireMock"""
    test_id = "boarding.get_application_by_auth.0"
    client = get_client(test_id)
    client.boarding.get_application_by_auth(x_id="17E", email="admin@email.com", reference_id="n6UCd1f1ygG7")
    verify_request_count(test_id, "POST", "/Boarding/read/17E", None, 1)


def test_boarding_get_by_id_link_application() -> None:
    """Test GetByIdLinkApplication endpoint with WireMock"""
    test_id = "boarding.get_by_id_link_application.0"
    client = get_client(test_id)
    client.boarding.get_by_id_link_application(boarding_link_id=91)
    verify_request_count(test_id, "GET", "/Boarding/linkbyId/91", None, 1)


def test_boarding_get_by_template_id_link_application() -> None:
    """Test GetByTemplateIdLinkApplication endpoint with WireMock"""
    test_id = "boarding.get_by_template_id_link_application.0"
    client = get_client(test_id)
    client.boarding.get_by_template_id_link_application(template_id=80)
    verify_request_count(test_id, "GET", "/Boarding/linkbyTemplate/80", None, 1)


def test_boarding_get_external_application() -> None:
    """Test getExternalApplication endpoint with WireMock"""
    test_id = "boarding.get_external_application.0"
    client = get_client(test_id)
    client.boarding.get_external_application(app_id=352, mail_2="mail2")
    verify_request_count(test_id, "PUT", "/Boarding/applink/352/mail2", None, 1)


def test_boarding_get_link_application() -> None:
    """Test GetLinkApplication endpoint with WireMock"""
    test_id = "boarding.get_link_application.0"
    client = get_client(test_id)
    client.boarding.get_link_application(boarding_link_reference="myorgaccountname-00091")
    verify_request_count(test_id, "GET", "/Boarding/link/myorgaccountname-00091", None, 1)


def test_boarding_list_applications() -> None:
    """Test ListApplications endpoint with WireMock"""
    test_id = "boarding.list_applications.0"
    client = get_client(test_id)
    client.boarding.list_applications(org_id=123, from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/boarding/123",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_boarding_list_boarding_links() -> None:
    """Test ListBoardingLinks endpoint with WireMock"""
    test_id = "boarding.list_boarding_links.0"
    client = get_client(test_id)
    client.boarding.list_boarding_links(org_id=123, from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/boardinglinks/123",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_boarding_update_application() -> None:
    """Test UpdateApplication endpoint with WireMock"""
    test_id = "boarding.update_application.0"
    client = get_client(test_id)
    client.boarding.update_application(app_id=352)
    verify_request_count(test_id, "PUT", "/Boarding/app/352", None, 1)
