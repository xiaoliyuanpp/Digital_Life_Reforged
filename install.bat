@echo off
python -m venv venv
.\venv\Scripts\pip.exe install -r requirements.txt
cd "TTS/vits/monotonic_align"
mkdir monotonic_align
..\..\..\venv\Scripts\python.exe setup.py build_ext --inplace
copy .\monotonic_align\*.pyd .\