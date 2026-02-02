import pytest

from net_utils import parse_port, resolve_host, validate_port_arg, validate_timeout


def test_parse_port_valid():
    assert parse_port("1") == 1
    assert parse_port("65535") == 65535
    assert parse_port(" 8080 ") == 8080


def test_parse_port_invalid():
    assert parse_port("0") is None
    assert parse_port("65536") is None
    assert parse_port("abc") is None


def test_resolve_host_valid_local():
    assert resolve_host("127.0.0.1") == "127.0.0.1"
    assert resolve_host("localhost") == "localhost"


def test_resolve_host_invalid():
    assert resolve_host("") is None
    assert resolve_host("invalid_host_###") is None


def test_validate_port_arg():
    assert validate_port_arg(80) == 80
    with pytest.raises(ValueError):
        validate_port_arg(0)


def test_validate_timeout():
    assert validate_timeout(0.0) == 0.0
    assert validate_timeout(2.5) == 2.5
    with pytest.raises(ValueError):
        validate_timeout(-1)
