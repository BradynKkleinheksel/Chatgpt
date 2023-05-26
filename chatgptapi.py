import openai









def chat_with_gpt(prompt, api_key):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine='davinci',                        # Chooses the engines being used. 
        prompt=prompt,                           # Prompt=Prompt :/
        max_tokens=100,                          # The max amount of tokens/Words you want generated
        temperature=0.7,                         # Refers to how confident the langauge model should be in its responses. Ranges from 0 to 2, the higher the value the more diverse the messages. 
        n = 1,                                   # The number of responses you want
        stop=None,                               # The stop parameter allows you to specify a stopping sequence for the generated text. 
    )
    return response.choices[0].text.strip()      # choices refers to which response will be returned, depending on how many prompts you wanted with n. 
                                                 # text extracts the generated text from the chosen response choice. It retrieves the actual content of the generated completion.
                                                 # Strip removes leading and trailing whitespace from the generated text. It ensures that any unnecessary spaces or line breaks are removed from the response.