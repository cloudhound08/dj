"""Tests for `notebookc` package."""
import pytest
from dj import dj


def test_convert(capsys):
    """Correct my_name argument prints"""
    dj.convert("Jill")
    captured = capsys.readouterr()
    assert "Jill" in captured.out