import json
import re
import string
import nltk
import pymorphy2
from nltk.corpus import stopwords
from telethon.sync import TelegramClient
from datetime import timedelta
from datetime import datetime

# from DB import DB
from Advanced_DB_RU import DbAdvanced


class Parser:

    def __init__(self, name='Semyon', api_id=15108736, api_hash='65fd102a9be7dab3632d17b2062188ae'):
        self.name = name
        self.api_id = api_id
        self.api_hash = api_hash

        self.spec_chars = string.punctuation + r'\n\x0«»\t—…[]\n*'
        self.stop_words = stopwords.words('russian')
        self.morph = pymorphy2.MorphAnalyzer()

        self.db_writer = DbAdvanced()
        self.last_date = self.db_writer.last_date()

        self.searching_period = datetime.now() - timedelta(days=10)

        self.dtp_chats = ['https://t.me/perecup_rf', 'https://t.me/ildar_auto_podbor', 'https://t.me/haraba_auto',
                          'https://t.me/nije_rinka_RF', 'https://t.me/tachki_nizhe_rynka', 'https://t.me/BitieAvtoZdes',
                          'https://t.me/perekupavtoRF', 'https://t.me/autotrade77', 'https://t.me/auto_sale_rf',
                          'https://t.me/avto999999555']

        #self.db_writer.db_cleaning()

    def parse(self):
        with TelegramClient(self.name, self.api_id, self.api_hash) as client:
            for index in range(len(self.dtp_chats)):
                for message in client.iter_messages(self.dtp_chats[index]):
                    # if message.date.timestamp() > self.searching_period.timestamp():
                    if message.date.timestamp() > self.last_date:

                        text = message.text

                        if text is None or len(text) < 100:
                            continue

                        if type(text) != float:
                            text = "".join([ch for ch in text if ch not in self.spec_chars])
                            text = re.sub('\n', '     ', text)
                            tokens = nltk.word_tokenize(text)
                            filtered_text = [word.lower() for word in tokens if word.lower() not in self.stop_words]
                            final_text = []

                            for word in filtered_text:
                                if word.isalpha() and len(word) > 2:
                                    final_text.append(self.morph.parse(word)[0].normal_form)
                                else:
                                    continue

                            adv_text = json.dumps(final_text)

                            new_line = [message.id, self.dtp_chats[index], message.chat.title,
                                        message.date.timestamp(), message.text, adv_text]

                            self.db_writer.insert_into_db(new_line)
                    else:
                        break


# if __name__ == '__main__':
#     test = Parser()
#     test.parse()