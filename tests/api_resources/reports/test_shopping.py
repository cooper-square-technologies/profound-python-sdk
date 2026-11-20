# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestShopping:
    @smoke_case("reports.shopping.brands:required", operation="brands", path="/v2/reports/shopping/brands")
    def test_method_brands(self) -> None:
        shopping = client.reports.shopping.brands(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            interval="day",
            scope="owned",
        )

    @smoke_case("reports.shopping.brands:all", operation="brands", path="/v2/reports/shopping/brands")
    def test_method_brands_with_all_params(self) -> None:
        shopping = client.reports.shopping.brands(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            group_by=["date"],
            metrics=["visibility_score"],
            interval="day",
            scope="owned",
            assets="",
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            limit=1,
            max_results=1,
            cursor="",
        )

    @smoke_case(
        "reports.shopping.streamBrands:required", operation="streamBrands", path="/v2/reports/shopping/brands/stream"
    )
    def test_method_stream_brands(self) -> None:
        stream = client.reports.shopping.stream_brands(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            interval="day",
            scope="owned",
        )

        for event in stream:
            print(event)

    @smoke_case(
        "reports.shopping.streamBrands:all", operation="streamBrands", path="/v2/reports/shopping/brands/stream"
    )
    def test_method_stream_brands_with_all_params(self) -> None:
        stream = client.reports.shopping.stream_brands(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            group_by=["date"],
            metrics=["visibility_score"],
            interval="day",
            scope="owned",
            assets="",
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            limit=1,
            max_results=1,
            cursor="",
        )

        for event in stream:
            print(event)

    @smoke_case("reports.shopping.products:required", operation="products", path="/v2/reports/shopping/products")
    def test_method_products(self) -> None:
        shopping = client.reports.shopping.products(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            interval="day",
            include_merchants=False,
            competitor_limit=5,
        )

    @smoke_case("reports.shopping.products:all", operation="products", path="/v2/reports/shopping/products")
    def test_method_products_with_all_params(self) -> None:
        shopping = client.reports.shopping.products(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            group_by=["date"],
            metrics=["visibility_score"],
            interval="day",
            include_merchants=False,
            target_product="x",
            competitor_limit=5,
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            limit=1,
            max_results=1,
            cursor="",
        )

    @smoke_case(
        "reports.shopping.streamProducts:required",
        operation="streamProducts",
        path="/v2/reports/shopping/products/stream",
    )
    def test_method_stream_products(self) -> None:
        stream = client.reports.shopping.stream_products(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            interval="day",
            include_merchants=False,
            competitor_limit=5,
        )

        for event in stream:
            print(event)

    @smoke_case(
        "reports.shopping.streamProducts:all", operation="streamProducts", path="/v2/reports/shopping/products/stream"
    )
    def test_method_stream_products_with_all_params(self) -> None:
        stream = client.reports.shopping.stream_products(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            group_by=["date"],
            metrics=["visibility_score"],
            interval="day",
            include_merchants=False,
            target_product="x",
            competitor_limit=5,
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            limit=1,
            max_results=1,
            cursor="",
        )

        for event in stream:
            print(event)

    @smoke_case("reports.shopping.merchants:required", operation="merchants", path="/v2/reports/shopping/merchants")
    def test_method_merchants(self) -> None:
        shopping = client.reports.shopping.merchants(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            interval="day",
        )

    @smoke_case("reports.shopping.merchants:all", operation="merchants", path="/v2/reports/shopping/merchants")
    def test_method_merchants_with_all_params(self) -> None:
        shopping = client.reports.shopping.merchants(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            group_by=["date"],
            metrics=["merchant_share"],
            interval="day",
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            limit=1,
            max_results=1,
            cursor="",
        )

    @smoke_case(
        "reports.shopping.streamMerchants:required",
        operation="streamMerchants",
        path="/v2/reports/shopping/merchants/stream",
    )
    def test_method_stream_merchants(self) -> None:
        stream = client.reports.shopping.stream_merchants(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            interval="day",
        )

        for event in stream:
            print(event)

    @smoke_case(
        "reports.shopping.streamMerchants:all",
        operation="streamMerchants",
        path="/v2/reports/shopping/merchants/stream",
    )
    def test_method_stream_merchants_with_all_params(self) -> None:
        stream = client.reports.shopping.stream_merchants(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            group_by=["date"],
            metrics=["merchant_share"],
            interval="day",
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            limit=1,
            max_results=1,
            cursor="",
        )

        for event in stream:
            print(event)

    @smoke_case(
        "reports.shopping.triggerRate:required", operation="triggerRate", path="/v2/reports/shopping/trigger-rate"
    )
    def test_method_trigger_rate(self) -> None:
        shopping = client.reports.shopping.trigger_rate(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            interval="day",
        )

    @smoke_case("reports.shopping.triggerRate:all", operation="triggerRate", path="/v2/reports/shopping/trigger-rate")
    def test_method_trigger_rate_with_all_params(self) -> None:
        shopping = client.reports.shopping.trigger_rate(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            group_by=["date"],
            metrics=["total_runs"],
            interval="day",
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            limit=1,
            max_results=1,
            cursor="",
        )

    @smoke_case(
        "reports.shopping.streamTriggerRate:required",
        operation="streamTriggerRate",
        path="/v2/reports/shopping/trigger-rate/stream",
    )
    def test_method_stream_trigger_rate(self) -> None:
        stream = client.reports.shopping.stream_trigger_rate(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            interval="day",
        )

        for event in stream:
            print(event)

    @smoke_case(
        "reports.shopping.streamTriggerRate:all",
        operation="streamTriggerRate",
        path="/v2/reports/shopping/trigger-rate/stream",
    )
    def test_method_stream_trigger_rate_with_all_params(self) -> None:
        stream = client.reports.shopping.stream_trigger_rate(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            group_by=["date"],
            metrics=["total_runs"],
            interval="day",
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            limit=1,
            max_results=1,
            cursor="",
        )

        for event in stream:
            print(event)
