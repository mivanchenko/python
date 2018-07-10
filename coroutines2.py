import requests

from tornado import gen, ioloop

@gen.coroutine
def fetch_coroutine(url):
    response = yield requests.get(url)
    return response.body

@gen.coroutine
def fetch_coroutine2(url):
    yield requests.get(url)

async def fetch_coroutine_async(url):
    yield requests.get(url)
#    response = yield requests.get(url)
#    return response

async def fetch_coroutine_async2(url):
    await requests.get(url)

async def fetch_coroutine_async3(url):
    await fetch_coroutine(url)

async def fetch_coroutine_async4(url):
    yield fetch_coroutine2(url)

#fetch_coroutine('http://example.com')

#ioloop.IOLoop.current().spawn_callback( fetch_coroutine_async, 'http://example.com' )
#ioloop.IOLoop.current().spawn_callback( fetch_coroutine_async3, 'http://example.com' )
#ioloop.IOLoop.current().spawn_callback( fetch_coroutine_async4, 'http://example.com' )


@gen.coroutine
def fetch_coroutine3(url):
    yield fetch_coroutine_async2(url)

fetch_coroutine3('http://example.com')
