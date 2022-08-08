from encodings import utf_8
from urllib import response
from rivescript import RiveScript

#unicoding for arabic 
bot=RiveScript(utf8=True)

#load Directories
bot.load_directory("brain");
bot.sort_replies();

#chat function for bot reply validation
def chat(message):
    if message=="":
      return -1, "No message found"
    else:
        responce= bot.reply("user",message)
    if "ERR:" in responce:
        return -1 , "No message found"
          
    else:
        return 0 , responce

#function to test bot 
# while True:
#    msg=str(input("User:"))
#    reply=str(bot.reply('localuser',msg))
#    if msg=="quit":
#      break
#    else :
#     print ("Bot: " + reply)