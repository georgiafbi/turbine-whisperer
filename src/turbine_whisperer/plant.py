"""Plant model: a tiny simulated gas turbine skid.

Yours to write (the plan says: no AI on this one).

Hints:
- Keep state for speed_pct, egt_degF, fuel_valve_pct, lube_oil_psi.
- Update once a second with simple first-order lags:
      x += (target - x) * dt / tau
- Fuel valve drives speed; speed and fuel drive EGT; speed drives lube oil pressure.
- Leave a hook for injecting faults (e.g. lube oil pressure drifting low).
"""


class Plant:
    def __init__(self) -> None:
        raise NotImplementedError("Write the plant model yourself.")

    def step(self, dt: float = 1.0) -> None:
        raise NotImplementedError

    def snapshot(self) -> dict[str, float]:
        """Return current engineering values keyed by tag name (see config/tags.yaml)."""
        raise NotImplementedError
