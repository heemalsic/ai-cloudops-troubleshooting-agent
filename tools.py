from google.cloud import logging
import json


def read_logs(project_id):

    client = logging.Client(project=project_id)

    entries = client.list_entries(
        filter_='resource.type="cloud_run_revision"',
        order_by=logging.DESCENDING,
        page_size=10
    )

    logs = []

    for entry in entries:

        if hasattr(entry, "payload") and entry.payload:
            logs.append(str(entry.payload))

        elif hasattr(entry, "text_payload") and entry.text_payload:
            logs.append(entry.text_payload)

    return "\n".join(logs)


def analyze_metrics():

    metrics = {
        "cpu_usage": "45%",
        "memory_usage": "70%",
        "restart_count": 2
    }

    return json.dumps(metrics, indent=2)