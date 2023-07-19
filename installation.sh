sudo apt update -y
sudo apt upgrade -y
sudo apt install python3-pip -y
pip install -U pip
pip install -U transformers
pip install -U torch
pip install -U einops
pip install -U accelerate
pip install -U scipy
pip install -U bitsandbytes
export PATH="$PATH:/home/ubuntu/.local/bin"
