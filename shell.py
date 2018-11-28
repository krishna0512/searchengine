from django.urls import reverse
from django.test.utils import setup_test_environment
from django.contrib.auth.models import User

from searchengine.models import *
# from searchengine.forms import *
# import requests
import os
import sys
import random
# from tabulate import tabulate

setup_test_environment()

from django.test import Client
c = Client()
