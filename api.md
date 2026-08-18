# profound Python API

Complete reference of every operation, grouped by resource. See [the README](./README.md) for usage and configuration.

## Contents

- [`Organization`](#organization)
  - [List organizations](#list-organizations)
  - [Get Regions](#get-regions)
  - [Get Models](#get-models)
  - [Get Domains](#get-domains)
  - [Get Assets](#get-assets)
  - [Get Personas](#get-personas)
  - [Get Categories](#get-categories)
  - [Get Category Topics](#get-category-topics)
  - [Get Category Tags](#get-category-tags)
  - [Get Category Regions](#get-category-regions)
  - [Get Category Citation Categories](#get-category-citation-categories)
  - [Get Category Citation Tags](#get-category-citation-tags)
  - [List prompts](#list-prompts)
  - [Create prompts](#create-prompts)
  - [Update prompts](#update-prompts)
  - [Update prompt status](#update-prompt-status)
  - [Get Category Assets](#get-category-assets)
  - [Get Category Personas](#get-category-personas)
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
    - [Shopping Triggered Prompts](#shopping-triggered-prompts)
    - [Shopping Triggered Topics](#shopping-triggered-topics)
    - [Shopping Merchant Share](#shopping-merchant-share)
    - [Shopping Product Merchant Urls](#shopping-product-merchant-urls)
    - [Shopping Executions](#shopping-executions)
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
    - [Query Claims](#query-claims)
    - [Stream Claims](#stream-claims)
  - [`Reports Social`](#reports-social)
    - [Query Youtube Channels](#query-youtube-channels)
    - [Query Youtube Videos](#query-youtube-videos)
    - [Query Youtube Summary](#query-youtube-summary)
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
- [`Integrations`](#integrations)
  - [List Integrations](#list-integrations)
- [`Documents`](#documents)
  - [List documents](#list-documents)
  - [Create a document](#create-a-document)
  - [Read a document](#read-a-document)
  - [Rename or reshare a document](#rename-or-reshare-a-document)
  - [Delete a document](#delete-a-document)
  - [Replace a document's content](#replace-a-documents-content)
- [`OpenAiAds`](#openaiads)
  - [Get Account Insights](#get-account-insights)
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

## Setup

```python
import os

from profound import Profound

client = Profound(
    api_key=os.environ.get("PROFOUND_API_KEY"),
)
```

## `Organization`

### List organizations

Return every organization the caller's API key grants access to. Use this to discover organization IDs before calling endpoints that accept an `organization_id` filter.

| Direction | Type |
| --- | --- |
| Response | [`OrganizationListV1OrgGetResponse`](./src/profound/types/organization_list_v1_org_get_response.py) |

```python
organization = client.organization.list_v1_org_get()
```

### Get Regions

Get the organization regions.

| Direction | Type |
| --- | --- |
| Request | [`OrganizationListRegionsV1OrgRegionsGetParams`](./src/profound/types/organization_list_regions_v1_org_regions_get_params.py) |
| Response | [`OrganizationListRegionsV1OrgRegionsGetResponse`](./src/profound/types/organization_list_regions_v1_org_regions_get_response.py) |

```python
organization = client.organization.list_regions_v1_org_regions_get()
```

### Get Models

Get the organization models.

| Direction | Type |
| --- | --- |
| Response | [`OrganizationListModelsV1OrgModelsGetResponse`](./src/profound/types/organization_list_models_v1_org_models_get_response.py) |

```python
organization = client.organization.list_models_v1_org_models_get()
```

### Get Domains

Get the organization domains.

| Direction | Type |
| --- | --- |
| Request | [`OrganizationListDomainsV1OrgDomainsGetParams`](./src/profound/types/organization_list_domains_v1_org_domains_get_params.py) |
| Response | [`OrganizationListDomainsV1OrgDomainsGetResponse`](./src/profound/types/organization_list_domains_v1_org_domains_get_response.py) |

```python
organization = client.organization.list_domains_v1_org_domains_get()
```

### Get Assets

Get the organization assets, one row per (asset, organization) pair.

An asset's category can belong to multiple organizations; one asset row is
emitted per owning org so no association is silently dropped.

| Direction | Type |
| --- | --- |
| Request | [`OrganizationListAssetsV1OrgAssetsGetParams`](./src/profound/types/organization_list_assets_v1_org_assets_get_params.py) |
| Response | [`OrganizationListAssetsV1OrgAssetsGetResponse`](./src/profound/types/organization_list_assets_v1_org_assets_get_response.py) |

```python
organization = client.organization.list_assets_v1_org_assets_get()
```

### Get Personas

Get the organization personas, one row per (persona, organization) pair.

Same (item, org) fan-out as ``get_assets``: a persona's category can be
owned by multiple orgs, and each owning org gets its own row so no
association is silently dropped.

| Direction | Type |
| --- | --- |
| Request | [`OrganizationListPersonasV1OrgPersonasGetParams`](./src/profound/types/organization_list_personas_v1_org_personas_get_params.py) |
| Response | [`OrganizationListPersonasV1OrgPersonasGetResponse`](./src/profound/types/organization_list_personas_v1_org_personas_get_response.py) |

```python
organization = client.organization.list_personas_v1_org_personas_get()
```

### Get Categories

Get the organization categories, one row per (category, organization) pair.

| Direction | Type |
| --- | --- |
| Request | [`OrganizationListCategoriesV1OrgCategoriesGetParams`](./src/profound/types/organization_list_categories_v1_org_categories_get_params.py) |
| Response | [`OrganizationListCategoriesV1OrgCategoriesGetResponse`](./src/profound/types/organization_list_categories_v1_org_categories_get_response.py) |

```python
organization = client.organization.list_categories_v1_org_categories_get()
```

### Get Category Topics

Get the topics for a specific category.

| Direction | Type |
| --- | --- |
| Response | [`OrganizationListCategoryTopicsV1OrgCategoriesCategoryTopicsGetResponse`](./src/profound/types/organization_list_category_topics_v1_org_categories_category_topics_get_response.py) |

```python
organization = client.organization.list_category_topics_v1_org_categories_category_topics_get(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Get Category Tags

Get the tags for a specific category.

| Direction | Type |
| --- | --- |
| Response | [`OrganizationListCategoryTagsV1OrgCategoriesCategoryTagsGetResponse`](./src/profound/types/organization_list_category_tags_v1_org_categories_category_tags_get_response.py) |

```python
organization = client.organization.list_category_tags_v1_org_categories_category_tags_get(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Get Category Regions

Get the regions for a specific category.

| Direction | Type |
| --- | --- |
| Response | [`OrganizationListCategoryRegionsV1OrgCategoriesCategoryRegionsGetResponse`](./src/profound/types/organization_list_category_regions_v1_org_categories_category_regions_get_response.py) |

```python
organization = client.organization.list_category_regions_v1_org_categories_category_regions_get(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Get Category Citation Categories

Get the citation categories for a category: the built-in buckets plus any custom categories.

| Direction | Type |
| --- | --- |
| Response | [`OrganizationListCategoryCitationCategoriesV1OrgCategoriesCategoryCitationCategoriesGetResponse`](./src/profound/types/organization_list_category_citation_categories_v1_org_categories_category_citation_categories_get_response.py) |

```python
organization = client.organization.list_category_citation_categories_v1_org_categories_category_citation_categories_get(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Get Category Citation Tags

Get the custom citation tags defined for a category.

| Direction | Type |
| --- | --- |
| Response | [`OrganizationListCategoryCitationTagsV1OrgCategoriesCategoryCitationTagsGetResponse`](./src/profound/types/organization_list_category_citation_tags_v1_org_categories_category_citation_tags_get_response.py) |

```python
organization = client.organization.list_category_citation_tags_v1_org_categories_category_citation_tags_get(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### List prompts

Retrieve prompts in a category with optional filtering by type, topic, tag, region, platform, or persona. Supports cursor-based pagination.

| Direction | Type |
| --- | --- |
| Request | [`OrganizationListCategoryPromptsV1OrgCategoriesCategoryPromptsGetParams`](./src/profound/types/organization_list_category_prompts_v1_org_categories_category_prompts_get_params.py) |
| Response | [`OrganizationListCategoryPromptsV1OrgCategoriesCategoryPromptsGetResponse`](./src/profound/types/organization_list_category_prompts_v1_org_categories_category_prompts_get_response.py) |

```python
organization = client.organization.list_category_prompts_v1_org_categories_category_prompts_get(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    limit=10000,
    status=["active"],
)
```

### Create prompts

Create one or more prompts in a category. Topics and tags are auto-created if referenced by name and not yet existing. Use dry_run to preview without persisting.

| Direction | Type |
| --- | --- |
| Request | [`OrganizationCreateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPostParams`](./src/profound/types/organization_create_category_prompts_v1_org_categories_category_id_prompts_post_params.py) |
| Response | [`OrganizationCreateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPostResponse`](./src/profound/types/organization_create_category_prompts_v1_org_categories_category_id_prompts_post_response.py) |

```python
organization = client.organization.create_category_prompts_v1_org_categories_category_id_prompts_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    prompts=[],
    dry_run=False,
)
```

### Update prompts

Update one or more existing prompts. Only provided fields are changed. Dimension fields (regions, platforms, personas, tags) replace the full set when provided. Use dry_run to preview without persisting.

| Direction | Type |
| --- | --- |
| Request | [`OrganizationUpdateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPatchParams`](./src/profound/types/organization_update_category_prompts_v1_org_categories_category_id_prompts_patch_params.py) |
| Response | [`OrganizationUpdateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPatchResponse`](./src/profound/types/organization_update_category_prompts_v1_org_categories_category_id_prompts_patch_response.py) |

```python
organization = client.organization.update_category_prompts_v1_org_categories_category_id_prompts_patch(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    prompts=[],
    dry_run=False,
)
```

### Update prompt status

Bulk-update the status of one or more prompts. Prompts already in the target status are skipped. Use dry_run to preview without persisting.

Status options:
- 'active': Prompts will run daily.
- 'disabled': Prompts will not run moving forward, but historical data is preserved.
- 'deleted': Prompts are deleted along with historical data

| Direction | Type |
| --- | --- |
| Request | [`OrganizationUpdateCategoryPromptStatusV1OrgCategoriesCategoryIDPromptsStatusPatchParams`](./src/profound/types/organization_update_category_prompt_status_v1_org_categories_category_id_prompts_status_patch_params.py) |
| Response | [`OrganizationUpdateCategoryPromptStatusV1OrgCategoriesCategoryIDPromptsStatusPatchResponse`](./src/profound/types/organization_update_category_prompt_status_v1_org_categories_category_id_prompts_status_patch_response.py) |

```python
organization = client.organization.update_category_prompt_status_v1_org_categories_category_id_prompts_status_patch(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    prompt_ids=[],
    status="active",
    dry_run=False,
)
```

### Get Category Assets

| Direction | Type |
| --- | --- |
| Response | [`OrganizationListCategoryAssetsV1OrgCategoriesCategoryAssetsGetResponse`](./src/profound/types/organization_list_category_assets_v1_org_categories_category_assets_get_response.py) |

```python
organization = client.organization.list_category_assets_v1_org_categories_category_assets_get(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Get Category Personas

| Direction | Type |
| --- | --- |
| Response | [`OrganizationListCategoryPersonasV1OrgCategoriesCategoryPersonasGetResponse`](./src/profound/types/organization_list_category_personas_v1_org_categories_category_personas_get_response.py) |

```python
organization = client.organization.list_category_personas_v1_org_categories_category_personas_get(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

## `Prompts`

### `Prompts Answers`

#### Get Answers

| Direction | Type |
| --- | --- |
| Request | [`AnswerCreateV1PostParams`](./src/profound/types/prompts/answer_create_v1_post_params.py) |
| Response | [`AnswerCreateV1PostResponse`](./src/profound/types/prompts/answer_create_v1_post_response.py) |

```python
answer = client.prompts.answers.create_v1_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
)
```

#### Query Answers V2

| Direction | Type |
| --- | --- |
| Request | [`AnswerQueryV2V2PostParams`](./src/profound/types/prompts/answer_query_v2_v2_post_params.py) |
| Response | [`AnswerQueryV2V2PostResponse`](./src/profound/types/prompts/answer_query_v2_v2_post_response.py) |

```python
answer = client.prompts.answers.query_v2_v2_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
)
```

#### Stream Answers V2

| Direction | Type |
| --- | --- |
| Request | [`AnswerStreamV2V2StreamPostParams`](./src/profound/types/prompts/answer_stream_v2_v2_stream_post_params.py) |
| Response | [`AnswerStreamV2V2StreamPostResponse`](./src/profound/types/prompts/answer_stream_v2_v2_stream_post_response.py) |

```python
stream = client.prompts.answers.stream_v2_v2_stream_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
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
| Request | [`ReportQuerySentimentV2V1SentimentV2PostParams`](./src/profound/types/report_query_sentiment_v2_v1_sentiment_v2_post_params.py) |
| Response | [`ReportQuerySentimentV2V1SentimentV2PostResponse`](./src/profound/types/report_query_sentiment_v2_v1_sentiment_v2_post_response.py) |

```python
report = client.reports.query_sentiment_v2_v1_sentiment_v2_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    asset_name="",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
    date_bucket="day",
    metrics=[],
)
```

### `Reports Citations`

#### Query Citations

Get citations for a given category.

The ``mentioned`` filter supports ``is true`` and ``is false``. It uses the
latest page analysis available at or before ``end_date``; pages without an
analysis by then are excluded from both values. ``citation_share`` keeps all
otherwise eligible citations in its denominator when this filter is used.

| Direction | Type |
| --- | --- |
| Request | [`CitationQueryV1PostParams`](./src/profound/types/reports/citation_query_v1_post_params.py) |
| Response | [`CitationQueryV1PostResponse`](./src/profound/types/reports/citation_query_v1_post_response.py) |

```python
citation = client.reports.citations.query_v1_post(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
)
```

#### Stream Citations

Stream citations with the same filter semantics as the non-streaming route.

| Direction | Type |
| --- | --- |
| Request | [`CitationStreamV1StreamPostParams`](./src/profound/types/reports/citation_stream_v1_stream_post_params.py) |
| Response | [`CitationStreamV1StreamPostResponse`](./src/profound/types/reports/citation_stream_v1_stream_post_response.py) |

```python
stream = client.reports.citations.stream_v1_stream_post(
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

#### Query Citations V2

| Direction | Type |
| --- | --- |
| Request | [`CitationQueryV2V2PostParams`](./src/profound/types/reports/citation_query_v2_v2_post_params.py) |
| Response | [`CitationQueryV2V2PostResponse`](./src/profound/types/reports/citation_query_v2_v2_post_response.py) |

```python
citation = client.reports.citations.query_v2_v2_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
    entity="domain",
    interval="day",
    scope="all",
)
```

#### Stream Citations V2

| Direction | Type |
| --- | --- |
| Request | [`CitationStreamV2V2StreamPostParams`](./src/profound/types/reports/citation_stream_v2_v2_stream_post_params.py) |
| Response | [`CitationStreamV2V2StreamPostResponse`](./src/profound/types/reports/citation_stream_v2_v2_stream_post_response.py) |

```python
stream = client.reports.citations.stream_v2_v2_stream_post(
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

### `Reports Visibility`

#### Query Visibility

Query visibility report.

| Direction | Type |
| --- | --- |
| Request | [`VisibilityQueryV1PostParams`](./src/profound/types/reports/visibility_query_v1_post_params.py) |
| Response | [`Response`](./src/profound/types/shared/response.py) |

```python
visibility = client.reports.visibility.query_v1_post(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
)
```

#### Stream Visibility

| Direction | Type |
| --- | --- |
| Request | [`VisibilityStreamV1StreamPostParams`](./src/profound/types/reports/visibility_stream_v1_stream_post_params.py) |
| Response | [`VisibilityStreamV1StreamPostResponse`](./src/profound/types/reports/visibility_stream_v1_stream_post_response.py) |

```python
stream = client.reports.visibility.stream_v1_stream_post(
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

#### Query Visibility V2

| Direction | Type |
| --- | --- |
| Request | [`VisibilityQueryV2V2PostParams`](./src/profound/types/reports/visibility_query_v2_v2_post_params.py) |
| Response | [`VisibilityQueryV2V2PostResponse`](./src/profound/types/reports/visibility_query_v2_v2_post_response.py) |

```python
visibility = client.reports.visibility.query_v2_v2_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
    interval="day",
    scope="owned",
)
```

#### Stream Visibility V2

| Direction | Type |
| --- | --- |
| Request | [`VisibilityStreamV2V2StreamPostParams`](./src/profound/types/reports/visibility_stream_v2_v2_stream_post_params.py) |
| Response | [`VisibilityStreamV2V2StreamPostResponse`](./src/profound/types/reports/visibility_stream_v2_v2_stream_post_response.py) |

```python
stream = client.reports.visibility.stream_v2_v2_stream_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
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
| Request | [`SentimentQueryV1PostParams`](./src/profound/types/reports/sentiment_query_v1_post_params.py) |
| Response | [`Response`](./src/profound/types/shared/response.py) |

```python
sentiment = client.reports.sentiment.query_v1_post(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
)
```

#### Stream Sentiment

| Direction | Type |
| --- | --- |
| Request | [`SentimentStreamV1StreamPostParams`](./src/profound/types/reports/sentiment_stream_v1_stream_post_params.py) |
| Response | [`SentimentStreamV1StreamPostResponse`](./src/profound/types/reports/sentiment_stream_v1_stream_post_response.py) |

```python
stream = client.reports.sentiment.stream_v1_stream_post(
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

#### Query Sentiment V2

| Direction | Type |
| --- | --- |
| Request | [`SentimentQueryV2V2PostParams`](./src/profound/types/reports/sentiment_query_v2_v2_post_params.py) |
| Response | [`SentimentQueryV2V2PostResponse`](./src/profound/types/reports/sentiment_query_v2_v2_post_response.py) |

```python
sentiment = client.reports.sentiment.query_v2_v2_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
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
| Request | [`SentimentStreamV2V2StreamPostParams`](./src/profound/types/reports/sentiment_stream_v2_v2_stream_post_params.py) |
| Response | [`SentimentStreamV2V2StreamPostResponse`](./src/profound/types/reports/sentiment_stream_v2_v2_stream_post_response.py) |

```python
stream = client.reports.sentiment.stream_v2_v2_stream_post(
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

### `Reports WebSearchResults`

#### Query Web Search Results

Get web search results for a given category.

| Direction | Type |
| --- | --- |
| Request | [`WebSearchResultQueryV1PostParams`](./src/profound/types/reports/web_search_result_query_v1_post_params.py) |
| Response | [`WebSearchResultQueryV1PostResponse`](./src/profound/types/reports/web_search_result_query_v1_post_response.py) |

```python
web_search_result = client.reports.web_search_results.query_v1_post(
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
| Request | [`WebSearchResultStreamV1StreamPostParams`](./src/profound/types/reports/web_search_result_stream_v1_stream_post_params.py) |
| Response | [`WebSearchResultStreamV1StreamPostResponse`](./src/profound/types/reports/web_search_result_stream_v1_stream_post_response.py) |

```python
stream = client.reports.web_search_results.stream_v1_stream_post(
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

### `Reports Referrals`

#### Get Referrals Report V1

Get referral traffic report from the daily aggregated materialized view.

This endpoint queries pre-aggregated daily referral data, making it efficient
for large date ranges and high-traffic sites.

| Direction | Type |
| --- | --- |
| Request | [`ReferralCreateV1V1PostParams`](./src/profound/types/reports/referral_create_v1_v1_post_params.py) |
| Response | [`Response`](./src/profound/types/shared/response.py) |

```python
referral = client.reports.referrals.create_v1_v1_post(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    domain="",
    start_date="2024-01-01T00:00:00.000Z",
)
```

#### Get Referrals Report V2

Get referral traffic report from the hourly aggregated materialized view (UTC-based).

Supports date_interval="hour", calendar intervals through "year", "quarter", and "relative_week".

| Direction | Type |
| --- | --- |
| Request | [`ReferralCreateV2V2PostParams`](./src/profound/types/reports/referral_create_v2_v2_post_params.py) |
| Response | [`Response`](./src/profound/types/shared/response.py) |

```python
referral = client.reports.referrals.create_v2_v2_post(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    domain="",
    start_date="2024-01-01T00:00:00.000Z",
    timezone="UTC",
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
| Request | [`BotCreateV1V1PostParams`](./src/profound/types/reports/bot_create_v1_v1_post_params.py) |
| Response | [`Response`](./src/profound/types/shared/response.py) |

```python
bot = client.reports.bots.create_v1_v1_post(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    domain="",
    start_date="2024-01-01T00:00:00.000Z",
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
| Request | [`BotCreateV2V2PostParams`](./src/profound/types/reports/bot_create_v2_v2_post_params.py) |
| Response | [`Response`](./src/profound/types/shared/response.py) |

```python
bot = client.reports.bots.create_v2_v2_post(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    domain="",
    start_date="2024-01-01T00:00:00.000Z",
    timezone="UTC",
)
```

### `Reports QueryFanouts`

#### Query Fanouts

| Direction | Type |
| --- | --- |
| Request | [`QueryFanoutV1PostParams`](./src/profound/types/reports/query_fanout_v1_post_params.py) |
| Response | [`Response`](./src/profound/types/shared/response.py) |

```python
query_fanout = client.reports.query_fanouts.v1_post(
    date_interval="day",
    dimensions=[],
    metrics=[],
    order_by={},
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
)
```

#### Query Fanouts V2

| Direction | Type |
| --- | --- |
| Request | [`QueryFanoutV2V2PostParams`](./src/profound/types/reports/query_fanout_v2_v2_post_params.py) |
| Response | [`QueryFanoutV2V2PostResponse`](./src/profound/types/reports/query_fanout_v2_v2_post_response.py) |

```python
query_fanout = client.reports.query_fanouts.v2_v2_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
    interval="day",
)
```

#### Stream Query Fanouts V2

| Direction | Type |
| --- | --- |
| Request | [`QueryFanoutStreamV2V2StreamPostParams`](./src/profound/types/reports/query_fanout_stream_v2_v2_stream_post_params.py) |
| Response | [`QueryFanoutStreamV2V2StreamPostResponse`](./src/profound/types/reports/query_fanout_stream_v2_v2_stream_post_response.py) |

```python
stream = client.reports.query_fanouts.stream_v2_v2_stream_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
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
| Request | [`ShoppingVisibilityV1VisibilityPostParams`](./src/profound/types/reports/shopping_visibility_v1_visibility_post_params.py) |
| Response | [`ShoppingRowsResponse`](./src/profound/types/shared/shopping_rows_response.py) |

```python
shopping = client.reports.shopping.visibility_v1_visibility_post(
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
| Request | [`ShoppingItemVisibilityV1ItemVisibilityPostParams`](./src/profound/types/reports/shopping_item_visibility_v1_item_visibility_post_params.py) |
| Response | [`ShoppingRowsResponse`](./src/profound/types/shared/shopping_rows_response.py) |

```python
shopping = client.reports.shopping.item_visibility_v1_item_visibility_post(
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
| Request | [`ShoppingMerchantDistributionV1MerchantDistributionPostParams`](./src/profound/types/reports/shopping_merchant_distribution_v1_merchant_distribution_post_params.py) |
| Response | [`ShoppingRowsResponse`](./src/profound/types/shared/shopping_rows_response.py) |

```python
shopping = client.reports.shopping.merchant_distribution_v1_merchant_distribution_post(
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
| Request | [`ShoppingMerchantVisibilityByBrandV1MerchantVisibilityByBrandPostParams`](./src/profound/types/reports/shopping_merchant_visibility_by_brand_v1_merchant_visibility_by_brand_post_params.py) |
| Response | [`ShoppingRowsResponse`](./src/profound/types/shared/shopping_rows_response.py) |

```python
shopping = client.reports.shopping.merchant_visibility_by_brand_v1_merchant_visibility_by_brand_post(
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
| Request | [`ShoppingMerchantByItemsV1MerchantByItemsPostParams`](./src/profound/types/reports/shopping_merchant_by_items_v1_merchant_by_items_post_params.py) |
| Response | [`ShoppingRowsResponse`](./src/profound/types/shared/shopping_rows_response.py) |

```python
shopping = client.reports.shopping.merchant_by_items_v1_merchant_by_items_post(
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
| Request | [`ShoppingAllItemsWithMerchantsV1AllItemsWithMerchantsPostParams`](./src/profound/types/reports/shopping_all_items_with_merchants_v1_all_items_with_merchants_post_params.py) |
| Response | [`ShoppingRowsResponse`](./src/profound/types/shared/shopping_rows_response.py) |

```python
shopping = client.reports.shopping.all_items_with_merchants_v1_all_items_with_merchants_post(
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
| Request | [`ShoppingTriggerRateV1TriggerRatePostParams`](./src/profound/types/reports/shopping_trigger_rate_v1_trigger_rate_post_params.py) |
| Response | [`ShoppingRowsResponse`](./src/profound/types/shared/shopping_rows_response.py) |

```python
shopping = client.reports.shopping.trigger_rate_v1_trigger_rate_post(
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

#### Shopping Triggered Prompts

| Direction | Type |
| --- | --- |
| Request | [`ShoppingTriggeredPromptsV1TriggeredPromptsPostParams`](./src/profound/types/reports/shopping_triggered_prompts_v1_triggered_prompts_post_params.py) |
| Response | [`ShoppingRowsResponse`](./src/profound/types/shared/shopping_rows_response.py) |

```python
shopping = client.reports.shopping.triggered_prompts_v1_triggered_prompts_post(
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

#### Shopping Triggered Topics

| Direction | Type |
| --- | --- |
| Request | [`ShoppingTriggeredTopicsV1TriggeredTopicsPostParams`](./src/profound/types/reports/shopping_triggered_topics_v1_triggered_topics_post_params.py) |
| Response | [`ShoppingRowsResponse`](./src/profound/types/shared/shopping_rows_response.py) |

```python
shopping = client.reports.shopping.triggered_topics_v1_triggered_topics_post(
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
| Request | [`ShoppingMerchantShareV1MerchantSharePostParams`](./src/profound/types/reports/shopping_merchant_share_v1_merchant_share_post_params.py) |
| Response | [`ShoppingRowsResponse`](./src/profound/types/shared/shopping_rows_response.py) |

```python
shopping = client.reports.shopping.merchant_share_v1_merchant_share_post(
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
| Request | [`ShoppingProductMerchantURLsV1ProductMerchantURLsPostParams`](./src/profound/types/reports/shopping_product_merchant_urls_v1_product_merchant_urls_post_params.py) |
| Response | [`ShoppingRowsResponse`](./src/profound/types/shared/shopping_rows_response.py) |

```python
shopping = client.reports.shopping.product_merchant_urls_v1_product_merchant_urls_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    product_names=[],
    start_date="2024-01-01T00:00:00.000Z",
    end_date="2024-01-01T00:00:00.000Z",
)
```

#### Shopping Executions

| Direction | Type |
| --- | --- |
| Request | [`ShoppingExecutionsV1ExecutionsPostParams`](./src/profound/types/reports/shopping_executions_v1_executions_post_params.py) |
| Response | [`ShoppingRowsResponse`](./src/profound/types/shared/shopping_rows_response.py) |

```python
shopping = client.reports.shopping.executions_v1_executions_post(
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

#### Query Shopping Brands V2

| Direction | Type |
| --- | --- |
| Request | [`ShoppingQueryBrandsV2V2BrandsPostParams`](./src/profound/types/reports/shopping_query_brands_v2_v2_brands_post_params.py) |
| Response | [`ShoppingQueryBrandsV2V2BrandsPostResponse`](./src/profound/types/reports/shopping_query_brands_v2_v2_brands_post_response.py) |

```python
shopping = client.reports.shopping.query_brands_v2_v2_brands_post(
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
| Request | [`ShoppingStreamBrandsV2V2BrandsStreamPostParams`](./src/profound/types/reports/shopping_stream_brands_v2_v2_brands_stream_post_params.py) |
| Response | [`ShoppingStreamBrandsV2V2BrandsStreamPostResponse`](./src/profound/types/reports/shopping_stream_brands_v2_v2_brands_stream_post_response.py) |

```python
stream = client.reports.shopping.stream_brands_v2_v2_brands_stream_post(
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
| Request | [`ShoppingQueryProductsV2V2ProductsPostParams`](./src/profound/types/reports/shopping_query_products_v2_v2_products_post_params.py) |
| Response | [`ShoppingQueryProductsV2V2ProductsPostResponse`](./src/profound/types/reports/shopping_query_products_v2_v2_products_post_response.py) |

```python
shopping = client.reports.shopping.query_products_v2_v2_products_post(
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
| Request | [`ShoppingStreamProductsV2V2ProductsStreamPostParams`](./src/profound/types/reports/shopping_stream_products_v2_v2_products_stream_post_params.py) |
| Response | [`ShoppingStreamProductsV2V2ProductsStreamPostResponse`](./src/profound/types/reports/shopping_stream_products_v2_v2_products_stream_post_response.py) |

```python
stream = client.reports.shopping.stream_products_v2_v2_products_stream_post(
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
| Request | [`ShoppingQueryMerchantsV2V2MerchantsPostParams`](./src/profound/types/reports/shopping_query_merchants_v2_v2_merchants_post_params.py) |
| Response | [`ShoppingQueryMerchantsV2V2MerchantsPostResponse`](./src/profound/types/reports/shopping_query_merchants_v2_v2_merchants_post_response.py) |

```python
shopping = client.reports.shopping.query_merchants_v2_v2_merchants_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
    interval="day",
)
```

#### Stream Shopping Merchants V2

| Direction | Type |
| --- | --- |
| Request | [`ShoppingStreamMerchantsV2V2MerchantsStreamPostParams`](./src/profound/types/reports/shopping_stream_merchants_v2_v2_merchants_stream_post_params.py) |
| Response | [`ShoppingStreamMerchantsV2V2MerchantsStreamPostResponse`](./src/profound/types/reports/shopping_stream_merchants_v2_v2_merchants_stream_post_response.py) |

```python
stream = client.reports.shopping.stream_merchants_v2_v2_merchants_stream_post(
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
| Request | [`ShoppingQueryTriggerRateV2V2TriggerRatePostParams`](./src/profound/types/reports/shopping_query_trigger_rate_v2_v2_trigger_rate_post_params.py) |
| Response | [`ShoppingQueryTriggerRateV2V2TriggerRatePostResponse`](./src/profound/types/reports/shopping_query_trigger_rate_v2_v2_trigger_rate_post_response.py) |

```python
shopping = client.reports.shopping.query_trigger_rate_v2_v2_trigger_rate_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
    interval="day",
)
```

#### Stream Shopping Trigger Rate V2

| Direction | Type |
| --- | --- |
| Request | [`ShoppingStreamTriggerRateV2V2TriggerRateStreamPostParams`](./src/profound/types/reports/shopping_stream_trigger_rate_v2_v2_trigger_rate_stream_post_params.py) |
| Response | [`ShoppingStreamTriggerRateV2V2TriggerRateStreamPostResponse`](./src/profound/types/reports/shopping_stream_trigger_rate_v2_v2_trigger_rate_stream_post_response.py) |

```python
stream = client.reports.shopping.stream_trigger_rate_v2_v2_trigger_rate_stream_post(
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
| Request | [`AccuracyOverviewV1OverviewPostParams`](./src/profound/types/reports/accuracy_overview_v1_overview_post_params.py) |
| Response | [`AccuracyOverviewV1OverviewPostResponse`](./src/profound/types/reports/accuracy_overview_v1_overview_post_response.py) |

```python
accuracy = client.reports.accuracy.overview_v1_overview_post(
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
| Request | [`AccuracyBreakdownV1BreakdownPostParams`](./src/profound/types/reports/accuracy_breakdown_v1_breakdown_post_params.py) |
| Response | [`AccuracyBreakdownV1BreakdownPostResponse`](./src/profound/types/reports/accuracy_breakdown_v1_breakdown_post_response.py) |

```python
accuracy = client.reports.accuracy.breakdown_v1_breakdown_post(
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
| Request | [`AccuracyCitationAnalysisV1CitationAnalysisPostParams`](./src/profound/types/reports/accuracy_citation_analysis_v1_citation_analysis_post_params.py) |
| Response | [`AccuracyCitationAnalysisV1CitationAnalysisPostResponse`](./src/profound/types/reports/accuracy_citation_analysis_v1_citation_analysis_post_response.py) |

```python
accuracy = client.reports.accuracy.citation_analysis_v1_citation_analysis_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    clean_href="",
    start_date="",
    end_date="",
)
```

#### Accuracy Topic Ids

| Direction | Type |
| --- | --- |
| Request | [`AccuracyTopicIDsV1TopicIDsPostParams`](./src/profound/types/reports/accuracy_topic_ids_v1_topic_ids_post_params.py) |
| Response | [`AccuracyTopicIDsV1TopicIDsPostResponse`](./src/profound/types/reports/accuracy_topic_ids_v1_topic_ids_post_response.py) |

```python
accuracy = client.reports.accuracy.topic_ids_v1_topic_ids_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
)
```

#### Accuracy Inaccurate Themes

| Direction | Type |
| --- | --- |
| Request | [`AccuracyInaccurateThemesV1InaccurateThemesPostParams`](./src/profound/types/reports/accuracy_inaccurate_themes_v1_inaccurate_themes_post_params.py) |
| Response | [`AccuracyInaccurateThemesV1InaccurateThemesPostResponse`](./src/profound/types/reports/accuracy_inaccurate_themes_v1_inaccurate_themes_post_response.py) |

```python
accuracy = client.reports.accuracy.inaccurate_themes_v1_inaccurate_themes_post(
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
| Request | [`AccuracyInaccurateClustersV1InaccurateClustersPostParams`](./src/profound/types/reports/accuracy_inaccurate_clusters_v1_inaccurate_clusters_post_params.py) |
| Response | [`AccuracyInaccurateClustersV1InaccurateClustersPostResponse`](./src/profound/types/reports/accuracy_inaccurate_clusters_v1_inaccurate_clusters_post_response.py) |

```python
accuracy = client.reports.accuracy.inaccurate_clusters_v1_inaccurate_clusters_post(
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
| Request | [`AccuracyInaccuracyDriversV1InaccuracyDriversPostParams`](./src/profound/types/reports/accuracy_inaccuracy_drivers_v1_inaccuracy_drivers_post_params.py) |
| Response | [`AccuracyInaccuracyDriversV1InaccuracyDriversPostResponse`](./src/profound/types/reports/accuracy_inaccuracy_drivers_v1_inaccuracy_drivers_post_response.py) |

```python
accuracy = client.reports.accuracy.inaccuracy_drivers_v1_inaccuracy_drivers_post(
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
| Request | [`AccuracyTopInaccurateClaimsV1TopInaccurateClaimsPostParams`](./src/profound/types/reports/accuracy_top_inaccurate_claims_v1_top_inaccurate_claims_post_params.py) |
| Response | [`AccuracyTopInaccurateClaimsV1TopInaccurateClaimsPostResponse`](./src/profound/types/reports/accuracy_top_inaccurate_claims_v1_top_inaccurate_claims_post_response.py) |

```python
accuracy = client.reports.accuracy.top_inaccurate_claims_v1_top_inaccurate_claims_post(
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
| Request | [`AccuracyClaimBreakdownV1ClaimBreakdownPostParams`](./src/profound/types/reports/accuracy_claim_breakdown_v1_claim_breakdown_post_params.py) |
| Response | [`AccuracyClaimBreakdownV1ClaimBreakdownPostResponse`](./src/profound/types/reports/accuracy_claim_breakdown_v1_claim_breakdown_post_response.py) |

```python
accuracy = client.reports.accuracy.claim_breakdown_v1_claim_breakdown_post(
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
| Request | [`AccuracyClaimCitationsV1ClaimCitationsPostParams`](./src/profound/types/reports/accuracy_claim_citations_v1_claim_citations_post_params.py) |
| Response | [`AccuracyClaimCitationsV1ClaimCitationsPostResponse`](./src/profound/types/reports/accuracy_claim_citations_v1_claim_citations_post_response.py) |

```python
accuracy = client.reports.accuracy.claim_citations_v1_claim_citations_post(
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
| Request | [`AccuracyClusterExampleRunsV1ClusterExampleRunsPostParams`](./src/profound/types/reports/accuracy_cluster_example_runs_v1_cluster_example_runs_post_params.py) |
| Response | [`AccuracyClusterExampleRunsV1ClusterExampleRunsPostResponse`](./src/profound/types/reports/accuracy_cluster_example_runs_v1_cluster_example_runs_post_response.py) |

```python
accuracy = client.reports.accuracy.cluster_example_runs_v1_cluster_example_runs_post(
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
| Request | [`AccuracyClusterVerificationPairsV1ClusterVerificationPairsPostParams`](./src/profound/types/reports/accuracy_cluster_verification_pairs_v1_cluster_verification_pairs_post_params.py) |
| Response | [`AccuracyClusterVerificationPairsV1ClusterVerificationPairsPostResponse`](./src/profound/types/reports/accuracy_cluster_verification_pairs_v1_cluster_verification_pairs_post_response.py) |

```python
accuracy = client.reports.accuracy.cluster_verification_pairs_v1_cluster_verification_pairs_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Accuracy Factcheck Setup Status

| Direction | Type |
| --- | --- |
| Request | [`AccuracyFactcheckSetupStatusV1FactcheckSetupStatusPostParams`](./src/profound/types/reports/accuracy_factcheck_setup_status_v1_factcheck_setup_status_post_params.py) |
| Response | [`AccuracyFactcheckSetupStatusV1FactcheckSetupStatusPostResponse`](./src/profound/types/reports/accuracy_factcheck_setup_status_v1_factcheck_setup_status_post_response.py) |

```python
accuracy = client.reports.accuracy.factcheck_setup_status_v1_factcheck_setup_status_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### `Reports Factcheck`

#### Query Scores

| Direction | Type |
| --- | --- |
| Request | [`FactcheckQueryScoresV2PostParams`](./src/profound/types/reports/factcheck_query_scores_v2_post_params.py) |
| Response | [`FactcheckQueryScoresV2PostResponse`](./src/profound/types/reports/factcheck_query_scores_v2_post_response.py) |

```python
factcheck = client.reports.factcheck.query_scores_v2_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
)
```

#### Stream Scores

| Direction | Type |
| --- | --- |
| Request | [`FactcheckStreamScoresV2StreamPostParams`](./src/profound/types/reports/factcheck_stream_scores_v2_stream_post_params.py) |
| Response | [`FactcheckStreamScoresV2StreamPostResponse`](./src/profound/types/reports/factcheck_stream_scores_v2_stream_post_response.py) |

```python
stream = client.reports.factcheck.stream_scores_v2_stream_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
)

for event in stream:
    print(event)
```

#### Query Claims

| Direction | Type |
| --- | --- |
| Request | [`FactcheckQueryClaimsV2ClaimsPostParams`](./src/profound/types/reports/factcheck_query_claims_v2_claims_post_params.py) |
| Response | [`FactcheckQueryClaimsV2ClaimsPostResponse`](./src/profound/types/reports/factcheck_query_claims_v2_claims_post_response.py) |

```python
factcheck = client.reports.factcheck.query_claims_v2_claims_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
)
```

#### Stream Claims

| Direction | Type |
| --- | --- |
| Request | [`FactcheckStreamClaimsV2ClaimsStreamPostParams`](./src/profound/types/reports/factcheck_stream_claims_v2_claims_stream_post_params.py) |
| Response | [`FactcheckStreamClaimsV2ClaimsStreamPostResponse`](./src/profound/types/reports/factcheck_stream_claims_v2_claims_stream_post_response.py) |

```python
stream = client.reports.factcheck.stream_claims_v2_claims_stream_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
)

for event in stream:
    print(event)
```

### `Reports Social`

#### Query Youtube Channels

Rank the YouTube channels cited in a category, or the video categories they publish in.

| Direction | Type |
| --- | --- |
| Request | [`SocialQueryYoutubeChannelsV2YoutubeChannelsPostParams`](./src/profound/types/reports/social_query_youtube_channels_v2_youtube_channels_post_params.py) |
| Response | [`SocialQueryYoutubeChannelsV2YoutubeChannelsPostResponse`](./src/profound/types/reports/social_query_youtube_channels_v2_youtube_channels_post_response.py) |

```python
social = client.reports.social.query_youtube_channels_v2_youtube_channels_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
)
```

#### Query Youtube Videos

Rank cited YouTube videos, for one channel or across all of them.

| Direction | Type |
| --- | --- |
| Request | [`SocialQueryYoutubeVideosV2YoutubeVideosPostParams`](./src/profound/types/reports/social_query_youtube_videos_v2_youtube_videos_post_params.py) |
| Response | [`SocialQueryYoutubeVideosV2YoutubeVideosPostResponse`](./src/profound/types/reports/social_query_youtube_videos_v2_youtube_videos_post_response.py) |

```python
social = client.reports.social.query_youtube_videos_v2_youtube_videos_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
    attribution="attributed",
)
```

#### Query Youtube Summary

Report how much of youtube.com the channel and video rankings account for.

| Direction | Type |
| --- | --- |
| Request | [`SocialQueryYoutubeSummaryV2YoutubeSummaryPostParams`](./src/profound/types/reports/social_query_youtube_summary_v2_youtube_summary_post_params.py) |
| Response | [`SocialQueryYoutubeSummaryV2YoutubeSummaryPostResponse`](./src/profound/types/reports/social_query_youtube_summary_v2_youtube_summary_post_response.py) |

```python
social = client.reports.social.query_youtube_summary_v2_youtube_summary_post(
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
| Request | [`OptimizationListV1AssetIDGetParams`](./src/profound/types/content/optimization_list_v1_asset_id_get_params.py) |
| Response | [`OptimizationListV1AssetIDGetResponse`](./src/profound/types/content/optimization_list_v1_asset_id_get_response.py) |

```python
optimization = client.content.optimization.list_v1_asset_id_get(
    asset_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    limit=10000,
    offset=0,
)
```

#### Optimization Analysis

| Direction | Type |
| --- | --- |
| Response | [`OptimizationAnalysisV1AssetIDIDGetResponse`](./src/profound/types/content/optimization_analysis_v1_asset_id_id_get_response.py) |

```python
optimization = client.content.optimization.analysis_v1_asset_id_id_get(
    asset_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    content_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

## `KnowledgeBases`

### List Knowledge Bases

List knowledge bases accessible to the API key.

| Direction | Type |
| --- | --- |
| Request | [`KnowledgeBaseListV1GetParams`](./src/profound/types/knowledge_base_list_v1_get_params.py) |
| Response | [`KnowledgeBaseListV1GetResponse`](./src/profound/types/knowledge_base_list_v1_get_response.py) |

```python
knowledge_base = client.knowledge_bases.list_v1_get()
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
| Request | [`DocumentCreateV1IDPostParams`](./src/profound/types/knowledge_bases/document_create_v1_id_post_params.py) |
| Response | [`DocumentOperationResponse`](./src/profound/types/shared/document_operation_response.py) |

```python
document = client.knowledge_bases.documents.create_v1_id_post(
    knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    name="x",
    text="x",
)
```

#### Update Document

Overwrite a knowledge base document using JSON text or multipart file upload.

| Direction | Type |
| --- | --- |
| Request | [`DocumentUpdateV1IDPutParams`](./src/profound/types/knowledge_bases/document_update_v1_id_put_params.py) |
| Response | [`DocumentOperationResponse`](./src/profound/types/shared/document_operation_response.py) |

```python
document = client.knowledge_bases.documents.update_v1_id_put(
    knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    name="x",
    text="x",
)
```

#### Delete Document

Delete an existing document from a knowledge base.

| Direction | Type |
| --- | --- |
| Request | [`DocumentDeleteV1IDDeleteParams`](./src/profound/types/knowledge_bases/document_delete_v1_id_delete_params.py) |
| Response | [`DocumentOperationResponse`](./src/profound/types/shared/document_operation_response.py) |

```python
document = client.knowledge_bases.documents.delete_v1_id_delete(
    knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    name="x",
)
```

### `KnowledgeBases Folders`

#### Add Folder

Create an empty folder at the requested knowledge base path.

| Direction | Type |
| --- | --- |
| Request | [`FolderCreateV1IDPostParams`](./src/profound/types/knowledge_bases/folder_create_v1_id_post_params.py) |
| Response | [`FolderCreateV1IDPostResponse`](./src/profound/types/knowledge_bases/folder_create_v1_id_post_response.py) |

```python
folder = client.knowledge_bases.folders.create_v1_id_post(
    knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    path="x",
)
```

#### Delete Folder

Delete a folder. With recursive=false, non-empty folders return 409 and no contents are deleted.

| Direction | Type |
| --- | --- |
| Request | [`FolderDeleteV1IDDeleteParams`](./src/profound/types/knowledge_bases/folder_delete_v1_id_delete_params.py) |
| Response | [`FolderDeleteV1IDDeleteResponse`](./src/profound/types/knowledge_bases/folder_delete_v1_id_delete_response.py) |

```python
folder = client.knowledge_bases.folders.delete_v1_id_delete(
    knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    path="x",
    recursive=False,
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
| Request | [`IntegrationListV1GetParams`](./src/profound/types/integration_list_v1_get_params.py) |
| Response | [`IntegrationListV1GetResponse`](./src/profound/types/integration_list_v1_get_response.py) |

```python
integration = client.integrations.list_v1_get()
```

## `Documents`

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
| Request | [`DocumentListV1GetParams`](./src/profound/types/document_list_v1_get_params.py) |
| Response | [`DocumentListV1GetResponse`](./src/profound/types/document_list_v1_get_response.py) |

```python
document = client.documents.list_v1_get(
    organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    limit=20,
)
```

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
| Request | [`DocumentCreateV1PostParams`](./src/profound/types/document_create_v1_post_params.py) |
| Response | [`DocumentCreateV1PostResponse`](./src/profound/types/document_create_v1_post_response.py) |

```python
document = client.documents.create_v1_post(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    name="x",
    content_markdown="x",
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
| Request | [`DocumentReadV1IDGetParams`](./src/profound/types/document_read_v1_id_get_params.py) |
| Response | [`DocumentReadV1IDGetResponse`](./src/profound/types/document_read_v1_id_get_response.py) |

```python
document = client.documents.read_v1_id_get(
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
| Request | [`DocumentPatchV1IDPatchParams`](./src/profound/types/document_patch_v1_id_patch_params.py) |
| Response | [`DocumentPatchV1IDPatchResponse`](./src/profound/types/document_patch_v1_id_patch_response.py) |

```python
document = client.documents.patch_v1_id_patch(
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
| Request | [`DocumentDeleteV1IDDeleteParams`](./src/profound/types/document_delete_v1_id_delete_params.py) |

```python
client.documents.delete_v1_id_delete(
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
| Request | [`DocumentReplaceContentV1IDContentPostParams`](./src/profound/types/document_replace_content_v1_id_content_post_params.py) |
| Response | [`DocumentReplaceContentV1IDContentPostResponse`](./src/profound/types/document_replace_content_v1_id_content_post_response.py) |

```python
document = client.documents.replace_content_v1_id_content_post(
    document_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    content_markdown="",
    skip_title_sync=False,
)
```

## `OpenAiAds`

### Get Account Insights

Get ad account insights for the organization's OpenAI Ads partner brand.

`aggregation_level=campaign` returns one row per campaign (with `campaign_id`
/ `campaign_name` and all metrics), so every campaign's insights come back in
a single call; `time_granularity=daily` gives per-day rows (e.g. daily spend).

| Direction | Type |
| --- | --- |
| Request | [`OpenAIAdListAccountInsightsV1OpenAIAccountInsightsGetParams`](./src/profound/types/open_ai_ad_list_account_insights_v1_openai_account_insights_get_params.py) |
| Response | [`OpenAIAdListAccountInsightsV1OpenAIAccountInsightsGetResponse`](./src/profound/types/open_ai_ad_list_account_insights_v1_openai_account_insights_get_response.py) |

```python
open_ai_ad = client.open_ai_ads.list_account_insights_v1_openai_account_insights_get()
```

## `Projects`

### List Projects

| Direction | Type |
| --- | --- |
| Request | [`ProjectListV1GetParams`](./src/profound/types/project_list_v1_get_params.py) |
| Response | [`ProjectListV1GetResponse`](./src/profound/types/project_list_v1_get_response.py) |

```python
project = client.projects.list_v1_get(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    limit=100,
    offset=0,
)
```

### Create Project

| Direction | Type |
| --- | --- |
| Request | [`ProjectCreateV1PostParams`](./src/profound/types/project_create_v1_post_params.py) |
| Response | [`ProjectCreateV1PostResponse`](./src/profound/types/project_create_v1_post_response.py) |

```python
project = client.projects.create_v1_post(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Get Project

| Direction | Type |
| --- | --- |
| Request | [`ProjectRetrieveV1GetParams`](./src/profound/types/project_retrieve_v1_get_params.py) |
| Response | [`ProjectRetrieveV1GetResponse`](./src/profound/types/project_retrieve_v1_get_response.py) |

```python
project = client.projects.retrieve_v1_get(
    project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Delete Project

| Direction | Type |
| --- | --- |
| Request | [`ProjectDeleteV1IDDeleteParams`](./src/profound/types/project_delete_v1_id_delete_params.py) |

```python
client.projects.delete_v1_id_delete(
    project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Get Project Status

| Direction | Type |
| --- | --- |
| Request | [`ProjectListStatusV1StatusGetParams`](./src/profound/types/project_list_status_v1_status_get_params.py) |
| Response | [`ProjectListStatusV1StatusGetResponse`](./src/profound/types/project_list_status_v1_status_get_response.py) |

```python
project = client.projects.list_status_v1_status_get(
    project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Archive Project

| Direction | Type |
| --- | --- |
| Request | [`ProjectArchiveV1IDArchivePostParams`](./src/profound/types/project_archive_v1_id_archive_post_params.py) |
| Response | [`ProjectArchiveV1IDArchivePostResponse`](./src/profound/types/project_archive_v1_id_archive_post_response.py) |

```python
project = client.projects.archive_v1_id_archive_post(
    project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Unarchive Project

| Direction | Type |
| --- | --- |
| Request | [`ProjectUnarchiveV1IDUnarchivePostParams`](./src/profound/types/project_unarchive_v1_id_unarchive_post_params.py) |
| Response | [`ProjectUnarchiveV1IDUnarchivePostResponse`](./src/profound/types/project_unarchive_v1_id_unarchive_post_response.py) |

```python
project = client.projects.unarchive_v1_id_unarchive_post(
    project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### `Projects Generations`

#### List Project Generations

| Direction | Type |
| --- | --- |
| Request | [`GenerationListV1GetParams`](./src/profound/types/projects/generation_list_v1_get_params.py) |
| Response | [`GenerationListV1GetResponse`](./src/profound/types/projects/generation_list_v1_get_response.py) |

```python
generation = client.projects.generations.list_v1_get(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    limit=100,
    offset=0,
)
```

#### Get Project Generation Status

| Direction | Type |
| --- | --- |
| Request | [`GenerationRetrieveStatusV1RunGetParams`](./src/profound/types/projects/generation_retrieve_status_v1_run_get_params.py) |
| Response | [`GenerationRetrieveStatusV1RunGetResponse`](./src/profound/types/projects/generation_retrieve_status_v1_run_get_response.py) |

```python
generation = client.projects.generations.retrieve_status_v1_run_get(
    run_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### `Projects Tasks`

#### List Project Tasks

| Direction | Type |
| --- | --- |
| Request | [`TaskListV1IDGetParams`](./src/profound/types/projects/task_list_v1_id_get_params.py) |
| Response | [`TaskListV1IDGetResponse`](./src/profound/types/projects/task_list_v1_id_get_response.py) |

```python
task = client.projects.tasks.list_v1_id_get(
    project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Create Project Task

| Direction | Type |
| --- | --- |
| Request | [`TaskCreateV1IDPostParams`](./src/profound/types/projects/task_create_v1_id_post_params.py) |
| Response | [`TaskCreateV1IDPostResponse`](./src/profound/types/projects/task_create_v1_id_post_response.py) |

```python
task = client.projects.tasks.create_v1_id_post(
    project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    title="x",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Get Project Task

| Direction | Type |
| --- | --- |
| Request | [`TaskRetrieveV1GetParams`](./src/profound/types/projects/task_retrieve_v1_get_params.py) |
| Response | [`TaskRetrieveV1GetResponse`](./src/profound/types/projects/task_retrieve_v1_get_response.py) |

```python
task = client.projects.tasks.retrieve_v1_get(
    project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Update Project Task

| Direction | Type |
| --- | --- |
| Request | [`TaskUpdateV1IDIDPatchParams`](./src/profound/types/projects/task_update_v1_id_id_patch_params.py) |
| Response | [`TaskUpdateV1IDIDPatchResponse`](./src/profound/types/projects/task_update_v1_id_id_patch_response.py) |

```python
task = client.projects.tasks.update_v1_id_id_patch(
    project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Delete Project Task

| Direction | Type |
| --- | --- |
| Request | [`TaskDeleteV1IDIDDeleteParams`](./src/profound/types/projects/task_delete_v1_id_id_delete_params.py) |

```python
client.projects.tasks.delete_v1_id_id_delete(
    project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Update Project Task Status

| Direction | Type |
| --- | --- |
| Request | [`TaskUpdateStatusV1IDIDStatusPostParams`](./src/profound/types/projects/task_update_status_v1_id_id_status_post_params.py) |
| Response | [`TaskUpdateStatusV1IDIDStatusPostResponse`](./src/profound/types/projects/task_update_status_v1_id_id_status_post_response.py) |

```python
task = client.projects.tasks.update_status_v1_id_id_status_post(
    project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    status="not_started",
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
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
| Request | [`AgentListV1GetParams`](./src/profound/types/agent_list_v1_get_params.py) |
| Response | [`AgentListV1GetResponse`](./src/profound/types/agent_list_v1_get_response.py) |

```python
agent = client.agents.list_v1_get(
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
| Request | [`AgentCreateV1PostParams`](./src/profound/types/agent_create_v1_post_params.py) |
| Response | [`Agent`](./src/profound/types/shared/agent.py) |

```python
agent = client.agents.create_v1_post(
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
| Response | [`Agent`](./src/profound/types/shared/agent.py) |

```python
agent = client.agents.publish_v1_id_publish_post(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Get an agent

Retrieve an agent and its schema details.

Agents can have both a live published version and a draft version with newer
unpublished changes. Use the `version` parameter to choose which state to return.

| Direction | Type |
| --- | --- |
| Request | [`AgentRetrieveV1GetParams`](./src/profound/types/agent_retrieve_v1_get_params.py) |
| Response | [`AgentRetrieveV1GetResponse`](./src/profound/types/agent_retrieve_v1_get_response.py) |

```python
agent = client.agents.retrieve_v1_get(
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
| Request | [`AgentUpdateV1IDPatchParams`](./src/profound/types/agent_update_v1_id_patch_params.py) |
| Response | [`AgentUpdateV1IDPatchResponse`](./src/profound/types/agent_update_v1_id_patch_response.py) |

```python
agent = client.agents.update_v1_id_patch(
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
| Request | [`AgentListGraphV1GraphGetParams`](./src/profound/types/agent_list_graph_v1_graph_get_params.py) |
| Response | [`AgentListGraphV1GraphGetResponse`](./src/profound/types/agent_list_graph_v1_graph_get_response.py) |

```python
agent = client.agents.list_graph_v1_graph_get(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
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
| Response | [`NodeTypeListV1GetResponse`](./src/profound/types/agents/node_type_list_v1_get_response.py) |

```python
node_type = client.agents.node_types.list_v1_get()
```

#### Get a node type schema

Retrieve the JSON schema for a single node type.

The `schema` field is an opaque JSON Schema for the node's configuration.
Use `schema_version` as a cache key — it bumps whenever the schema changes.

| Direction | Type |
| --- | --- |
| Response | [`NodeTypeListSchemaV1SchemaGetResponse`](./src/profound/types/agents/node_type_list_schema_v1_schema_get_response.py) |

```python
node_type = client.agents.node_types.list_schema_v1_schema_get(
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
| Request | [`RunV1IDPostParams`](./src/profound/types/agents/run_v1_id_post_params.py) |
| Response | [`RunV1IDPostResponse`](./src/profound/types/agents/run_v1_id_post_response.py) |

```python
run = client.agents.runs.v1_id_post(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Get an agent run

Retrieve the current status and result details for an agent run.

| Direction | Type |
| --- | --- |
| Request | [`RunRetrieveV1GetParams`](./src/profound/types/agents/run_retrieve_v1_get_params.py) |
| Response | [`RunRetrieveV1GetResponse`](./src/profound/types/agents/run_retrieve_v1_get_response.py) |

```python
run = client.agents.runs.retrieve_v1_get(
    agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    run_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    verbose=False,
)
```
