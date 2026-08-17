# profound Python API

Complete reference of every operation, grouped by resource. See [the README](./README.md) for usage and configuration.

## Contents

- [`Organizations`](#organizations)
  - [Get Regions](#get-regions)
  - [Get Models](#get-models)
  - [Get Domains](#get-domains)
  - [Get Assets](#get-assets)
  - [Get Personas](#get-personas)
  - [List organizations](#list-organizations)
  - [`Organizations Categories`](#organizations-categories)
    - [Get Categories](#get-categories)
    - [Get Category Topics](#get-category-topics)
    - [Get Category Tags](#get-category-tags)
    - [List prompts](#list-prompts)
    - [Get Category Assets](#get-category-assets)
    - [Get Category Personas](#get-category-personas)
    - [Create prompts](#create-prompts)
    - [Update prompts](#update-prompts)
    - [Update prompt status](#update-prompt-status)
- [`Prompts`](#prompts)
  - [Get Answers](#get-answers)
- [`Reports`](#reports)
  - [Query Citations](#query-citations)
  - [Query Visibility](#query-visibility)
  - [Query Sentiment](#query-sentiment)
  - [Get Referrals Report V1](#get-referrals-report-v1)
  - [Get Bots Report V1](#get-bots-report-v1)
  - [Get Referrals Report V2](#get-referrals-report-v2)
  - [Get Bots Report V2](#get-bots-report-v2)
  - [Query Fanouts](#query-fanouts)
  - [Stream Citations](#stream-citations)
  - [Stream Visibility](#stream-visibility)
  - [Stream Sentiment](#stream-sentiment)
  - [`Reports WebSearchResults`](#reports-websearchresults)
    - [Query Web Search Results](#query-web-search-results)
    - [Stream Web Search Results](#stream-web-search-results)
  - [`Reports Shopping`](#reports-shopping)
    - [Shopping Visibility](#shopping-visibility)
    - [Shopping Item Visibility](#shopping-item-visibility)
    - [Shopping Merchant Distribution](#shopping-merchant-distribution)
    - [Shopping Merchant Visibility By Brand](#shopping-merchant-visibility-by-brand)
    - [Shopping Merchant By Items](#shopping-merchant-by-items)
    - [Shopping All Items With Merchants](#shopping-all-items-with-merchants)
    - [Shopping Trigger Rate](#shopping-trigger-rate)
    - [Shopping Merchant Share](#shopping-merchant-share)
    - [Shopping Product Merchant Urls](#shopping-product-merchant-urls)
    - [Shopping Executions](#shopping-executions)
- [`Content`](#content)
  - [`Content Optimization`](#content-optimization)
    - [Optimization List](#optimization-list)
    - [Optimization Analysis](#optimization-analysis)
- [`Agents`](#agents)
  - [List agents](#list-agents)
  - [Get an agent](#get-an-agent)
  - [`Agents Runs`](#agents-runs)
    - [Run an agent](#run-an-agent)
    - [Get an agent run](#get-an-agent-run)
- [`KnowledgeBases`](#knowledgebases)
  - [List Knowledge Bases](#list-knowledge-bases)
  - [Search Knowledge Base](#search-knowledge-base)
  - [`KnowledgeBases Documents`](#knowledgebases-documents)
    - [Add Document](#add-document)
    - [Update Document](#update-document)
    - [Delete Document](#delete-document)
  - [`KnowledgeBases Folders`](#knowledgebases-folders)
    - [Add Folder](#add-folder)
    - [Delete Folder](#delete-folder)

## Setup

```python
import os

from profound import Profound

client = Profound(
    api_key=os.environ.get("PROFOUND_API_KEY"),
)
```

## `Organizations`

### Get Regions

Get the organization regions.

| Direction | Type |
| --- | --- |
| Request | [`OrganizationRegionsParams`](./src/profound/types/organization_regions_params.py) |
| Response | [`OrganizationRegionsResponse`](./src/profound/types/organization_regions_response.py) |

```python
organization = client.organizations.regions()
```

### Get Models

Get the organization models.

| Direction | Type |
| --- | --- |
| Response | [`OrganizationModelsResponse`](./src/profound/types/organization_models_response.py) |

```python
organization = client.organizations.models()
```

### Get Domains

Get the organization domains.

| Direction | Type |
| --- | --- |
| Request | [`OrganizationDomainsParams`](./src/profound/types/organization_domains_params.py) |
| Response | [`OrganizationDomainsResponse`](./src/profound/types/organization_domains_response.py) |

```python
organization = client.organizations.domains()
```

### Get Assets

Get the organization assets, one row per (asset, organization) pair.

An asset's category can belong to multiple organizations; one asset row is
emitted per owning org so no association is silently dropped.

| Direction | Type |
| --- | --- |
| Request | [`OrganizationListAssetsParams`](./src/profound/types/organization_list_assets_params.py) |
| Response | [`OrganizationListAssetsResponse`](./src/profound/types/organization_list_assets_response.py) |

```python
organization = client.organizations.list_assets()
```

### Get Personas

Get the organization personas, one row per (persona, organization) pair.

Same (item, org) fan-out as ``get_assets``: a persona's category can be
owned by multiple orgs, and each owning org gets its own row so no
association is silently dropped.

| Direction | Type |
| --- | --- |
| Request | [`OrganizationGetPersonasParams`](./src/profound/types/organization_get_personas_params.py) |
| Response | [`OrganizationGetPersonasResponse`](./src/profound/types/organization_get_personas_response.py) |

```python
organization = client.organizations.get_personas()
```

### List organizations

Return every organization the caller's API key grants access to. Use this to discover organization IDs before calling endpoints that accept an `organization_id` filter.

| Direction | Type |
| --- | --- |
| Response | [`OrganizationListResponse`](./src/profound/types/organization_list_response.py) |

```python
organization = client.organizations.list()
```

### `Organizations Categories`

#### Get Categories

Get the organization categories, one row per (category, organization) pair.

| Direction | Type |
| --- | --- |
| Request | [`CategoryListParams`](./src/profound/types/organizations/category_list_params.py) |
| Response | [`CategoryListResponse`](./src/profound/types/organizations/category_list_response.py) |

```python
category = client.organizations.categories.list()
```

#### Get Category Topics

Get the topics for a specific category.

| Direction | Type |
| --- | --- |
| Response | [`CategoryTopicsResponse`](./src/profound/types/organizations/category_topics_response.py) |

```python
category = client.organizations.categories.topics(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Get Category Tags

Get the tags for a specific category.

| Direction | Type |
| --- | --- |
| Response | [`CategoryTagsResponse`](./src/profound/types/organizations/category_tags_response.py) |

```python
category = client.organizations.categories.tags(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### List prompts

Retrieve prompts in a category with optional filtering by type, topic, tag, region, platform, or persona. Supports cursor-based pagination.

| Direction | Type |
| --- | --- |
| Request | [`CategoryPromptsParams`](./src/profound/types/organizations/category_prompts_params.py) |
| Response | [`CategoryPromptsResponse`](./src/profound/types/organizations/category_prompts_response.py) |

```python
category = client.organizations.categories.prompts(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    limit=10000,
    status=["active"],
)
```

#### Get Category Assets

| Direction | Type |
| --- | --- |
| Response | [`CategoryAssetsResponse`](./src/profound/types/organizations/category_assets_response.py) |

```python
category = client.organizations.categories.assets(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Get Category Personas

| Direction | Type |
| --- | --- |
| Response | [`CategoryGetCategoryPersonasResponse`](./src/profound/types/organizations/category_get_category_personas_response.py) |

```python
category = client.organizations.categories.get_category_personas(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Create prompts

Create one or more prompts in a category. Topics and tags are auto-created if referenced by name and not yet existing. Use dry_run to preview without persisting.

| Direction | Type |
| --- | --- |
| Request | [`CategoryCreatePromptsParams`](./src/profound/types/organizations/category_create_prompts_params.py) |
| Response | [`CategoryCreatePromptsResponse`](./src/profound/types/organizations/category_create_prompts_response.py) |

```python
category = client.organizations.categories.create_prompts(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    prompts=[],
    dry_run=False,
)
```

#### Update prompts

Update one or more existing prompts. Only provided fields are changed. Dimension fields (regions, platforms, personas, tags) replace the full set when provided. Use dry_run to preview without persisting.

| Direction | Type |
| --- | --- |
| Request | [`CategoryUpdatePromptsParams`](./src/profound/types/organizations/category_update_prompts_params.py) |
| Response | [`CategoryUpdatePromptsResponse`](./src/profound/types/organizations/category_update_prompts_response.py) |

```python
category = client.organizations.categories.update_prompts(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    prompts=[],
    dry_run=False,
)
```

#### Update prompt status

Bulk-update the status of one or more prompts. Prompts already in the target status are skipped. Use dry_run to preview without persisting.

Status options:
- 'active': Prompts will run daily.
- 'disabled': Prompts will not run moving forward, but historical data is preserved.
- 'deleted': Prompts are deleted along with historical data

| Direction | Type |
| --- | --- |
| Request | [`CategoryUpdatePromptStatusParams`](./src/profound/types/organizations/category_update_prompt_status_params.py) |
| Response | [`CategoryUpdatePromptStatusResponse`](./src/profound/types/organizations/category_update_prompt_status_response.py) |

```python
category = client.organizations.categories.update_prompt_status(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    prompt_ids=[],
    status="active",
    dry_run=False,
)
```

## `Prompts`

### Get Answers

| Direction | Type |
| --- | --- |
| Request | [`PromptAnswersParams`](./src/profound/types/prompt_answers_params.py) |
| Response | [`PromptAnswersResponse`](./src/profound/types/prompt_answers_response.py) |

```python
prompt = client.prompts.answers(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
)
```

## `Reports`

### Query Citations

Get citations for a given category.

The ``mentioned`` filter supports ``is true`` and ``is false``. It uses the
latest page analysis available at or before ``end_date``; pages without an
analysis by then are excluded from both values. ``citation_share`` keeps all
otherwise eligible citations in its denominator when this filter is used.

| Direction | Type |
| --- | --- |
| Request | [`ReportCitationsParams`](./src/profound/types/report_citations_params.py) |
| Response | [`ReportCitationsResponse`](./src/profound/types/report_citations_response.py) |

```python
report = client.reports.citations(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
)
```

### Query Visibility

Query visibility report.

| Direction | Type |
| --- | --- |
| Request | [`ReportVisibilityParams`](./src/profound/types/report_visibility_params.py) |
| Response | [`ReportResponse`](./src/profound/types/report_response.py) |

```python
report = client.reports.visibility(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
)
```

### Query Sentiment

Get citations for a given category.

| Direction | Type |
| --- | --- |
| Request | [`ReportSentimentParams`](./src/profound/types/report_sentiment_params.py) |
| Response | [`ReportResponse`](./src/profound/types/report_response.py) |

```python
report = client.reports.sentiment(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
)
```

### Get Referrals Report V1

Get referral traffic report from the daily aggregated materialized view.

This endpoint queries pre-aggregated daily referral data, making it efficient
for large date ranges and high-traffic sites.

| Direction | Type |
| --- | --- |
| Request | [`ReportGetReferralsReportParams`](./src/profound/types/report_get_referrals_report_params.py) |
| Response | [`ReportResponse`](./src/profound/types/report_response.py) |

```python
report = client.reports.get_referrals_report(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    domain="",
    start_date="2024-01-01T00:00:00.000Z",
)
```

### Get Bots Report V1

Get bot traffic report from the daily aggregated materialized view.

This endpoint queries pre-aggregated daily bot data, making it efficient
for large date ranges and high-traffic sites.

Metrics:
- count: unique bot visits
- citations: unique citation events
- indexing: unique indexing events
- training: unique training events
- last_visit: most recent visit timestamp

| Direction | Type |
| --- | --- |
| Request | [`ReportGetBotsReportParams`](./src/profound/types/report_get_bots_report_params.py) |
| Response | [`ReportResponse`](./src/profound/types/report_response.py) |

```python
report = client.reports.get_bots_report(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    domain="",
    start_date="2024-01-01T00:00:00.000Z",
)
```

### Get Referrals Report V2

Get referral traffic report from the hourly aggregated materialized view (UTC-based).

Supports date_interval="hour", calendar intervals through "year", "quarter", and "relative_week".

| Direction | Type |
| --- | --- |
| Request | [`ReportGetReferralsReportV2Params`](./src/profound/types/report_get_referrals_report_v2_params.py) |
| Response | [`ReportResponse`](./src/profound/types/report_response.py) |

```python
report = client.reports.get_referrals_report_v2(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    domain="",
    start_date="2024-01-01T00:00:00.000Z",
    timezone="UTC",
)
```

### Get Bots Report V2

Get bot traffic report from the hourly aggregated materialized view (UTC-based).

Supports date_interval="hour", calendar intervals through "year", "quarter", and "relative_week".

Metrics:
- count: unique bot visits
- citations: unique citation events (ai_assistant bot type)
- indexing: unique indexing events (index bot type)
- training: unique training events (ai_training bot type)
- last_visit: most recent visit timestamp

Dimensions:
- date, path, bot_name, bot_provider, bot_type

| Direction | Type |
| --- | --- |
| Request | [`ReportGetBotsReportV2Params`](./src/profound/types/report_get_bots_report_v2_params.py) |
| Response | [`ReportResponse`](./src/profound/types/report_response.py) |

```python
report = client.reports.get_bots_report_v2(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    domain="",
    start_date="2024-01-01T00:00:00.000Z",
    timezone="UTC",
)
```

### Query Fanouts

| Direction | Type |
| --- | --- |
| Request | [`ReportQueryFanoutsParams`](./src/profound/types/report_query_fanouts_params.py) |
| Response | [`ReportResponse`](./src/profound/types/report_response.py) |

```python
report = client.reports.query_fanouts(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
)
```

### Stream Citations

Stream citations with the same filter semantics as the non-streaming route.

| Direction | Type |
| --- | --- |
| Request | [`ReportStreamCitationsParams`](./src/profound/types/report_stream_citations_params.py) |
| Response | [`ReportStreamCitationsResponse`](./src/profound/types/report_stream_citations_response.py) |

```python
stream = client.reports.stream_citations(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
)

for event in stream:
    print(event)
```

### Stream Visibility

| Direction | Type |
| --- | --- |
| Request | [`ReportStreamVisibilityParams`](./src/profound/types/report_stream_visibility_params.py) |
| Response | [`ReportStreamVisibilityResponse`](./src/profound/types/report_stream_visibility_response.py) |

```python
stream = client.reports.stream_visibility(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
)

for event in stream:
    print(event)
```

### Stream Sentiment

| Direction | Type |
| --- | --- |
| Request | [`ReportStreamSentimentParams`](./src/profound/types/report_stream_sentiment_params.py) |
| Response | [`ReportStreamSentimentResponse`](./src/profound/types/report_stream_sentiment_response.py) |

```python
stream = client.reports.stream_sentiment(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
)

for event in stream:
    print(event)
```

### `Reports WebSearchResults`

#### Query Web Search Results

Get web search results for a given category.

| Direction | Type |
| --- | --- |
| Request | [`WebSearchResultQueryParams`](./src/profound/types/reports/web_search_result_query_params.py) |
| Response | [`WebSearchResultQueryResponse`](./src/profound/types/reports/web_search_result_query_response.py) |

```python
web_search_result = client.reports.web_search_results.query(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
)
```

#### Stream Web Search Results

| Direction | Type |
| --- | --- |
| Request | [`WebSearchResultStreamParams`](./src/profound/types/reports/web_search_result_stream_params.py) |
| Response | [`WebSearchResultStreamResponse`](./src/profound/types/reports/web_search_result_stream_response.py) |

```python
stream = client.reports.web_search_results.stream(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
)

for event in stream:
    print(event)
```

### `Reports Shopping`

#### Shopping Visibility

| Direction | Type |
| --- | --- |
| Request | [`ShoppingVisibilityParams`](./src/profound/types/reports/shopping_visibility_params.py) |
| Response | [`ShoppingVisibilityResponse`](./src/profound/types/reports/shopping_visibility_response.py) |

```python
shopping = client.reports.shopping.visibility(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
    date_interval="day",
    include_count=False,
    tag_filter_type="any",
    include_no_tag=False,
    exclude_topic_ids=False,
    include_asset_only=False,
    rank_by="visibility_score",
    include_position_frequency=False,
)
```

#### Shopping Item Visibility

| Direction | Type |
| --- | --- |
| Request | [`ShoppingItemVisibilityParams`](./src/profound/types/reports/shopping_item_visibility_params.py) |
| Response | [`ShoppingItemVisibilityResponse`](./src/profound/types/reports/shopping_item_visibility_response.py) |

```python
shopping = client.reports.shopping.item_visibility(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
    date_interval="day",
    include_count=False,
    tag_filter_type="any",
    include_no_tag=False,
    exclude_topic_ids=False,
    merchant_filter_type="any",
    include_competitors=False,
    competitor_limit=5,
    include_position_frequency=False,
)
```

#### Shopping Merchant Distribution

| Direction | Type |
| --- | --- |
| Request | [`ShoppingMerchantDistributionParams`](./src/profound/types/reports/shopping_merchant_distribution_params.py) |
| Response | [`ShoppingMerchantDistributionResponse`](./src/profound/types/reports/shopping_merchant_distribution_response.py) |

```python
shopping = client.reports.shopping.merchant_distribution(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
    date_interval="day",
    include_count=False,
    tag_filter_type="any",
    include_no_tag=False,
    exclude_topic_ids=False,
)
```

#### Shopping Merchant Visibility By Brand

| Direction | Type |
| --- | --- |
| Request | [`ShoppingMerchantVisibilityByBrandParams`](./src/profound/types/reports/shopping_merchant_visibility_by_brand_params.py) |
| Response | [`ShoppingMerchantVisibilityByBrandResponse`](./src/profound/types/reports/shopping_merchant_visibility_by_brand_response.py) |

```python
shopping = client.reports.shopping.merchant_visibility_by_brand(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
    date_interval="day",
    include_count=False,
    tag_filter_type="any",
    include_no_tag=False,
    exclude_topic_ids=False,
    include_brand_only=False,
)
```

#### Shopping Merchant By Items

| Direction | Type |
| --- | --- |
| Request | [`ShoppingMerchantByItemsParams`](./src/profound/types/reports/shopping_merchant_by_items_params.py) |
| Response | [`ShoppingMerchantByItemsResponse`](./src/profound/types/reports/shopping_merchant_by_items_response.py) |

```python
shopping = client.reports.shopping.merchant_by_items(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
    date_interval="day",
    include_count=False,
    tag_filter_type="any",
    include_no_tag=False,
    exclude_topic_ids=False,
)
```

#### Shopping All Items With Merchants

| Direction | Type |
| --- | --- |
| Request | [`ShoppingAllItemsWithMerchantsParams`](./src/profound/types/reports/shopping_all_items_with_merchants_params.py) |
| Response | [`ShoppingAllItemsWithMerchantsResponse`](./src/profound/types/reports/shopping_all_items_with_merchants_response.py) |

```python
shopping = client.reports.shopping.all_items_with_merchants(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
    date_interval="day",
    include_count=False,
    tag_filter_type="any",
    include_no_tag=False,
    exclude_topic_ids=False,
    merchant_filter_type="any",
    rank_by="visibility",
    sort_order="desc",
)
```

#### Shopping Trigger Rate

| Direction | Type |
| --- | --- |
| Request | [`ShoppingTriggerRateParams`](./src/profound/types/reports/shopping_trigger_rate_params.py) |
| Response | [`ShoppingTriggerRateResponse`](./src/profound/types/reports/shopping_trigger_rate_response.py) |

```python
shopping = client.reports.shopping.trigger_rate(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
    date_interval="day",
    include_count=False,
    tag_filter_type="any",
    include_no_tag=False,
    exclude_topic_ids=False,
)
```

#### Shopping Merchant Share

| Direction | Type |
| --- | --- |
| Request | [`ShoppingMerchantShareParams`](./src/profound/types/reports/shopping_merchant_share_params.py) |
| Response | [`ShoppingMerchantShareResponse`](./src/profound/types/reports/shopping_merchant_share_response.py) |

```python
shopping = client.reports.shopping.merchant_share(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
    date_interval="day",
    include_count=False,
    tag_filter_type="any",
    include_no_tag=False,
    exclude_topic_ids=False,
)
```

#### Shopping Product Merchant Urls

| Direction | Type |
| --- | --- |
| Request | [`ShoppingProductMerchantURLsParams`](./src/profound/types/reports/shopping_product_merchant_urls_params.py) |
| Response | [`ShoppingProductMerchantURLsResponse`](./src/profound/types/reports/shopping_product_merchant_urls_response.py) |

```python
shopping = client.reports.shopping.product_merchant_urls(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    product_names=[],
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
)
```

#### Shopping Executions

| Direction | Type |
| --- | --- |
| Request | [`ShoppingExecutionsParams`](./src/profound/types/reports/shopping_executions_params.py) |
| Response | [`ShoppingExecutionsResponse`](./src/profound/types/reports/shopping_executions_response.py) |

```python
shopping = client.reports.shopping.executions(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
    date_interval="day",
    include_count=False,
    tag_filter_type="any",
    include_no_tag=False,
    exclude_topic_ids=False,
    analysis_filter_type="any",
)
```

## `Content`

### `Content Optimization`

#### Optimization List

| Direction | Type |
| --- | --- |
| Request | [`OptimizationListParams`](./src/profound/types/content/optimization_list_params.py) |
| Response | [`OptimizationListResponse`](./src/profound/types/content/optimization_list_response.py) |

```python
optimization = client.content.optimization.list(
    asset_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    limit=10000,
    offset=0,
)
```

#### Optimization Analysis

| Direction | Type |
| --- | --- |
| Response | [`OptimizationRetrieveResponse`](./src/profound/types/content/optimization_retrieve_response.py) |

```python
optimization = client.content.optimization.retrieve(
    asset_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    content_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

## `Agents`

### List agents

List agents available to your organization.

Agent status reflects whether an agent has ever been published. `published`
agents have a live published version. `draft` agents have not been
published yet.

| Direction | Type |
| --- | --- |
| Request | [`AgentListParams`](./src/profound/types/agent_list_params.py) |
| Response | [`AgentListResponse`](./src/profound/types/agent_list_response.py) |

```python
agent = client.agents.list(
    limit=100,
)
```

### Get an agent

Retrieve an agent and its schema details.

Agents can have both a live published version and a draft version with newer
unpublished changes. Use the `version` parameter to choose which state to return.

| Direction | Type |
| --- | --- |
| Request | [`AgentRetrieveParams`](./src/profound/types/agent_retrieve_params.py) |
| Response | [`AgentRetrieveResponse`](./src/profound/types/agent_retrieve_response.py) |

```python
agent = client.agents.retrieve(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### `Agents Runs`

#### Run an agent

Start a new run for an agent.

Runs always execute the agent's live published version, so the agent must be
published first with `POST /v1/agents/{agent_id}/publish`. Unpublished drafts
cannot be run.

| Direction | Type |
| --- | --- |
| Request | [`RunCreateParams`](./src/profound/types/agents/run_create_params.py) |
| Response | [`RunCreateResponse`](./src/profound/types/agents/run_create_response.py) |

```python
run = client.agents.runs.create(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Get an agent run

Retrieve the current status and result details for an agent run.

| Direction | Type |
| --- | --- |
| Request | [`RunRetrieveParams`](./src/profound/types/agents/run_retrieve_params.py) |
| Response | [`RunRetrieveResponse`](./src/profound/types/agents/run_retrieve_response.py) |

```python
run = client.agents.runs.retrieve(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    run_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    verbose=False,
)
```

## `KnowledgeBases`

### List Knowledge Bases

List knowledge bases accessible to the API key.

| Direction | Type |
| --- | --- |
| Request | [`KnowledgeBaseListParams`](./src/profound/types/knowledge_base_list_params.py) |
| Response | [`KnowledgeBaseListResponse`](./src/profound/types/knowledge_base_list_response.py) |

```python
knowledge_base = client.knowledge_bases.list()
```

### Search Knowledge Base

Search a knowledge base and return matching snippets or pages.

| Direction | Type |
| --- | --- |
| Request | [`KnowledgeBaseSearchParams`](./src/profound/types/knowledge_base_search_params.py) |
| Response | [`KnowledgeBaseSearchResponse`](./src/profound/types/knowledge_base_search_response.py) |

```python
knowledge_base = client.knowledge_bases.search(
    knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    query="x",
    top_k=0,
    return_full_page=False,
)
```

### `KnowledgeBases Documents`

#### Add Document

Add a document to a knowledge base using JSON text or multipart file upload.

| Direction | Type |
| --- | --- |
| Request | [`DocumentCreateParams`](./src/profound/types/knowledge_bases/document_create_params.py) |
| Response | [`DocumentCreateResponse`](./src/profound/types/knowledge_bases/document_create_response.py) |

```python
document = client.knowledge_bases.documents.create(
    knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    name="x",
    text="x",
)
```

#### Update Document

Overwrite a knowledge base document using JSON text or multipart file upload.

| Direction | Type |
| --- | --- |
| Request | [`DocumentUpdateParams`](./src/profound/types/knowledge_bases/document_update_params.py) |
| Response | [`DocumentUpdateResponse`](./src/profound/types/knowledge_bases/document_update_response.py) |

```python
document = client.knowledge_bases.documents.update(
    knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    name="x",
    text="x",
)
```

#### Delete Document

Delete an existing document from a knowledge base.

| Direction | Type |
| --- | --- |
| Request | [`DocumentDeleteParams`](./src/profound/types/knowledge_bases/document_delete_params.py) |
| Response | [`DocumentDeleteResponse`](./src/profound/types/knowledge_bases/document_delete_response.py) |

```python
document = client.knowledge_bases.documents.delete(
    knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    name="x",
)
```

### `KnowledgeBases Folders`

#### Add Folder

Create an empty folder at the requested knowledge base path.

| Direction | Type |
| --- | --- |
| Request | [`FolderCreateParams`](./src/profound/types/knowledge_bases/folder_create_params.py) |
| Response | [`FolderCreateResponse`](./src/profound/types/knowledge_bases/folder_create_response.py) |

```python
folder = client.knowledge_bases.folders.create(
    knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    path="x",
)
```

#### Delete Folder

Delete a folder. With recursive=false, non-empty folders return 409 and no contents are deleted.

| Direction | Type |
| --- | --- |
| Request | [`FolderDeleteParams`](./src/profound/types/knowledge_bases/folder_delete_params.py) |
| Response | [`FolderDeleteResponse`](./src/profound/types/knowledge_bases/folder_delete_response.py) |

```python
folder = client.knowledge_bases.folders.delete(
    knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    path="x",
    recursive=False,
)
```
