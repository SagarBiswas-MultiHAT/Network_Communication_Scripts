import argparse
import socket
import ssl
import sys
import threading

from net_utils import (
    add_common_args,
    prompt_for_host,
    prompt_for_port,
    resolve_host,
    validate_port_arg,
    validate_timeout,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simple TCP client.")
    parser.add_argument(
        "--host",
        type=str,
        help="Server IP/hostname. If omitted, prompts interactively.",
    )
    add_common_args(parser)
    return parser.parse_args()


def wrap_tls_client(sock: socket.socket, host: str, insecure: bool) -> ssl.SSLSocket:
    if insecure:
        context = ssl._create_unverified_context()
        return context.wrap_socket(sock, server_hostname=host)
    context = ssl.create_default_context()
    return context.wrap_socket(sock, server_hostname=host)


def main() -> int:
    args = parse_args()
    try:
        port = validate_port_arg(args.port)
        timeout = validate_timeout(args.timeout)
    except ValueError as exc:
        print(str(exc))
        return 1

    host = None
    if args.host:
        host = resolve_host(args.host)
        if host is None:
            print("Invalid host or IP address.")
            return 1
    else:
        try:
            host = prompt_for_host("Enter the IP address of the server: ")
        except ValueError as exc:
            print(str(exc))
            return 1

    if port is None:
        try:
            port = prompt_for_port("Enter the port you want to connect to: ")
        except ValueError as exc:
            print(str(exc))
            return 1

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if timeout > 0:
        sock.settimeout(timeout)
    try:
        sock.connect((host, port))
    except Exception as exc:
        print(f"Could not connect to {host}:{port} — {exc}")
        return 1

    if args.tls:
        try:
            sock = wrap_tls_client(sock, host, args.tls_insecure)
        except Exception as exc:
            print(f"TLS handshake failed: {exc}")
            sock.close()
            return 1

    print(f"Connected to {host}:{port}")

    stop_event = threading.Event()

    def recv_loop() -> None:
        try:
            while not stop_event.is_set():
                data = sock.recv(4096)
                if not data:
                    print("\nConnection closed by remote host.")
                    stop_event.set()
                    break
                sys.stdout.write(data.decode(errors="replace"))
                sys.stdout.flush()
        except Exception as exc:
            if not stop_event.is_set():
                print(f"\nReceive error: {exc}")
                stop_event.set()

    def send_loop() -> None:
        try:
            while not stop_event.is_set():
                line = sys.stdin.readline()
                if not line:
                    stop_event.set()
                    break
                sock.sendall(line.encode())
        except Exception as exc:
            if not stop_event.is_set():
                print(f"\nSend error: {exc}")
                stop_event.set()

    recv_thread = threading.Thread(target=recv_loop, daemon=True)
    send_thread = threading.Thread(target=send_loop, daemon=True)
    recv_thread.start()
    send_thread.start()
    recv_thread.join()
    send_thread.join()

    sock.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
