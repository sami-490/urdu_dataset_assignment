# Assignment Specification: Urdu Speech & Text Dataset Collection

**Course / Project Title:** Speech & Natural Language Processing Dataset Collection  
**Assignment Name:** Conversational Urdu Audio & Chunked Multi-Script Dataset (500 Samples / 1,500 Chunks)  
**Task Type:** Individual Assignment (Strictly No Grouping Allowed)  
**Submission Format:** Google Drive Shareable Link (ZIP of Dataset)  

---

## 1. Executive Overview & Policy

This assignment requires each individual participant to collect, record, process, chunk, and format a high-quality dataset consisting of **500 full 1-minute Urdu voice recordings**, each divided into **3 chunks (15 seconds each)**, producing **1,500 chunk folders in total**.

Each chunk folder must contain:
1. `full_voice.wav` - The complete 1-minute audio recording for that sample.
2. `chunk.wav` - The sliced audio segment (15 seconds) for that specific chunk.
3. `metadata.json` - A UTF-8 JSON file containing the transcript for that chunk in Urdu and Roman Urdu:
   ```json
   {
     "urdu": "کیا حال ہے؟ میں ابھی دفتر پہنچا ہوں۔",
     "RomanUrdu": "kya haal hai? main abhi daftar pohancha hoon."
   }
   ```

---

## 2. Dataset Structure Specifications

```text
dataset/
├── Sample1/
│   ├── Chunk1/
│   │   ├── full_voice.wav
│   │   ├── chunk.wav
│   │   └── metadata.json
│   ├── Chunk2/
│   │   ├── full_voice.wav
│   │   ├── chunk.wav
│   │   └── metadata.json
│   └── Chunk3/
│       ├── full_voice.wav
│       ├── chunk.wav
│       └── metadata.json
├── ...
└── Sample500/
    ├── Chunk1/
    │   ├── full_voice.wav
    │   ├── chunk.wav
    │   └── metadata.json
    ├── Chunk2/
    │   ├── full_voice.wav
    │   ├── chunk.wav
    │   └── metadata.json
    └── Chunk3/
        ├── full_voice.wav
        ├── chunk.wav
        └── metadata.json
```

### Folder Calculations:
* **Total 1-Minute Voice Recordings:** 500 Samples (`Sample1` to `Sample500`)
* **Chunks per Sample:** 3 Chunks (`Chunk1` to `Chunk3`, 15 seconds each)
* **Total Chunk Folders:** 500 × 3 = **1,500 Folders**

---

## 3. Phase Instructions

### Phase 1: Script Preparation
* Sentence Length: Spoken fragments corresponding to 15-second chunk length.
* Phonetic Coverage: Include retroflex sounds (ڈ ،ٹ ،ڑ) and aspirated consonants (پھ, تھ, ٹھ, کھ, گھ).
* Conversational Style: Use natural WhatsApp fillers (تو, یار, مطلب).
* Spelling: Spell numbers in words (e.g., پانچ سو) and loanwords phonetically in Urdu script (e.g., واٹس ایپ, فائل).

### Phase 2: Recording Environment
* Record in a quiet room with minimal reverb/echo.
* Record 1-minute full audio sessions per sample, taking breaks to avoid vocal fatigue (max 2 hours/day).

### Phase 3: Audio Processing & Chunking
* **Audio Encoding:** Uncompressed WAV (`.wav`), 44.1 kHz / 48 kHz, 16-bit Mono PCM.
* **Volume Normalization:** Peak volume normalized to -1 dBFS or -23 LUFS.
* **Chunk Slicing:** Slice each 1-minute recording into 3 contiguous 15-second segments (`chunk.wav`). Place the master audio as `full_voice.wav` in each chunk folder.

### Phase 4: Quality Control & Validation
* Run `python scripts/validate_dataset.py` to check for missing audio files, JSON syntax errors, and missing keys (`urdu`, `RomanUrdu`).

### Phase 5: Submission
* Zip the `dataset/` directory into `[Your_Name]_[RollNo]_Urdu_Dataset.zip`.
* Upload to Google Drive with link setting "Anyone with the link can view/download".
