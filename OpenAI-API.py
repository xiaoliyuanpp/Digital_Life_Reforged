from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
from TTS import TTService
import random
import os
import time

ttsApi = FastAPI()
class TTSRequest(BaseModel):
    model:str = "vits"
    input:str = "V极客湾50不然三天之内找人弄你"
    voice:str = "paimon"
    speed:float = 1.0

char_name = {
            'paimon': ['TTS/models/paimon6k.json', 'TTS/models/paimon6k_390k.pth', 'character_paimon', 1],
            'yunfei': ['TTS/models/yunfeimix2.json', 'TTS/models/yunfeimix2_53k.pth', 'character_yunfei', 1.1],
            'catmaid': ['TTS/models/catmix.json', 'TTS/models/catmix_107k.pth', 'character_catmaid', 1.2]
        }

@ttsApi.post("/audio/speech")
def genAudio(request:TTSRequest):
    if(request.model=="vits"):
        # try:
            logFile = open("./logs/"+str(time.localtime().tm_year)+"-"+str(time.localtime().tm_mon)+"-"+str(time.localtime().tm_mday)+".log","a+")
            logFile.write("["+str(time.process_time())+"]Text:"+request.input+",Speed:"+str(char_name[request.voice][3])+"\n")
            vits = TTService.TTService(*char_name[request.voice])
            exportFile="./tmp/"+str(random.randint(0,10000))+".wav"
            vits.read_save(request.input,exportFile,vits.hps.data.sampling_rate)
            logFile.write("["+str(time.process_time())+"]Export to:"+exportFile+"\n")
            audioFile=os.open(exportFile,os.O_RDONLY)
            audio=os.read(audioFile,os.path.getsize(exportFile))
            os.close(audioFile)
            os.remove(exportFile)
            logFile.close()
            return Response(content=audio,media_type="audio/wav")
        # except Exception as e:
        #     print(e)
        #     raise HTTPException(status_code=500, detail=str(e))
    else:
         return HTTPException(status_code=404, detail="Can't find model "+request.model)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(ttsApi, host="0.0.0.0", port=38400)