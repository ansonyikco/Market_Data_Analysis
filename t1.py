from mistralai import Mistral
api_key = "mnT7XsHfhKDBy00W75rhZ7QubAVq71VL"
model = "mistral-small-latest"
Prompt = '''Given a portoflio that contains the items in listA, please make comment to it within 200 words.
            You may talk about:
            1. nature and 
             - risk of that type of items (e.g. factor affecting prices) and 
             - benefits of this typeof items in portoflio (e.g. what risks it can tackle). 
            
           
            The format should be like:
            
            1. IAU: iShares Gold Trust
            - Tracks the price of gold bullion
            - Benefits: Hedge against inflation and currency devaluation, as well as provide diversification
            - Risks: Gold prices can be volatile and are subject to market sentiment
            
            2. .....
            3. .....

            Overall, this combination is......

           

          
            

        * Please inform if you are not sure about something.
        
            ListA is '''
client = Mistral(api_key=api_key)
Ticker_list = ['VOO','TLT','IAU','VTC','DBC']
chat_response = client.chat.complete(
    model=model,
    messages=[{"role":"user", "content":Prompt+str(Ticker_list)}]
)



print(chat_response.choices[0].message.content)