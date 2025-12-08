from .conftest import get_client, verify_request_count


def test_ocr_ocr_document_form() -> None:
    """Test OcrDocumentForm endpoint with WireMock"""
    test_id = "ocr.ocr_document_form.0"
    client = get_client(test_id)
    client.ocr.ocr_document_form(type_result="typeResult")
    verify_request_count(test_id, "POST", "/Import/ocrDocumentForm/typeResult", None, 1)


def test_ocr_ocr_document_json() -> None:
    """Test OcrDocumentJson endpoint with WireMock"""
    test_id = "ocr.ocr_document_json.0"
    client = get_client(test_id)
    client.ocr.ocr_document_json(type_result="typeResult")
    verify_request_count(test_id, "POST", "/Import/ocrDocumentJson/typeResult", None, 1)
