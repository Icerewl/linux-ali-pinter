import telebot
import requests
Api_Key = "5680357315:AAHgNRo6OC5Dp8Bsgx25TfXcuaTxsWsTG9k"
chat_id = "5676034733"

def send_status_to_bot(yess):
    response = requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(Api_Key, "sendMessage"),
            data={'chat_id': chat_id, 'text': yess}
        ).json()
    return True
