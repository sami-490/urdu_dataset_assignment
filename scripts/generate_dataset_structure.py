import os
import sys
import json

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Base path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
dataset_dir = os.path.join(root_dir, "dataset")

# Rich conversational Urdu & Roman Urdu template pairs
urdu_base = [
    ("کیا حال ہے؟ میں ابھی دفتر پہنچا ہوں۔", "kya haal hai? main abhi daftar pohancha hoon."),
    ("مجھے وہ فائل واٹس ایپ پر بھیج دیں۔", "mujhe woh file whatsapp par bhej dein."),
    ("یار مطلب تم کل نہیں آؤ گے؟", "yaar matlab tum kal nahi aao gay?"),
    ("جی تم کب تک گھر پہنچو گے؟", "jee tum kab tak ghar pohancho gay?"),
    ("تو کل بازار سے دو کلو سیب اور تین کلو آم لے آنا۔", "to kal bazaar say do kilo seb aur teen kilo aam lay aana."),
    ("سنو مجھے پانچ منٹ میں دوبارہ کال کرو۔", "suno mujhe paanch minute mein dobara call karo."),
    ("یار کیا تم نے آج کا اخبار پڑھا ہے؟", "yaar kya tum nay aaj ka akhbar parha hai?"),
    ("دیکھو آج موسم بہت خوشگوار اور ٹھنڈا ہے۔", "dekho aaj mausam bohat khushgawar aur thanda hai."),
    ("ارے گاڑی کو آرام سے چلاؤ، جلدی نہ کرو۔", "arey gari ko aaram say chalao, jaldi nah karo."),
    ("مطلب مائیکروفون کا بٹن دبا کر ریکارڈنگ شروع کریں۔", "matlab microphone ka button daba kar recording shuru karein."),
    ("جی بھائی صاحب، کیا یہ بس لاہور جا رہی ہے؟", "jee bhai sahib, kya yeh bus lahore ja rahi hai?"),
    ("تو چائے میں چینی تھوڑی کم رکھنا۔", "to chaey mein cheeni thori kam rakhna."),
    ("سنو رات کے دس بجے ہماری میٹنگ شروع ہوگی۔", "suno raat kay das bajay hamari meeting shuru hogi."),
    ("یار دروازہ بند کر دو اور کھڑکی کھول دو۔", "yaar darwaza band kar do aur khirki khol do."),
    ("دیکھو تم نے پچھلے ہفتے کون سی کتاب پڑھی تھی؟", "dekho tum nay pichlay haftay kaun si kitab parhi thi?"),
    ("ارے پلیز مجھے اس لوکیشن کا میپ بھیج دو۔", "arey please mujhe is location ka map bhej do."),
    ("مطلب وہ لڑکا صبح سے پارک میں دوڑ رہا ہے۔", "matlab woh larka subah say park mein daur raha hai."),
    ("جی ہمارے پاس صرف بیس منٹ کا وقت باقی ہے۔", "jee hamaray paas sirf bees minute ka waqt baqi hai."),
    ("تو ڈاکٹر نے یہ دوائی دن میں تین بار کھانے کو کہی ہے۔", "to doctor nay yeh dawai din mein teen bar khanay ko kahi hai."),
    ("سنو تم موبائل پر اتنا وقت کیوں ضائع کرتے ہو؟", "suno tum mobile par itna waqt kyun zaya kartay ho?"),
]

total_samples = 500
chunks_per_sample = 3

def generate_structure():
    print(f"Generating {total_samples} samples x {chunks_per_sample} chunks = {total_samples * chunks_per_sample} folders...")

    chunk_count = 0
    for s in range(1, total_samples + 1):
        sample_folder = os.path.join(dataset_dir, f"Sample{s}")
        for c in range(1, chunks_per_sample + 1):
            chunk_folder = os.path.join(sample_folder, f"Chunk{c}")
            os.makedirs(chunk_folder, exist_ok=True)
            
            # Pick template text
            idx = (s - 1) * chunks_per_sample + (c - 1)
            u_text, r_text = urdu_base[idx % len(urdu_base)]
            
            if idx >= len(urdu_base):
                suffix_u = f" (نمونہ {s} - حصہ {c})"
                suffix_r = f" (Sample {s} - Chunk {c})"
                u_text += suffix_u
                r_text += suffix_r

            # Create metadata.json
            metadata = {
                "urdu": u_text,
                "RomanUrdu": r_text
            }
            
            metadata_path = os.path.join(chunk_folder, "metadata.json")
            with open(metadata_path, "w", encoding="utf-8") as f:
                json.dump(metadata, f, ensure_ascii=False, indent=2)
                
            chunk_count += 1

    print(f"[SUCCESS] Successfully created {chunk_count} chunk folders with metadata.json files in {dataset_dir}!")

if __name__ == "__main__":
    generate_structure()
