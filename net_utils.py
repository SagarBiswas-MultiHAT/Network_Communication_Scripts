import argparse
import ipaddress
import socket
from typing import Optional


def parse_port(value: str) -> Optional[int]:
    try:
        port = int(value.strip())
        if 1 <= port <= 65535:
            return port
    except Exception:
        pass
    return None


def resolve_host(value: str) -> Optional[str]:
    host = value.strip()
    if not host:
        return None
    try:
        ipaddress.ip_address(host)
        return host
    except ValueError:
        try:
            socket.getaddrinfo(host, None)
            return host
        except Exception:
            return None


def prompt_for_port(prompt: str) -> int:
    port_str = input(prompt)
    port = parse_port(port_str)
    if port is None:
        raise ValueError("Invalid port number. Please enter a number between 1 and 65535.")
    return port


def prompt_for_host(prompt: str) -> str:
    host = input(prompt).strip()
    resolved = resolve_host(host)
    if resolved is None:
        raise ValueError("Invalid host or IP address.")
    return resolved


def add_common_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--port",
        type=int,
        help="TCP port (1-65535). If omitted, prompts interactively.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=0.0,
        help="Socket timeout in seconds (0 = blocking).",
    )
    parser.add_argument(
        "--tls",
        action="store_true",
        help="Enable TLS. Requires --cert and --key.",
    )
    parser.add_argument("--cert", type=str, help="Path to TLS certificate (PEM).")
    parser.add_argument("--key", type=str, help="Path to TLS private key (PEM).")
    parser.add_argument(
        "--tls-insecure",
        action="store_true",
        help="Disable TLS certificate verification (use only for local testing).",
    )


def validate_port_arg(value: Optional[int]) -> Optional[int]:
    if value is None:
        return None
    if 1 <= value <= 65535:
        return value
    raise ValueError("Invalid port number. Please enter a number between 1 and 65535.")


def validate_timeout(value: float) -> float:
    if value < 0:
        raise ValueError("Timeout must be >= 0.")
    return value
