from .conftest import get_client, verify_request_count


def test_query_list_batch_details() -> None:
    """Test ListBatchDetails endpoint with WireMock"""
    test_id = "query.list_batch_details.0"
    client = get_client(test_id)
    client.query.list_batch_details(entry="8cfec329267", from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/batchDetails/8cfec329267",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_batch_details_org() -> None:
    """Test ListBatchDetailsOrg endpoint with WireMock"""
    test_id = "query.list_batch_details_org.0"
    client = get_client(test_id)
    client.query.list_batch_details_org(org_id=123, from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/batchDetails/org/123",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_batches() -> None:
    """Test ListBatches endpoint with WireMock"""
    test_id = "query.list_batches.0"
    client = get_client(test_id)
    client.query.list_batches(entry="8cfec329267", from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/batches/8cfec329267",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_batches_org() -> None:
    """Test ListBatchesOrg endpoint with WireMock"""
    test_id = "query.list_batches_org.0"
    client = get_client(test_id)
    client.query.list_batches_org(org_id=123, from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/batches/org/123",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_batches_out() -> None:
    """Test ListBatchesOut endpoint with WireMock"""
    test_id = "query.list_batches_out.0"
    client = get_client(test_id)
    client.query.list_batches_out(entry="8cfec329267", from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/batchesOut/8cfec329267",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_batches_out_org() -> None:
    """Test ListBatchesOutOrg endpoint with WireMock"""
    test_id = "query.list_batches_out_org.0"
    client = get_client(test_id)
    client.query.list_batches_out_org(org_id=123, from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/batchesOut/org/123",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_chargebacks() -> None:
    """Test ListChargebacks endpoint with WireMock"""
    test_id = "query.list_chargebacks.0"
    client = get_client(test_id)
    client.query.list_chargebacks(entry="8cfec329267", from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/chargebacks/8cfec329267",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_chargebacks_org() -> None:
    """Test ListChargebacksOrg endpoint with WireMock"""
    test_id = "query.list_chargebacks_org.0"
    client = get_client(test_id)
    client.query.list_chargebacks_org(org_id=123, from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/chargebacks/org/123",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_customers() -> None:
    """Test ListCustomers endpoint with WireMock"""
    test_id = "query.list_customers.0"
    client = get_client(test_id)
    client.query.list_customers(entry="8cfec329267", from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/customers/8cfec329267",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_customers_org() -> None:
    """Test ListCustomersOrg endpoint with WireMock"""
    test_id = "query.list_customers_org.0"
    client = get_client(test_id)
    client.query.list_customers_org(org_id=123, from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/customers/org/123",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_notification_reports() -> None:
    """Test ListNotificationReports endpoint with WireMock"""
    test_id = "query.list_notification_reports.0"
    client = get_client(test_id)
    client.query.list_notification_reports(
        entry="8cfec329267", from_record=251, limit_record=0, sort_by="desc(field_name)"
    )
    verify_request_count(
        test_id,
        "GET",
        "/Query/notificationReports/8cfec329267",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_notification_reports_org() -> None:
    """Test ListNotificationReportsOrg endpoint with WireMock"""
    test_id = "query.list_notification_reports_org.0"
    client = get_client(test_id)
    client.query.list_notification_reports_org(org_id=123, from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/notificationReports/org/123",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_notifications() -> None:
    """Test ListNotifications endpoint with WireMock"""
    test_id = "query.list_notifications.0"
    client = get_client(test_id)
    client.query.list_notifications(entry="8cfec329267", from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/notifications/8cfec329267",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_notifications_org() -> None:
    """Test ListNotificationsOrg endpoint with WireMock"""
    test_id = "query.list_notifications_org.0"
    client = get_client(test_id)
    client.query.list_notifications_org(org_id=123, from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/notifications/org/123",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_organizations() -> None:
    """Test ListOrganizations endpoint with WireMock"""
    test_id = "query.list_organizations.0"
    client = get_client(test_id)
    client.query.list_organizations(org_id=123, from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/organizations/123",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_payout() -> None:
    """Test ListPayout endpoint with WireMock"""
    test_id = "query.list_payout.0"
    client = get_client(test_id)
    client.query.list_payout(entry="8cfec329267", from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/payouts/8cfec329267",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_payout_org() -> None:
    """Test ListPayoutOrg endpoint with WireMock"""
    test_id = "query.list_payout_org.0"
    client = get_client(test_id)
    client.query.list_payout_org(org_id=123, from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/payouts/org/123",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_paypoints() -> None:
    """Test ListPaypoints endpoint with WireMock"""
    test_id = "query.list_paypoints.0"
    client = get_client(test_id)
    client.query.list_paypoints(org_id=123, from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/paypoints/123",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_settlements() -> None:
    """Test ListSettlements endpoint with WireMock"""
    test_id = "query.list_settlements.0"
    client = get_client(test_id)
    client.query.list_settlements(entry="8cfec329267", from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/settlements/8cfec329267",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_settlements_org() -> None:
    """Test ListSettlementsOrg endpoint with WireMock"""
    test_id = "query.list_settlements_org.0"
    client = get_client(test_id)
    client.query.list_settlements_org(org_id=123, from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/settlements/org/123",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_subscriptions() -> None:
    """Test ListSubscriptions endpoint with WireMock"""
    test_id = "query.list_subscriptions.0"
    client = get_client(test_id)
    client.query.list_subscriptions(entry="8cfec329267", from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/subscriptions/8cfec329267",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_subscriptions_org() -> None:
    """Test ListSubscriptionsOrg endpoint with WireMock"""
    test_id = "query.list_subscriptions_org.0"
    client = get_client(test_id)
    client.query.list_subscriptions_org(org_id=123, from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/subscriptions/org/123",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_transactions() -> None:
    """Test ListTransactions endpoint with WireMock"""
    test_id = "query.list_transactions.0"
    client = get_client(test_id)
    client.query.list_transactions(entry="8cfec329267", from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/transactions/8cfec329267",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_transactions_org() -> None:
    """Test ListTransactionsOrg endpoint with WireMock"""
    test_id = "query.list_transactions_org.0"
    client = get_client(test_id)
    client.query.list_transactions_org(org_id=123, from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/transactions/org/123",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_transfer_details() -> None:
    """Test ListTransferDetails endpoint with WireMock"""
    test_id = "query.list_transfer_details.0"
    client = get_client(test_id)
    client.query.list_transfer_details(entry="47862acd", transfer_id=123456)
    verify_request_count(test_id, "GET", "/Query/transferDetails/47862acd/123456", None, 1)


def test_query_list_transfers() -> None:
    """Test ListTransfers endpoint with WireMock"""
    test_id = "query.list_transfers.0"
    client = get_client(test_id)
    client.query.list_transfers(entry="47862acd", from_record=0, limit_record=20)
    verify_request_count(test_id, "GET", "/Query/transfers/47862acd", {"fromRecord": "0", "limitRecord": "20"}, 1)


def test_query_list_transfers_org() -> None:
    """Test ListTransfersOrg endpoint with WireMock"""
    test_id = "query.list_transfers_org.0"
    client = get_client(test_id)
    client.query.list_transfers_org(org_id=123, from_record=0, limit_record=20)
    verify_request_count(test_id, "GET", "/Query/transfers/org/123", {"fromRecord": "0", "limitRecord": "20"}, 1)


def test_query_list_users_org() -> None:
    """Test ListUsersOrg endpoint with WireMock"""
    test_id = "query.list_users_org.0"
    client = get_client(test_id)
    client.query.list_users_org(org_id=123, from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/users/org/123",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_users_paypoint() -> None:
    """Test ListUsersPaypoint endpoint with WireMock"""
    test_id = "query.list_users_paypoint.0"
    client = get_client(test_id)
    client.query.list_users_paypoint(entry="8cfec329267", from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/users/point/8cfec329267",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_vendors() -> None:
    """Test ListVendors endpoint with WireMock"""
    test_id = "query.list_vendors.0"
    client = get_client(test_id)
    client.query.list_vendors(entry="8cfec329267", from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/vendors/8cfec329267",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_vendors_org() -> None:
    """Test ListVendorsOrg endpoint with WireMock"""
    test_id = "query.list_vendors_org.0"
    client = get_client(test_id)
    client.query.list_vendors_org(org_id=123, from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/vendors/org/123",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_vcards() -> None:
    """Test ListVcards endpoint with WireMock"""
    test_id = "query.list_vcards.0"
    client = get_client(test_id)
    client.query.list_vcards(entry="8cfec329267", from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/vcards/8cfec329267",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )


def test_query_list_vcards_org() -> None:
    """Test ListVcardsOrg endpoint with WireMock"""
    test_id = "query.list_vcards_org.0"
    client = get_client(test_id)
    client.query.list_vcards_org(org_id=123, from_record=251, limit_record=0, sort_by="desc(field_name)")
    verify_request_count(
        test_id,
        "GET",
        "/Query/vcards/org/123",
        {"fromRecord": "251", "limitRecord": "0", "sortBy": "desc(field_name)"},
        1,
    )
