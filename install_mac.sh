python3.10 venv venv
./venv/bin/pip install -r requirements_mac.txt
cd TTS/vits/monotonic_align
mkdir monotonic_align
../../../venv/bin/python setup.py build_ext --inplace
cp monotonic_align/*.so .