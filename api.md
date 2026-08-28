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
    - [Get Category Regions](#get-category-regions)
    - [Get Category Citation Categories](#get-category-citation-categories)
- [`Prompts`](#prompts)
  - [Get Answers](#get-answers)
  - [Query Answers V2](#query-answers-v2)
  - [Stream Answers V2](#stream-answers-v2)
- [`Reports`](#reports)
  - [Query Citations](#query-citations)
  - [Query Visibility](#query-visibility)
  - [Query Sentiment](#query-sentiment)
  - [Query Sentiment V2](#query-sentiment-v2)
  - [Get Referrals Report V1](#get-referrals-report-v1)
  - [Get Bots Report V1](#get-bots-report-v1)
  - [Query Fanouts](#query-fanouts)
  - [Stream Citations](#stream-citations)
  - [Stream Visibility](#stream-visibility)
  - [Stream Sentiment](#stream-sentiment)
  - [Stream Citations V2](#stream-citations-v2)
  - [Stream Visibility V2](#stream-visibility-v2)
  - [Stream Sentiment V2](#stream-sentiment-v2)
  - [Stream Query Fanouts V2](#stream-query-fanouts-v2)
  - [Get Referrals Report V2](#get-referrals-report-v2)
  - [Get Bots Report V2](#get-bots-report-v2)
  - [Query Visibility V2](#query-visibility-v2)
  - [Query Citations V2](#query-citations-v2)
  - [Query Sentiment V2](#query-sentiment-v2-1)
  - [Query Fanouts V2](#query-fanouts-v2)
  - [`Reports WebSearchResults`](#reports-websearchresults)
    - [Query Web Search Results](#query-web-search-results)
    - [Stream Web Search Results](#stream-web-search-results)
  - [`Reports Shopping`](#reports-shopping)
    - [Query Shopping Brands V2](#query-shopping-brands-v2)
    - [Stream Shopping Brands V2](#stream-shopping-brands-v2)
    - [Query Shopping Products V2](#query-shopping-products-v2)
    - [Stream Shopping Products V2](#stream-shopping-products-v2)
    - [Query Shopping Merchants V2](#query-shopping-merchants-v2)
    - [Stream Shopping Merchants V2](#stream-shopping-merchants-v2)
    - [Query Shopping Trigger Rate V2](#query-shopping-trigger-rate-v2)
    - [Stream Shopping Trigger Rate V2](#stream-shopping-trigger-rate-v2)
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
  - [`Reports Factcheck`](#reports-factcheck)
    - [Query Scores](#query-scores)
    - [Stream Scores](#stream-scores)
    - [`Reports Factcheck Claims`](#reports-factcheck-claims)
      - [Query Claims](#query-claims)
      - [Stream Claims](#stream-claims)
  - [`Reports Social`](#reports-social)
    - [`Reports Social Youtube`](#reports-social-youtube)
      - [Query Youtube Channels](#query-youtube-channels)
      - [Query Youtube Videos](#query-youtube-videos)
      - [Query Youtube Summary](#query-youtube-summary)
- [`Content`](#content)
  - [`Content Optimization`](#content-optimization)
    - [Optimization List](#optimization-list)
    - [Optimization Analysis](#optimization-analysis)
- [`Agents`](#agents)
  - [List agents](#list-agents)
  - [Get an agent](#get-an-agent)
  - [Create an agent](#create-an-agent)
  - [Publish an agent](#publish-an-agent)
  - [Update an agent](#update-an-agent)
  - [Get an agent's graph](#get-an-agents-graph)
  - [`Agents Runs`](#agents-runs)
    - [Run an agent](#run-an-agent)
    - [Get an agent run](#get-an-agent-run)
  - [`Agents NodeTypes`](#agents-nodetypes)
    - [List node types](#list-node-types)
    - [Get a node type schema](#get-a-node-type-schema)
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
- [`Projects`](#projects)
  - [List Projects](#list-projects)
  - [Create Project](#create-project)
  - [Get Project](#get-project)
  - [Delete Project](#delete-project)
  - [Get Project Status](#get-project-status)
  - [Archive Project](#archive-project)
  - [Unarchive Project](#unarchive-project)
  - [`Projects Generations`](#projects-generations)
    - [List Project Generations](#list-project-generations)
    - [Get Project Generation Status](#get-project-generation-status)
  - [`Projects Tasks`](#projects-tasks)
    - [List Project Tasks](#list-project-tasks)
    - [Create Project Task](#create-project-task)
    - [Get Project Task](#get-project-task)
    - [Update Project Task](#update-project-task)
    - [Delete Project Task](#delete-project-task)
    - [Update Project Task Status](#update-project-task-status)
- [`Integrations`](#integrations)
  - [List Integrations](#list-integrations)
- [`Documents`](#documents)
  - [Create a document](#create-a-document)
  - [List documents](#list-documents)
  - [Read a document](#read-a-document)
  - [Rename or reshare a document](#rename-or-reshare-a-document)
  - [Delete a document](#delete-a-document)
  - [Replace a document's content](#replace-a-documents-content)
- [`Ads`](#ads)
  - [`Ads OpenaiAds`](#ads-openaiads)
    - [`Ads OpenaiAds AdAccount`](#ads-openaiads-adaccount)
      - [Get Account Insights](#get-account-insights)

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

#### Get Category Regions

Get the regions for a specific category.

| Direction | Type |
| --- | --- |
| Response | [`CategoryRetrieveRegionsResponse`](./src/profound/types/organizations/category_retrieve_regions_response.py) |

```python
category = client.organizations.categories.retrieve_regions(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Get Category Citation Categories

Get the citation categories for a category: the built-in buckets plus any custom categories.

| Direction | Type |
| --- | --- |
| Response | [`CategoryGetCitationCategoriesResponse`](./src/profound/types/organizations/category_get_citation_categories_response.py) |

```python
category = client.organizations.categories.get_citation_categories(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
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

### Query Answers V2

| Direction | Type |
| --- | --- |
| Request | [`PromptAnswersV2Params`](./src/profound/types/prompt_answers_v2_params.py) |
| Response | [`PromptAnswersV2Response`](./src/profound/types/prompt_answers_v2_response.py) |

```python
prompt = client.prompts.answers_v2(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
)
```

### Stream Answers V2

| Direction | Type |
| --- | --- |
| Request | [`PromptStreamAnswersV2Params`](./src/profound/types/prompt_stream_answers_v2_params.py) |
| Response | [`PromptStreamAnswersV2Response`](./src/profound/types/prompt_stream_answers_v2_response.py) |

```python
stream = client.prompts.stream_answers_v2(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
)

for event in stream:
    print(event)
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

### Query Sentiment V2

| Direction | Type |
| --- | --- |
| Request | [`ReportSentimentV2Params`](./src/profound/types/report_sentiment_v2_params.py) |
| Response | [`ReportSentimentV2Response`](./src/profound/types/report_sentiment_v2_response.py) |

```python
report = client.reports.sentiment_v2(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    asset_name="",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
    date_bucket="day",
    metrics=[],
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

### Stream Citations V2

| Direction | Type |
| --- | --- |
| Request | [`ReportStreamCitationsV2Params`](./src/profound/types/report_stream_citations_v2_params.py) |
| Response | [`ReportStreamCitationsV2Response`](./src/profound/types/report_stream_citations_v2_response.py) |

```python
stream = client.reports.stream_citations_v2(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
    entity="domain",
    interval="day",
    scope="all",
)

for event in stream:
    print(event)
```

### Stream Visibility V2

| Direction | Type |
| --- | --- |
| Request | [`ReportStreamVisibilityV2Params`](./src/profound/types/report_stream_visibility_v2_params.py) |
| Response | [`ReportStreamVisibilityV2Response`](./src/profound/types/report_stream_visibility_v2_response.py) |

```python
stream = client.reports.stream_visibility_v2(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
    interval="day",
    scope="owned",
)

for event in stream:
    print(event)
```

### Stream Sentiment V2

| Direction | Type |
| --- | --- |
| Request | [`ReportStreamSentimentV2Params`](./src/profound/types/report_stream_sentiment_v2_params.py) |
| Response | [`ReportStreamSentimentV2Response`](./src/profound/types/report_stream_sentiment_v2_response.py) |

```python
stream = client.reports.stream_sentiment_v2(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    asset="",
    start_date="",
    end_date="",
    interval="day",
    include_cited_websites=False,
)

for event in stream:
    print(event)
```

### Stream Query Fanouts V2

| Direction | Type |
| --- | --- |
| Request | [`ReportStreamQueryFanoutsParams`](./src/profound/types/report_stream_query_fanouts_params.py) |
| Response | [`ReportStreamQueryFanoutsResponse`](./src/profound/types/report_stream_query_fanouts_response.py) |

```python
stream = client.reports.stream_query_fanouts(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
    interval="day",
)

for event in stream:
    print(event)
```

### Get Referrals Report V2

Get referral traffic report from the hourly aggregated materialized view (UTC-based).

Supports date_interval="hour", calendar intervals through "year", "quarter", and "relative_week".
When `view_id` is provided, the query is scoped to that domain segment's hosts and paths.

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
When `view_id` is provided, the query is scoped to that domain segment's hosts and paths.

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

### Query Visibility V2

| Direction | Type |
| --- | --- |
| Request | [`ReportQueryVisibilityParams`](./src/profound/types/report_query_visibility_params.py) |
| Response | [`ReportQueryVisibilityResponse`](./src/profound/types/report_query_visibility_response.py) |

```python
report = client.reports.query_visibility(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
    interval="day",
    scope="owned",
)
```

### Query Citations V2

| Direction | Type |
| --- | --- |
| Request | [`ReportQueryCitationsParams`](./src/profound/types/report_query_citations_params.py) |
| Response | [`ReportQueryCitationsResponse`](./src/profound/types/report_query_citations_response.py) |

```python
report = client.reports.query_citations(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
    entity="domain",
    interval="day",
    scope="all",
)
```

### Query Sentiment V2

| Direction | Type |
| --- | --- |
| Request | [`ReportQuerySentimentParams`](./src/profound/types/report_query_sentiment_params.py) |
| Response | [`ReportQuerySentimentResponse`](./src/profound/types/report_query_sentiment_response.py) |

```python
report = client.reports.query_sentiment(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    asset="",
    start_date="",
    end_date="",
    interval="day",
    include_cited_websites=False,
)
```

### Query Fanouts V2

| Direction | Type |
| --- | --- |
| Request | [`ReportQueryQueryFanoutsParams`](./src/profound/types/report_query_query_fanouts_params.py) |
| Response | [`ReportQueryQueryFanoutsResponse`](./src/profound/types/report_query_query_fanouts_response.py) |

```python
report = client.reports.query_query_fanouts(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
    interval="day",
)
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

#### Query Shopping Brands V2

| Direction | Type |
| --- | --- |
| Request | [`ShoppingBrandsParams`](./src/profound/types/reports/shopping_brands_params.py) |
| Response | [`ShoppingBrandsResponse`](./src/profound/types/reports/shopping_brands_response.py) |

```python
shopping = client.reports.shopping.brands(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
    interval="day",
    scope="owned",
)
```

#### Stream Shopping Brands V2

| Direction | Type |
| --- | --- |
| Request | [`ShoppingStreamBrandsParams`](./src/profound/types/reports/shopping_stream_brands_params.py) |
| Response | [`ShoppingStreamBrandsResponse`](./src/profound/types/reports/shopping_stream_brands_response.py) |

```python
stream = client.reports.shopping.stream_brands(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
    interval="day",
    scope="owned",
)

for event in stream:
    print(event)
```

#### Query Shopping Products V2

| Direction | Type |
| --- | --- |
| Request | [`ShoppingProductsParams`](./src/profound/types/reports/shopping_products_params.py) |
| Response | [`ShoppingProductsResponse`](./src/profound/types/reports/shopping_products_response.py) |

```python
shopping = client.reports.shopping.products(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
    interval="day",
    include_merchants=False,
    competitor_limit=5,
)
```

#### Stream Shopping Products V2

| Direction | Type |
| --- | --- |
| Request | [`ShoppingStreamProductsParams`](./src/profound/types/reports/shopping_stream_products_params.py) |
| Response | [`ShoppingStreamProductsResponse`](./src/profound/types/reports/shopping_stream_products_response.py) |

```python
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
```

#### Query Shopping Merchants V2

| Direction | Type |
| --- | --- |
| Request | [`ShoppingMerchantsParams`](./src/profound/types/reports/shopping_merchants_params.py) |
| Response | [`ShoppingMerchantsResponse`](./src/profound/types/reports/shopping_merchants_response.py) |

```python
shopping = client.reports.shopping.merchants(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
    interval="day",
)
```

#### Stream Shopping Merchants V2

| Direction | Type |
| --- | --- |
| Request | [`ShoppingStreamMerchantsParams`](./src/profound/types/reports/shopping_stream_merchants_params.py) |
| Response | [`ShoppingStreamMerchantsResponse`](./src/profound/types/reports/shopping_stream_merchants_response.py) |

```python
stream = client.reports.shopping.stream_merchants(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
    interval="day",
)

for event in stream:
    print(event)
```

#### Query Shopping Trigger Rate V2

| Direction | Type |
| --- | --- |
| Request | [`ShoppingTriggerRateParams`](./src/profound/types/reports/shopping_trigger_rate_params.py) |
| Response | [`ShoppingTriggerRateResponse`](./src/profound/types/reports/shopping_trigger_rate_response.py) |

```python
shopping = client.reports.shopping.trigger_rate(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
    interval="day",
)
```

#### Stream Shopping Trigger Rate V2

| Direction | Type |
| --- | --- |
| Request | [`ShoppingStreamTriggerRateParams`](./src/profound/types/reports/shopping_stream_trigger_rate_params.py) |
| Response | [`ShoppingStreamTriggerRateResponse`](./src/profound/types/reports/shopping_stream_trigger_rate_response.py) |

```python
stream = client.reports.shopping.stream_trigger_rate(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
    interval="day",
)

for event in stream:
    print(event)
```

### `Reports Accuracy`

#### Accuracy Overview

| Direction | Type |
| --- | --- |
| Request | [`AccuracyCreateOverviewParams`](./src/profound/types/reports/accuracy_create_overview_params.py) |
| Response | [`AccuracyCreateOverviewResponse`](./src/profound/types/reports/accuracy_create_overview_response.py) |

```python
accuracy = client.reports.accuracy.create_overview(
    start_date="",
    end_date="",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    exclude_topic_ids=False,
    tag_filter_type="any",
    include_no_tag=False,
    include_no_persona=False,
    group_by="period",
)
```

#### Accuracy Breakdown

| Direction | Type |
| --- | --- |
| Request | [`AccuracyCreateBreakdownParams`](./src/profound/types/reports/accuracy_create_breakdown_params.py) |
| Response | [`AccuracyCreateBreakdownResponse`](./src/profound/types/reports/accuracy_create_breakdown_response.py) |

```python
accuracy = client.reports.accuracy.create_breakdown(
    start_date="",
    end_date="",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    exclude_topic_ids=False,
    tag_filter_type="any",
    include_no_tag=False,
    include_no_persona=False,
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
| Request | [`AccuracyCreateCitationAnalysisParams`](./src/profound/types/reports/accuracy_create_citation_analysis_params.py) |
| Response | [`AccuracyCreateCitationAnalysisResponse`](./src/profound/types/reports/accuracy_create_citation_analysis_response.py) |

```python
accuracy = client.reports.accuracy.create_citation_analysis(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    clean_href="",
    start_date="",
    end_date="",
)
```

#### Accuracy Topic Ids

| Direction | Type |
| --- | --- |
| Request | [`AccuracyCreateTopicIDsParams`](./src/profound/types/reports/accuracy_create_topic_ids_params.py) |
| Response | [`AccuracyCreateTopicIDsResponse`](./src/profound/types/reports/accuracy_create_topic_ids_response.py) |

```python
accuracy = client.reports.accuracy.create_topic_ids(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
)
```

#### Accuracy Inaccurate Themes

| Direction | Type |
| --- | --- |
| Request | [`AccuracyCreateInaccurateThemesParams`](./src/profound/types/reports/accuracy_create_inaccurate_themes_params.py) |
| Response | [`AccuracyCreateInaccurateThemesResponse`](./src/profound/types/reports/accuracy_create_inaccurate_themes_response.py) |

```python
accuracy = client.reports.accuracy.create_inaccurate_themes(
    start_date="",
    end_date="",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    exclude_topic_ids=False,
    tag_filter_type="any",
    include_no_tag=False,
    include_no_persona=False,
    limit=10,
    offset=0,
    sort_by="response_share",
    sort_order="desc",
)
```

#### Accuracy Inaccurate Clusters

| Direction | Type |
| --- | --- |
| Request | [`AccuracyCreateInaccurateClustersParams`](./src/profound/types/reports/accuracy_create_inaccurate_clusters_params.py) |
| Response | [`AccuracyCreateInaccurateClustersResponse`](./src/profound/types/reports/accuracy_create_inaccurate_clusters_response.py) |

```python
accuracy = client.reports.accuracy.create_inaccurate_clusters(
    start_date="",
    end_date="",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    exclude_topic_ids=False,
    tag_filter_type="any",
    include_no_tag=False,
    include_no_persona=False,
    limit=5000,
    offset=0,
    include_models=False,
)
```

#### Accuracy Inaccuracy Drivers

| Direction | Type |
| --- | --- |
| Request | [`AccuracyCreateInaccuracyDriversParams`](./src/profound/types/reports/accuracy_create_inaccuracy_drivers_params.py) |
| Response | [`AccuracyCreateInaccuracyDriversResponse`](./src/profound/types/reports/accuracy_create_inaccuracy_drivers_response.py) |

```python
accuracy = client.reports.accuracy.create_inaccuracy_drivers(
    start_date="",
    end_date="",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    exclude_topic_ids=False,
    tag_filter_type="any",
    include_no_tag=False,
    include_no_persona=False,
    limit=5,
)
```

#### Accuracy Top Inaccurate Claims

| Direction | Type |
| --- | --- |
| Request | [`AccuracyCreateTopInaccurateClaimsParams`](./src/profound/types/reports/accuracy_create_top_inaccurate_claims_params.py) |
| Response | [`AccuracyCreateTopInaccurateClaimsResponse`](./src/profound/types/reports/accuracy_create_top_inaccurate_claims_response.py) |

```python
accuracy = client.reports.accuracy.create_top_inaccurate_claims(
    start_date="",
    end_date="",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    exclude_topic_ids=False,
    tag_filter_type="any",
    include_no_tag=False,
    include_no_persona=False,
    limit=5,
)
```

#### Accuracy Claim Breakdown

| Direction | Type |
| --- | --- |
| Request | [`AccuracyCreateClaimBreakdownParams`](./src/profound/types/reports/accuracy_create_claim_breakdown_params.py) |
| Response | [`AccuracyCreateClaimBreakdownResponse`](./src/profound/types/reports/accuracy_create_claim_breakdown_response.py) |

```python
accuracy = client.reports.accuracy.create_claim_breakdown(
    start_date="",
    end_date="",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    exclude_topic_ids=False,
    tag_filter_type="any",
    include_no_tag=False,
    include_no_persona=False,
    cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Accuracy Claim Citations

| Direction | Type |
| --- | --- |
| Request | [`AccuracyCreateClaimCitationsParams`](./src/profound/types/reports/accuracy_create_claim_citations_params.py) |
| Response | [`AccuracyCreateClaimCitationsResponse`](./src/profound/types/reports/accuracy_create_claim_citations_response.py) |

```python
accuracy = client.reports.accuracy.create_claim_citations(
    start_date="",
    end_date="",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    exclude_topic_ids=False,
    tag_filter_type="any",
    include_no_tag=False,
    include_no_persona=False,
    cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    limit=10,
    offset=0,
    sort_order="desc",
)
```

#### Accuracy Cluster Example Runs

| Direction | Type |
| --- | --- |
| Request | [`AccuracyCreateClusterExampleRunsParams`](./src/profound/types/reports/accuracy_create_cluster_example_runs_params.py) |
| Response | [`AccuracyCreateClusterExampleRunsResponse`](./src/profound/types/reports/accuracy_create_cluster_example_runs_response.py) |

```python
accuracy = client.reports.accuracy.create_cluster_example_runs(
    start_date="",
    end_date="",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    exclude_topic_ids=False,
    tag_filter_type="any",
    include_no_tag=False,
    include_no_persona=False,
    cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    limit=20,
    offset=0,
)
```

#### Accuracy Cluster Verification Pairs

| Direction | Type |
| --- | --- |
| Request | [`AccuracyCreateClusterVerificationPairsParams`](./src/profound/types/reports/accuracy_create_cluster_verification_pairs_params.py) |
| Response | [`AccuracyCreateClusterVerificationPairsResponse`](./src/profound/types/reports/accuracy_create_cluster_verification_pairs_response.py) |

```python
accuracy = client.reports.accuracy.create_cluster_verification_pairs(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Accuracy Factcheck Setup Status

| Direction | Type |
| --- | --- |
| Request | [`AccuracyCreateFactcheckSetupStatusParams`](./src/profound/types/reports/accuracy_create_factcheck_setup_status_params.py) |
| Response | [`AccuracyCreateFactcheckSetupStatusResponse`](./src/profound/types/reports/accuracy_create_factcheck_setup_status_response.py) |

```python
accuracy = client.reports.accuracy.create_factcheck_setup_status(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### `Reports Factcheck`

#### Query Scores

| Direction | Type |
| --- | --- |
| Request | [`FactcheckQueryScoresParams`](./src/profound/types/reports/factcheck_query_scores_params.py) |
| Response | [`FactcheckQueryScoresResponse`](./src/profound/types/reports/factcheck_query_scores_response.py) |

```python
factcheck = client.reports.factcheck.query_scores(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
)
```

#### Stream Scores

| Direction | Type |
| --- | --- |
| Request | [`FactcheckStreamScoresParams`](./src/profound/types/reports/factcheck_stream_scores_params.py) |
| Response | [`FactcheckStreamScoresResponse`](./src/profound/types/reports/factcheck_stream_scores_response.py) |

```python
stream = client.reports.factcheck.stream_scores(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
)

for event in stream:
    print(event)
```

#### `Reports Factcheck Claims`

##### Query Claims

| Direction | Type |
| --- | --- |
| Request | [`ClaimQueryClaimsParams`](./src/profound/types/reports/factcheck/claim_query_claims_params.py) |
| Response | [`ClaimQueryClaimsResponse`](./src/profound/types/reports/factcheck/claim_query_claims_response.py) |

```python
claim = client.reports.factcheck.claims.query_claims(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
)
```

##### Stream Claims

| Direction | Type |
| --- | --- |
| Request | [`ClaimStreamClaimsParams`](./src/profound/types/reports/factcheck/claim_stream_claims_params.py) |
| Response | [`ClaimStreamClaimsResponse`](./src/profound/types/reports/factcheck/claim_stream_claims_response.py) |

```python
stream = client.reports.factcheck.claims.stream_claims(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
)

for event in stream:
    print(event)
```

### `Reports Social`

#### `Reports Social Youtube`

##### Query Youtube Channels

Rank the YouTube channels cited in a category, or the video categories they publish in.

| Direction | Type |
| --- | --- |
| Request | [`YoutubeGetChannelsParams`](./src/profound/types/reports/social/youtube_get_channels_params.py) |
| Response | [`YoutubeGetChannelsResponse`](./src/profound/types/reports/social/youtube_get_channels_response.py) |

```python
youtube = client.reports.social.youtube.get_channels(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
)
```

##### Query Youtube Videos

Rank cited YouTube videos, for one channel or across all of them.

| Direction | Type |
| --- | --- |
| Request | [`YoutubeGetVideosParams`](./src/profound/types/reports/social/youtube_get_videos_params.py) |
| Response | [`YoutubeGetVideosResponse`](./src/profound/types/reports/social/youtube_get_videos_response.py) |

```python
youtube = client.reports.social.youtube.get_videos(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
    attribution="attributed",
)
```

##### Query Youtube Summary

Report how much of youtube.com the channel and video rankings account for.

| Direction | Type |
| --- | --- |
| Request | [`YoutubeGetSummaryParams`](./src/profound/types/reports/social/youtube_get_summary_params.py) |
| Response | [`YoutubeGetSummaryResponse`](./src/profound/types/reports/social/youtube_get_summary_response.py) |

```python
youtube = client.reports.social.youtube.get_summary(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
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

### Create an agent

Create a new draft agent owned by the given organization.

`organization_id` is required and you must be a member of it. The agent is created
as a `draft`; publish it with `POST /v1/agents/{agent_id}/publish` once its graph
is ready.

| Direction | Type |
| --- | --- |
| Request | [`AgentCreateParams`](./src/profound/types/agent_create_params.py) |
| Response | [`AgentCreateResponse`](./src/profound/types/agent_create_response.py) |

```python
agent = client.agents.create(
    organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    name="x",
)
```

### Publish an agent

Publish an agent's latest draft as its live published version.

You must be a member of the agent's organization. Publishing promotes the current
draft graph to a new published version. A draft that cannot produce its declared
input/output contract is rejected with `422` and is not published.

| Direction | Type |
| --- | --- |
| Response | [`AgentPublishResponse`](./src/profound/types/agent_publish_response.py) |

```python
agent = client.agents.publish(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
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
| Request | [`AgentUpdateParams`](./src/profound/types/agent_update_params.py) |
| Response | [`AgentUpdateResponse`](./src/profound/types/agent_update_response.py) |

```python
agent = client.agents.update(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
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
| Request | [`AgentRetrieveGraphParams`](./src/profound/types/agent_retrieve_graph_params.py) |
| Response | [`AgentRetrieveGraphResponse`](./src/profound/types/agent_retrieve_graph_response.py) |

```python
agent = client.agents.retrieve_graph(
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

### `Agents NodeTypes`

#### List node types

List the node types available for building agents.

The set is deterministic and does not depend on the caller, so the response
is safe to cache across sessions. Integration-dependent and dynamic-schema
node types are intentionally excluded in v1.

| Direction | Type |
| --- | --- |
| Response | [`NodeTypeListResponse`](./src/profound/types/agents/node_type_list_response.py) |

```python
node_type = client.agents.node_types.list()
```

#### Get a node type schema

Retrieve the JSON schema for a single node type.

The `schema` field is an opaque JSON Schema for the node's configuration.
Use `schema_version` as a cache key — it bumps whenever the schema changes.

| Direction | Type |
| --- | --- |
| Response | [`NodeTypeRetrieveSchemaResponse`](./src/profound/types/agents/node_type_retrieve_schema_response.py) |

```python
node_type = client.agents.node_types.retrieve_schema(
    node_type="nodeType",
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

## `Projects`

### List Projects

| Direction | Type |
| --- | --- |
| Request | [`ProjectListParams`](./src/profound/types/project_list_params.py) |
| Response | [`ProjectListResponse`](./src/profound/types/project_list_response.py) |

```python
project = client.projects.list(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    limit=100,
    offset=0,
)
```

### Create Project

| Direction | Type |
| --- | --- |
| Request | [`ProjectCreateParams`](./src/profound/types/project_create_params.py) |
| Response | [`ProjectCreateResponse`](./src/profound/types/project_create_response.py) |

```python
project = client.projects.create(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Get Project

| Direction | Type |
| --- | --- |
| Request | [`ProjectRetrieveParams`](./src/profound/types/project_retrieve_params.py) |
| Response | [`ProjectRetrieveResponse`](./src/profound/types/project_retrieve_response.py) |

```python
project = client.projects.retrieve(
    project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Delete Project

| Direction | Type |
| --- | --- |
| Request | [`ProjectDeleteParams`](./src/profound/types/project_delete_params.py) |

```python
client.projects.delete(
    project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Get Project Status

| Direction | Type |
| --- | --- |
| Request | [`ProjectGetStatusParams`](./src/profound/types/project_get_status_params.py) |
| Response | [`ProjectGetStatusResponse`](./src/profound/types/project_get_status_response.py) |

```python
project = client.projects.get_status(
    project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Archive Project

| Direction | Type |
| --- | --- |
| Request | [`ProjectArchiveParams`](./src/profound/types/project_archive_params.py) |
| Response | [`ProjectArchiveResponse`](./src/profound/types/project_archive_response.py) |

```python
project = client.projects.archive(
    project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Unarchive Project

| Direction | Type |
| --- | --- |
| Request | [`ProjectUnarchiveParams`](./src/profound/types/project_unarchive_params.py) |
| Response | [`ProjectUnarchiveResponse`](./src/profound/types/project_unarchive_response.py) |

```python
project = client.projects.unarchive(
    project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### `Projects Generations`

#### List Project Generations

| Direction | Type |
| --- | --- |
| Request | [`GenerationListParams`](./src/profound/types/projects/generation_list_params.py) |
| Response | [`GenerationListResponse`](./src/profound/types/projects/generation_list_response.py) |

```python
generation = client.projects.generations.list(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    limit=100,
    offset=0,
)
```

#### Get Project Generation Status

| Direction | Type |
| --- | --- |
| Request | [`GenerationRetrieveParams`](./src/profound/types/projects/generation_retrieve_params.py) |
| Response | [`GenerationRetrieveResponse`](./src/profound/types/projects/generation_retrieve_response.py) |

```python
generation = client.projects.generations.retrieve(
    run_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### `Projects Tasks`

#### List Project Tasks

| Direction | Type |
| --- | --- |
| Request | [`TaskListParams`](./src/profound/types/projects/task_list_params.py) |
| Response | [`TaskListResponse`](./src/profound/types/projects/task_list_response.py) |

```python
task = client.projects.tasks.list(
    project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Create Project Task

| Direction | Type |
| --- | --- |
| Request | [`TaskCreateParams`](./src/profound/types/projects/task_create_params.py) |
| Response | [`TaskCreateResponse`](./src/profound/types/projects/task_create_response.py) |

```python
task = client.projects.tasks.create(
    project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    title="x",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Get Project Task

| Direction | Type |
| --- | --- |
| Request | [`TaskRetrieveParams`](./src/profound/types/projects/task_retrieve_params.py) |
| Response | [`TaskRetrieveResponse`](./src/profound/types/projects/task_retrieve_response.py) |

```python
task = client.projects.tasks.retrieve(
    project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Update Project Task

| Direction | Type |
| --- | --- |
| Request | [`TaskUpdateParams`](./src/profound/types/projects/task_update_params.py) |
| Response | [`TaskUpdateResponse`](./src/profound/types/projects/task_update_response.py) |

```python
task = client.projects.tasks.update(
    project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Delete Project Task

| Direction | Type |
| --- | --- |
| Request | [`TaskDeleteParams`](./src/profound/types/projects/task_delete_params.py) |

```python
client.projects.tasks.delete(
    project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Update Project Task Status

| Direction | Type |
| --- | --- |
| Request | [`TaskUpdateStatusParams`](./src/profound/types/projects/task_update_status_params.py) |
| Response | [`TaskUpdateStatusResponse`](./src/profound/types/projects/task_update_status_response.py) |

```python
task = client.projects.tasks.update_status(
    project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    status="not_started",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

## `Integrations`

### List Integrations

List the organization's connected integrations.

Returns every connected integration by default, each with its lifecycle
`status`; pass `status_filter` to narrow to one status (e.g. `needs_reauth`).
Each row's `integration_id` is the value a hub-backed node needs bound to it.

| Direction | Type |
| --- | --- |
| Request | [`IntegrationListParams`](./src/profound/types/integration_list_params.py) |
| Response | [`IntegrationListResponse`](./src/profound/types/integration_list_response.py) |

```python
integration = client.integrations.list()
```

## `Documents`

### Create a document

Create a Profound document with markdown content.

`organization_id` is required and you must be a member of it. You choose the
document's `id`, and creation is idempotent on it: repeating the request returns
the existing document rather than creating a second one.

New documents are visible only to their creator; share them from the Profound app,
or open one with the `url` in the response.

A `201` response does not confirm that a new document was created: it is also
returned when `id` already existed, in which case the existing document comes
back unchanged. Upstream gives no signal to tell the two apart, so this endpoint
does not claim to either — it is safe to retry with the same `id` either way.

| Direction | Type |
| --- | --- |
| Request | [`DocumentCreateParams`](./src/profound/types/document_create_params.py) |
| Response | [`DocumentCreateResponse`](./src/profound/types/document_create_response.py) |

```python
document = client.documents.create(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    name="x",
    content_markdown="x",
)
```

### List documents

List documents visible to your organization, newest-modified-first.

Documents are ordered by last-modified time, most recent first, with no other
sort option. This is a walk over a live, mutable collection: a document created
or modified while you are paging can shift which page it lands on, so a single
walk may show it to you twice or, rarely, skip it.

This response never includes a total count. Upstream counts totals before
applying your organization's access filter, so a total, or treating a short
page as the last one, would misreport what you can actually see. Keep
following `pagination.next_cursor` until it comes back null — that, and not
a short or even an empty page, is the end of the walk. A page whose rows the
access filter removed entirely is empty while later pages still hold
documents, so the last page of a walk may legitimately be an empty one.

| Direction | Type |
| --- | --- |
| Request | [`DocumentListParams`](./src/profound/types/document_list_params.py) |
| Response | [`DocumentListResponse`](./src/profound/types/document_list_response.py) |

```python
document = client.documents.list(
    organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    limit=20,
)
```

### Read a document

Read a document: its metadata, its default tab's body, its other tabs, its comments, and its version hash.

You can read any document you have access to in the Profound app, including ones
created there rather than through this API.

By default this is a preview: the body is truncated to save your context, and the
version hash is withheld so a preview alone can never be used to replace a document
blindly. Pass `preview=false` when you intend to write.

| Direction | Type |
| --- | --- |
| Request | [`DocumentRetrieveParams`](./src/profound/types/document_retrieve_params.py) |
| Response | [`DocumentRetrieveResponse`](./src/profound/types/document_retrieve_response.py) |

```python
document = client.documents.retrieve(
    document_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    include_tabs=True,
    include_comments=True,
    preview=True,
)
```

### Rename or reshare a document

Rename a document, change who can see it, or both in one call.

Renaming sets a permanent lock on the title, and changing visibility can silently
change who has access — see the `name` and `visibility` field descriptions for what
each one does before you use it.

Renaming needs edit access; changing visibility is creator-only, and upstream
enforces it. You can act on a document this API created, or one you created
yourself in the Profound app — not one merely shared with you.

| Direction | Type |
| --- | --- |
| Request | [`DocumentUpdateParams`](./src/profound/types/document_update_params.py) |
| Response | [`DocumentUpdateResponse`](./src/profound/types/document_update_response.py) |

```python
document = client.documents.update(
    document_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Delete a document

Delete a document created through this integration.

Only documents created through this integration can be deleted here. A document
created in the Profound app can never be deleted through this route, even by the
person who owns it — creation provenance is stamped once, at creation, and is never
backfilled onto documents made another way.

The delete is soft: the row is marked deleted at the storage layer rather than
destroyed. There is no restore through this API, or any other — treat a delete as
final even though the data itself is not gone.

A 404 means the document is not visible to you at all. It covers three cases the
response does not distinguish, on purpose: the document never existed, it was
already deleted by an earlier call to this same route, or it exists but your
credential resolves no role on it. Deleting the same document twice returns 404 on
the second call, not a second 204.

A 403 means the opposite: the document is visible to you but not deletable here,
and the message says which rule refused — it was not created through this
integration, or you are not its creator. Deleting is creator-only, so edit access
is not enough to remove a document out from under its owner.

| Direction | Type |
| --- | --- |
| Request | [`DocumentDeleteParams`](./src/profound/types/document_delete_params.py) |

```python
client.documents.delete(
    document_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Replace a document's content

Overwrite a document's entire body with new markdown, replacing what it held before.

This is a whole-body replace, not a patch: send the complete new text every time. An
empty `content_markdown` is valid and clears the document.

Two destructive side effects apply on every call, regardless of what you send:

- The document collapses to its default tab. Every non-default tab is deleted, and
  the comments map is cleared for **all** tabs, including the default one — a
  document with a live comment thread on any tab loses it.
- `skip_title_sync` defaults to `false`, matching the Profound app: the title follows
  the new content's first heading, so a replace silently renames the document unless
  the heading matches the current title or `skip_title_sync` is set.

There is no compare-and-swap: this call does not accept a precondition, and nothing
stops two concurrent replaces from silently overwriting each other last-writer-wins.
Upstream's own `version_hash` documentation says as much — the token is "still a
change detector rather than a precondition: a caller must not treat a matching token
as licence to overwrite blindly, because it names the room at a moment cortex
observed and not the moment its own write lands." Sending a `working_version_hash`
(or any spelling of it) is rejected with a `400` naming this rather than accepted
and silently discarded, which is what happens on the upstream route this wraps.

You can replace a document this API created, or one you created yourself directly —
not merely one shared with you.

| Direction | Type |
| --- | --- |
| Request | [`DocumentReplaceContentParams`](./src/profound/types/document_replace_content_params.py) |
| Response | [`DocumentReplaceContentResponse`](./src/profound/types/document_replace_content_response.py) |

```python
document = client.documents.replace_content(
    document_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    content_markdown="",
    skip_title_sync=False,
)
```

## `Ads`

### `Ads OpenaiAds`

#### `Ads OpenaiAds AdAccount`

##### Get Account Insights

Get ad account insights for the organization's OpenAI Ads partner brand.

`aggregation_level=campaign` returns one row per campaign (with `campaign_id`
/ `campaign_name` and all metrics), so every campaign's insights come back in
a single call; `time_granularity=daily` gives per-day rows (e.g. daily spend).

| Direction | Type |
| --- | --- |
| Request | [`AdAccountRetrieveInsightsParams`](./src/profound/types/ads/openai_ads/ad_account_retrieve_insights_params.py) |
| Response | [`AdAccountRetrieveInsightsResponse`](./src/profound/types/ads/openai_ads/ad_account_retrieve_insights_response.py) |

```python
ad_account = client.ads.openai_ads.ad_account.retrieve_insights()
```
