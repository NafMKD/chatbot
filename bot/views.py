from django.shortcuts import render
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create your views here.
messages = []
chatbot = ChatBot("Bot")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    "chatterbot.corpus.english"
)
def home(request):
    if request.method == 'POST':
        if(request.POST['message']!=''):
            first = []
            first.append(request.POST['message'])
            first.append(chatbot.get_response(request.POST['message']))
            messages.append(first)
    return render(request, 'home.html', {'messages' : messages})