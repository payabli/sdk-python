from .conftest import get_client, verify_request_count


def test_export_export_applications() -> None:
    """Test ExportApplications endpoint with WireMock"""
    test_id = "export.export_applications.0"
    client = get_client(test_id)
    client.export.export_applications(
        format="csv",
        org_id=123,
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/boarding/csv/123",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_batch_details() -> None:
    """Test ExportBatchDetails endpoint with WireMock"""
    test_id = "export.export_batch_details.0"
    client = get_client(test_id)
    client.export.export_batch_details(
        entry="8cfec329267",
        format="csv",
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/batchDetails/csv/8cfec329267",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_batch_details_org() -> None:
    """Test ExportBatchDetailsOrg endpoint with WireMock"""
    test_id = "export.export_batch_details_org.0"
    client = get_client(test_id)
    client.export.export_batch_details_org(
        format="csv",
        org_id=123,
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/batchDetails/csv/org/123",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_batches() -> None:
    """Test ExportBatches endpoint with WireMock"""
    test_id = "export.export_batches.0"
    client = get_client(test_id)
    client.export.export_batches(
        entry="8cfec329267",
        format="csv",
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/batches/csv/8cfec329267",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_batches_org() -> None:
    """Test ExportBatchesOrg endpoint with WireMock"""
    test_id = "export.export_batches_org.0"
    client = get_client(test_id)
    client.export.export_batches_org(
        format="csv",
        org_id=123,
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/batches/csv/org/123",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_batches_out() -> None:
    """Test ExportBatchesOut endpoint with WireMock"""
    test_id = "export.export_batches_out.0"
    client = get_client(test_id)
    client.export.export_batches_out(
        entry="8cfec329267",
        format="csv",
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/batchesOut/csv/8cfec329267",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_batches_out_org() -> None:
    """Test ExportBatchesOutOrg endpoint with WireMock"""
    test_id = "export.export_batches_out_org.0"
    client = get_client(test_id)
    client.export.export_batches_out_org(
        format="csv",
        org_id=123,
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/batchesOut/csv/org/123",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_bills() -> None:
    """Test ExportBills endpoint with WireMock"""
    test_id = "export.export_bills.0"
    client = get_client(test_id)
    client.export.export_bills(
        entry="8cfec329267",
        format="csv",
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/bills/csv/8cfec329267",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_bills_org() -> None:
    """Test ExportBillsOrg endpoint with WireMock"""
    test_id = "export.export_bills_org.0"
    client = get_client(test_id)
    client.export.export_bills_org(
        format="csv",
        org_id=123,
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/bills/csv/org/123",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_chargebacks() -> None:
    """Test ExportChargebacks endpoint with WireMock"""
    test_id = "export.export_chargebacks.0"
    client = get_client(test_id)
    client.export.export_chargebacks(
        entry="8cfec329267",
        format="csv",
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/chargebacks/csv/8cfec329267",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_chargebacks_org() -> None:
    """Test ExportChargebacksOrg endpoint with WireMock"""
    test_id = "export.export_chargebacks_org.0"
    client = get_client(test_id)
    client.export.export_chargebacks_org(
        format="csv",
        org_id=123,
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/chargebacks/csv/org/123",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_customers() -> None:
    """Test ExportCustomers endpoint with WireMock"""
    test_id = "export.export_customers.0"
    client = get_client(test_id)
    client.export.export_customers(
        entry="8cfec329267",
        format="csv",
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/customers/csv/8cfec329267",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_customers_org() -> None:
    """Test ExportCustomersOrg endpoint with WireMock"""
    test_id = "export.export_customers_org.0"
    client = get_client(test_id)
    client.export.export_customers_org(
        format="csv",
        org_id=123,
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/customers/csv/org/123",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_invoices() -> None:
    """Test ExportInvoices endpoint with WireMock"""
    test_id = "export.export_invoices.0"
    client = get_client(test_id)
    client.export.export_invoices(
        entry="8cfec329267",
        format="csv",
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/invoices/csv/8cfec329267",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_invoices_org() -> None:
    """Test ExportInvoicesOrg endpoint with WireMock"""
    test_id = "export.export_invoices_org.0"
    client = get_client(test_id)
    client.export.export_invoices_org(
        format="csv",
        org_id=123,
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/invoices/csv/org/123",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_organizations() -> None:
    """Test ExportOrganizations endpoint with WireMock"""
    test_id = "export.export_organizations.0"
    client = get_client(test_id)
    client.export.export_organizations(
        format="csv",
        org_id=123,
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/organizations/csv/org/123",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_payout() -> None:
    """Test ExportPayout endpoint with WireMock"""
    test_id = "export.export_payout.0"
    client = get_client(test_id)
    client.export.export_payout(
        entry="8cfec329267",
        format="csv",
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/payouts/csv/8cfec329267",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_payout_org() -> None:
    """Test ExportPayoutOrg endpoint with WireMock"""
    test_id = "export.export_payout_org.0"
    client = get_client(test_id)
    client.export.export_payout_org(
        format="csv",
        org_id=123,
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/payouts/csv/org/123",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_paypoints() -> None:
    """Test ExportPaypoints endpoint with WireMock"""
    test_id = "export.export_paypoints.0"
    client = get_client(test_id)
    client.export.export_paypoints(
        format="csv",
        org_id=123,
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/paypoints/csv/123",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_settlements() -> None:
    """Test ExportSettlements endpoint with WireMock"""
    test_id = "export.export_settlements.0"
    client = get_client(test_id)
    client.export.export_settlements(
        entry="8cfec329267",
        format="csv",
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/settlements/csv/8cfec329267",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_settlements_org() -> None:
    """Test ExportSettlementsOrg endpoint with WireMock"""
    test_id = "export.export_settlements_org.0"
    client = get_client(test_id)
    client.export.export_settlements_org(
        format="csv",
        org_id=123,
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/settlements/csv/org/123",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_subscriptions() -> None:
    """Test ExportSubscriptions endpoint with WireMock"""
    test_id = "export.export_subscriptions.0"
    client = get_client(test_id)
    client.export.export_subscriptions(
        entry="8cfec329267",
        format="csv",
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/subscriptions/csv/8cfec329267",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_subscriptions_org() -> None:
    """Test ExportSubscriptionsOrg endpoint with WireMock"""
    test_id = "export.export_subscriptions_org.0"
    client = get_client(test_id)
    client.export.export_subscriptions_org(
        format="csv",
        org_id=123,
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/subscriptions/csv/org/123",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_transactions() -> None:
    """Test ExportTransactions endpoint with WireMock"""
    test_id = "export.export_transactions.0"
    client = get_client(test_id)
    client.export.export_transactions(
        entry="8cfec329267",
        format="csv",
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/transactions/csv/8cfec329267",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_transactions_org() -> None:
    """Test ExportTransactionsOrg endpoint with WireMock"""
    test_id = "export.export_transactions_org.0"
    client = get_client(test_id)
    client.export.export_transactions_org(
        format="csv",
        org_id=123,
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/transactions/csv/org/123",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_transfer_details() -> None:
    """Test ExportTransferDetails endpoint with WireMock"""
    test_id = "export.export_transfer_details.0"
    client = get_client(test_id)
    client.export.export_transfer_details(
        entry="8cfec329267",
        format="csv",
        transfer_id=1000000,
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
        sort_by="desc(field_name)",
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/transferDetails/csv/8cfec329267/1000000",
        {
            "columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name",
            "fromRecord": "251",
            "limitRecord": "1000",
            "sortBy": "desc(field_name)",
        },
        1,
    )


def test_export_export_transfers() -> None:
    """Test ExportTransfers endpoint with WireMock"""
    test_id = "export.export_transfers.0"
    client = get_client(test_id)
    client.export.export_transfers(
        entry="8cfec329267",
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
        sort_by="desc(field_name)",
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/transfers/8cfec329267",
        {
            "columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name",
            "fromRecord": "251",
            "limitRecord": "1000",
            "sortBy": "desc(field_name)",
        },
        1,
    )


def test_export_export_vendors() -> None:
    """Test ExportVendors endpoint with WireMock"""
    test_id = "export.export_vendors.0"
    client = get_client(test_id)
    client.export.export_vendors(
        entry="8cfec329267",
        format="csv",
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/vendors/csv/8cfec329267",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )


def test_export_export_vendors_org() -> None:
    """Test ExportVendorsOrg endpoint with WireMock"""
    test_id = "export.export_vendors_org.0"
    client = get_client(test_id)
    client.export.export_vendors_org(
        format="csv",
        org_id=123,
        columns_export="BatchDate:Batch_Date,PaypointName:Legal_name",
        from_record=251,
        limit_record=1000,
    )
    verify_request_count(
        test_id,
        "GET",
        "/Export/vendors/csv/org/123",
        {"columnsExport": "BatchDate:Batch_Date,PaypointName:Legal_name", "fromRecord": "251", "limitRecord": "1000"},
        1,
    )
