from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from pandas import DataFrame
from teach.models import * # Import all the models created so far
from teach.forms import *
from django import forms
import googlemaps
from datetime import datetime
from django.contrib.auth.models import User # import User model
from teach.static.teach.images import * # Import all images
import random
import string
from django.contrib import messages
