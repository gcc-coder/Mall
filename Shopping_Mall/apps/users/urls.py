#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time: 2020/7/27 16:45
@Author: Rick
@Contact：firelong.guo@hotmail.com 
@File: urls.py
@Software: PyCharm
@Description:
"""
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='re'),

]