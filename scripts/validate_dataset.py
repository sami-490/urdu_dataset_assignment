import os
import sys
import wave

# Ensure UTF-8 output encoding for Windows terminal
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def validate():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    metadata_path = os.path.join(root_dir, "dataset", "metadata.csv")
    wavs_dir = os.path.join(root_dir, "dataset", "wavs")
    
    print("==========================================")
    print(" Urdu Dataset Automated QA & Validation ")
    print("==========================================")
    
    errors = []
    warnings = []
    
    if not os.path.exists(metadata_path):
        print(f"[ERROR] Metadata file missing at {metadata_path}")
        sys.exit(1)
        
    print(f"[OK] Found metadata.csv at {metadata_path}")
    
    with open(metadata_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
        
    print(f"✓ Total Metadata Lines: {len(lines)}")
    if len(lines) != 500:
        warnings.append(f"Expected exactly 500 metadata entries, but found {len(lines)}.")
        
    valid_lines = 0
    for idx, line in enumerate(lines, 1):
        parts = line.split("|")
        if len(parts) != 3:
            errors.append(f"Line {idx}: Must have 3 pipe-separated fields (file_id|urdu|roman). Got {len(parts)} fields.")
            continue
            
        file_id, urdu_text, roman_text = parts
        if not file_id.startswith("urdu_") or not file_id.endswith(".wav"):
            errors.append(f"Line {idx}: Invalid file ID '{file_id}'. Expected format 'urdu_000XXX.wav'.")
            
        if not urdu_text:
            errors.append(f"Line {idx}: Urdu text field is empty.")
        if not roman_text:
            errors.append(f"Line {idx}: Roman Urdu text field is empty.")
            
        wav_path = os.path.join(wavs_dir, file_id)
        if os.path.exists(wav_path):
            try:
                with wave.open(wav_path, 'rb') as wf:
                    channels = wf.getnchannels()
                    framerate = wf.getframerate()
                    frames = wf.getnframes()
                    duration = frames / float(framerate)
                    
                    if channels != 1:
                        errors.append(f"{file_id}: Must be Mono (1 channel), got {channels} channels.")
                    if framerate not in [44100, 48000, 16000]:
                        warnings.append(f"{file_id}: Sample rate is {framerate} Hz. Expected 44100 Hz or 48000 Hz.")
                    if duration < 3.0 or duration > 10.0:
                        warnings.append(f"{file_id}: Duration {duration:.2f}s outside recommended range (3-7s).")
            except Exception as e:
                errors.append(f"{file_id}: Failed to parse WAV file ({e}).")
        else:
            warnings.append(f"Missing WAV file: {file_id}")
            
        valid_lines += 1
        
    print(f"[OK] Parsed {valid_lines} metadata entries successfully.")
    
    print("\n---------------- RESULTS ----------------")
    if warnings:
        print(f"[WARNINGS] ({len(warnings)}):")
        for w in warnings[:5]:
            print(f"  - {w}")
        if len(warnings) > 5:
            print(f"  ... and {len(warnings)-5} more warnings (missing WAV files expected prior to recording).")
            
    if errors:
        print(f"[ERRORS] ({len(errors)}):")
        for e in errors[:10]:
            print(f"  - {e}")
        if len(errors) > 10:
            print(f"  ... and {len(errors)-10} more errors.")
        print("\n[FAILED] Validation Failed! Fix the errors listed above.")
        sys.exit(1)
    else:
        print("\n[SUCCESS] Dataset Metadata & Structure Passed Validation!")

if __name__ == "__main__":
    validate()
