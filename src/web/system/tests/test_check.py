import pytest
from src.web.system.modules.check import Check


def test_CheckPhone():
    assert Check.CheckPhone("7123123121s") is False
    assert Check.CheckPhone("899922233221") is False
    assert Check.CheckPhone("+79002003322") is True
