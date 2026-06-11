## Based on Windows
> ⚠ ATTENTION：  
> If you're completely clueless about what you're doing (a complete beginner), I recommend using a **simple installation script (install.bat)**.
> Before performing the following operations，Please ensure that Git and Python 3.10 are installed.

### Configuration environment
1. (Optional)Use virtualvenv to create a Python virtual environment
```
python -m venv venv
```
If you don't want to use virtualvenv, please remove '.\venv\Scripts\python.exe -m'
2. Install PyTorch
> You can run `nvcc --version` in terminal，find `Cuda compilation tools` to see the cuda version.

For cuda11.8： 

```
.\venv\Scripts\python.exe -m pip install torch==2.0.1+cu118 torchvision==0.15.2+cu118 torchaudio==2.0.2+cu118 --extra-index-url https://download.pytorch.org/whl/cu118
```

For **NONE NVIDIA GPU**：

```
.\venv\Scripts\python.exe -m pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2
```

3. Install other dependencies
 ```
.\venv\Scripts\python.exe -m pip install -r requirements.txt
 ```

4. Build `monotonic_align`
```
cd "TTS/vits/monotonic_align"
mkdir monotonic_align
python setup.py build_ext --inplace
copy .\\monotonic_align\\*.pyd .\\
```

5. For **NONE NVIDIA GPU**

​	Edit ```Digital_Life_Reforged\TTS\TTService.py``` line 36

```python
From
self.net_g = SynthesizerTrn(...).cuda()
To
self.net_g = SynthesizerTrn(...).cpu()
```

6. Download models
   [百度网盘](https://pan.baidu.com/s/1EnHDPADNdhDl71x_DHeElg?pwd=75gr)  
   ASR Model:   
   to `/ASR/resources/models`  
   Sentiment Model:  
   to `/SentimentEngine/models`  
   TTS Model:  
   to `/TTS/models`