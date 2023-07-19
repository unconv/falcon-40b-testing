# Falcon-40B-Instruct Testing

This is a repository where I document my testing with the Falcon-40B-Instruct and Falcon-7B-Instruct LLM's.

## 1. Setting up EC2 instance

You need an EC2 instance that has a graphics card and supports CUDA. By selecting a "Deep Learning with PyTorch 2.0.1" AMI and a supported instance type, a graphics card and CUDA should be supported out of the box.

I recommend `g5.2xlarge` with 60 GB EBS for 7B and `g5.12xlarge` with 120 GB EBS for 40B.

You can then run the `installation.sh` to install all the dependencies for Falcon-40B-Instruct.

You might need to `pip install xformers` as well, but I had problems after installing that.

## 2. Running Falcon

After installing the dependencies, you can run Falcon by running the `falcon.py` script. Update the `model` to the one you want to use.

On first run it will download all the model weights. For 7B it will be around 15 gigabytes. For 40B it will be around 100 gigabytes.

## Video

Watch the video where I install it here: https://www.youtube.com/watch?v=EdpkVdo1yBM
