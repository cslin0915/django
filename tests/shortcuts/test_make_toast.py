#!/usr/bin/python
# -*- coding: utf-8 -*-
""" Short Description
"""
from django.shortcuts import make_toast
from django.test import SimpleTestCase


class MakeToastTestCase(SimpleTestCase):
    def test_make_toast(self):
        self.assertEqual(make_toast(), "toast")
