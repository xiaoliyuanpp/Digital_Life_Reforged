import logging

def get_tune(character, model):
    if "gpt" in model:
        filename = character+'gpt.txt'
        logging.info('chatGPT prompt: %s' % filename)
        return open('GPT/prompts/' + filename, 'r', encoding='utf-8').read()
    if 'deepseek' in model:
        filename = character+'ds.txt'
        logging.info('Deepseek prompt: %s' % filename)
        return open('GPT/prompts/' + filename, 'r', encoding='utf-8').read()
    else:
        filename = character+'-general.txt'
        logging.info('General prompt: %s' % filename)
        return open('GPT/prompts/' + filename, 'r', encoding='utf-8').read()






exceed_reply = """
你问的太多了，我们的毛都被你撸秃了，滚去充值或者等限额重置了再过来！
"""

error_reply = """
你等一下，我连接不上大脑了。你是不是网有问题，或者是API Key填错了？
"""