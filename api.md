# profound Python API

Complete reference of every operation, grouped by resource. See [the README](./README.md) for usage and configuration.

## Contents

- [`Organization`](#organization)
  - [Get Category Regions](#get-category-regions)
- [`Prompts`](#prompts)
  - [`Prompts Answers`](#prompts-answers)
    - [Get Answers](#get-answers)
    - [Query Answers V2](#query-answers-v2)
    - [Stream Answers V2](#stream-answers-v2)
- [`Reports`](#reports)
  - [Query Sentiment V2](#query-sentiment-v2)
  - [`Reports Citations`](#reports-citations)
    - [Query Citations](#query-citations)
    - [Stream Citations](#stream-citations)
    - [Query Citations V2](#query-citations-v2)
    - [Stream Citations V2](#stream-citations-v2)
  - [`Reports Visibility`](#reports-visibility)
    - [Query Visibility](#query-visibility)
    - [Stream Visibility](#stream-visibility)
    - [Query Visibility V2](#query-visibility-v2)
    - [Stream Visibility V2](#stream-visibility-v2)
  - [`Reports Sentiment`](#reports-sentiment)
    - [Query Sentiment](#query-sentiment)
    - [Stream Sentiment](#stream-sentiment)
    - [Query Sentiment V2](#query-sentiment-v2-1)
    - [Stream Sentiment V2](#stream-sentiment-v2)
  - [`Reports WebSearchResults`](#reports-websearchresults)
    - [Query Web Search Results](#query-web-search-results)
    - [Stream Web Search Results](#stream-web-search-results)
  - [`Reports Referrals`](#reports-referrals)
    - [Get Referrals Report V1](#get-referrals-report-v1)
    - [Get Referrals Report V2](#get-referrals-report-v2)
  - [`Reports Bots`](#reports-bots)
    - [Get Bots Report V1](#get-bots-report-v1)
    - [Get Bots Report V2](#get-bots-report-v2)
  - [`Reports QueryFanouts`](#reports-queryfanouts)
    - [Query Fanouts](#query-fanouts)
    - [Query Fanouts V2](#query-fanouts-v2)
    - [Stream Query Fanouts V2](#stream-query-fanouts-v2)
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
  - [`Reports Accuracy`](#reports-accuracy)
    - [Accuracy Overview](#accuracy-overview)
    - [Accuracy Breakdown](#accuracy-breakdown)
    - [Accuracy Citation Analysis](#accuracy-citation-analysis)
    - [Accuracy Topic Ids](#accuracy-topic-ids)
    - [Accuracy Inaccurate Themes](#accuracy-inaccurate-themes)
    - [Accuracy Inaccurate Clusters](#accuracy-inaccurate-clusters)
    - [Accuracy Inaccuracy Drivers](#accuracy-inaccuracy-drivers)
    - [Accuracy Top Inaccurate Claims](#accuracy-top-inaccurate-claims)
    - [Accuracy Claim Breakdown](#accuracy-claim-breakdown)
    - [Accuracy Claim Citations](#accuracy-claim-citations)
    - [Accuracy Cluster Example Runs](#accuracy-cluster-example-runs)
    - [Accuracy Cluster Verification Pairs](#accuracy-cluster-verification-pairs)
    - [Accuracy Factcheck Setup Status](#accuracy-factcheck-setup-status)
- [`Content`](#content)
  - [`Content Optimization`](#content-optimization)
    - [Optimization List](#optimization-list)
    - [Optimization Analysis](#optimization-analysis)
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
- [`Agents`](#agents)
  - [List agents](#list-agents)
  - [Create an agent](#create-an-agent)
  - [Publish an agent](#publish-an-agent)
  - [Get an agent](#get-an-agent)
  - [Update an agent](#update-an-agent)
  - [Get an agent's graph](#get-an-agents-graph)
  - [`Agents NodeTypes`](#agents-nodetypes)
    - [List node types](#list-node-types)
    - [Get a node type schema](#get-a-node-type-schema)
  - [`Agents Runs`](#agents-runs)
    - [Run an agent](#run-an-agent)
    - [Get an agent run](#get-an-agent-run)
- [`Organizations`](#organizations)
  - [List organizations](#list-organizations)
  - [Get Regions](#get-regions)
  - [Get Models](#get-models)
  - [Get Domains](#get-domains)
  - [Get Assets](#get-assets)
  - [Get Personas](#get-personas)
  - [`Organizations Categories`](#organizations-categories)
    - [Get Categories](#get-categories)
    - [Get Category Topics](#get-category-topics)
    - [Get Category Tags](#get-category-tags)
    - [List prompts](#list-prompts)
    - [Create prompts](#create-prompts)
    - [Update prompts](#update-prompts)
    - [Update prompt status](#update-prompt-status)
    - [Get Category Assets](#get-category-assets)
    - [Get Category Personas](#get-category-personas)

## Setup

```python
import os

from profound import Profound

client = Profound(
    api_key_header=os.environ.get("API_KEY_HEADER"),
)
```

## `Organization`

### Get Category Regions

Get the regions for a specific category.

| Direction | Type |
| --- | --- |
| Response | [`OrganizationListCategoryRegionsV1OrgCategoriesCategoryRegionsGetResponse`](./src/types/organization_list_category_regions_v1_org_categories_category_regions_get_response.py) |

```python
organization = client.organization.list_category_regions_v1_org_categories_category_regions_get(
    category_id="categoryId",
)
```

## `Prompts`

### `Prompts Answers`

#### Get Answers

| Direction | Type |
| --- | --- |
| Request | [`AnswerCreateV1PromptsPostParams`](./src/types/prompts/answer_create_v1_prompts_post_params.py) |
| Response | [`AnswerCreateV1PromptsPostResponse`](./src/types/prompts/answer_create_v1_prompts_post_response.py) |

```python
answer = client.prompts.answers.create_v1_prompts_post(
    category_id="",
    start_date="",
    end_date="",
)
```

#### Query Answers V2

| Direction | Type |
| --- | --- |
| Request | [`AnswerQueryV2V2PromptsPostParams`](./src/types/prompts/answer_query_v2_v2_prompts_post_params.py) |
| Response | [`AnswerQueryV2V2PromptsPostResponse`](./src/types/prompts/answer_query_v2_v2_prompts_post_response.py) |

```python
answer = client.prompts.answers.query_v2_v2_prompts_post(
    category_id="",
    start_date="",
    end_date="",
)
```

#### Stream Answers V2

| Direction | Type |
| --- | --- |
| Request | [`AnswerStreamV2V2PromptsStreamPostParams`](./src/types/prompts/answer_stream_v2_v2_prompts_stream_post_params.py) |
| Response | [`AnswerStreamV2V2PromptsStreamPostResponse`](./src/types/prompts/answer_stream_v2_v2_prompts_stream_post_response.py) |

```python
stream = client.prompts.answers.stream_v2_v2_prompts_stream_post(
    category_id="",
    start_date="",
    end_date="",
)
for event in stream:
    print(event)
```

## `Reports`

### Query Sentiment V2

| Direction | Type |
| --- | --- |
| Request | [`ReportQuerySentimentV2V1SentimentV2PostParams`](./src/types/report_query_sentiment_v2_v1_sentiment_v2_post_params.py) |
| Response | [`ReportQuerySentimentV2V1SentimentV2PostResponse`](./src/types/report_query_sentiment_v2_v1_sentiment_v2_post_response.py) |

```python
report = client.reports.query_sentiment_v2_v1_sentiment_v2_post(
    category_id="",
    asset_name="",
    start_date="",
    end_date="",
    date_interval="day",
    metrics=[],
)
```

### `Reports Citations`

#### Query Citations

Get citations for a given category.

| Direction | Type |
| --- | --- |
| Request | [`CitationQueryV1ReportsPostParams`](./src/types/reports/citation_query_v1_reports_post_params.py) |
| Response | [`CitationQueryV1ReportsPostResponse`](./src/types/reports/citation_query_v1_reports_post_response.py) |

```python
citation = client.reports.citations.query_v1_reports_post(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    category_id="",
    start_date="",
    end_date="",
)
```

#### Stream Citations

| Direction | Type |
| --- | --- |
| Request | [`CitationStreamV1ReportsStreamPostParams`](./src/types/reports/citation_stream_v1_reports_stream_post_params.py) |
| Response | [`CitationStreamV1ReportsStreamPostResponse`](./src/types/reports/citation_stream_v1_reports_stream_post_response.py) |

```python
stream = client.reports.citations.stream_v1_reports_stream_post(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    category_id="",
    start_date="",
    end_date="",
)
for event in stream:
    print(event)
```

#### Query Citations V2

| Direction | Type |
| --- | --- |
| Request | [`CitationQueryV2V2ReportsPostParams`](./src/types/reports/citation_query_v2_v2_reports_post_params.py) |
| Response | [`CitationQueryV2V2ReportsPostResponse`](./src/types/reports/citation_query_v2_v2_reports_post_response.py) |

```python
citation = client.reports.citations.query_v2_v2_reports_post(
    category_id="",
    start_date="",
    end_date="",
    interval="day",
    scope="all",
)
```

#### Stream Citations V2

| Direction | Type |
| --- | --- |
| Request | [`CitationStreamV2V2ReportsStreamPostParams`](./src/types/reports/citation_stream_v2_v2_reports_stream_post_params.py) |
| Response | [`CitationStreamV2V2ReportsStreamPostResponse`](./src/types/reports/citation_stream_v2_v2_reports_stream_post_response.py) |

```python
stream = client.reports.citations.stream_v2_v2_reports_stream_post(
    category_id="",
    start_date="",
    end_date="",
    interval="day",
    scope="all",
)
for event in stream:
    print(event)
```

### `Reports Visibility`

#### Query Visibility

Query visibility report.

| Direction | Type |
| --- | --- |
| Request | [`VisibilityQueryV1ReportsPostParams`](./src/types/reports/visibility_query_v1_reports_post_params.py) |
| Response | [`ReportResponse`](./src/types/report_response.py) |

```python
visibility = client.reports.visibility.query_v1_reports_post(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    category_id="",
    start_date="",
    end_date="",
)
```

#### Stream Visibility

| Direction | Type |
| --- | --- |
| Request | [`VisibilityStreamV1ReportsStreamPostParams`](./src/types/reports/visibility_stream_v1_reports_stream_post_params.py) |
| Response | [`VisibilityStreamV1ReportsStreamPostResponse`](./src/types/reports/visibility_stream_v1_reports_stream_post_response.py) |

```python
stream = client.reports.visibility.stream_v1_reports_stream_post(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    category_id="",
    start_date="",
    end_date="",
)
for event in stream:
    print(event)
```

#### Query Visibility V2

| Direction | Type |
| --- | --- |
| Request | [`VisibilityQueryV2V2ReportsPostParams`](./src/types/reports/visibility_query_v2_v2_reports_post_params.py) |
| Response | [`VisibilityQueryV2V2ReportsPostResponse`](./src/types/reports/visibility_query_v2_v2_reports_post_response.py) |

```python
visibility = client.reports.visibility.query_v2_v2_reports_post(
    category_id="",
    start_date="",
    end_date="",
    interval="day",
    scope="owned",
)
```

#### Stream Visibility V2

| Direction | Type |
| --- | --- |
| Request | [`VisibilityStreamV2V2ReportsStreamPostParams`](./src/types/reports/visibility_stream_v2_v2_reports_stream_post_params.py) |
| Response | [`VisibilityStreamV2V2ReportsStreamPostResponse`](./src/types/reports/visibility_stream_v2_v2_reports_stream_post_response.py) |

```python
stream = client.reports.visibility.stream_v2_v2_reports_stream_post(
    category_id="",
    start_date="",
    end_date="",
    interval="day",
    scope="owned",
)
for event in stream:
    print(event)
```

### `Reports Sentiment`

#### Query Sentiment

Get citations for a given category.

| Direction | Type |
| --- | --- |
| Request | [`SentimentQueryV1ReportsPostParams`](./src/types/reports/sentiment_query_v1_reports_post_params.py) |
| Response | [`ReportResponse`](./src/types/report_response.py) |

```python
sentiment = client.reports.sentiment.query_v1_reports_post(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    category_id="",
    start_date="",
    end_date="",
)
```

#### Stream Sentiment

| Direction | Type |
| --- | --- |
| Request | [`SentimentStreamV1ReportsStreamPostParams`](./src/types/reports/sentiment_stream_v1_reports_stream_post_params.py) |
| Response | [`SentimentStreamV1ReportsStreamPostResponse`](./src/types/reports/sentiment_stream_v1_reports_stream_post_response.py) |

```python
stream = client.reports.sentiment.stream_v1_reports_stream_post(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    category_id="",
    start_date="",
    end_date="",
)
for event in stream:
    print(event)
```

#### Query Sentiment V2

| Direction | Type |
| --- | --- |
| Request | [`SentimentQueryV2V2ReportsPostParams`](./src/types/reports/sentiment_query_v2_v2_reports_post_params.py) |
| Response | [`SentimentQueryV2V2ReportsPostResponse`](./src/types/reports/sentiment_query_v2_v2_reports_post_response.py) |

```python
sentiment = client.reports.sentiment.query_v2_v2_reports_post(
    category_id="",
    asset="",
    start_date="",
    end_date="",
    interval="day",
    include_cited_websites=False,
)
```

#### Stream Sentiment V2

| Direction | Type |
| --- | --- |
| Request | [`SentimentStreamV2V2ReportsStreamPostParams`](./src/types/reports/sentiment_stream_v2_v2_reports_stream_post_params.py) |
| Response | [`SentimentStreamV2V2ReportsStreamPostResponse`](./src/types/reports/sentiment_stream_v2_v2_reports_stream_post_response.py) |

```python
stream = client.reports.sentiment.stream_v2_v2_reports_stream_post(
    category_id="",
    asset="",
    start_date="",
    end_date="",
    interval="day",
    include_cited_websites=False,
)
for event in stream:
    print(event)
```

### `Reports WebSearchResults`

#### Query Web Search Results

Get web search results for a given category.

| Direction | Type |
| --- | --- |
| Request | [`WebSearchResultQueryParams`](./src/types/reports/web_search_result_query_params.py) |
| Response | [`WebSearchResultQueryResponse`](./src/types/reports/web_search_result_query_response.py) |

```python
web_search_result = client.reports.web_search_results.query(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    category_id="",
    start_date="",
    end_date="",
)
```

#### Stream Web Search Results

| Direction | Type |
| --- | --- |
| Request | [`WebSearchResultStreamParams`](./src/types/reports/web_search_result_stream_params.py) |
| Response | [`WebSearchResultStreamResponse`](./src/types/reports/web_search_result_stream_response.py) |

```python
stream = client.reports.web_search_results.stream(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    category_id="",
    start_date="",
    end_date="",
)
for event in stream:
    print(event)
```

### `Reports Referrals`

#### Get Referrals Report V1

Get referral traffic report from the daily aggregated materialized view.

This endpoint queries pre-aggregated daily referral data, making it efficient
for large date ranges and high-traffic sites.

| Direction | Type |
| --- | --- |
| Request | [`ReferralCreateReportV1V1ReportsPostParams`](./src/types/reports/referral_create_report_v1_v1_reports_post_params.py) |
| Response | [`ReportResponse`](./src/types/report_response.py) |

```python
referral = client.reports.referrals.create_report_v1_v1_reports_post(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    domain="",
    start_date="",
)
```

#### Get Referrals Report V2

Get referral traffic report from the hourly aggregated materialized view (UTC-based).

Supports date_interval="hour", calendar intervals through "year", "quarter", and "relative_week".

| Direction | Type |
| --- | --- |
| Request | [`ReferralCreateReportV2V2ReportsPostParams`](./src/types/reports/referral_create_report_v2_v2_reports_post_params.py) |
| Response | [`ReportResponse`](./src/types/report_response.py) |

```python
referral = client.reports.referrals.create_report_v2_v2_reports_post(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    domain="",
    start_date="",
)
```

### `Reports Bots`

#### Get Bots Report V1

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
| Request | [`BotCreateReportV1V1ReportsPostParams`](./src/types/reports/bot_create_report_v1_v1_reports_post_params.py) |
| Response | [`ReportResponse`](./src/types/report_response.py) |

```python
bot = client.reports.bots.create_report_v1_v1_reports_post(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    domain="",
    start_date="",
)
```

#### Get Bots Report V2

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
| Request | [`BotCreateReportV2V2ReportsPostParams`](./src/types/reports/bot_create_report_v2_v2_reports_post_params.py) |
| Response | [`ReportResponse`](./src/types/report_response.py) |

```python
bot = client.reports.bots.create_report_v2_v2_reports_post(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    domain="",
    start_date="",
)
```

### `Reports QueryFanouts`

#### Query Fanouts

| Direction | Type |
| --- | --- |
| Request | [`QueryFanoutV1ReportsPostParams`](./src/types/reports/query_fanout_v1_reports_post_params.py) |
| Response | [`ReportResponse`](./src/types/report_response.py) |

```python
query_fanout = client.reports.query_fanouts.v1_reports_post(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    category_id="",
    start_date="",
    end_date="",
)
```

#### Query Fanouts V2

| Direction | Type |
| --- | --- |
| Request | [`QueryFanoutV2V2ReportsPostParams`](./src/types/reports/query_fanout_v2_v2_reports_post_params.py) |
| Response | [`QueryFanoutV2V2ReportsPostResponse`](./src/types/reports/query_fanout_v2_v2_reports_post_response.py) |

```python
query_fanout = client.reports.query_fanouts.v2_v2_reports_post(
    category_id="",
    start_date="",
    end_date="",
    interval="day",
)
```

#### Stream Query Fanouts V2

| Direction | Type |
| --- | --- |
| Request | [`QueryFanoutStreamV2V2ReportsStreamPostParams`](./src/types/reports/query_fanout_stream_v2_v2_reports_stream_post_params.py) |
| Response | [`QueryFanoutStreamV2V2ReportsStreamPostResponse`](./src/types/reports/query_fanout_stream_v2_v2_reports_stream_post_response.py) |

```python
stream = client.reports.query_fanouts.stream_v2_v2_reports_stream_post(
    category_id="",
    start_date="",
    end_date="",
    interval="day",
)
for event in stream:
    print(event)
```

### `Reports Shopping`

#### Shopping Visibility

| Direction | Type |
| --- | --- |
| Request | [`ShoppingVisibilityParams`](./src/types/reports/shopping_visibility_params.py) |
| Response | [`ShoppingVisibilityResponse`](./src/types/reports/shopping_visibility_response.py) |

```python
shopping = client.reports.shopping.visibility(
    category_id="",
    start_date="",
    end_date="",
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
| Request | [`ShoppingItemVisibilityParams`](./src/types/reports/shopping_item_visibility_params.py) |
| Response | [`ShoppingItemVisibilityResponse`](./src/types/reports/shopping_item_visibility_response.py) |

```python
shopping = client.reports.shopping.item_visibility(
    category_id="",
    start_date="",
    end_date="",
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
| Request | [`ShoppingMerchantDistributionParams`](./src/types/reports/shopping_merchant_distribution_params.py) |
| Response | [`ShoppingMerchantDistributionResponse`](./src/types/reports/shopping_merchant_distribution_response.py) |

```python
shopping = client.reports.shopping.merchant_distribution(
    category_id="",
    start_date="",
    end_date="",
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
| Request | [`ShoppingMerchantVisibilityByBrandParams`](./src/types/reports/shopping_merchant_visibility_by_brand_params.py) |
| Response | [`ShoppingMerchantVisibilityByBrandResponse`](./src/types/reports/shopping_merchant_visibility_by_brand_response.py) |

```python
shopping = client.reports.shopping.merchant_visibility_by_brand(
    category_id="",
    start_date="",
    end_date="",
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
| Request | [`ShoppingMerchantByItemsParams`](./src/types/reports/shopping_merchant_by_items_params.py) |
| Response | [`ShoppingMerchantByItemsResponse`](./src/types/reports/shopping_merchant_by_items_response.py) |

```python
shopping = client.reports.shopping.merchant_by_items(
    category_id="",
    start_date="",
    end_date="",
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
| Request | [`ShoppingAllItemsWithMerchantsParams`](./src/types/reports/shopping_all_items_with_merchants_params.py) |
| Response | [`ShoppingAllItemsWithMerchantsResponse`](./src/types/reports/shopping_all_items_with_merchants_response.py) |

```python
shopping = client.reports.shopping.all_items_with_merchants(
    category_id="",
    start_date="",
    end_date="",
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
| Request | [`ShoppingTriggerRateParams`](./src/types/reports/shopping_trigger_rate_params.py) |
| Response | [`ShoppingTriggerRateResponse`](./src/types/reports/shopping_trigger_rate_response.py) |

```python
shopping = client.reports.shopping.trigger_rate(
    category_id="",
    start_date="",
    end_date="",
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
| Request | [`ShoppingMerchantShareParams`](./src/types/reports/shopping_merchant_share_params.py) |
| Response | [`ShoppingMerchantShareResponse`](./src/types/reports/shopping_merchant_share_response.py) |

```python
shopping = client.reports.shopping.merchant_share(
    category_id="",
    start_date="",
    end_date="",
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
| Request | [`ShoppingProductMerchantUrlsParams`](./src/types/reports/shopping_product_merchant_urls_params.py) |
| Response | [`ShoppingProductMerchantUrlsResponse`](./src/types/reports/shopping_product_merchant_urls_response.py) |

```python
shopping = client.reports.shopping.product_merchant_urls(
    category_id="",
    product_names=[],
    start_date="",
    end_date="",
)
```

#### Shopping Executions

| Direction | Type |
| --- | --- |
| Request | [`ShoppingExecutionsParams`](./src/types/reports/shopping_executions_params.py) |
| Response | [`ShoppingExecutionsResponse`](./src/types/reports/shopping_executions_response.py) |

```python
shopping = client.reports.shopping.executions(
    category_id="",
    start_date="",
    end_date="",
    date_interval="day",
    include_count=False,
    tag_filter_type="any",
    include_no_tag=False,
    exclude_topic_ids=False,
    analysis_filter_type="any",
)
```

### `Reports Accuracy`

#### Accuracy Overview

| Direction | Type |
| --- | --- |
| Request | [`AccuracyOverviewV1ReportsOverviewPostParams`](./src/types/reports/accuracy_overview_v1_reports_overview_post_params.py) |
| Response | [`AccuracyOverviewV1ReportsOverviewPostResponse`](./src/types/reports/accuracy_overview_v1_reports_overview_post_response.py) |

```python
accuracy = client.reports.accuracy.overview_v1_reports_overview_post(
    start_date="",
    end_date="",
    category_id="",
    exclude_topic_ids=False,
    tag_filter_type="any",
    include_no_tag=True,
    include_no_persona=True,
    group_by="period",
)
```

#### Accuracy Breakdown

| Direction | Type |
| --- | --- |
| Request | [`AccuracyBreakdownV1ReportsBreakdownPostParams`](./src/types/reports/accuracy_breakdown_v1_reports_breakdown_post_params.py) |
| Response | [`AccuracyBreakdownV1ReportsBreakdownPostResponse`](./src/types/reports/accuracy_breakdown_v1_reports_breakdown_post_response.py) |

```python
accuracy = client.reports.accuracy.breakdown_v1_reports_breakdown_post(
    start_date="",
    end_date="",
    category_id="",
    exclude_topic_ids=False,
    tag_filter_type="any",
    include_no_tag=True,
    include_no_persona=True,
    breakdown_by="citation",
    limit=10,
    offset=0,
    sort_by="citationShare",
    sort_order="desc",
)
```

#### Accuracy Citation Analysis

| Direction | Type |
| --- | --- |
| Request | [`AccuracyCitationAnalysisV1ReportsCitationAnalysisPostParams`](./src/types/reports/accuracy_citation_analysis_v1_reports_citation_analysis_post_params.py) |
| Response | [`AccuracyCitationAnalysisV1ReportsCitationAnalysisPostResponse`](./src/types/reports/accuracy_citation_analysis_v1_reports_citation_analysis_post_response.py) |

```python
accuracy = client.reports.accuracy.citation_analysis_v1_reports_citation_analysis_post(
    category_id="",
    clean_href="",
    start_date="",
    end_date="",
)
```

#### Accuracy Topic Ids

| Direction | Type |
| --- | --- |
| Request | [`AccuracyTopicIdsV1ReportsTopicIdsPostParams`](./src/types/reports/accuracy_topic_ids_v1_reports_topic_ids_post_params.py) |
| Response | [`AccuracyTopicIdsV1ReportsTopicIdsPostResponse`](./src/types/reports/accuracy_topic_ids_v1_reports_topic_ids_post_response.py) |

```python
accuracy = client.reports.accuracy.topic_ids_v1_reports_topic_ids_post(
    category_id="",
    start_date="",
    end_date="",
)
```

#### Accuracy Inaccurate Themes

| Direction | Type |
| --- | --- |
| Request | [`AccuracyInaccurateThemesV1ReportsInaccurateThemesPostParams`](./src/types/reports/accuracy_inaccurate_themes_v1_reports_inaccurate_themes_post_params.py) |
| Response | [`AccuracyInaccurateThemesV1ReportsInaccurateThemesPostResponse`](./src/types/reports/accuracy_inaccurate_themes_v1_reports_inaccurate_themes_post_response.py) |

```python
accuracy = client.reports.accuracy.inaccurate_themes_v1_reports_inaccurate_themes_post(
    start_date="",
    end_date="",
    category_id="",
    exclude_topic_ids=False,
    tag_filter_type="any",
    include_no_tag=True,
    include_no_persona=True,
    limit=10,
    offset=0,
    sort_by="response_share",
    sort_order="desc",
)
```

#### Accuracy Inaccurate Clusters

| Direction | Type |
| --- | --- |
| Request | [`AccuracyInaccurateClustersV1ReportsInaccurateClustersPostParams`](./src/types/reports/accuracy_inaccurate_clusters_v1_reports_inaccurate_clusters_post_params.py) |
| Response | [`AccuracyInaccurateClustersV1ReportsInaccurateClustersPostResponse`](./src/types/reports/accuracy_inaccurate_clusters_v1_reports_inaccurate_clusters_post_response.py) |

```python
accuracy = client.reports.accuracy.inaccurate_clusters_v1_reports_inaccurate_clusters_post(
    start_date="",
    end_date="",
    category_id="",
    exclude_topic_ids=False,
    tag_filter_type="any",
    include_no_tag=True,
    include_no_persona=True,
    theme_id="",
    limit=5000,
    offset=0,
)
```

#### Accuracy Inaccuracy Drivers

| Direction | Type |
| --- | --- |
| Request | [`AccuracyInaccuracyDriversV1ReportsInaccuracyDriversPostParams`](./src/types/reports/accuracy_inaccuracy_drivers_v1_reports_inaccuracy_drivers_post_params.py) |
| Response | [`AccuracyInaccuracyDriversV1ReportsInaccuracyDriversPostResponse`](./src/types/reports/accuracy_inaccuracy_drivers_v1_reports_inaccuracy_drivers_post_response.py) |

```python
accuracy = client.reports.accuracy.inaccuracy_drivers_v1_reports_inaccuracy_drivers_post(
    start_date="",
    end_date="",
    category_id="",
    exclude_topic_ids=False,
    tag_filter_type="any",
    include_no_tag=True,
    include_no_persona=True,
    limit=5,
)
```

#### Accuracy Top Inaccurate Claims

| Direction | Type |
| --- | --- |
| Request | [`AccuracyTopInaccurateClaimsV1ReportsTopInaccurateClaimsPostParams`](./src/types/reports/accuracy_top_inaccurate_claims_v1_reports_top_inaccurate_claims_post_params.py) |
| Response | [`AccuracyTopInaccurateClaimsV1ReportsTopInaccurateClaimsPostResponse`](./src/types/reports/accuracy_top_inaccurate_claims_v1_reports_top_inaccurate_claims_post_response.py) |

```python
accuracy = client.reports.accuracy.top_inaccurate_claims_v1_reports_top_inaccurate_claims_post(
    start_date="",
    end_date="",
    category_id="",
    exclude_topic_ids=False,
    tag_filter_type="any",
    include_no_tag=True,
    include_no_persona=True,
    limit=5,
)
```

#### Accuracy Claim Breakdown

| Direction | Type |
| --- | --- |
| Request | [`AccuracyClaimBreakdownV1ReportsClaimBreakdownPostParams`](./src/types/reports/accuracy_claim_breakdown_v1_reports_claim_breakdown_post_params.py) |
| Response | [`AccuracyClaimBreakdownV1ReportsClaimBreakdownPostResponse`](./src/types/reports/accuracy_claim_breakdown_v1_reports_claim_breakdown_post_response.py) |

```python
accuracy = client.reports.accuracy.claim_breakdown_v1_reports_claim_breakdown_post(
    start_date="",
    end_date="",
    category_id="",
    exclude_topic_ids=False,
    tag_filter_type="any",
    include_no_tag=True,
    include_no_persona=True,
    cluster_id="",
)
```

#### Accuracy Claim Citations

| Direction | Type |
| --- | --- |
| Request | [`AccuracyClaimCitationsV1ReportsClaimCitationsPostParams`](./src/types/reports/accuracy_claim_citations_v1_reports_claim_citations_post_params.py) |
| Response | [`AccuracyClaimCitationsV1ReportsClaimCitationsPostResponse`](./src/types/reports/accuracy_claim_citations_v1_reports_claim_citations_post_response.py) |

```python
accuracy = client.reports.accuracy.claim_citations_v1_reports_claim_citations_post(
    start_date="",
    end_date="",
    category_id="",
    exclude_topic_ids=False,
    tag_filter_type="any",
    include_no_tag=True,
    include_no_persona=True,
    cluster_id="",
    limit=10,
    offset=0,
    sort_order="desc",
)
```

#### Accuracy Cluster Example Runs

| Direction | Type |
| --- | --- |
| Request | [`AccuracyClusterExampleRunsV1ReportsClusterExampleRunsPostParams`](./src/types/reports/accuracy_cluster_example_runs_v1_reports_cluster_example_runs_post_params.py) |
| Response | [`AccuracyClusterExampleRunsV1ReportsClusterExampleRunsPostResponse`](./src/types/reports/accuracy_cluster_example_runs_v1_reports_cluster_example_runs_post_response.py) |

```python
accuracy = client.reports.accuracy.cluster_example_runs_v1_reports_cluster_example_runs_post(
    category_id="",
    cluster_id="",
    start_date="",
    end_date="",
    limit=20,
    offset=0,
)
```

#### Accuracy Cluster Verification Pairs

| Direction | Type |
| --- | --- |
| Request | [`AccuracyClusterVerificationPairsV1ReportsClusterVerificationPairsPostParams`](./src/types/reports/accuracy_cluster_verification_pairs_v1_reports_cluster_verification_pairs_post_params.py) |
| Response | [`AccuracyClusterVerificationPairsV1ReportsClusterVerificationPairsPostResponse`](./src/types/reports/accuracy_cluster_verification_pairs_v1_reports_cluster_verification_pairs_post_response.py) |

```python
accuracy = client.reports.accuracy.cluster_verification_pairs_v1_reports_cluster_verification_pairs_post(
    category_id="",
    cluster_id="",
)
```

#### Accuracy Factcheck Setup Status

| Direction | Type |
| --- | --- |
| Request | [`AccuracyFactcheckSetupStatusV1ReportsFactcheckSetupStatusPostParams`](./src/types/reports/accuracy_factcheck_setup_status_v1_reports_factcheck_setup_status_post_params.py) |
| Response | [`AccuracyFactcheckSetupStatusV1ReportsFactcheckSetupStatusPostResponse`](./src/types/reports/accuracy_factcheck_setup_status_v1_reports_factcheck_setup_status_post_response.py) |

```python
accuracy = client.reports.accuracy.factcheck_setup_status_v1_reports_factcheck_setup_status_post(
    category_id="",
)
```

## `Content`

### `Content Optimization`

#### Optimization List

| Direction | Type |
| --- | --- |
| Request | [`OptimizationListParams`](./src/types/content/optimization_list_params.py) |
| Response | [`OptimizationListResponse`](./src/types/content/optimization_list_response.py) |

```python
optimization = client.content.optimization.list(
    asset_id="assetId",
    limit=10000,
    offset=0,
)
```

#### Optimization Analysis

| Direction | Type |
| --- | --- |
| Response | [`OptimizationRetrieveResponse`](./src/types/content/optimization_retrieve_response.py) |

```python
optimization = client.content.optimization.retrieve(
    asset_id="assetId",
    content_id="contentId",
)
```

## `KnowledgeBases`

### List Knowledge Bases

List knowledge bases accessible to the API key.

| Direction | Type |
| --- | --- |
| Request | [`KnowledgeBaseListParams`](./src/types/knowledge_base_list_params.py) |
| Response | [`KnowledgeBaseListResponse`](./src/types/knowledge_base_list_response.py) |

```python
knowledge_base = client.knowledge_bases.list()
```

### Search Knowledge Base

Search a knowledge base and return matching snippets or pages.

| Direction | Type |
| --- | --- |
| Request | [`KnowledgeBaseSearchParams`](./src/types/knowledge_base_search_params.py) |
| Response | [`KnowledgeBaseSearchResponse`](./src/types/knowledge_base_search_response.py) |

```python
knowledge_base = client.knowledge_bases.search(
    knowledge_base_id="knowledgeBaseId",
    query="",
    top_k=0,
    return_full_page=False,
)
```

### `KnowledgeBases Documents`

#### Add Document

Add a document to a knowledge base using JSON text or multipart file upload.

| Direction | Type |
| --- | --- |
| Request | [`DocumentCreateParams`](./src/types/knowledge_bases/document_create_params.py) |
| Response | [`DocumentCreateResponse`](./src/types/knowledge_bases/document_create_response.py) |

```python
document = client.knowledge_bases.documents.create(
    knowledge_base_id="knowledgeBaseId",
    name="",
    text="",
)
```

#### Update Document

Overwrite a knowledge base document using JSON text or multipart file upload.

| Direction | Type |
| --- | --- |
| Request | [`DocumentUpdateParams`](./src/types/knowledge_bases/document_update_params.py) |
| Response | [`DocumentUpdateResponse`](./src/types/knowledge_bases/document_update_response.py) |

```python
document = client.knowledge_bases.documents.update(
    knowledge_base_id="knowledgeBaseId",
    name="",
    text="",
)
```

#### Delete Document

Delete an existing document from a knowledge base.

| Direction | Type |
| --- | --- |
| Request | [`DocumentDeleteParams`](./src/types/knowledge_bases/document_delete_params.py) |
| Response | [`DocumentDeleteResponse`](./src/types/knowledge_bases/document_delete_response.py) |

```python
document = client.knowledge_bases.documents.delete(
    knowledge_base_id="knowledgeBaseId",
    name="",
)
```

### `KnowledgeBases Folders`

#### Add Folder

Create an empty folder at the requested knowledge base path.

| Direction | Type |
| --- | --- |
| Request | [`FolderCreateParams`](./src/types/knowledge_bases/folder_create_params.py) |
| Response | [`FolderCreateResponse`](./src/types/knowledge_bases/folder_create_response.py) |

```python
folder = client.knowledge_bases.folders.create(
    knowledge_base_id="knowledgeBaseId",
    path="",
)
```

#### Delete Folder

Delete a folder. With recursive=false, non-empty folders return 409 and no contents are deleted.

| Direction | Type |
| --- | --- |
| Request | [`FolderDeleteParams`](./src/types/knowledge_bases/folder_delete_params.py) |
| Response | [`FolderDeleteResponse`](./src/types/knowledge_bases/folder_delete_response.py) |

```python
folder = client.knowledge_bases.folders.delete(
    knowledge_base_id="knowledgeBaseId",
    path="",
    recursive=False,
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
| Request | [`AgentListParams`](./src/types/agent_list_params.py) |
| Response | [`AgentListResponse`](./src/types/agent_list_response.py) |

```python
agent = client.agents.list(
    limit=100,
)
```

### Create an agent

Create a new draft agent owned by the given organization.

`organization_id` is required and you must be a member of it. The agent is created
as a `draft`; publish it with `POST /v1/agents/{agent_id}/publish` once its graph
is ready.

| Direction | Type |
| --- | --- |
| Request | [`AgentCreateV1PostParams`](./src/types/agent_create_v1_post_params.py) |
| Response | [`AgentCreateV1PostResponse`](./src/types/agent_create_v1_post_response.py) |

```python
agent = client.agents.create_v1_post(
    organization_id="",
    name="",
)
```

### Publish an agent

Publish an agent's latest draft as its live published version.

You must be a member of the agent's organization. Publishing promotes the current
draft graph to a new published version. A draft that cannot produce its declared
input/output contract is rejected with `422` and is not published.

| Direction | Type |
| --- | --- |
| Response | [`AgentPublishV1IdPublishPostResponse`](./src/types/agent_publish_v1_id_publish_post_response.py) |

```python
agent = client.agents.publish_v1_id_publish_post(
    agent_id="agentId",
)
```

### Get an agent

Retrieve an agent and its schema details.

Agents can have both a live published version and a draft version with newer
unpublished changes. Use the `version` parameter to choose which state to return.

| Direction | Type |
| --- | --- |
| Request | [`AgentRetrieveParams`](./src/types/agent_retrieve_params.py) |
| Response | [`AgentRetrieveResponse`](./src/types/agent_retrieve_response.py) |

```python
agent = client.agents.retrieve(
    agent_id="agentId",
)
```

### Update an agent

Update an agent's draft graph in place.

You must be a member of the agent's organization. The agent's draft is replaced with the
supplied graph and re-validated, so you can iterate one draft — create, then update per
fix — instead of creating a new agent on every change. The response carries the updated
`validation`; publish with `POST /v1/agents/{agent_id}/publish` once `validation.valid`.

| Direction | Type |
| --- | --- |
| Request | [`AgentUpdateV1IdPatchParams`](./src/types/agent_update_v1_id_patch_params.py) |
| Response | [`AgentUpdateV1IdPatchResponse`](./src/types/agent_update_v1_id_patch_response.py) |

```python
agent = client.agents.update_v1_id_patch(
    agent_id="agentId",
    graph={},
)
```

### Get an agent's graph

Retrieve an agent's full workflow graph (`{nodes, edges}`).

The graph is returned verbatim in the canonical dialect — the same shape `POST /v1/agents`
and `PATCH /v1/agents/{agent_id}` accept — so a known-good agent can be read back, copied,
and edited. Tool-backed nodes appear in their lowered `tool` form rather than the friendly
v1 node types. A `draft` is visible only to its creator; the `published` version is visible
across its organization.

| Direction | Type |
| --- | --- |
| Request | [`AgentListGraphV1GraphGetParams`](./src/types/agent_list_graph_v1_graph_get_params.py) |
| Response | [`AgentListGraphV1GraphGetResponse`](./src/types/agent_list_graph_v1_graph_get_response.py) |

```python
agent = client.agents.list_graph_v1_graph_get(
    agent_id="agentId",
)
```

### `Agents NodeTypes`

#### List node types

List the node types available for building agents.

The set is deterministic and does not depend on the caller, so the response
is safe to cache across sessions. Integration-dependent and dynamic-schema
node types are intentionally excluded in v1.

| Direction | Type |
| --- | --- |
| Response | [`NodeTypeListV1AgentsGetResponse`](./src/types/agents/node_type_list_v1_agents_get_response.py) |

```python
node_type = client.agents.node_types.list_v1_agents_get()
```

#### Get a node type schema

Retrieve the JSON schema and worked examples for a single node type.

The `schema` field is an opaque JSON Schema for the node's configuration.
Use `schema_version` as a cache key — it bumps whenever the schema changes.

| Direction | Type |
| --- | --- |
| Response | [`NodeTypeListSchemaV1AgentsSchemaGetResponse`](./src/types/agents/node_type_list_schema_v1_agents_schema_get_response.py) |

```python
node_type = client.agents.node_types.list_schema_v1_agents_schema_get(
    node_type="nodeType",
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
| Request | [`RunCreateParams`](./src/types/agents/run_create_params.py) |
| Response | [`RunCreateResponse`](./src/types/agents/run_create_response.py) |

```python
run = client.agents.runs.create(
    agent_id="agentId",
)
```

#### Get an agent run

Retrieve the current status and result details for an agent run.

| Direction | Type |
| --- | --- |
| Response | [`RunRetrieveResponse`](./src/types/agents/run_retrieve_response.py) |

```python
run = client.agents.runs.retrieve(
    agent_id="agentId",
    run_id="runId",
)
```

## `Organizations`

### List organizations

Return every organization the caller's API key grants access to. Use this to discover organization IDs before calling endpoints that accept an `organization_id` filter.

| Direction | Type |
| --- | --- |
| Response | [`OrganizationListResponse`](./src/types/organization_list_response.py) |

```python
organization = client.organizations.list()
```

### Get Regions

Get the organization regions.

| Direction | Type |
| --- | --- |
| Request | [`OrganizationRegionsParams`](./src/types/organization_regions_params.py) |
| Response | [`OrganizationRegionsResponse`](./src/types/organization_regions_response.py) |

```python
organization = client.organizations.regions()
```

### Get Models

Get the organization models.

| Direction | Type |
| --- | --- |
| Response | [`OrganizationModelsResponse`](./src/types/organization_models_response.py) |

```python
organization = client.organizations.models()
```

### Get Domains

Get the organization domains.

| Direction | Type |
| --- | --- |
| Request | [`OrganizationDomainsParams`](./src/types/organization_domains_params.py) |
| Response | [`OrganizationDomainsResponse`](./src/types/organization_domains_response.py) |

```python
organization = client.organizations.domains()
```

### Get Assets

Get the organization assets, one row per (asset, organization) pair.

An asset's category can belong to multiple organizations; one asset row is
emitted per owning org so no association is silently dropped.

| Direction | Type |
| --- | --- |
| Request | [`OrganizationListAssetsParams`](./src/types/organization_list_assets_params.py) |
| Response | [`OrganizationListAssetsResponse`](./src/types/organization_list_assets_response.py) |

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
| Request | [`OrganizationGetPersonasParams`](./src/types/organization_get_personas_params.py) |
| Response | [`OrganizationGetPersonasResponse`](./src/types/organization_get_personas_response.py) |

```python
organization = client.organizations.get_personas()
```

### `Organizations Categories`

#### Get Categories

Get the organization categories, one row per (category, organization) pair.

| Direction | Type |
| --- | --- |
| Request | [`CategoryListParams`](./src/types/organizations/category_list_params.py) |
| Response | [`CategoryListResponse`](./src/types/organizations/category_list_response.py) |

```python
category = client.organizations.categories.list()
```

#### Get Category Topics

Get the topics for a specific category.

| Direction | Type |
| --- | --- |
| Response | [`CategoryTopicsResponse`](./src/types/organizations/category_topics_response.py) |

```python
category = client.organizations.categories.topics(
    category_id="categoryId",
)
```

#### Get Category Tags

Get the tags for a specific category.

| Direction | Type |
| --- | --- |
| Response | [`CategoryTagsResponse`](./src/types/organizations/category_tags_response.py) |

```python
category = client.organizations.categories.tags(
    category_id="categoryId",
)
```

#### List prompts

Retrieve prompts in a category with optional filtering by type, topic, tag, region, platform, or persona. Supports cursor-based pagination.

| Direction | Type |
| --- | --- |
| Request | [`CategoryPromptsParams`](./src/types/organizations/category_prompts_params.py) |
| Response | [`CategoryPromptsResponse`](./src/types/organizations/category_prompts_response.py) |

```python
category = client.organizations.categories.prompts(
    category_id="categoryId",
    limit=10000,
    status=["active"],
)
```

#### Create prompts

Create one or more prompts in a category. Topics and tags are auto-created if referenced by name and not yet existing. Use dry_run to preview without persisting.

| Direction | Type |
| --- | --- |
| Request | [`CategoryCreatePromptsParams`](./src/types/organizations/category_create_prompts_params.py) |
| Response | [`CategoryCreatePromptsResponse`](./src/types/organizations/category_create_prompts_response.py) |

```python
category = client.organizations.categories.create_prompts(
    category_id="categoryId",
    prompts=[],
    dry_run=False,
)
```

#### Update prompts

Update one or more existing prompts. Only provided fields are changed. Dimension fields (regions, platforms, personas, tags) replace the full set when provided. Use dry_run to preview without persisting.

| Direction | Type |
| --- | --- |
| Request | [`CategoryUpdatePromptsParams`](./src/types/organizations/category_update_prompts_params.py) |
| Response | [`CategoryUpdatePromptsResponse`](./src/types/organizations/category_update_prompts_response.py) |

```python
category = client.organizations.categories.update_prompts(
    category_id="categoryId",
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
| Request | [`CategoryUpdatePromptStatusParams`](./src/types/organizations/category_update_prompt_status_params.py) |
| Response | [`CategoryUpdatePromptStatusResponse`](./src/types/organizations/category_update_prompt_status_response.py) |

```python
category = client.organizations.categories.update_prompt_status(
    category_id="categoryId",
    prompt_ids=[],
    status="active",
    dry_run=False,
)
```

#### Get Category Assets

| Direction | Type |
| --- | --- |
| Response | [`CategoryAssetsResponse`](./src/types/organizations/category_assets_response.py) |

```python
category = client.organizations.categories.assets(
    category_id="categoryId",
)
```

#### Get Category Personas

| Direction | Type |
| --- | --- |
| Response | [`CategoryGetCategoryPersonasResponse`](./src/types/organizations/category_get_category_personas_response.py) |

```python
category = client.organizations.categories.get_category_personas(
    category_id="categoryId",
)
```
