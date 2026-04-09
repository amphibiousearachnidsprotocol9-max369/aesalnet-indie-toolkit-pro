from src.status import get_status

def test_status_schema():
    status = get_status()

    expected_keys = {
        "time",
        "cpu",
        "memory",
        "disk",
        "net_sent",
        "net_recv",
        "uptime_sec",
        "pid",
        "state",
    }

    assert expected_keys.issubset(status.keys())

def test_status_values():
    status = get_status()
    assert status["cpu"] >= 0
    assert status["memory"] >= 0
    assert status["disk"] >= 0
    assert status["uptime_sec"] >= 0
    assert status["state"] == "ONLINE"
