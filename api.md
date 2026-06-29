# Shared Types

```python
from profound.types import (
    AnalysisTypeFilter,
    AssetIDFilter,
    BotNameFilter,
    BotProviderFilter,
    CursorPagination,
    ModelIDFilter,
    Pagination,
    PathFilter,
    PersonaIDFilter,
    PromptFilter,
    PromptTypeFilter,
    RegionIDFilter,
    RegionNameFilter,
    TagIDFilter,
    TopicIDFilter,
)
```

# Organizations

Types:

```python
from profound.types import (
    Category,
    NamedResource,
    Organization,
    PersonaProfile,
    PersonaProfileBehavior,
    PersonaProfileDemographics,
    PersonaProfileEmployment,
    OrganizationListResponse,
    OrganizationDomainsResponse,
    OrganizationGetPersonasResponse,
    OrganizationListAssetsResponse,
    OrganizationModelsResponse,
    OrganizationRegionsResponse,
)
```

Methods:

- <code title="get /v1/org">client.organizations.<a href="./src/profound/resources/organizations/organizations.py">list</a>() -> <a href="./src/profound/types/organization_list_response.py">OrganizationListResponse</a></code>
- <code title="get /v1/org/domains">client.organizations.<a href="./src/profound/resources/organizations/organizations.py">domains</a>(\*\*<a href="src/profound/types/organization_domains_params.py">params</a>) -> <a href="./src/profound/types/organization_domains_response.py">OrganizationDomainsResponse</a></code>
- <code title="get /v1/org/personas">client.organizations.<a href="./src/profound/resources/organizations/organizations.py">get_personas</a>(\*\*<a href="src/profound/types/organization_get_personas_params.py">params</a>) -> <a href="./src/profound/types/organization_get_personas_response.py">OrganizationGetPersonasResponse</a></code>
- <code title="get /v1/org/assets">client.organizations.<a href="./src/profound/resources/organizations/organizations.py">list_assets</a>(\*\*<a href="src/profound/types/organization_list_assets_params.py">params</a>) -> <a href="./src/profound/types/organization_list_assets_response.py">OrganizationListAssetsResponse</a></code>
- <code title="get /v1/org/models">client.organizations.<a href="./src/profound/resources/organizations/organizations.py">models</a>() -> <a href="./src/profound/types/organization_models_response.py">OrganizationModelsResponse</a></code>
- <code title="get /v1/org/regions">client.organizations.<a href="./src/profound/resources/organizations/organizations.py">regions</a>(\*\*<a href="src/profound/types/organization_regions_params.py">params</a>) -> <a href="./src/profound/types/organization_regions_response.py">OrganizationRegionsResponse</a></code>

## Categories

Types:

```python
from profound.types.organizations import (
    FieldDiff,
    IDOrName,
    NamedResourceDiffList,
    CategoryListResponse,
    CategoryAssetsResponse,
    CategoryCreatePromptsResponse,
    CategoryGetCategoryPersonasResponse,
    CategoryPromptsResponse,
    CategoryRetrieveRegionsResponse,
    CategoryTagsResponse,
    CategoryTopicsResponse,
    CategoryUpdatePromptStatusResponse,
    CategoryUpdatePromptsResponse,
)
```

Methods:

- <code title="get /v1/org/categories">client.organizations.categories.<a href="./src/profound/resources/organizations/categories.py">list</a>(\*\*<a href="src/profound/types/organizations/category_list_params.py">params</a>) -> <a href="./src/profound/types/organizations/category_list_response.py">CategoryListResponse</a></code>
- <code title="get /v1/org/categories/{category_id}/assets">client.organizations.categories.<a href="./src/profound/resources/organizations/categories.py">assets</a>(category_id) -> <a href="./src/profound/types/organizations/category_assets_response.py">CategoryAssetsResponse</a></code>
- <code title="post /v1/org/categories/{category_id}/prompts">client.organizations.categories.<a href="./src/profound/resources/organizations/categories.py">create_prompts</a>(category_id, \*\*<a href="src/profound/types/organizations/category_create_prompts_params.py">params</a>) -> <a href="./src/profound/types/organizations/category_create_prompts_response.py">CategoryCreatePromptsResponse</a></code>
- <code title="get /v1/org/categories/{category_id}/personas">client.organizations.categories.<a href="./src/profound/resources/organizations/categories.py">get_category_personas</a>(category_id) -> <a href="./src/profound/types/organizations/category_get_category_personas_response.py">CategoryGetCategoryPersonasResponse</a></code>
- <code title="get /v1/org/categories/{category_id}/prompts">client.organizations.categories.<a href="./src/profound/resources/organizations/categories.py">prompts</a>(category_id, \*\*<a href="src/profound/types/organizations/category_prompts_params.py">params</a>) -> <a href="./src/profound/types/organizations/category_prompts_response.py">CategoryPromptsResponse</a></code>
- <code title="get /v1/org/categories/{category_id}/regions">client.organizations.categories.<a href="./src/profound/resources/organizations/categories.py">retrieve_regions</a>(category_id) -> <a href="./src/profound/types/organizations/category_retrieve_regions_response.py">CategoryRetrieveRegionsResponse</a></code>
- <code title="get /v1/org/categories/{category_id}/tags">client.organizations.categories.<a href="./src/profound/resources/organizations/categories.py">tags</a>(category_id) -> <a href="./src/profound/types/organizations/category_tags_response.py">CategoryTagsResponse</a></code>
- <code title="get /v1/org/categories/{category_id}/topics">client.organizations.categories.<a href="./src/profound/resources/organizations/categories.py">topics</a>(category_id) -> <a href="./src/profound/types/organizations/category_topics_response.py">CategoryTopicsResponse</a></code>
- <code title="patch /v1/org/categories/{category_id}/prompts/status">client.organizations.categories.<a href="./src/profound/resources/organizations/categories.py">update_prompt_status</a>(category_id, \*\*<a href="src/profound/types/organizations/category_update_prompt_status_params.py">params</a>) -> <a href="./src/profound/types/organizations/category_update_prompt_status_response.py">CategoryUpdatePromptStatusResponse</a></code>
- <code title="patch /v1/org/categories/{category_id}/prompts">client.organizations.categories.<a href="./src/profound/resources/organizations/categories.py">update_prompts</a>(category_id, \*\*<a href="src/profound/types/organizations/category_update_prompts_params.py">params</a>) -> <a href="./src/profound/types/organizations/category_update_prompts_response.py">CategoryUpdatePromptsResponse</a></code>

# Prompts

Types:

```python
from profound.types import PromptAnswersResponse, PromptAnswersV2Response
```

Methods:

- <code title="post /v1/prompts/answers">client.prompts.<a href="./src/profound/resources/prompts.py">answers</a>(\*\*<a href="src/profound/types/prompt_answers_params.py">params</a>) -> <a href="./src/profound/types/prompt_answers_response.py">PromptAnswersResponse</a></code>
- <code title="post /v2/prompts/answers">client.prompts.<a href="./src/profound/resources/prompts.py">answers_v2</a>(\*\*<a href="src/profound/types/prompt_answers_v2_params.py">params</a>) -> <a href="./src/profound/types/prompt_answers_v2_response.py">PromptAnswersV2Response</a></code>
- <code title="post /v2/prompts/answers/stream">client.prompts.<a href="./src/profound/resources/prompts.py">stream_answers_v2</a>(\*\*<a href="src/profound/types/prompt_stream_answers_v2_params.py">params</a>) -> None</code>

# Reports

Types:

```python
from profound.types import (
    HostnameFilter,
    PromptIDFilter,
    ReportInfo,
    ReportResponse,
    ReportResult,
    RootDomainFilter,
    TagNameFilter,
    TopicNameFilter,
    URLFilter,
    ReportCitationsResponse,
    ReportQueryCitationsResponse,
    ReportQueryQueryFanoutsResponse,
    ReportQuerySentimentResponse,
    ReportQueryVisibilityResponse,
    ReportSentimentV2Response,
    ReportStreamCitationsResponse,
    ReportStreamSentimentResponse,
    ReportStreamVisibilityResponse,
)
```

Methods:

- <code title="post /v1/reports/citations">client.reports.<a href="./src/profound/resources/reports/reports.py">citations</a>(\*\*<a href="src/profound/types/report_citations_params.py">params</a>) -> <a href="./src/profound/types/report_citations_response.py">ReportCitationsResponse</a></code>
- <code title="post /v1/reports/bots">client.reports.<a href="./src/profound/resources/reports/reports.py">get_bots_report</a>(\*\*<a href="src/profound/types/report_get_bots_report_params.py">params</a>) -> <a href="./src/profound/types/report_response.py">ReportResponse</a></code>
- <code title="post /v2/reports/bots">client.reports.<a href="./src/profound/resources/reports/reports.py">get_bots_report_v2</a>(\*\*<a href="src/profound/types/report_get_bots_report_v2_params.py">params</a>) -> <a href="./src/profound/types/report_response.py">ReportResponse</a></code>
- <code title="post /v1/reports/referrals">client.reports.<a href="./src/profound/resources/reports/reports.py">get_referrals_report</a>(\*\*<a href="src/profound/types/report_get_referrals_report_params.py">params</a>) -> <a href="./src/profound/types/report_response.py">ReportResponse</a></code>
- <code title="post /v2/reports/referrals">client.reports.<a href="./src/profound/resources/reports/reports.py">get_referrals_report_v2</a>(\*\*<a href="src/profound/types/report_get_referrals_report_v2_params.py">params</a>) -> <a href="./src/profound/types/report_response.py">ReportResponse</a></code>
- <code title="post /v2/reports/citations">client.reports.<a href="./src/profound/resources/reports/reports.py">query_citations</a>(\*\*<a href="src/profound/types/report_query_citations_params.py">params</a>) -> <a href="./src/profound/types/report_query_citations_response.py">ReportQueryCitationsResponse</a></code>
- <code title="post /v1/reports/query-fanouts">client.reports.<a href="./src/profound/resources/reports/reports.py">query_fanouts</a>(\*\*<a href="src/profound/types/report_query_fanouts_params.py">params</a>) -> <a href="./src/profound/types/report_response.py">ReportResponse</a></code>
- <code title="post /v2/reports/query-fanouts">client.reports.<a href="./src/profound/resources/reports/reports.py">query_query_fanouts</a>(\*\*<a href="src/profound/types/report_query_query_fanouts_params.py">params</a>) -> <a href="./src/profound/types/report_query_query_fanouts_response.py">ReportQueryQueryFanoutsResponse</a></code>
- <code title="post /v2/reports/sentiment">client.reports.<a href="./src/profound/resources/reports/reports.py">query_sentiment</a>(\*\*<a href="src/profound/types/report_query_sentiment_params.py">params</a>) -> <a href="./src/profound/types/report_query_sentiment_response.py">ReportQuerySentimentResponse</a></code>
- <code title="post /v2/reports/visibility">client.reports.<a href="./src/profound/resources/reports/reports.py">query_visibility</a>(\*\*<a href="src/profound/types/report_query_visibility_params.py">params</a>) -> <a href="./src/profound/types/report_query_visibility_response.py">ReportQueryVisibilityResponse</a></code>
- <code title="post /v1/reports/sentiment">client.reports.<a href="./src/profound/resources/reports/reports.py">sentiment</a>(\*\*<a href="src/profound/types/report_sentiment_params.py">params</a>) -> <a href="./src/profound/types/report_response.py">ReportResponse</a></code>
- <code title="post /v1/reports/sentiment-v2">client.reports.<a href="./src/profound/resources/reports/reports.py">sentiment_v2</a>(\*\*<a href="src/profound/types/report_sentiment_v2_params.py">params</a>) -> <a href="./src/profound/types/report_sentiment_v2_response.py">ReportSentimentV2Response</a></code>
- <code title="post /v1/reports/citations/stream">client.reports.<a href="./src/profound/resources/reports/reports.py">stream_citations</a>(\*\*<a href="src/profound/types/report_stream_citations_params.py">params</a>) -> <a href="./src/profound/types/report_stream_citations_response.py">ReportStreamCitationsResponse</a></code>
- <code title="post /v2/reports/citations/stream">client.reports.<a href="./src/profound/resources/reports/reports.py">stream_citations_v2</a>(\*\*<a href="src/profound/types/report_stream_citations_v2_params.py">params</a>) -> None</code>
- <code title="post /v2/reports/query-fanouts/stream">client.reports.<a href="./src/profound/resources/reports/reports.py">stream_query_fanouts</a>(\*\*<a href="src/profound/types/report_stream_query_fanouts_params.py">params</a>) -> None</code>
- <code title="post /v1/reports/sentiment/stream">client.reports.<a href="./src/profound/resources/reports/reports.py">stream_sentiment</a>(\*\*<a href="src/profound/types/report_stream_sentiment_params.py">params</a>) -> <a href="./src/profound/types/report_stream_sentiment_response.py">ReportStreamSentimentResponse</a></code>
- <code title="post /v2/reports/sentiment/stream">client.reports.<a href="./src/profound/resources/reports/reports.py">stream_sentiment_v2</a>(\*\*<a href="src/profound/types/report_stream_sentiment_v2_params.py">params</a>) -> None</code>
- <code title="post /v1/reports/visibility/stream">client.reports.<a href="./src/profound/resources/reports/reports.py">stream_visibility</a>(\*\*<a href="src/profound/types/report_stream_visibility_params.py">params</a>) -> <a href="./src/profound/types/report_stream_visibility_response.py">ReportStreamVisibilityResponse</a></code>
- <code title="post /v2/reports/visibility/stream">client.reports.<a href="./src/profound/resources/reports/reports.py">stream_visibility_v2</a>(\*\*<a href="src/profound/types/report_stream_visibility_v2_params.py">params</a>) -> None</code>
- <code title="post /v1/reports/visibility">client.reports.<a href="./src/profound/resources/reports/reports.py">visibility</a>(\*\*<a href="src/profound/types/report_visibility_params.py">params</a>) -> <a href="./src/profound/types/report_response.py">ReportResponse</a></code>

## WebSearchResults

Types:

```python
from profound.types.reports import WebSearchResultQueryResponse, WebSearchResultStreamResponse
```

Methods:

- <code title="post /v1/reports/web-search-results">client.reports.web_search_results.<a href="./src/profound/resources/reports/web_search_results.py">query</a>(\*\*<a href="src/profound/types/reports/web_search_result_query_params.py">params</a>) -> <a href="./src/profound/types/reports/web_search_result_query_response.py">WebSearchResultQueryResponse</a></code>
- <code title="post /v1/reports/web-search-results/stream">client.reports.web_search_results.<a href="./src/profound/resources/reports/web_search_results.py">stream</a>(\*\*<a href="src/profound/types/reports/web_search_result_stream_params.py">params</a>) -> <a href="./src/profound/types/reports/web_search_result_stream_response.py">WebSearchResultStreamResponse</a></code>

## Shopping

Types:

```python
from profound.types.reports import (
    BrandNameFilter,
    MerchantNameFilter,
    ProductNameFilter,
    ShoppingAllItemsWithMerchantsResponse,
    ShoppingExecutionsResponse,
    ShoppingItemVisibilityResponse,
    ShoppingMerchantByItemsResponse,
    ShoppingMerchantDistributionResponse,
    ShoppingMerchantShareResponse,
    ShoppingMerchantVisibilityByBrandResponse,
    ShoppingProductMerchantURLsResponse,
    ShoppingTriggerRateResponse,
    ShoppingVisibilityResponse,
)
```

Methods:

- <code title="post /v1/reports/shopping/all-items-with-merchants">client.reports.shopping.<a href="./src/profound/resources/reports/shopping.py">all_items_with_merchants</a>(\*\*<a href="src/profound/types/reports/shopping_all_items_with_merchants_params.py">params</a>) -> <a href="./src/profound/types/reports/shopping_all_items_with_merchants_response.py">ShoppingAllItemsWithMerchantsResponse</a></code>
- <code title="post /v1/reports/shopping/executions">client.reports.shopping.<a href="./src/profound/resources/reports/shopping.py">executions</a>(\*\*<a href="src/profound/types/reports/shopping_executions_params.py">params</a>) -> <a href="./src/profound/types/reports/shopping_executions_response.py">ShoppingExecutionsResponse</a></code>
- <code title="post /v1/reports/shopping/item-visibility">client.reports.shopping.<a href="./src/profound/resources/reports/shopping.py">item_visibility</a>(\*\*<a href="src/profound/types/reports/shopping_item_visibility_params.py">params</a>) -> <a href="./src/profound/types/reports/shopping_item_visibility_response.py">ShoppingItemVisibilityResponse</a></code>
- <code title="post /v1/reports/shopping/merchant-by-items">client.reports.shopping.<a href="./src/profound/resources/reports/shopping.py">merchant_by_items</a>(\*\*<a href="src/profound/types/reports/shopping_merchant_by_items_params.py">params</a>) -> <a href="./src/profound/types/reports/shopping_merchant_by_items_response.py">ShoppingMerchantByItemsResponse</a></code>
- <code title="post /v1/reports/shopping/merchant-distribution">client.reports.shopping.<a href="./src/profound/resources/reports/shopping.py">merchant_distribution</a>(\*\*<a href="src/profound/types/reports/shopping_merchant_distribution_params.py">params</a>) -> <a href="./src/profound/types/reports/shopping_merchant_distribution_response.py">ShoppingMerchantDistributionResponse</a></code>
- <code title="post /v1/reports/shopping/merchant-share">client.reports.shopping.<a href="./src/profound/resources/reports/shopping.py">merchant_share</a>(\*\*<a href="src/profound/types/reports/shopping_merchant_share_params.py">params</a>) -> <a href="./src/profound/types/reports/shopping_merchant_share_response.py">ShoppingMerchantShareResponse</a></code>
- <code title="post /v1/reports/shopping/merchant-visibility-by-brand">client.reports.shopping.<a href="./src/profound/resources/reports/shopping.py">merchant_visibility_by_brand</a>(\*\*<a href="src/profound/types/reports/shopping_merchant_visibility_by_brand_params.py">params</a>) -> <a href="./src/profound/types/reports/shopping_merchant_visibility_by_brand_response.py">ShoppingMerchantVisibilityByBrandResponse</a></code>
- <code title="post /v1/reports/shopping/product-merchant-urls">client.reports.shopping.<a href="./src/profound/resources/reports/shopping.py">product_merchant_urls</a>(\*\*<a href="src/profound/types/reports/shopping_product_merchant_urls_params.py">params</a>) -> <a href="./src/profound/types/reports/shopping_product_merchant_urls_response.py">ShoppingProductMerchantURLsResponse</a></code>
- <code title="post /v1/reports/shopping/trigger-rate">client.reports.shopping.<a href="./src/profound/resources/reports/shopping.py">trigger_rate</a>(\*\*<a href="src/profound/types/reports/shopping_trigger_rate_params.py">params</a>) -> <a href="./src/profound/types/reports/shopping_trigger_rate_response.py">ShoppingTriggerRateResponse</a></code>
- <code title="post /v1/reports/shopping/visibility">client.reports.shopping.<a href="./src/profound/resources/reports/shopping.py">visibility</a>(\*\*<a href="src/profound/types/reports/shopping_visibility_params.py">params</a>) -> <a href="./src/profound/types/reports/shopping_visibility_response.py">ShoppingVisibilityResponse</a></code>

## Accuracy

Types:

```python
from profound.types.reports import (
    AccuracyCreateBreakdownResponse,
    AccuracyCreateCitationAnalysisResponse,
    AccuracyCreateClaimBreakdownResponse,
    AccuracyCreateClaimCitationsResponse,
    AccuracyCreateClusterExampleRunsResponse,
    AccuracyCreateClusterVerificationPairsResponse,
    AccuracyCreateFactcheckSetupStatusResponse,
    AccuracyCreateInaccuracyDriversResponse,
    AccuracyCreateInaccurateClustersResponse,
    AccuracyCreateInaccurateThemesResponse,
    AccuracyCreateOverviewResponse,
    AccuracyCreateTopInaccurateClaimsResponse,
    AccuracyCreateTopicIDsResponse,
)
```

Methods:

- <code title="post /v1/reports/accuracy/breakdown">client.reports.accuracy.<a href="./src/profound/resources/reports/accuracy.py">create_breakdown</a>(\*\*<a href="src/profound/types/reports/accuracy_create_breakdown_params.py">params</a>) -> <a href="./src/profound/types/reports/accuracy_create_breakdown_response.py">AccuracyCreateBreakdownResponse</a></code>
- <code title="post /v1/reports/accuracy/citation-analysis">client.reports.accuracy.<a href="./src/profound/resources/reports/accuracy.py">create_citation_analysis</a>(\*\*<a href="src/profound/types/reports/accuracy_create_citation_analysis_params.py">params</a>) -> <a href="./src/profound/types/reports/accuracy_create_citation_analysis_response.py">AccuracyCreateCitationAnalysisResponse</a></code>
- <code title="post /v1/reports/accuracy/claim-breakdown">client.reports.accuracy.<a href="./src/profound/resources/reports/accuracy.py">create_claim_breakdown</a>(\*\*<a href="src/profound/types/reports/accuracy_create_claim_breakdown_params.py">params</a>) -> <a href="./src/profound/types/reports/accuracy_create_claim_breakdown_response.py">AccuracyCreateClaimBreakdownResponse</a></code>
- <code title="post /v1/reports/accuracy/claim-citations">client.reports.accuracy.<a href="./src/profound/resources/reports/accuracy.py">create_claim_citations</a>(\*\*<a href="src/profound/types/reports/accuracy_create_claim_citations_params.py">params</a>) -> <a href="./src/profound/types/reports/accuracy_create_claim_citations_response.py">AccuracyCreateClaimCitationsResponse</a></code>
- <code title="post /v1/reports/accuracy/cluster-example-runs">client.reports.accuracy.<a href="./src/profound/resources/reports/accuracy.py">create_cluster_example_runs</a>(\*\*<a href="src/profound/types/reports/accuracy_create_cluster_example_runs_params.py">params</a>) -> <a href="./src/profound/types/reports/accuracy_create_cluster_example_runs_response.py">AccuracyCreateClusterExampleRunsResponse</a></code>
- <code title="post /v1/reports/accuracy/cluster-verification-pairs">client.reports.accuracy.<a href="./src/profound/resources/reports/accuracy.py">create_cluster_verification_pairs</a>(\*\*<a href="src/profound/types/reports/accuracy_create_cluster_verification_pairs_params.py">params</a>) -> <a href="./src/profound/types/reports/accuracy_create_cluster_verification_pairs_response.py">AccuracyCreateClusterVerificationPairsResponse</a></code>
- <code title="post /v1/reports/accuracy/factcheck-setup-status">client.reports.accuracy.<a href="./src/profound/resources/reports/accuracy.py">create_factcheck_setup_status</a>(\*\*<a href="src/profound/types/reports/accuracy_create_factcheck_setup_status_params.py">params</a>) -> <a href="./src/profound/types/reports/accuracy_create_factcheck_setup_status_response.py">AccuracyCreateFactcheckSetupStatusResponse</a></code>
- <code title="post /v1/reports/accuracy/inaccuracy-drivers">client.reports.accuracy.<a href="./src/profound/resources/reports/accuracy.py">create_inaccuracy_drivers</a>(\*\*<a href="src/profound/types/reports/accuracy_create_inaccuracy_drivers_params.py">params</a>) -> <a href="./src/profound/types/reports/accuracy_create_inaccuracy_drivers_response.py">AccuracyCreateInaccuracyDriversResponse</a></code>
- <code title="post /v1/reports/accuracy/inaccurate-clusters">client.reports.accuracy.<a href="./src/profound/resources/reports/accuracy.py">create_inaccurate_clusters</a>(\*\*<a href="src/profound/types/reports/accuracy_create_inaccurate_clusters_params.py">params</a>) -> <a href="./src/profound/types/reports/accuracy_create_inaccurate_clusters_response.py">AccuracyCreateInaccurateClustersResponse</a></code>
- <code title="post /v1/reports/accuracy/inaccurate-themes">client.reports.accuracy.<a href="./src/profound/resources/reports/accuracy.py">create_inaccurate_themes</a>(\*\*<a href="src/profound/types/reports/accuracy_create_inaccurate_themes_params.py">params</a>) -> <a href="./src/profound/types/reports/accuracy_create_inaccurate_themes_response.py">AccuracyCreateInaccurateThemesResponse</a></code>
- <code title="post /v1/reports/accuracy/overview">client.reports.accuracy.<a href="./src/profound/resources/reports/accuracy.py">create_overview</a>(\*\*<a href="src/profound/types/reports/accuracy_create_overview_params.py">params</a>) -> <a href="./src/profound/types/reports/accuracy_create_overview_response.py">AccuracyCreateOverviewResponse</a></code>
- <code title="post /v1/reports/accuracy/top-inaccurate-claims">client.reports.accuracy.<a href="./src/profound/resources/reports/accuracy.py">create_top_inaccurate_claims</a>(\*\*<a href="src/profound/types/reports/accuracy_create_top_inaccurate_claims_params.py">params</a>) -> <a href="./src/profound/types/reports/accuracy_create_top_inaccurate_claims_response.py">AccuracyCreateTopInaccurateClaimsResponse</a></code>
- <code title="post /v1/reports/accuracy/topic-ids">client.reports.accuracy.<a href="./src/profound/resources/reports/accuracy.py">create_topic_ids</a>(\*\*<a href="src/profound/types/reports/accuracy_create_topic_ids_params.py">params</a>) -> <a href="./src/profound/types/reports/accuracy_create_topic_ids_response.py">AccuracyCreateTopicIDsResponse</a></code>

# Logs

## Raw

Types:

```python
from profound.types.logs import RawBotsResponse, RawLogsResponse
```

Methods:

- <code title="post /v1/logs/raw/bots">client.logs.raw.<a href="./src/profound/resources/logs/raw.py">bots</a>(\*\*<a href="src/profound/types/logs/raw_bots_params.py">params</a>) -> <a href="./src/profound/types/logs/raw_bots_response.py">RawBotsResponse</a></code>
- <code title="post /v1/logs/raw">client.logs.raw.<a href="./src/profound/resources/logs/raw.py">logs</a>(\*\*<a href="src/profound/types/logs/raw_logs_params.py">params</a>) -> <a href="./src/profound/types/logs/raw_logs_response.py">RawLogsResponse</a></code>

# Content

## Optimization

Types:

```python
from profound.types.content import OptimizationRetrieveResponse, OptimizationListResponse
```

Methods:

- <code title="get /v1/content/{asset_id}/optimization/{content_id}">client.content.optimization.<a href="./src/profound/resources/content/optimization.py">retrieve</a>(content_id, \*, asset_id) -> <a href="./src/profound/types/content/optimization_retrieve_response.py">OptimizationRetrieveResponse</a></code>
- <code title="get /v1/content/{asset_id}/optimization">client.content.optimization.<a href="./src/profound/resources/content/optimization.py">list</a>(asset_id, \*\*<a href="src/profound/types/content/optimization_list_params.py">params</a>) -> <a href="./src/profound/types/content/optimization_list_response.py">OptimizationListResponse</a></code>

# Agents

Types:

```python
from profound.types import (
    AgentCreateResponse,
    AgentRetrieveResponse,
    AgentUpdateResponse,
    AgentListResponse,
    AgentPublishResponse,
    AgentRetrieveGraphResponse,
)
```

Methods:

- <code title="post /v1/agents">client.agents.<a href="./src/profound/resources/agents/agents.py">create</a>(\*\*<a href="src/profound/types/agent_create_params.py">params</a>) -> <a href="./src/profound/types/agent_create_response.py">AgentCreateResponse</a></code>
- <code title="get /v1/agents/{agent_id}">client.agents.<a href="./src/profound/resources/agents/agents.py">retrieve</a>(agent_id, \*\*<a href="src/profound/types/agent_retrieve_params.py">params</a>) -> <a href="./src/profound/types/agent_retrieve_response.py">AgentRetrieveResponse</a></code>
- <code title="patch /v1/agents/{agent_id}">client.agents.<a href="./src/profound/resources/agents/agents.py">update</a>(agent_id, \*\*<a href="src/profound/types/agent_update_params.py">params</a>) -> <a href="./src/profound/types/agent_update_response.py">AgentUpdateResponse</a></code>
- <code title="get /v1/agents">client.agents.<a href="./src/profound/resources/agents/agents.py">list</a>(\*\*<a href="src/profound/types/agent_list_params.py">params</a>) -> <a href="./src/profound/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="post /v1/agents/{agent_id}/publish">client.agents.<a href="./src/profound/resources/agents/agents.py">publish</a>(agent_id) -> <a href="./src/profound/types/agent_publish_response.py">AgentPublishResponse</a></code>
- <code title="get /v1/agents/{agent_id}/graph">client.agents.<a href="./src/profound/resources/agents/agents.py">retrieve_graph</a>(agent_id, \*\*<a href="src/profound/types/agent_retrieve_graph_params.py">params</a>) -> <a href="./src/profound/types/agent_retrieve_graph_response.py">AgentRetrieveGraphResponse</a></code>

## Runs

Types:

```python
from profound.types.agents import RunCreateResponse, RunRetrieveResponse
```

Methods:

- <code title="post /v1/agents/{agent_id}/runs">client.agents.runs.<a href="./src/profound/resources/agents/runs.py">create</a>(agent_id, \*\*<a href="src/profound/types/agents/run_create_params.py">params</a>) -> <a href="./src/profound/types/agents/run_create_response.py">RunCreateResponse</a></code>
- <code title="get /v1/agents/{agent_id}/runs/{run_id}">client.agents.runs.<a href="./src/profound/resources/agents/runs.py">retrieve</a>(run_id, \*, agent_id) -> <a href="./src/profound/types/agents/run_retrieve_response.py">RunRetrieveResponse</a></code>

## NodeTypes

Types:

```python
from profound.types.agents import NodeTypeListResponse, NodeTypeRetrieveSchemaResponse
```

Methods:

- <code title="get /v1/agents/node-types">client.agents.node_types.<a href="./src/profound/resources/agents/node_types.py">list</a>() -> <a href="./src/profound/types/agents/node_type_list_response.py">NodeTypeListResponse</a></code>
- <code title="get /v1/agents/node-types/{node_type}/schema">client.agents.node_types.<a href="./src/profound/resources/agents/node_types.py">retrieve_schema</a>(node_type) -> <a href="./src/profound/types/agents/node_type_retrieve_schema_response.py">NodeTypeRetrieveSchemaResponse</a></code>

# KnowledgeBases

Types:

```python
from profound.types import KnowledgeBaseListResponse, KnowledgeBaseSearchResponse
```

Methods:

- <code title="get /v1/knowledge-bases">client.knowledge_bases.<a href="./src/profound/resources/knowledge_bases/knowledge_bases.py">list</a>(\*\*<a href="src/profound/types/knowledge_base_list_params.py">params</a>) -> <a href="./src/profound/types/knowledge_base_list_response.py">KnowledgeBaseListResponse</a></code>
- <code title="post /v1/knowledge-bases/{knowledge_base_id}/search">client.knowledge_bases.<a href="./src/profound/resources/knowledge_bases/knowledge_bases.py">search</a>(knowledge_base_id, \*\*<a href="src/profound/types/knowledge_base_search_params.py">params</a>) -> <a href="./src/profound/types/knowledge_base_search_response.py">KnowledgeBaseSearchResponse</a></code>

## Documents

Types:

```python
from profound.types.knowledge_bases import (
    DocumentCreateResponse,
    DocumentUpdateResponse,
    DocumentDeleteResponse,
)
```

Methods:

- <code title="post /v1/knowledge-bases/{knowledge_base_id}/documents">client.knowledge_bases.documents.<a href="./src/profound/resources/knowledge_bases/documents.py">create</a>(knowledge_base_id, \*\*<a href="src/profound/types/knowledge_bases/document_create_params.py">params</a>) -> <a href="./src/profound/types/knowledge_bases/document_create_response.py">DocumentCreateResponse</a></code>
- <code title="put /v1/knowledge-bases/{knowledge_base_id}/documents">client.knowledge_bases.documents.<a href="./src/profound/resources/knowledge_bases/documents.py">update</a>(knowledge_base_id, \*\*<a href="src/profound/types/knowledge_bases/document_update_params.py">params</a>) -> <a href="./src/profound/types/knowledge_bases/document_update_response.py">DocumentUpdateResponse</a></code>
- <code title="delete /v1/knowledge-bases/{knowledge_base_id}/documents">client.knowledge_bases.documents.<a href="./src/profound/resources/knowledge_bases/documents.py">delete</a>(knowledge_base_id, \*\*<a href="src/profound/types/knowledge_bases/document_delete_params.py">params</a>) -> <a href="./src/profound/types/knowledge_bases/document_delete_response.py">DocumentDeleteResponse</a></code>

## Folders

Types:

```python
from profound.types.knowledge_bases import FolderCreateResponse, FolderDeleteResponse
```

Methods:

- <code title="post /v1/knowledge-bases/{knowledge_base_id}/folders">client.knowledge_bases.folders.<a href="./src/profound/resources/knowledge_bases/folders.py">create</a>(knowledge_base_id, \*\*<a href="src/profound/types/knowledge_bases/folder_create_params.py">params</a>) -> <a href="./src/profound/types/knowledge_bases/folder_create_response.py">FolderCreateResponse</a></code>
- <code title="delete /v1/knowledge-bases/{knowledge_base_id}/folders">client.knowledge_bases.folders.<a href="./src/profound/resources/knowledge_bases/folders.py">delete</a>(knowledge_base_id, \*\*<a href="src/profound/types/knowledge_bases/folder_delete_params.py">params</a>) -> <a href="./src/profound/types/knowledge_bases/folder_delete_response.py">FolderDeleteResponse</a></code>
