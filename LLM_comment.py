from mistralai import Mistral
api_key = "mnT7XsHfhKDBy00W75rhZ7QubAVq71VL"
model = "mistral-small-latest"
Prompt = '''Given a portoflio that contains the items in the following list, please make comment to it within 150 words.
            You may talk about:
            1. nature and 
             - risk of that type of items (e.g. factor affecting prices) and 
             - benefits of this typeof items in portoflio (e.g. what risks it can tackle). 
            2. Any significant problems with the portfolio, e.g. all of items are actually investing the same things.
           
            The format of your response should be like:
            ---Attention: Content from AI---
            1. IAU: iShares Gold Trust
            - Tracks the price of gold bullion
            - Benefits: Hedge against inflation and currency devaluation, as well as provide diversification
            - Risks: Gold prices can be volatile and are subject to market sentiment
            
            2. .....
            3. .....

            Overall, this combination is......

           

          
            

        * Please inform if you are not sure about something.
        
            The portfolio is '''

def Text_AI_comment(Text:str):
    client = Mistral(api_key=api_key)
   
    chat_response = client.chat.complete(
        model=model,
        messages=[{"role":"user", "content":Text}]
    )



    return (chat_response.choices[0].message.content)
def AI_comment(Ticker_list:list):
    client = Mistral(api_key=api_key)
    
    chat_response = client.chat.complete(
        model=model,
        messages=[{"role":"user", "content":Prompt+str(Ticker_list)}]
    )



    return (chat_response.choices[0].message.content)
Ticker_list = ['BITO','BITS','ARKB']


