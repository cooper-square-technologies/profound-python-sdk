# Shared Types

```python
from profound.types import (
    AnalysisTypeFilter,
    AssetIDFilter,
    AssetNameFilter,
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
- <code title="get /v1/org/categories/{category_id}/tags">client.organizations.categories.<a href="./src/profound/resources/organizations/categories.py">tags</a>(category_id) -> <a href="./src/profound/types/organizations/category_tags_response.py">CategoryTagsResponse</a></code>
- <code title="get /v1/org/categories/{category_id}/topics">client.organizations.categories.<a href="./src/profound/resources/organizations/categories.py">topics</a>(category_id) -> <a href="./src/profound/types/organizations/category_topics_response.py">CategoryTopicsResponse</a></code>
- <code title="patch /v1/org/categories/{category_id}/prompts/status">client.organizations.categories.<a href="./src/profound/resources/organizations/categories.py">update_prompt_status</a>(category_id, \*\*<a href="src/profound/types/organizations/category_update_prompt_status_params.py">params</a>) -> <a href="./src/profound/types/organizations/category_update_prompt_status_response.py">CategoryUpdatePromptStatusResponse</a></code>
- <code title="patch /v1/org/categories/{category_id}/prompts">client.organizations.categories.<a href="./src/profound/resources/organizations/categories.py">update_prompts</a>(category_id, \*\*<a href="src/profound/types/organizations/category_update_prompts_params.py">params</a>) -> <a href="./src/profound/types/organizations/category_update_prompts_response.py">CategoryUpdatePromptsResponse</a></code>

# Prompts

Types:

```python
from profound.types import PromptAnswersResponse
```

Methods:

- <code title="post /v1/prompts/answers">client.prompts.<a href="./src/profound/resources/prompts.py">answers</a>(\*\*<a href="src/profound/types/prompt_answers_params.py">params</a>) -> <a href="./src/profound/types/prompt_answers_response.py">PromptAnswersResponse</a></code>

# Reports

Types:

```python
from profound.types import (
    PromptIDFilter,
    ReportInfo,
    ReportResponse,
    ReportResult,
    TagNameFilter,
    TopicNameFilter,
    ReportCitationsResponse,
    ReportStreamCitationsResponse,
    ReportStreamSentimentResponse,
    ReportStreamVisibilityResponse,
)
```

Methods:

- <code title="post /v1/reports/citations">client.reports.<a href="./src/profound/resources/reports.py">citations</a>(\*\*<a href="src/profound/types/report_citations_params.py">params</a>) -> <a href="./src/profound/types/report_citations_response.py">ReportCitationsResponse</a></code>
- <code title="post /v1/reports/bots">client.reports.<a href="./src/profound/resources/reports.py">get_bots_report</a>(\*\*<a href="src/profound/types/report_get_bots_report_params.py">params</a>) -> <a href="./src/profound/types/report_response.py">ReportResponse</a></code>
- <code title="post /v2/reports/bots">client.reports.<a href="./src/profound/resources/reports.py">get_bots_report_v2</a>(\*\*<a href="src/profound/types/report_get_bots_report_v2_params.py">params</a>) -> <a href="./src/profound/types/report_response.py">ReportResponse</a></code>
- <code title="post /v1/reports/referrals">client.reports.<a href="./src/profound/resources/reports.py">get_referrals_report</a>(\*\*<a href="src/profound/types/report_get_referrals_report_params.py">params</a>) -> <a href="./src/profound/types/report_response.py">ReportResponse</a></code>
- <code title="post /v2/reports/referrals">client.reports.<a href="./src/profound/resources/reports.py">get_referrals_report_v2</a>(\*\*<a href="src/profound/types/report_get_referrals_report_v2_params.py">params</a>) -> <a href="./src/profound/types/report_response.py">ReportResponse</a></code>
- <code title="post /v1/reports/query-fanouts">client.reports.<a href="./src/profound/resources/reports.py">query_fanouts</a>(\*\*<a href="src/profound/types/report_query_fanouts_params.py">params</a>) -> <a href="./src/profound/types/report_response.py">ReportResponse</a></code>
- <code title="post /v1/reports/sentiment">client.reports.<a href="./src/profound/resources/reports.py">sentiment</a>(\*\*<a href="src/profound/types/report_sentiment_params.py">params</a>) -> <a href="./src/profound/types/report_response.py">ReportResponse</a></code>
- <code title="post /v1/reports/citations/stream">client.reports.<a href="./src/profound/resources/reports.py">stream_citations</a>(\*\*<a href="src/profound/types/report_stream_citations_params.py">params</a>) -> <a href="./src/profound/types/report_stream_citations_response.py">ReportStreamCitationsResponse</a></code>
- <code title="post /v1/reports/sentiment/stream">client.reports.<a href="./src/profound/resources/reports.py">stream_sentiment</a>(\*\*<a href="src/profound/types/report_stream_sentiment_params.py">params</a>) -> <a href="./src/profound/types/report_stream_sentiment_response.py">ReportStreamSentimentResponse</a></code>
- <code title="post /v1/reports/visibility/stream">client.reports.<a href="./src/profound/resources/reports.py">stream_visibility</a>(\*\*<a href="src/profound/types/report_stream_visibility_params.py">params</a>) -> <a href="./src/profound/types/report_stream_visibility_response.py">ReportStreamVisibilityResponse</a></code>
- <code title="post /v1/reports/visibility">client.reports.<a href="./src/profound/resources/reports.py">visibility</a>(\*\*<a href="src/profound/types/report_visibility_params.py">params</a>) -> <a href="./src/profound/types/report_response.py">ReportResponse</a></code>

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
from profound.types import AgentRetrieveResponse, AgentListResponse
```

Methods:

- <code title="get /v1/agents/{agent_id}">client.agents.<a href="./src/profound/resources/agents/agents.py">retrieve</a>(agent_id, \*\*<a href="src/profound/types/agent_retrieve_params.py">params</a>) -> <a href="./src/profound/types/agent_retrieve_response.py">AgentRetrieveResponse</a></code>
- <code title="get /v1/agents">client.agents.<a href="./src/profound/resources/agents/agents.py">list</a>(\*\*<a href="src/profound/types/agent_list_params.py">params</a>) -> <a href="./src/profound/types/agent_list_response.py">AgentListResponse</a></code>

## Runs

Types:

```python
from profound.types.agents import RunCreateResponse, RunRetrieveResponse
```

Methods:

- <code title="post /v1/agents/{agent_id}/runs">client.agents.runs.<a href="./src/profound/resources/agents/runs.py">create</a>(agent_id, \*\*<a href="src/profound/types/agents/run_create_params.py">params</a>) -> <a href="./src/profound/types/agents/run_create_response.py">RunCreateResponse</a></code>
- <code title="get /v1/agents/{agent_id}/runs/{run_id}">client.agents.runs.<a href="./src/profound/resources/agents/runs.py">retrieve</a>(run_id, \*, agent_id) -> <a href="./src/profound/types/agents/run_retrieve_response.py">RunRetrieveResponse</a></code>

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
