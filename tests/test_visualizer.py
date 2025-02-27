import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from src.visualizer import Visualizer


@pytest.fixture
def score_matrix():
    """Returns a sample alignment score matrix."""
    return np.array([[0, 2, 4], [2, 3, 5], [4, 5, 6]])


def test_print_colored_alignment(capsys):
    """Test colored alignment output (CLI)."""
    aligned_seq1 = "ACTG"
    aligned_seq2 = "AC-G"

    Visualizer.print_colored_alignment(aligned_seq1, aligned_seq2)
    captured = capsys.readouterr()

    assert "ACTG" in captured.out
    assert "AC-G" in captured.out


def test_print_ascii_heatmap(capsys, score_matrix):
    """Test ASCII heatmap visualization."""
    Visualizer.print_ascii_heatmap(score_matrix)
    captured = capsys.readouterr()

    assert " 2" in captured.out


def test_plot_heatmap(score_matrix):
    """Test Matplotlib heatmap (no assertion, just ensure no crash)."""
    Visualizer.plot_heatmap(score_matrix)
