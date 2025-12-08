from .conftest import get_client, verify_request_count


def test_templates_delete_template() -> None:
    """Test DeleteTemplate endpoint with WireMock"""
    test_id = "templates.delete_template.0"
    client = get_client(test_id)
    client.templates.delete_template(template_id=80)
    verify_request_count(test_id, "DELETE", "/Templates/80", None, 1)


def test_templates_getlink_template() -> None:
    """Test getlinkTemplate endpoint with WireMock"""
    test_id = "templates.getlink_template.0"
    client = get_client(test_id)
    client.templates.getlink_template(ignore_empty=True, template_id=80)
    verify_request_count(test_id, "GET", "/Templates/getlink/80/true", None, 1)


def test_templates_get_template() -> None:
    """Test getTemplate endpoint with WireMock"""
    test_id = "templates.get_template.0"
    client = get_client(test_id)
    client.templates.get_template(template_id=80)
    verify_request_count(test_id, "GET", "/Templates/get/80", None, 1)


def test_templates_list_templates() -> None:
    """Test ListTemplates endpoint with WireMock"""
    test_id = "templates.list_templates.0"
    client = get_client(test_id)
    client.templates.list_templates(org_id=123, from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/templates/123",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )
