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

    def traceback_smith_waterman(self, score_matrix, seq1, seq2):
        """Traceback for Smith-Waterman to reconstruct aligned sequences."""
        alignment_seq1, alignment_seq2 = "", ""

        # Find the highest score position (starting point for traceback)
        i, j = np.unravel_index(np.argmax(score_matrix), score_matrix.shape)

        while i > 0 and j > 0 and score_matrix[i, j] > 0:
            current_score = score_matrix[i, j]
            diagonal = score_matrix[i - 1, j - 1] if i > 0 and j > 0 else 0
            up = score_matrix[i - 1, j] if i > 0 else 0

            if current_score == diagonal + (self.match if seq1[i - 1] == seq2[j - 1] else self.mismatch):
                alignment_seq1 = seq1[i - 1] + alignment_seq1
                alignment_seq2 = seq2[j - 1] + alignment_seq2
                i -= 1
                j -= 1
            elif current_score == up + self.gap:
                alignment_seq1 = seq1[i - 1] + alignment_seq1
                alignment_seq2 = "-" + alignment_seq2
                i -= 1
            else:
                alignment_seq1 = "-" + alignment_seq1
                alignment_seq2 = seq2[j - 1] + alignment_seq2
                j -= 1

        return alignment_seq1, alignment_seq2

    def traceback_needleman_wunsch(self, score_matrix, seq1, seq2):
        """Reconstructs the aligned sequences using traceback for Needleman-Wunsch."""
        i, j = len(seq1), len(seq2)
        alignment_seq1, alignment_seq2 = "", ""

        while i > 0 or j > 0:
            if (
                i > 0
                and j > 0
                and (
                    score_matrix[i, j]
                    == score_matrix[i - 1, j - 1] + (self.match if seq1[i - 1] == seq2[j - 1] else self.mismatch)
                )
            ):
                alignment_seq1 = seq1[i - 1] + alignment_seq1
                alignment_seq2 = seq2[j - 1] + alignment_seq2
                i -= 1
                j -= 1
            elif i > 0 and (score_matrix[i, j] == score_matrix[i - 1, j] + self.gap):
                alignment_seq1 = seq1[i - 1] + alignment_seq1
                alignment_seq2 = "-" + alignment_seq2
                i -= 1
            else:
                alignment_seq1 = "-" + alignment_seq1
                alignment_seq2 = seq2[j - 1] + alignment_seq2
                j -= 1

        return alignment_seq1, alignment_seq2
