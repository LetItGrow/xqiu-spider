# -*-coding=utf-8-*-
import logging
import requests
from HD.headers import HEADER,AUTH, RETRY

logger = logging.getLogger("CK")
logging.info('use CK')

class FetchCookies():
    def __init__(self,url = 'https://xueqiu.com/snowman/login'):
        self.url = url
        self.session = requests.session()

    def dictcookies(self):
        count = 0
        self.session.cookies.clear_session_cookies()
        logging.info('self.session.CK.clear_session_cookies(): %s' % dict(self.session.cookies))
        while count < RETRY:
            if(dict(self.session.cookies) =={}):
                try:
                    logging.info('fetch login text: %s' % self.session.post(self.url, headers=HEADER))
                    logging.info('fetch CK: %s' % dict(self.session.cookies))
                    count += 1
                except Exception as e:
                    logging.error('Exception: %s' % e)
                    logging.info('fetch login text: %s' % self.session.post(self.url, headers=HEADER,data=AUTH,verify=False))
                    logging.info('fetch CK: %s' % dict(self.session.cookies))
                    count += 1
                return dict(self.session.cookies)

if __name__ == '__main__':
    pass