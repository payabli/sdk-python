from .conftest import get_client, verify_request_count


def test_user_add_user() -> None:
    """Test AddUser endpoint with WireMock"""
    test_id = "user.add_user.0"
    client = get_client(test_id)
    client.user.add_user()
    verify_request_count(test_id, "POST", "/User", None, 1)


def test_user_auth_refresh_user() -> None:
    """Test AuthRefreshUser endpoint with WireMock"""
    test_id = "user.auth_refresh_user.0"
    client = get_client(test_id)
    client.user.auth_refresh_user()
    verify_request_count(test_id, "POST", "/User/authrefresh", None, 1)


def test_user_auth_reset_user() -> None:
    """Test AuthResetUser endpoint with WireMock"""
    test_id = "user.auth_reset_user.0"
    client = get_client(test_id)
    client.user.auth_reset_user()
    verify_request_count(test_id, "POST", "/User/authreset", None, 1)


def test_user_auth_user() -> None:
    """Test AuthUser endpoint with WireMock"""
    test_id = "user.auth_user.0"
    client = get_client(test_id)
    client.user.auth_user(provider="provider")
    verify_request_count(test_id, "POST", "/User/auth/provider", None, 1)


def test_user_change_psw_user() -> None:
    """Test ChangePswUser endpoint with WireMock"""
    test_id = "user.change_psw_user.0"
    client = get_client(test_id)
    client.user.change_psw_user()
    verify_request_count(test_id, "PUT", "/User/authpsw", None, 1)


def test_user_delete_user() -> None:
    """Test DeleteUser endpoint with WireMock"""
    test_id = "user.delete_user.0"
    client = get_client(test_id)
    client.user.delete_user(user_id=1000000)
    verify_request_count(test_id, "DELETE", "/User/1000000", None, 1)


def test_user_edit_mfa_user() -> None:
    """Test EditMfaUser endpoint with WireMock"""
    test_id = "user.edit_mfa_user.0"
    client = get_client(test_id)
    client.user.edit_mfa_user(user_id=1000000)
    verify_request_count(test_id, "PUT", "/User/mfa/1000000", None, 1)


def test_user_edit_user() -> None:
    """Test EditUser endpoint with WireMock"""
    test_id = "user.edit_user.0"
    client = get_client(test_id)
    client.user.edit_user(user_id=1000000)
    verify_request_count(test_id, "PUT", "/User/1000000", None, 1)


def test_user_get_user() -> None:
    """Test GetUser endpoint with WireMock"""
    test_id = "user.get_user.0"
    client = get_client(test_id)
    client.user.get_user(user_id=1000000, entry="478ae1234")
    verify_request_count(test_id, "GET", "/User/1000000", {"entry": "478ae1234"}, 1)


def test_user_logout_user() -> None:
    """Test LogoutUser endpoint with WireMock"""
    test_id = "user.logout_user.0"
    client = get_client(test_id)
    client.user.logout_user()
    verify_request_count(test_id, "GET", "/User/authlogout", None, 1)


def test_user_resend_mfa_code() -> None:
    """Test ResendMFACode endpoint with WireMock"""
    test_id = "user.resend_mfa_code.0"
    client = get_client(test_id)
    client.user.resend_mfa_code(entry="Entry", entry_type=1, usrname="usrname")
    verify_request_count(test_id, "POST", "/User/resendmfa/usrname/Entry/1", None, 1)


def test_user_validate_mfa_user() -> None:
    """Test ValidateMfaUser endpoint with WireMock"""
    test_id = "user.validate_mfa_user.0"
    client = get_client(test_id)
    client.user.validate_mfa_user()
    verify_request_count(test_id, "POST", "/User/mfa", None, 1)
