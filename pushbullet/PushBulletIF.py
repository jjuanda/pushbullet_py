import requests



class PushBulletIF:
    def __init__(self, token):
        self.token = token

    def push_note(self, title, body):
        if type(body) == list:
            body = '\n'.join(body)
        msg = {
            'type'  : 'note',
            'title' : title,
            'body'  : body
        }
        requests.post('https://api.pushbullet.com/v2/pushes', data=msg, auth=(self.token, ""))


    def push_link(self, title, body, url):
        if type(body) == list:
            body = '\n'.join(body)
        msg = {
            'type'  : 'link',
            'title' : title,
            'body'  : body,
            'url'   : url
        }
        requests.post('https://api.pushbullet.com/v2/pushes', data=msg, auth=(self.token, ""))


