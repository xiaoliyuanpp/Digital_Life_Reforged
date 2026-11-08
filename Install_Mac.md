## Based on macOS
[Windows](Install.md)
> ⚠ ATTENTION：  
> If you're completely clueless about what you're doing (a complete beginner), I recommend using a **simple installation script (install.bat)**.
> Before performing the following operations，Please ensure that Git and Python 3.10 are installed.

### Configuration environment
1. (Optional)Use virtualvenv to create a Python virtual environment
```
python3.10 -m venv venv
```
If you don't want to use virtualvenv, please remove './venv/bin/' and '../../..'

2. Install other dependencies
 ```
./venv/bin/pip install -r requirements_mac.txt
 ```

3. Build `monotonic_align`
```
cd TTS/vits/monotonic_align
mkdir monotonic_align
../../../venv/bin/python setup.py build_ext --inplace 
cp monotonic_align/*.so .
```

4. Download models
   [百度网盘](https://pan.baidu.com/s/1EnHDPADNdhDl71x_DHeElg?pwd=75gr)  
   ASR Model:   
   to `/ASR/resources/models`  
   Sentiment Model:  
   to `/SentimentEngine/models`  
   TTS Model:  
   to `/TTS/models`