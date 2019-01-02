#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Leon Tang' 

' url handlers '
import time
from coroweb import get
from models import User, Blog

@get('/users')
async def all_users(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }

@get('/')
async def index(request):
    summary = 'No pains, no gains. With talents, great success!'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time()-120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time()-3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time()-7200)
        ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }
