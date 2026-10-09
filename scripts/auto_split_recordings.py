import os
import sys
import wave

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
dataset_dir = os.path.join(root_dir, "dataset")
wavs_dir = os.path.join(dataset_dir, "wavs")

def split_and_save_sample(sample_num, input_wav_path):
    """
    Splits a 45-60s WAV recording into 3x 15s chunks and saves them to:
    dataset/Sample{sample_num}/Chunk1/
    dataset/Sample{sample_num}/Chunk2/
    dataset/Sample{sample_num}/Chunk3/
    """
    if not os.path.exists(input_wav_path):
        print(f"[ERROR] Input WAV file not found: {input_wav_path}")
        return False

    with wave.open(input_wav_path, 'rb') as wf:
        params = wf.getparams()
        framerate = wf.getframerate()
        nframes = wf.getnframes()
        raw_bytes = wf.readframes(nframes)

    # 15 seconds per chunk
    chunk_frames = int(framerate * 15)
    bytes_per_frame = params.sampwidth * params.nchannels

    for chunk_idx in range(1, 4):
        chunk_folder = os.path.join(dataset_dir, f"Sample{sample_num}", f"Chunk{chunk_idx}")
        os.makedirs(chunk_folder, exist_ok=True)

        # 1. Save full_voice.wav
        full_voice_path = os.path.join(chunk_folder, "full_voice.wav")
        with wave.open(full_voice_path, 'wb') as out_full:
            out_full.setparams(params)
            out_full.writeframes(raw_bytes)

        # 2. Extract 15s segment and save chunk.wav
        start_frame = (chunk_idx - 1) * chunk_frames
        end_frame = min(chunk_idx * chunk_frames, nframes)
        
        start_byte = start_frame * bytes_per_frame
        end_byte = end_frame * bytes_per_frame
        chunk_bytes = raw_bytes[start_byte:end_byte]

        chunk_wav_path = os.path.join(chunk_folder, "chunk.wav")
        with wave.open(chunk_wav_path, 'wb') as out_chunk:
            out_chunk.setparams(params)
            out_chunk.writeframes(chunk_bytes)

        print(f" Saved Sample{sample_num} -> Chunk{chunk_idx}: full_voice.wav & chunk.wav")

    return True

def auto_process_all_wavs():
    print("==================================================")
    print(" Automated Audio Slicer & Dataset File Saver ")
    print("==================================================")
    
    processed = 0
    for s in range(1, 501):
        filename = f"urdu_{s:06d}.wav"
        input_path = os.path.join(wavs_dir, filename)
        if os.path.exists(input_path):
            split_and_save_sample(s, input_path)
            processed += 1

    print(f"\n[SUMMARY] Processed {processed} sample recordings into dataset chunk folders.")

if __name__ == "__main__":
    auto_process_all_wavs()
