"""Modbus TCP server: exposes Plant values as holding registers.

TODO:
- Load config/tags.yaml.
- Build a pymodbus server context with holding registers.
- Every second: plant.step(), then write round(value / scale) into each tag's address.
- Verify with your own raw-socket Modbus client.
"""

HOST = "127.0.0.1"
PORT = 5020  # non-privileged port; 502 needs admin rights


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
