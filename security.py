#-*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

from hashlib import md5
import requests
import json

class ApiAuthBackend(ModelBackend):

    def authenticate(self, request, username, password):

        password = md5(password.encode('utf-8')).hexdigest()

        url = 'http://127.0.0.1:8000/apis/login/'
        result = requests.post(url, data={'login': username, 'senha': password})

        data = json.loads(result.content)

        token = data['token']
        usuario = data[username]

        request.session['token'] = token

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(username=username)
            user.password = usuario['password']
            user.email = usuario['email']
            user.first_name = usuario['first_name']
            user.last_name = usuario['last_name']
            user.is_active = usuario['is_active']
            user.save()

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
