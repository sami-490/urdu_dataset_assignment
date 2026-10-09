import os
import sys
import json
import wave

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def validate():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    dataset_dir = os.path.join(root_dir, "dataset")
    
    print("==================================================")
    print(" 1,500 Chunks Urdu Dataset Automated Validation ")
    print("==================================================")
    
    errors = []
    warnings = []
    
    total_samples = 500
    chunks_per_sample = 3
    expected_total_folders = total_samples * chunks_per_sample
    
    found_folders = 0
    valid_metadata_count = 0
    
    for s in range(1, total_samples + 1):
        sample_folder = os.path.join(dataset_dir, f"Sample{s}")
        if not os.path.exists(sample_folder):
            errors.append(f"Missing sample folder: Sample{s}")
            continue
            
        for c in range(1, chunks_per_sample + 1):
            chunk_folder = os.path.join(sample_folder, f"Chunk{c}")
            if not os.path.exists(chunk_folder):
                errors.append(f"Missing chunk folder: Sample{s}/Chunk{c}")
                continue
                
            found_folders += 1
            
            # 1. Validate metadata.json
            metadata_path = os.path.join(chunk_folder, "metadata.json")
            if not os.path.exists(metadata_path):
                errors.append(f"Sample{s}/Chunk{c}: Missing metadata.json")
            else:
                try:
                    with open(metadata_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    if "urdu" not in data:
                        errors.append(f"Sample{s}/Chunk{c}/metadata.json: Missing 'urdu' key.")
                    if "RomanUrdu" not in data:
                        errors.append(f"Sample{s}/Chunk{c}/metadata.json: Missing 'RomanUrdu' key.")
                    valid_metadata_count += 1
                except Exception as e:
                    errors.append(f"Sample{s}/Chunk{c}/metadata.json: JSON decode error ({e}).")
                    
            # 2. Check full_voice.wav
            full_voice_path = os.path.join(chunk_folder, "full_voice.wav")
            if not os.path.exists(full_voice_path):
                warnings.append(f"Sample{s}/Chunk{c}: Missing full_voice.wav")
                
            # 3. Check chunk.wav
            chunk_path = os.path.join(chunk_folder, "chunk.wav")
            if not os.path.exists(chunk_path):
                warnings.append(f"Sample{s}/Chunk{c}: Missing chunk.wav")

    print(f"[OK] Total Chunk Folders Scanned: {found_folders}/{expected_total_folders}")
    print(f"[OK] Valid metadata.json Files: {valid_metadata_count}/{expected_total_folders}")
    
    print("\n---------------- RESULTS ----------------")
    if warnings:
        print(f"[WARNINGS] ({len(warnings)}):")
        for w in warnings[:5]:
            print(f"  - {w}")
        if len(warnings) > 5:
            print(f"  ... and {len(warnings)-5} more warnings (missing WAV audio clips expected prior to recording).")
            
    if errors:
        print(f"[ERRORS] ({len(errors)}):")
        for e in errors[:10]:
            print(f"  - {e}")
        if len(errors) > 10:
            print(f"  ... and {len(errors)-10} more errors.")
        print("\n[FAILED] Validation Failed!")
        sys.exit(1)
    else:
        print("\n[SUCCESS] All 1,500 Chunk Folders & Metadata Structures Passed Validation!")

if __name__ == "__main__":
    validate()
