"""
Get all hosts for your organization returns "OK" response
DD_SITE="datadoghq.com" DD_API_KEY="418f0d142506a0a56b31b2d2a0e77676" DD_APP_KEY="674fb87bbe8e2a5e7c76b6111469c84404eec51c" python3 "example.py"
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = HostsApi(api_client)
    response = api_instance.list_hosts(
        filter="env:ci",
    )

    print(response)
