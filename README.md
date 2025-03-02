# DNA Sequence Alignment CLI Tool

## Overview

This tool provides DNA sequence alignment using **Smith-Waterman (local alignment)** and **Needleman-Wunsch (global alignment)** algorithms. It is implemented in Python with a modular design for efficiency, scalability, and ease of use.

## Features

- ✅ Supports **Smith-Waterman** (local) and **Needleman-Wunsch** (global) alignment.
- ✅ Takes **direct CLI input** or reads from **JSON/YAML/TXT** files.
- ✅ Saves alignment results to **output files**.
- ✅ Uses **NumPy** for fast computation.
- ✅ Modular structure for easy extension.

## Installation

Ensure you have Python installed, then install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### 1️⃣ Run with Direct Input

```bash
python main.py --seq1 "ACTG" --seq2 "ACTGG"
```

### 2️⃣ Run with File Input (JSON/YAML/TXT)

Create an input file (**input.json**):

```json
{
  "seq1": "ACTG",
  "seq2": "ACTGG"
}
```

Then run:

```bash
python main.py --file input.json
```

### 3️⃣ Choose Alignment Method

By default, it runs **Smith-Waterman**. To use **Needleman-Wunsch**, specify:

```bash
python main.py --seq1 "ACTG" --seq2 "ACTGG" --method needleman-wunsch
```

### 4️⃣ Save Results to File

```bash
python main.py --seq1 "ACTG" --seq2 "ACTGG" --output results.txt
```

### Usage Examples

<img width="388" height="388" alt="ss1" src="https://github.com/user-attachments/assets/2eb916bd-3560-40e9-b04c-5b0b08109ba6" />

<img width="388" height="388" alt="ss2" src="https://github.com/user-attachments/assets/06c54fc7-615f-4ec9-96b2-4682e4b8dfed" />


## Future Enhancements 🚀

- ⚡ Multi-threading for faster alignment
- 🔍 Support for **multi-sequence alignment**
- 📊 **Visualization** of alignment results

## License

This project is **open-source** under the MIT License.

---
