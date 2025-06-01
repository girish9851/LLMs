from huggingface_hub import hf_hub_download
import os

def download_tinyllama_gguf():
    model_repo = "TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF"
    model_file = "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"
    target_dir = "./models/tinyllama"

    os.makedirs(target_dir, exist_ok=True)

    downloaded_path = hf_hub_download(
        repo_id=model_repo,
        filename=model_file,
        local_dir=target_dir,
        local_dir_use_symlinks=False
    )

    print(f"✅ Downloaded to: {downloaded_path}")
    
if __name__ == "__main__":
    download_tinyllama_gguf()