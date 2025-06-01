import os
from huggingface_hub import snapshot_download

def download_model():
    model_dir = "models/TinyLlama"
    if not os.path.exists(model_dir):
        print("Downloading model from Hugging Face...")
        snapshot_download(
            repo_id="TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF",
            local_dir=model_dir,
            allow_patterns="*.gguf"
        )
    return model_dir

