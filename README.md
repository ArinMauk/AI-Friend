# F5-TTS Setup Guide

This guide outlines the steps and troubleshooting necessary to run F5-TTS (a local TTS model) on your machine.

## Prerequisites

### 1. **Python Installation**

Make sure you have Python 3.12 or higher installed. You can download Python from the official website [here](https://www.python.org/downloads/).

### 2. **CUDA Installation**

For GPU acceleration, install CUDA 11.8 on your system. You can check if CUDA is installed using:


```
nvcc --version
```

Ensure that the version matches CUDA 11.8. If it's not installed, download the CUDA toolkit from [NVIDIA's website](https://developer.nvidia.com/cuda-downloads).

### 3. **NVIDIA Drivers**

Ensure you have the latest NVIDIA drivers installed, as these are necessary for GPU acceleration with CUDA. You can check your driver version using:


```
nvidia-smi
```
by lmstudio-community. 

If the drivers are outdated, you can update them from [here](https://www.nvidia.com/Download/index.aspx).

## Steps to Run F5-TTS

### 1. **Clone the Repository**

First, clone the F5-TTS repository from GitHub:


```
git clone https://github.com/SWivid/F5-TTS.git

cd F5-TTS
```
 
### 2. **Create a Virtual Environment**

Create and activate a virtual environment to avoid conflicts with global packages:

```
python -m venv venv
```

For PowerShell, activate the virtual environment using:

```
venv\Scripts\Activate.ps1
```

If you're using another shell, use:

```
.\venv\Scripts\activate
```

Before running these, ensure the execution policy allows scripts:

```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```

### 3. **Install Dependencies**

Install the required dependencies. First, install PyTorch with CUDA support (if you have CUDA 11.8 installed):

```
pip install torch==2.3.0+cu118 --extra-index-url https://download.pytorch.org/whl/cu118
pip install torchaudio==2.3.0+cu118 --extra-index-url https://download.pytorch.org/whl/cu118
```

Then, install the remaining dependencies:

```
pip install -r requirements.txt
```

### 4. **Resolve Additional Dependencies**

Along the way, we encountered several missing dependencies. Install them one by one if you encounter similar issues:

- Install `numpy` (downgrade to version 1.x if necessary):

```
pip install numpy<2 tqdm cached_path soundfile
```

### 5. **Running F5-TTS**

Once everything is set up, test to make sure F5-TTS is up and running. You can run the inference using the following command:

```
python inference-cli.py --model "F5-TTS" --gen_text "Your text to be synthesized here"
```

### Troubleshooting

- **Permission Issues**: If you encounter permission errors while setting up the virtual environment or installing dependencies, ensure you're running the terminal with elevated privileges (Administrator on Windows).

- **DLL Missing Issues**: If you see errors related to missing DLLs (e.g., `shm.dll`), ensure that the CUDA and PyTorch versions are compatible and properly installed. Also, check the environment variables to ensure CUDA paths are added correctly.

- **Virtual Environment Issues**: If you're working in a PowerShell environment, you may need to adjust the execution policy to allow scripts to run (`Set-ExecutionPolicy` as mentioned earlier).

### 6. **Deactivating the Virtual Environment**

Once you're done, you can deactivate the virtual environment with:

```
deactivate
```

With these steps, you should be able to run F5-TTS locally. If you encounter any additional issues or need to install missing packages, follow the troubleshooting steps to resolve them.

