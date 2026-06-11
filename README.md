# Digital Life Reforged
**Yet another voice assistant, but alive.**

[简体中文](README_CN.md)

Three years ago,Geekerwan released [Digital Life](https://www.bilibili.com/video/BV1bm4y117ba/). However, the big pie that the project once painted in the video, such as adding more model support, character support and listing on Steam, has not been realized until now. In fact, because LLM models were updated, it can't work now if you use the original version.
## Forked from
   - [Digital_Life_Server](https://github.com/zixiiu/Digital_Life_Server)
   - [Digital_Life_Server_deepseek](https://github.com/xiaowangaixuexijishu/Digital_Life_Server_deepseek)

For other part of the project, please refer to:  
[Launcher](https://github.com/CzJam/DL_Launcher)  
[UE Client](https://github.com/QSWWLTN/DigitalLife)    

## Features
   - Contexts
   - Full OpenAI API Support(Included 3rd-party models)
   - Anthropic/Gemini API
   - 

## Support models
**If you want to support other models which compatible with OpenAI/Anthropic API,use --base_url argument to set the base url.**

Tested:
   - Deepseek
      - deepseek-v4-flash
Not tested:
   - Deepseek
      - deepseek-v4-pro
   - ChatGPT
      - gpt-5.5
      - gpt-5.4
      - gpt-5.4-mini
   - Claude
      - claude-sonnet-4-6
      - claude-opus-4-8
      - claude-fable-5
      - claude-haiku-4-5
   - GLM
      - GLM-5.1
   - Mimo
      - mimo-v2-flash
      - mimo-v2-omni
      - mimo-v2.5
      - mimo-v2-pro
      - mimo-v2.5-pro
   - Grok
      - grok-4.3
   - MiniMax
      - MiniMax-M3
      - MiniMax-M2.7
      - MiniMax-M2.7-highspeed
   - Qwen
      - qwen3.7-max
      - qwen3.7-plus
      - qwen3.6-flash
   - Kimi
      - kimi-k2.6
      - kimi-k2.5

## Getting stuffs ready to roll:
### Clone this repo
```bash
git clone https://github.com/xiaoliyuanpp/Digital_Life_Reforged.git --recursive
```
### Install
   *Only Windows* Download [Python 3.10 For Windows](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe)  

   Run ```install.bat``` for fast installation
   
   For full guide,please read [Install Guide](Install.md)

### Download models
   [百度网盘](https://pan.baidu.com/s/1EnHDPADNdhDl71x_DHeElg?pwd=75gr)  
   ASR Model:   
   to `/ASR/resources/models`  
   Sentiment Model:  
   to `/SentimentEngine/models`  
   TTS Model:  
   to `/TTS/models`
   
### Start the server
   ```bash
   python SocketServer.py --chatVer {1:OpenAI API/2:Anthropic API/3:Gemini API} --APIKey {Your API Key} --model {[Compatible models]} --stream {True/False} --character {character} --proxy {Proxy url} --base_url {Custom base url}
   ```

This translation was done using Google's translation tool and my poor English skills; please feel free to correct any errors.
个人使用谷歌生草机和垃圾英语水平渣翻，请广大网友指正。