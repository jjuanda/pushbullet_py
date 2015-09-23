import requests



class PushBulletIF:
    def __init__(self, token):
        self.token = token

    def send(self, contents):
        if type(contents) == list:
            contents = '\n'.join(contents)
        msg = {
            'type'  : 'note',
            'title' : 'Tsdb update',
            'body'  : contents
        }
        requests.post('https://api.pushbullet.com/v2/pushes', data=msg, auth=(self.token, ""))


