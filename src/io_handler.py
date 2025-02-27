import csv
import json

import numpy as np
import yaml


class IOHandler:
    @staticmethod
    def read_from_file(filename):
        """Reads DNA sequences from a file (JSON, YAML, or TXT)."""
        ext = filename.split(".")[-1].lower()

        if ext == "json":
            with open(filename, "r") as file:
                data = json.load(file)
            return data["seq1"], data["seq2"]

        elif ext in ["yml", "yaml"]:
            with open(filename, "r") as file:
                data = yaml.safe_load(file)
            return data["seq1"], data["seq2"]

        elif ext == "txt":
            with open(filename, "r") as file:
                lines = file.readlines()
            return lines[0].strip(), lines[1].strip()

        else:
            raise ValueError("Unsupported file format! Use JSON, YAML, or TXT.")

    @staticmethod
    def write_to_file(filename, score_matrix, file_format="txt"):
        """Writes alignment results to a file in TXT, CSV, or JSON format."""
        ext = filename.split(".")[-1].lower()

        if file_format == "txt" or ext == "txt":
            np.savetxt(filename, score_matrix, fmt="%d")

        elif file_format == "csv" or ext == "csv":
            with open(filename, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(score_matrix)

        elif file_format == "json" or ext == "json":
            with open(filename, "w") as file:
                json.dump({"alignment_matrix": score_matrix.tolist()}, file, indent=4)

        else:
            raise ValueError("Unsupported file format! Use TXT, CSV, or JSON.")
