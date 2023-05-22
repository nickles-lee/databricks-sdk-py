import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import settings

w = WorkspaceClient()

created = w.ip_access_lists.create(label=f'sdk-{time.time_ns()}',
                                   ip_addresses=["1.0.0.0/16"],
                                   list_type=settings.ListType.BLOCK)

# cleanup
w.ip_access_lists.delete(delete=created.ip_access_list.list_id)