# Conversational Urdu Speech & Chunked Multi-Script Dataset

![Dataset Status](https://img.shields.io/badge/Dataset-500%20Samples%20%2F%201%2C500%20Chunks-blue)
![Language](https://img.shields.io/badge/Language-Urdu%20%7C%20Roman%20Urdu-green)
![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen)
![Task](https://img.shields.io/badge/Task-ASR%20%26%20Speech%20Recognition-orange)

## 📌 Project Overview
This repository contains the architecture, data management scripts, transcription metadata, and structured layout for a **Conversational Urdu Speech Dataset**.

The dataset consists of **500 full 1-minute Urdu voice recordings**, divided into **3 contiguous 15-second chunks per sample**, yielding **1,500 chunk folders** in total. Each chunk is accompanied by UTF-8 encoded bilingual transcriptions (Urdu script and Roman Urdu).

---

## 📁 Repository & Dataset Structure

```text
urdu_voice_assignment/
├── README.md                           # Main repository documentation
├── ASSIGNMENT.md                       # Complete assignment specifications
├── .gitignore                          # Git ignore configuration
├── dataset/                            # Core dataset directory
│   ├── metadata.csv                    # Consolidated CSV metadata for 500 samples
│   ├── wavs/                           # Directory for master raw audio files (urdu_000001.wav - urdu_000500.wav)
│   ├── Sample1/                        # Sample 1 directory
│   │   ├── Chunk1/                     # Chunk 1 (0s - 15s)
│   │   │   ├── full_voice.wav          # Master 1-minute audio recording
│   │   │   ├── chunk.wav               # Sliced 15-second audio clip
│   │   │   └── metadata.json           # Chunk transcription (Urdu & Roman Urdu)
│   │   ├── Chunk2/                     # Chunk 2 (15s - 30s)
│   │   └── Chunk3/                     # Chunk 3 (30s - 45s)
│   ├── ...
│   └── Sample500/                      # Sample 500 directory
│       ├── Chunk1/
│       ├── Chunk2/
│       └── Chunk3/
└── scripts/                            # Python automation scripts
    ├── generate_dataset_structure.py   # Dataset folder & metadata generator
    ├── auto_split_recordings.py        # Automated audio slicer and file sorter
    └── validate_dataset_structure.py   # Automated QA & validation script
```

---

## 📊 Dataset Specifications

| Metric | Specification |
| :--- | :--- |
| **Total Voice Samples** | 500 Samples (`Sample1` – `Sample500`) |
| **Chunks per Sample** | 3 Chunks (`Chunk1` – `Chunk3`) |
| **Chunk Duration** | 15 seconds per chunk |
| **Total Chunk Folders** | **1,500 Folders** |
| **Audio Format** | Uncompressed WAV (`.wav`), 44.1 kHz / 48 kHz, 16-bit Mono PCM |
| **Transcription Formats** | UTF-8 Urdu Script & Roman Urdu |

---

## 📝 Sample Metadata Format (`metadata.json`)

Each chunk folder contains a `metadata.json` file structured as follows:

```json
{
  "urdu": "کیا حال ہے؟ میں ابھی دفتر پہنچا ہوں۔",
  "RomanUrdu": "kya haal hai? main abhi daftar pohancha hoon."
}
```

---

## 🛠️ Automation Scripts & Tools

### 1. **Generate Dataset Folder Structure & Metadata**
Generates all 500 Sample folders with 3 Chunk subdirectories and `metadata.json` files:
```bash
python scripts/generate_dataset_structure.py
```

### 2. **Slice Audio & Auto-Save Chunks**
Processes raw master `.wav` recordings from `dataset/wavs/` and automatically slices them into 15-second `chunk.wav` and `full_voice.wav` files in each chunk directory:
```bash
python scripts/auto_split_recordings.py
```

### 3. **Run Dataset Quality Validation**
Runs full validation checks across all 1,500 chunk folders for file integrity, audio formats, and JSON transcript keys:
```bash
python scripts/validate_dataset_structure.py
```

---

## 🎯 Phonetic & Linguistic Features

- **Phonetic Coverage**: retroflex consonants (ڈ ،ٹ ،ڑ) and aspirated consonants (پھ, تھ, ٹھ, کھ, گھ).
- **Natural Conversational Fillers**: Includes casual conversational triggers (*تو*, *یار*, *مطلب*, *دیکھو*, *سنو*).
- **Standardized Spelling**: Numbers written out phonetically in words (*پانچ سو*, *دس*) and common loanwords (*واٹس ایپ*, *مائیکروفون*, *فائل*).

---

## 📜 License
This project is prepared as an individual Speech & NLP Dataset assignment submission. All rights reserved.
