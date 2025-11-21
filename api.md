# Shared Types

```python
from profound.types import Pagination
```

# Organizations

Types:

```python
from profound.types import (
    OrganizationDomainsResponse,
    OrganizationListAssetsResponse,
    OrganizationModelsResponse,
    OrganizationRegionsResponse,
)
```

Methods:

- <code title="get /v1/org/domains">client.organizations.<a href="./src/profound/resources/organizations/organizations.py">domains</a>() -> <a href="./src/profound/types/organization_domains_response.py">OrganizationDomainsResponse</a></code>
- <code title="get /v1/org/assets">client.organizations.<a href="./src/profound/resources/organizations/organizations.py">list_assets</a>() -> <a href="./src/profound/types/organization_list_assets_response.py">OrganizationListAssetsResponse</a></code>
- <code title="get /v1/org/models">client.organizations.<a href="./src/profound/resources/organizations/organizations.py">models</a>() -> <a href="./src/profound/types/organization_models_response.py">OrganizationModelsResponse</a></code>
- <code title="get /v1/org/regions">client.organizations.<a href="./src/profound/resources/organizations/organizations.py">regions</a>() -> <a href="./src/profound/types/organization_regions_response.py">OrganizationRegionsResponse</a></code>

## Categories

Types:

```python
from profound.types.organizations import (
    OrgItem,
    CategoryListResponse,
    CategoryAssetsResponse,
    CategoryPromptsResponse,
    CategoryTagsResponse,
    CategoryTopicsResponse,
)
```

Methods:

- <code title="get /v1/org/categories">client.organizations.categories.<a href="./src/profound/resources/organizations/categories.py">list</a>() -> <a href="./src/profound/types/organizations/category_list_response.py">CategoryListResponse</a></code>
- <code title="get /v1/org/categories/{category_id}/assets">client.organizations.categories.<a href="./src/profound/resources/organizations/categories.py">assets</a>(category_id) -> <a href="./src/profound/types/organizations/category_assets_response.py">CategoryAssetsResponse</a></code>
- <code title="get /v1/org/categories/{category_id}/prompts">client.organizations.categories.<a href="./src/profound/resources/organizations/categories.py">prompts</a>(category_id) -> <a href="./src/profound/types/organizations/category_prompts_response.py">CategoryPromptsResponse</a></code>
- <code title="get /v1/org/categories/{category_id}/tags">client.organizations.categories.<a href="./src/profound/resources/organizations/categories.py">tags</a>(category_id) -> <a href="./src/profound/types/organizations/category_tags_response.py">CategoryTagsResponse</a></code>
- <code title="get /v1/org/categories/{category_id}/topics">client.organizations.categories.<a href="./src/profound/resources/organizations/categories.py">topics</a>(category_id) -> <a href="./src/profound/types/organizations/category_topics_response.py">CategoryTopicsResponse</a></code>

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
from profound.types import ReportInfo, ReportResponse, ReportResult, ReportCitationsResponse
```

Methods:

- <code title="post /v1/reports/citations">client.reports.<a href="./src/profound/resources/reports.py">citations</a>(\*\*<a href="src/profound/types/report_citations_params.py">params</a>) -> <a href="./src/profound/types/report_citations_response.py">ReportCitationsResponse</a></code>
- <code title="post /v1/reports/sentiment">client.reports.<a href="./src/profound/resources/reports.py">sentiment</a>(\*\*<a href="src/profound/types/report_sentiment_params.py">params</a>) -> <a href="./src/profound/types/report_response.py">ReportResponse</a></code>
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
