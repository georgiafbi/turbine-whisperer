"""Agent loop: an LLM with tool calling, asked questions in a terminal.

TODO:
- Describe the tools in tools.py to the model (Claude or any model with tool calling).
- Loop: read a question, call the model, run requested tools, feed results back,
  print the plain-English answer.
- Log every tool call and answer to logs/ for replay.
"""

SYSTEM_PROMPT = (
    "You are TurbineWhisperer, an assistant watching a simulated gas turbine. "
    "Use the tools to read live values. Explain what you see in plain English. "
    "You cannot write to the plant; you may only propose changes for a human to approve."
)


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
