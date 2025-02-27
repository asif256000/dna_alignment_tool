import numpy as np


class DNAAligner:
    def __init__(self, match=2, mismatch=-1, gap=-2):
        """Initialize scoring parameters."""
        self.match = match
        self.mismatch = mismatch
        self.gap = gap

    def smith_waterman(self, seq1, seq2):
        """Performs Smith-Waterman local sequence alignment."""
        m, n = len(seq1), len(seq2)
        score_matrix = np.zeros((m + 1, n + 1))
        max_score, max_pos = 0, (0, 0)

        # Fill scoring matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                match_score = self.match if seq1[i - 1] == seq2[j - 1] else self.mismatch
                score_matrix[i, j] = max(
                    0,
                    score_matrix[i - 1, j - 1] + match_score,  # Match/Mismatch
                    score_matrix[i - 1, j] + self.gap,  # Gap in seq1
                    score_matrix[i, j - 1] + self.gap,  # Gap in seq2
                )
                if score_matrix[i, j] > max_score:
                    max_score = score_matrix[i, j]
                    max_pos = (i, j)

        return score_matrix, max_score, max_pos

    def needleman_wunsch(self, seq1, seq2):
        """Performs Needleman-Wunsch global sequence alignment."""
        m, n = len(seq1), len(seq2)
        score_matrix = np.zeros((m + 1, n + 1))

        # Initialize
        for i in range(m + 1):
            score_matrix[i, 0] = i * self.gap
        for j in range(n + 1):
            score_matrix[0, j] = j * self.gap

        # Fill scoring matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                match_score = self.match if seq1[i - 1] == seq2[j - 1] else self.mismatch
                score_matrix[i, j] = max(
                    score_matrix[i - 1, j - 1] + match_score,  # Match/Mismatch
                    score_matrix[i - 1, j] + self.gap,  # Gap in seq1
                    score_matrix[i, j - 1] + self.gap,  # Gap in seq2
                )

        return score_matrix
