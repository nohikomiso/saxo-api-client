"""Tests for packaged agent GUIDE."""

from pathlib import Path

from saxo_api_client.agent import read_guide, write_guide
from saxo_api_client.agent.__main__ import main


def test_read_guide_contains_saxoclient():
    text = read_guide()
    assert "SaxoClient" in text
    assert "SaxoTrader" in text  # mentioned as removed
    assert "Layer 3" in text


def test_write_guide_to_file(tmp_path: Path):
    out = write_guide(tmp_path / "out.md")
    assert out.is_file()
    assert "SaxoClient" in out.read_text(encoding="utf-8")


def test_write_guide_to_directory(tmp_path: Path):
    out = write_guide(tmp_path)
    assert out.name == "GUIDE.md"
    assert out.is_file()


def test_cli_agent_guide_stdout(capsys):
    assert main(["agent-guide"]) == 0
    captured = capsys.readouterr()
    assert "SaxoClient" in captured.out


def test_cli_default_no_args(capsys):
    assert main([]) == 0
    assert "SaxoClient" in capsys.readouterr().out
