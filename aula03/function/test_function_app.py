import json

import azure.functions as func

from function_app import health


def test_health_returns_200_and_ok_status():
    req = func.HttpRequest(
        method="GET",
        url="/api/health",
        body=None,
    )
    resp = health(req)

    assert resp.status_code == 200
    body = json.loads(resp.get_body())
    assert body["status"] == "ok"
