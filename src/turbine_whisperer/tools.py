"""Agent tools. Read-only by default.

The agent gets exactly these. Writes go only through propose_setpoint,
which queues a change for a human to approve; it never writes directly.
"""


def read_tags() -> dict[str, dict]:
    """Return every tag's current value, units and alarm state."""
    raise NotImplementedError


def get_alarms() -> list[dict]:
    """Return active alarms: tag, level (high/high_high/low/low_low), value, limit."""
    raise NotImplementedError


def trend(tag: str, seconds: int) -> list[tuple[float, float]]:
    """Return (timestamp, value) samples for one tag over the last `seconds`."""
    raise NotImplementedError


def propose_setpoint(tag: str, value: float, reason: str) -> str:
    """Queue a setpoint change for human approval. Returns a proposal id. (Mission 1.)"""
    raise NotImplementedError
