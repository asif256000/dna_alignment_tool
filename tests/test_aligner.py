import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from src.aligner import DNAAligner


@pytest.fixture
def aligner():
    """Returns an instance of DNAAligner with default parameters."""
    return DNAAligner(match=2, mismatch=-1, gap=-2)


def test_smith_waterman(aligner):
    """Test Smith-Waterman local alignment algorithm."""
    seq1 = "ACTG"
    seq2 = "ACCG"

    score_matrix, max_score, max_pos = aligner.smith_waterman(seq1, seq2)

    assert isinstance(score_matrix, np.ndarray)
    assert max_score > 0
    assert max_pos is not None


def test_needleman_wunsch(aligner):
    """Test Needleman-Wunsch global alignment algorithm."""
    seq1 = "ACTG"
    seq2 = "ACCG"

    score_matrix = aligner.needleman_wunsch(seq1, seq2)

    assert isinstance(score_matrix, np.ndarray)
    assert score_matrix.shape == (len(seq1) + 1, len(seq2) + 1)


def test_traceback_smith_waterman(aligner):
    """Test Smith-Waterman traceback with proper expectations."""
    seq1 = "ACGTG"
    seq2 = "ACTG"

    score_matrix, _, _ = aligner.smith_waterman(seq1, seq2)
    aligned_seq1, aligned_seq2 = aligner.traceback_smith_waterman(score_matrix, seq1, seq2)

    # Ensure sequences are of equal length
    assert len(aligned_seq1) == len(aligned_seq2)

    # Check for expected alignment patterns
    assert aligned_seq1.replace("-", "") == seq1 or aligned_seq2.replace("-", "") == seq2


def test_traceback_needleman_wunsch(aligner):
    """Test Needleman-Wunsch traceback with proper expectations."""
    seq1 = "GATTACA"
    seq2 = "GCATGCU"

    score_matrix = aligner.needleman_wunsch(seq1, seq2)
    aligned_seq1, aligned_seq2 = aligner.traceback_needleman_wunsch(score_matrix, seq1, seq2)

    # Ensure sequences are of equal length
    assert len(aligned_seq1) == len(aligned_seq2)

    # Expected result should align completely
    assert aligned_seq1.replace("-", "") == seq1
    assert aligned_seq2.replace("-", "") == seq2
