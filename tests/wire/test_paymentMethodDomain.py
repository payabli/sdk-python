from .conftest import get_client, verify_request_count


def test_paymentMethodDomain_add_payment_method_domain() -> None:
    """Test AddPaymentMethodDomain endpoint with WireMock"""
    test_id = "payment_method_domain.add_payment_method_domain.0"
    client = get_client(test_id)
    client.payment_method_domain.add_payment_method_domain(
        domain_name="checkout.example.com",
        entity_id=109,
        entity_type="paypoint",
        apple_pay={"is_enabled": True},
        google_pay={"is_enabled": True},
    )
    verify_request_count(test_id, "POST", "/PaymentMethodDomain", None, 1)


def test_paymentMethodDomain_cascade_payment_method_domain() -> None:
    """Test CascadePaymentMethodDomain endpoint with WireMock"""
    test_id = "payment_method_domain.cascade_payment_method_domain.0"
    client = get_client(test_id)
    client.payment_method_domain.cascade_payment_method_domain(domain_id="pmd_b8237fa45c964d8a9ef27160cd42b8c5")
    verify_request_count(test_id, "POST", "/PaymentMethodDomain/pmd_b8237fa45c964d8a9ef27160cd42b8c5/cascade", None, 1)


def test_paymentMethodDomain_delete_payment_method_domain() -> None:
    """Test DeletePaymentMethodDomain endpoint with WireMock"""
    test_id = "payment_method_domain.delete_payment_method_domain.0"
    client = get_client(test_id)
    client.payment_method_domain.delete_payment_method_domain(domain_id="pmd_b8237fa45c964d8a9ef27160cd42b8c5")
    verify_request_count(test_id, "DELETE", "/PaymentMethodDomain/pmd_b8237fa45c964d8a9ef27160cd42b8c5", None, 1)


def test_paymentMethodDomain_get_payment_method_domain() -> None:
    """Test GetPaymentMethodDomain endpoint with WireMock"""
    test_id = "payment_method_domain.get_payment_method_domain.0"
    client = get_client(test_id)
    client.payment_method_domain.get_payment_method_domain(domain_id="pmd_b8237fa45c964d8a9ef27160cd42b8c5")
    verify_request_count(test_id, "GET", "/PaymentMethodDomain/pmd_b8237fa45c964d8a9ef27160cd42b8c5", None, 1)


def test_paymentMethodDomain_list_payment_method_domains() -> None:
    """Test ListPaymentMethodDomains endpoint with WireMock"""
    test_id = "payment_method_domain.list_payment_method_domains.0"
    client = get_client(test_id)
    client.payment_method_domain.list_payment_method_domains(entity_id=1147, entity_type="paypoint")
    verify_request_count(test_id, "GET", "/PaymentMethodDomain/list", {"entityId": "1147", "entityType": "paypoint"}, 1)


def test_paymentMethodDomain_update_payment_method_domain() -> None:
    """Test UpdatePaymentMethodDomain endpoint with WireMock"""
    test_id = "payment_method_domain.update_payment_method_domain.0"
    client = get_client(test_id)
    client.payment_method_domain.update_payment_method_domain(
        domain_id="pmd_b8237fa45c964d8a9ef27160cd42b8c5",
        apple_pay={"is_enabled": False},
        google_pay={"is_enabled": False},
    )
    verify_request_count(test_id, "PATCH", "/PaymentMethodDomain/pmd_b8237fa45c964d8a9ef27160cd42b8c5", None, 1)


def test_paymentMethodDomain_verify_payment_method_domain() -> None:
    """Test VerifyPaymentMethodDomain endpoint with WireMock"""
    test_id = "payment_method_domain.verify_payment_method_domain.0"
    client = get_client(test_id)
    client.payment_method_domain.verify_payment_method_domain(domain_id="pmd_b8237fa45c964d8a9ef27160cd42b8c5")
    verify_request_count(test_id, "POST", "/PaymentMethodDomain/pmd_b8237fa45c964d8a9ef27160cd42b8c5/verify", None, 1)
