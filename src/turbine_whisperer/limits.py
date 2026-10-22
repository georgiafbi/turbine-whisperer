"""Hard limits, enforced in plain code the model cannot change.

Every approved write passes through check() before it reaches Modbus.
An out-of-range value is rejected even if a human approved it.
"""

SETPOINT_LIMITS: dict[str, tuple[float, float]] = {
    "speed_setpoint_pct": (0.0, 102.0),
}


class LimitViolation(Exception):
    pass


def check(tag: str, value: float) -> None:
    if tag not in SETPOINT_LIMITS:
        raise LimitViolation(f"{tag} is not writable")
    lo, hi = SETPOINT_LIMITS[tag]
    if not lo <= value <= hi:
        raise LimitViolation(f"{tag}={value} outside [{lo}, {hi}]")
