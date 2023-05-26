import Prompts
import chatgptapi

api_key = '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'

def bootup():
    actor = Prompts.Actors()
    adjective = Prompts.Adjective()
    prompt = Prompts.prompt(actor, adjective)
    gptresponse = chatgptapi.chat_with_gpt(prompt, api_key)
    print(gptresponse)






bootup()