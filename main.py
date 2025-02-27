import argparse

import pandas as pd

from src.aligner import DNAAligner
from src.config import CONFIG
from src.io_handler import IOHandler


def main():
    parser = argparse.ArgumentParser(description="DNA Sequence Alignment Tool")
    parser.add_argument("--seq1", type=str, help="First DNA sequence")
    parser.add_argument("--seq2", type=str, help="Second DNA sequence")
    parser.add_argument("--file", type=str, help="Input file (JSON, YAML, TXT)")
    parser.add_argument(
        "--method", choices=["smith-waterman", "needleman-wunsch"], default="smith-waterman", help="Alignment method"
    )
    parser.add_argument("--output", type=str, help="Output file for alignment results")

    args = parser.parse_args()

    # Get sequences from file or CLI
    if args.file:
        seq1, seq2 = IOHandler.read_from_file(args.file)
    elif args.seq1 and args.seq2:
        seq1, seq2 = args.seq1, args.seq2
    else:
        print("Error: Provide sequences via --seq1 and --seq2 or use --file")
        return

    # Initialize aligner
    aligner = DNAAligner(match=CONFIG["match"], mismatch=CONFIG["mismatch"], gap=CONFIG["gap"])

    # Perform alignment
    if args.method == "smith-waterman":
        score_matrix, max_score, max_pos = aligner.smith_waterman(seq1, seq2)
        print("\nAlignment Score Matrix:\n", pd.DataFrame(score_matrix))
        print("\nMaximum Alignment Score:", max_score)
        print("Max Score Position:", max_pos)
    else:
        score_matrix = aligner.needleman_wunsch(seq1, seq2)
        print("\nAlignment Score Matrix:\n", pd.DataFrame(score_matrix))

    # Save output if specified
    if args.output:
        IOHandler.write_to_file(args.output, score_matrix)
        print(f"Results saved to {args.output}")


if __name__ == "__main__":
    main()
