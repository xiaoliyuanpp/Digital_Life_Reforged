import logging
import os
import time

import GPT.machine_id
import GPT.tune as tune
from openai import OpenAI 
from anthropic import Anthropic
from google import genai
import re


class GPTService():
    def __init__(self, args):
        logging.info('Initializing LLM Service...')
        self.chatVer = args.chatVer

        self.tune = tune.get_tune(args.character, args.model)

        self.counter = 0

        # self.brainwash = args.brainwash

        self.model = args.model
        self.chat = [{"role": "system", "content": self.tune}]
        self.api_key = args.APIKey
        
        # if self.chatVer == 1:
        #     from revChatGPT.V1 import Chatbot
        #     config = {}
        #     if args.accessToken:
        #         logging.info('Try to login with access token.')
        #         config['access_token'] = args.accessToken

        #     else:
        #         logging.info('Try to login with email and password.')
        #         config['email'] = args.email
        #         config['password'] = args.password
        #     config['paid'] = args.paid
        #     config['model'] = args.model
        #     if type(args.proxy) == str:
        #         config['proxy'] = args.proxy

        #     self.chatbot = Chatbot(config=config)
        #     logging.info('WEB Chatbot initialized.')


        # elif self.chatVer == 3:
        #     mach_id = GPT.machine_id.get_machine_unique_identifier()
        #     from revChatGPT.V3 import Chatbot
        #     if args.APIKey:
        #         logging.info('you have your own api key. Great.')
        #         api_key = args.APIKey
        #     else:
        #         logging.info('using custom API proxy, with rate limit.')
        #         os.environ['API_URL'] = "https://api.geekerwan.net/chatgpt2"
        #         api_key = mach_id

        #     self.chatbot = Chatbot(api_key=api_key, proxy=args.proxy, system_prompt=self.tune)
        #     logging.info('API Chatbot initialized.')

            
        if self.chatVer % 3 == 1:  
            if args.base_url != None:
                logging.info("Your custom base url:"+args.base_url)
                self.base_url = args.base_url
            elif "deepseek" in self.model:
                logging.info("You are using Deepseek.")
                self.base_url = "https://api.deepseek.com/v1"
            elif "MiniMax" in self.model:
                logging.info("You are using MiniMax.")
                self.base_url = "https://api.minimaxi.com/v1"
            elif "qwen" in self.model:
                logging.info("You are using Qwen.")
                self.base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
            elif "glm" in self.model:
                logging.info("You are using GLM.")
                self.base_url = "https://open.bigmodel.cn/api/paas/v4/"
            elif "kimi" in self.model:
                logging.info("You are using Kimi.")
                self.base_url = "https://api.moonshot.cn/v1"
            elif "mimo" in self.model:
                logging.info("You are using Mimo.")
                self.base_url = "https://api.xiaomimimo.com/v1"
            elif "grok" in self.model:
                logging.info("You are using Grok.")
                self.base_url = "https://api.x.ai/v1"
            self.client = OpenAI(
                base_url=self.base_url,
                api_key=self.api_key #You must have your own API key.
            )
            logging.info('OpenAI Chatbot initialized.')
        elif self.chatVer % 3 == 2:
            if args.base_url != None:
                logging.info("Your custom base url:"+args.base_url)
                self.base_url = args.base_url
            elif "deepseek" in self.model:
                logging.info("You are using Deepseek.")
                self.base_url = "https://api.deepseek.com/anthropic"
            elif "minimax" in self.model:
                logging.info("You are using MiniMax.")
                self.base_url = "https://api.minimaxi.com/anthropic"
            elif "glm" in self.model:
                logging.info("You are using GLM.")
                self.base_url = "https://open.bigmodel.cn/api/anthropic"
            elif "mimo" in self.model:
                logging.info("You are using Mimo.")
                self.base_url = "https://api.xiaomimimo.com/anthropic"
            self.client = Anthropic(
                base_url=self.base_url,
                api_key=self.api_key
            )
            logging.info('Anthropic Chatbot initialized.')
        elif self.chatVer % 3 == 0:
            self.client = genai.Client(api_key=self.api_key)
            self.chatbot = self.client.chats.create(model=self.model)
            self.chatbot.send_message(self.tune)
            logging.info('Gemini Chatbot initialized.')


    def ask(self, text):
        stime = time.time()
        # if self.chatVer == 3:
        #     prev_text = self.chatbot.ask(text)

        # # V1
        # elif self.chatVer == 1:
        #     for data in self.chatbot.ask(
        #             self.tune + '\n' + text
        #     ):
        #         prev_text = data["message"]
        if self.chatVer > 3:
            logging.info("You are using type mode,please write your input here:")
            input(text)
        # Require OpenAI >= 1.0.0
        self.chat.append({"role": "user", "content": text})
        if self.chatVer % 3 == 1:
            logging.info("Use OpenAI API")
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.chat,
                temperature=1,
                stream=False
            )
            prev_text = response.choices[0].message.content
        elif self.chatVer % 3 == 2:
            logging.info("Use Anthropic API")
            response = self.client.messages.create(
                model=self.model,
                messages=self.chat,
                temperature=1,
                stream=False
            )
            prev_text = response.content
        elif self.chatVer % 3 == 0:
            logging.info("Use Gemini API")
            response = self.chatbot.send_message(text)
            prev_text = response.text
        # 过滤掉中文括号（）和英文括号 () 及其内部的所有文字
        prev_text = re.sub(r'[\(\uff08].*?[\)\uff09]', '', prev_text).strip()
        self.chat.append({"role": "assistant","content": prev_text})
        logging.info('Response: %s, time used %.2f' % (prev_text, time.time() - stime))
        return prev_text

    def ask_stream(self, text):
        logging.info("Use stream output")
        complete_text = ""
        stime = time.time()
        if self.chatVer > 3:
            logging.info("You are using type mode.")
            text = input("Please write your input here:")
        # if self.chatVer == 1 or self.chatVer == 3:
        #     if self.counter % 5 == 0 and self.chatVer == 1:

        #         if self.brainwash:
        #             logging.info('Brainwash mode activated, reinforce the tune.')
        #         else:
        #             logging.info('Injecting tunes')
        #         asktext = self.tune + '\n' + text
        #     else:
        #         asktext = text
        #     self.counter += 1
        #     for data in self.chatbot.ask(asktext) if self.chatVer == 1 else self.chatbot.ask_stream(text):
        #         message = data["message"][len(prev_text):] if self.chatVer == 1 else data

        #         if ("。" in message or "！" in message or "？" in message or "\n" in message) and len(complete_text) > 3:
        #             complete_text += message
        #             logging.info('ChatGPT Stream Response: %s, @Time %.2f' % (complete_text, time.time() - stime))
        #             yield complete_text.strip()
        #             complete_text = ""
        #         else:
        #             complete_text += message

        #         prev_text = data["message"] if self.chatVer == 1 else data
        self.chat.append({"role": "user", "content": text})
        try:
            if self.chatVer % 3 == 1:
                logging.info("Use OpenAI API")
                response = self.client.chat.completions.create(
                    model = self.model,
                    messages=self.chat,
                    stream=True,
                    timeout=30
                )
            if self.chatVer % 3 == 0:
                logging.info("Use Gemini API")
                response = self.chatbot.send_message_stream(text)
            complete_text = ""
            assistant_full_reply = ""
            sentence_endings = re.compile(r'([。！？\n])')  # 正则表达式匹配终止符
            if self.chatVer % 3 == 1:
                for chunk in response:
                    if chunk.choices[0].finish_reason == 'stop':
                        if complete_text.strip():
                            logging.info('Stream Response: %s, @Time %.2f' % (complete_text, time.time() - stime))
                            yield complete_text.strip()
                        break
                    message = chunk.choices[0].delta.content or ""
                    complete_text += message
                    # 统一分割逻辑
                    parts = sentence_endings.split(complete_text)
                    for i in range(0, len(parts) - 1, 2):
                        sentence = (parts[i] + parts[i + 1]).strip()
                        if sentence:
                            # 过滤掉中文括号（）和英文括号 () 及其内部的所有文字
                            sentence = re.sub(r'[\(\uff08].*?[\)\uff09]', '', sentence).strip()
                            if not sentence: # 如果过滤完句子空了（比如整句只有括号），就跳过
                                continue
                            logging.info('Stream Response: %s, @Time %.2f' % (sentence, time.time() - stime))
                            assistant_full_reply += sentence
                            yield sentence
                    complete_text = parts[-1] if len(parts) % 2 else ""
            elif self.chatVer % 3 == 0:
                for chunk in response:
                    message = chunk.text or ""
                    complete_text += message
                    # 统一分割逻辑
                    parts = sentence_endings.split(complete_text)
                    for i in range(0, len(parts) - 1, 2):
                        sentence = (parts[i] + parts[i + 1]).strip()
                        if sentence:
                            # 过滤掉中文括号（）和英文括号 () 及其内部的所有文字
                            sentence = re.sub(r'[\(\uff08].*?[\)\uff09]', '', sentence).strip()
                            if not sentence: # 如果过滤完句子空了（比如整句只有括号），就跳过
                                continue
                            logging.info('Stream Response: %s, @Time %.2f' % (sentence, time.time() - stime))
                            assistant_full_reply += sentence
                            yield sentence
                    complete_text = parts[-1] if len(parts) % 2 else ""
            else:
                with self.client.messages.stream(
                    max_tokens=1048576,
                    messages=self.chat,
                    model=self.model
                ) as stream:
                    for message_text in stream.text_stream:
                        complete_text += message_text
                        parts = sentence_endings.split(complete_text)
                        for i in range(0, len(parts) - 1, 2):
                            sentence = (parts[i] + parts[i + 1]).strip()
                            if sentence:
                                sentence = re.sub(r'[\(\uff08].*?[\)\uff09]', '', sentence).strip()
                                if not sentence:
                                    continue
                                logging.info('Stream Response: %s, @Time %.2f' % (sentence, time.time() - stime))
                                assistant_full_reply += sentence
                                yield sentence
                        complete_text = parts[-1] if len(parts) % 2 else ""

            self.chat.append({"role": "assistant","content": assistant_full_reply})
        except Exception:
            yield tune.error_reply
            
