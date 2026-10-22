# TurbineWhisperer

**An AI agent that watches a simulated gas turbine skid over Modbus TCP, spots trouble, explains it in plain English, and only touches a setpoint after a human says yes.**

The plant is a small Python model (speed, EGT, fuel valve, lube oil pressure) exposed as Modbus holding registers. The agent reads those registers through a few narrow tools, reasons over them with an LLM, and proposes actions. A human approves or rejects every write.

## Architecture

```
READ PATH (agent uses freely)
  plant model ──▶ Modbus TCP server ──▶ tag map (YAML) ──▶ read-only tools ──▶ LLM agent ──▶ plain-English answer

GATED WRITE PATH (the only way back to the plant)
  agent ──▶ propose_setpoint ──▶ human y/n ──▶ hard limits (plain code) ──▶ Modbus write
                                     │                    │
                                     └──── audit log ◀────┘
```

## Guardrails

- **Read-only by default.** The agent gets `read_tags`, `get_alarms` and `trend`. A single `propose_setpoint` tool queues a change; nothing writes until a human approves.
- **Hard limits outside the AI.** Setpoint ranges and trip logic live in plain code (`limits.py`) the model cannot change.
- **Everything logged.** Each reading, proposal and approval goes to a file you can replay.
- **Simulated hardware only.** No real equipment. Generic physics and public knowledge only.

## Layout

```
config/tags.yaml                  register map: names, units, scaling, alarm limits (the agent's "P&ID")
src/turbine_whisperer/plant.py    plant model — first-order lags, updated once a second
src/turbine_whisperer/modbus_server.py   exposes plant values as holding registers (pymodbus)
src/turbine_whisperer/tools.py    read_tags, get_alarms, trend(tag, seconds)
src/turbine_whisperer/limits.py   hard setpoint limits, enforced in plain code
src/turbine_whisperer/agent.py    LLM tool-calling loop in a terminal
logs/                             audit logs (git-ignored)
```

## Quick start

```bash
python3.12 -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
python -m turbine_whisperer.modbus_server   # terminal 1
python -m turbine_whisperer.agent           # terminal 2 — ask "how's the turbine?"
```

## Roadmap

**First weekend**

- [ ] Plant model: speed, EGT, fuel valve %, lube oil pressure
- [ ] Modbus server with `pymodbus`, checked with a raw-socket client
- [ ] Tag map YAML
- [ ] Read-only agent tools
- [ ] Agent loop with LLM tool calling
- [ ] Inject a fault (lube oil pressure drifting low) and see if the agent catches it
- [ ] Paste one good Q&A below

**Next missions**

1. Human approval gate — `propose_setpoint`, queue, y/n prompt, hard limits
2. Fault library — EGT spread, sticking fuel valve, speed hunting, sensor flatline; score detection rate
3. Memory and logs — SQLite history, replayable audit log
4. Dashboard — live trends, agent notes, approve/reject buttons
5. Real wire — Arduino Modbus RTU slave over RS-485
6. OPC UA or MQTT
7. ROS 2 bridge
8. 2-minute demo video

## Sample Q&A

_Coming soon._

## License

MIT
