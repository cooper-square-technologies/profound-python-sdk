# Org

Types:

```python
from profound.types import (
    OrgRetrieveDomainsResponse,
    OrgRetrieveModelsResponse,
    OrgRetrieveRegionsResponse,
)
```

Methods:

- <code title="get /v1/org/domains">client.org.<a href="./src/profound/resources/org/org.py">retrieve_domains</a>() -> <a href="./src/profound/types/org_retrieve_domains_response.py">OrgRetrieveDomainsResponse</a></code>
- <code title="get /v1/org/models">client.org.<a href="./src/profound/resources/org/org.py">retrieve_models</a>() -> <a href="./src/profound/types/org_retrieve_models_response.py">OrgRetrieveModelsResponse</a></code>
- <code title="get /v1/org/regions">client.org.<a href="./src/profound/resources/org/org.py">retrieve_regions</a>() -> <a href="./src/profound/types/org_retrieve_regions_response.py">OrgRetrieveRegionsResponse</a></code>

## Categories

Types:

```python
from profound.types.org import (
    OrgItem,
    CategoryListResponse,
    CategoryRetrievePromptsResponse,
    CategoryRetrieveTagsResponse,
    CategoryRetrieveTopicsResponse,
)
```

Methods:

- <code title="get /v1/org/categories">client.org.categories.<a href="./src/profound/resources/org/categories.py">list</a>() -> <a href="./src/profound/types/org/category_list_response.py">CategoryListResponse</a></code>
- <code title="get /v1/org/categories/{category_id}/prompts">client.org.categories.<a href="./src/profound/resources/org/categories.py">retrieve_prompts</a>(category_id) -> <a href="./src/profound/types/org/category_retrieve_prompts_response.py">CategoryRetrievePromptsResponse</a></code>
- <code title="get /v1/org/categories/{category_id}/tags">client.org.categories.<a href="./src/profound/resources/org/categories.py">retrieve_tags</a>(category_id) -> <a href="./src/profound/types/org/category_retrieve_tags_response.py">CategoryRetrieveTagsResponse</a></code>
- <code title="get /v1/org/categories/{category_id}/topics">client.org.categories.<a href="./src/profound/resources/org/categories.py">retrieve_topics</a>(category_id) -> <a href="./src/profound/types/org/category_retrieve_topics_response.py">CategoryRetrieveTopicsResponse</a></code>

# Prompts

Types:

```python
from profound.types import Pagination, PromptGetAnswersResponse
```

Methods:

- <code title="post /v1/prompts/answers">client.prompts.<a href="./src/profound/resources/prompts.py">get_answers</a>(\*\*<a href="src/profound/types/prompt_get_answers_params.py">params</a>) -> <a href="./src/profound/types/prompt_get_answers_response.py">PromptGetAnswersResponse</a></code>

# Reports

Types:

```python
from profound.types import Info, Response, Result, ReportQueryCitationsResponse
```

Methods:

- <code title="post /v1/reports/citations">client.reports.<a href="./src/profound/resources/reports.py">query_citations</a>(\*\*<a href="src/profound/types/report_query_citations_params.py">params</a>) -> <a href="./src/profound/types/report_query_citations_response.py">ReportQueryCitationsResponse</a></code>
- <code title="post /v1/reports/sentiment">client.reports.<a href="./src/profound/resources/reports.py">query_sentiment</a>(\*\*<a href="src/profound/types/report_query_sentiment_params.py">params</a>) -> <a href="./src/profound/types/response.py">Response</a></code>
- <code title="post /v1/reports/visibility">client.reports.<a href="./src/profound/resources/reports.py">query_visibility</a>(\*\*<a href="src/profound/types/report_query_visibility_params.py">params</a>) -> <a href="./src/profound/types/response.py">Response</a></code>

# Logs

## Raw

Types:

```python
from profound.types.logs import RawGetBotsResponse, RawGetLogsResponse
```

Methods:

- <code title="post /v1/logs/raw/bots">client.logs.raw.<a href="./src/profound/resources/logs/raw.py">get_bots</a>(\*\*<a href="src/profound/types/logs/raw_get_bots_params.py">params</a>) -> <a href="./src/profound/types/logs/raw_get_bots_response.py">RawGetBotsResponse</a></code>
- <code title="post /v1/logs/raw">client.logs.raw.<a href="./src/profound/resources/logs/raw.py">get_logs</a>(\*\*<a href="src/profound/types/logs/raw_get_logs_params.py">params</a>) -> <a href="./src/profound/types/logs/raw_get_logs_response.py">RawGetLogsResponse</a></code>
