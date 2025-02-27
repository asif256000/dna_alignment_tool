import matplotlib.pyplot as plt
from termcolor import colored


class Visualizer:
    @staticmethod
    def print_colored_alignment(seq1, seq2):
        """Prints the aligned sequences with color-coding in CLI."""
        aligned_str = ""
        for a, b in zip(seq1, seq2):
            if a == b:
                aligned_str += colored(a, "green")  # Match (Green)
            elif a == "-" or b == "-":
                aligned_str += colored(a if a != "-" else b, "yellow")  # Gaps (Yellow)
            else:
                aligned_str += colored(a, "red")  # Mismatch (Red)

        print("\nAlignment Result:")
        print("Seq1:", seq1)
        print("Seq2:", seq2)
        print("     ", aligned_str)

    @staticmethod
    def print_ascii_heatmap(score_matrix):
        """Prints an ASCII-based heatmap of the score matrix."""
        print("\nAlignment Score Matrix (Heatmap):")
        for row in score_matrix:
            print(" ".join(colored(f"{int(score):2}", "cyan") if score > 5 else f"{int(score):2}" for score in row))

    @staticmethod
    def plot_heatmap(score_matrix):
        """Plots the score matrix as a heatmap using Matplotlib."""
        plt.figure(figsize=(8, 6))
        plt.imshow(score_matrix, cmap="coolwarm", interpolation="nearest")
        plt.colorbar(label="Score")
        plt.title("Alignment Score Matrix")
        plt.show()
