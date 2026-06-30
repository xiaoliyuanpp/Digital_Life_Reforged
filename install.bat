@echo off
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
cd "TTS/vits/monotonic_align"
mkdir monotonic_align
..\..\..\venv\Scripts\python.exe setup.py build_ext --inplace
copy .\monotonic_align\*.pyd .\
cd ..
cd ..
powershell -Command "(Get-Content 'TTService.py' -Raw) -replace ').cuda()', ').cpu()' | Set-Content 'TTService.py'"