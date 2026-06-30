@echo off
python -m venv venv
.\venv\Scripts\python.exe -m pip install torch==2.0.1+cu118 torchvision==0.15.2+cu118 torchaudio==2.0.2+cu118 --extra-index-url https://download.pytorch.org/whl/cu118
.\venv\Scripts\python.exe -m pip install -r requirements_cuda.txt
cd "TTS/vits/monotonic_align"
mkdir monotonic_align
..\..\..\venv\Scripts\python.exe setup.py build_ext --inplace
copy .\monotonic_align\*.pyd .\
