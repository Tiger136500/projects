from www.models_test import User
from www.coroweb import get
import asyncio


@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }
