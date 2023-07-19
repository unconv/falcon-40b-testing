# CUDA notes

If you need to install CUDA, these resouces might be helpful:

## Install CUDA

```console
$ sudo apt install nvidia-cuda-toolkit
```

This was needed to solve some OpenSSL error:

```console
$ pip install urllib3==1.26.6
```

## Download CUDA 11.7 for Ubuntu 22.04

https://developer.nvidia.com/cuda-11-7-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_local

## Switch CUDA version

```console
$ sudo rm /usr/local/cuda
$ sudo ln -s /usr/local/cuda-11.7 /usr/local/cuda
```

Source: https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-base.html
