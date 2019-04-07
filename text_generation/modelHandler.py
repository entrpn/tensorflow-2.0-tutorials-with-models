import tornado
import tornado.ioloop
from tornado.web import RequestHandler
from tornado import concurrent
from tornado.concurrent import Future
from datetime import datetime
from tornado import gen


class ModelHandler(RequestHandler):
    executor = concurrent.futures.ThreadPoolExecutor(5)

    def initialize(self, model):
        print('created')
        self.model = model

    async def post(self):
        body = tornado.escape.json_decode(self.request.body)
        print('Text: ', body['text'])
        gen_text = await tornado.ioloop.IOLoop.current().run_in_executor(None, self.model.generate_text, body['text'])
        self.write(gen_text)
