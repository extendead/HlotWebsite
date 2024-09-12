import pytest
from src.web.system.modules.hasher import Hasher


def test_hasher():
    hash_ = Hasher
    hash_pass = "scrypt:32768:8:1$wCOfQcx8595OfXar$6da2c441b889c984af66da15bce2549515b5c9807b09e65921c0ba018c02d19f6193b8a1957d64d5d352d5d185b3bd285249beb6e45809dfaf65eb39212086a2"
    check_pass = hash_.UnHashPassword(hash_pass, "1")
    assert check_pass is True
