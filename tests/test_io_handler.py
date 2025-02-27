import json
import os
import sys

import numpy as np
import pytest
import yaml

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from src.io_handler import IOHandler


@pytest.fixture
def setup_test_files():
    """Create sample files for testing and clean up after."""
    json_file = "test_sequences.json"
    yaml_file = "test_sequences.yaml"
    txt_file = "test_sequences.txt"
    csv_file = "test_results.csv"
    json_output = "test_results.json"

    seq1, seq2 = "ACTG", "ACCG"

    with open(json_file, "w") as file:
        json.dump({"seq1": seq1, "seq2": seq2}, file)

    with open(yaml_file, "w") as file:
        yaml.dump({"seq1": seq1, "seq2": seq2}, file)

    with open(txt_file, "w") as file:
        file.write(f"{seq1}\n{seq2}")

    yield json_file, yaml_file, txt_file, csv_file, json_output, seq1, seq2

    # Cleanup
    for file in [json_file, yaml_file, txt_file, csv_file, json_output]:
        if os.path.exists(file):
            os.remove(file)


def test_read_from_json(setup_test_files):
    json_file, _, _, _, _, expected_seq1, expected_seq2 = setup_test_files
    seq1, seq2 = IOHandler.read_from_file(json_file)
    assert seq1 == expected_seq1
    assert seq2 == expected_seq2


def test_read_from_yaml(setup_test_files):
    _, yaml_file, _, _, _, expected_seq1, expected_seq2 = setup_test_files
    seq1, seq2 = IOHandler.read_from_file(yaml_file)
    assert seq1 == expected_seq1
    assert seq2 == expected_seq2


def test_read_from_txt(setup_test_files):
    _, _, txt_file, _, _, expected_seq1, expected_seq2 = setup_test_files
    seq1, seq2 = IOHandler.read_from_file(txt_file)
    assert seq1 == expected_seq1
    assert seq2 == expected_seq2


def test_write_and_read_csv(setup_test_files):
    """Test writing and reading from CSV file with correct order."""
    _, _, _, csv_file, _, _, _ = setup_test_files
    score_matrix = np.array([[1, 2], [3, 4]])

    IOHandler.write_to_file(csv_file, score_matrix, file_format="csv")

    with open(csv_file, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    assert lines[0] == "1,2"
    assert lines[1] == "3,4"


def test_write_and_read_json(setup_test_files):
    _, _, _, _, json_output, _, _ = setup_test_files
    score_matrix = np.array([[1, 2], [3, 4]])
    IOHandler.write_to_file(json_output, score_matrix, file_format="json")

    with open(json_output, "r") as file:
        data = json.load(file)
    assert data["alignment_matrix"] == [[1, 2], [3, 4]]
