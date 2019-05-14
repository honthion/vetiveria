from googlevoice import Voice
import sys
import BeautifulSoup
import fileinput


def login():
    username, password = "honthion@gmail.com", "314159Gmail"

    voice = Voice()
    client = voice.login(username, password)
    client.call('+8618623001528')
    return client

login()