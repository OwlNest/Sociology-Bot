import telepot
from telepot.loop import MessageLoop
from telepot.delegate import per_chat_id, create_open, pave_event_space, include_callback_query_chat_id
from telepot.namedtuple import ReplyKeyboardMarkup
import time
from config import TOKEN, questions, keyboards, messages

#telepot.api.set_proxy("")

#telepot.api.set_proxy("")

knownUsers = [] 


def newcomer(id):
    if id not in knownUsers:  
        knownUsers.append(id)  

class Poll(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(Poll, self).__init__(*args, **kwargs)
        self._step = 0
        self._id = 0
        self._is_first = True
        self._answers = {1: 'undefined', 2: 'undefined', 3: 'undefined', 4: 'undefined', 5: 'undefined', 6: 'undefined', 7: 'undefined', 8: 'undefined', 9: 'undefined', 10: 'undefined', 11: 'undefined', 12: 'undefined'}
        self._attempt = True
        self._editor = None
        self._edit_msg_ident = None

    def on_chat_message(self, msg):
        if self._is_first == True:
            self.handle(msg)
            self.bot.sendMessage(self._id, messages[self._attempt])
            self._is_first = False
        elif (self._step <= 12) and (self._attempt == True):
            #bot.editMessageReplyMarkup(self._edit_msg_ident, reply_markup=None)
            try:
                self._answers[self._step] = msg['text']
            except:
                self.bot.sendMessage(self._id, messages['err'])
            self._step += 1
            sent = self.bot.sendMessage(self._id, questions[self._step], reply_markup = keyboards[self._step])
            self._editor = telepot.helper.Editor(self.bot, sent)
            self._edit_msg_ident = telepot.message_identifier(sent)
        elif (self._step == 13) and (self._attempt == True):
            self.export()
            self.result_f()
            self._step += 1
        else:
            self.bot.sendMessage(self._id, messages['e'], reply_markup = None) 
            #bot.editMessageReplyMarkup(self._edit_msg_ident, reply_markup=None)    

       
    def result_f(self):
        self.bot.sendMessage(self._id, 'Ваш ответ на первый вопрос: ' +  str(self._answers[1])) 
        self.bot.sendMessage(self._id, 'Ваш ответ на второй вопрос: ' + str(self._answers[2])) 
        self.bot.sendMessage(self._id, 'Ваш ответ на третий вопрос: ' + str(self._answers[3]))
        self.bot.sendMessage(self._id, 'Ваш ответ на четвертый вопрос: ' + str(self._answers[4])) 
        self.bot.sendMessage(self._id, 'Ваш ответ на пятый вопрос: ' + str(self._answers[5]))
        self.bot.sendMessage(self._id, 'Ваш ответ на шестой вопрос: ' + str(self._answers[6]))
        self.bot.sendMessage(self._id, 'Ваш ответ на седьмой вопрос: ' + str(self._answers[7]))
        self.bot.sendMessage(self._id, 'Ваш ответ на восьмой вопрос: ' + str(self._answers[8])) 
        self.bot.sendMessage(self._id, 'Ваш ответ на девятый вопрос: ' + str(self._answers[9]))
        self.bot.sendMessage(self._id, 'Ваш ответ на десятый вопрос: ' + str(self._answers[10]))
        self.bot.sendMessage(self._id, 'Ваш ответ на одиннадцатый вопрос: ' + str(self._answers[11]))
        self.bot.sendMessage(self._id, 'Ваш ответ на двенадцатый вопрос: ' + str(self._answers[12]))
        print(self._chat_id, ' прошел опрос')

    def attempt(self, id):
        if int(id) in knownUsers:
            self._attempt = False
        else:
             self._attempt = True

    def handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        self.attempt(chat_id)
        newcomer(chat_id)
        self._id = chat_id

    def export(self):
        f = open('base.txt' , 'a')
        newid = str(self._id)
        f.write(newid + ':1:' + str(self._answers[1]) + ';')
        f.write(newid + ':2:' + str(self._answers[2]) + ';')
        f.write(newid + ':3:' + str(self._answers[3]) + ';')
        f.write(newid + ':4:' + str(self._answers[4]) + ';')
        f.write(newid + ':5:' + str(self._answers[5]) + ';')
        f.write(newid + ':6:' + str(self._answers[6]) + ';')
        f.write(newid + ':7:' + str(self._answers[7]) + ';')
        f.write(newid + ':8:' + str(self._answers[8]) + ';')
        f.write(newid + ':9:' + str(self._answers[9]) + ';')
        f.write(newid + ':10:' + str(self._answers[10]) + ';')
        f.write(newid + ':11:' + str(self._answers[11]) + ';')
        f.write(newid + ':12:' + str(self._answers[12]) + ';' + '\n')
        f.close()
        g = open('users.txt', 'a')
        g.write(newid + ';' + '\n')
        g.close()

g = open('users.txt')
for line in g:
    knownUsers.append(int(line.split(';')[0]))

print(knownUsers)

bot = telepot.DelegatorBot(TOKEN, [
    include_callback_query_chat_id(
        pave_event_space())(
            per_chat_id(types=['private']), create_open, Poll, timeout=10000),
])
print(bot.getMe())

MessageLoop(bot).run_as_thread()

while 1:
    time.sleep(10)