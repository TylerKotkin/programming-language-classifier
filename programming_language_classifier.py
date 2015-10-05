import csv
import re
import pandas as pd
import numpy as np
import random
import glob

from collections import Counter, defaultdict, namedtuple
from sklearn.pipeline import make_pipeline, make_union
from sklearn.base import TransformerMixin
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix


def percentage_of_punctuation(text):
    total_length = len(text)
    text = re.sub(r'[\w\s]', '', text)
    punc_length = len(text)

    return punc_length*2 / total_length


def percentage_of_parenthesis(text):
    total_length = len(text)
    text = re.sub(r'\(', '', text)
    length = len(text)
    return length/total_length

def percentage_of_colon(text):
    total_length = len(text)
    text = re.sub(r':', '', text)
    length = len(text)
    return length/total_length

def percentage_of_def(text):
    total_length = len(text)
    text = re.sub(r'[def]', '', text)
    length = len(text)
    return length/total_length

def percentage_of_at(text):
    total_length = len(text)
    text = re.sub(r'[@]', '', text)
    length = len(text)
    return length/total_length

def percentage_of_star(text):
    total_length = len(text)
    text = re.sub(r'[\*]', '', text)
    length = len(text)
    return length/total_length

def percent_start_end_parenthesis(text):
    total_length = len(text)
    text = re.findall(r'((?:^|\n)\(.*\)(?:$|\n))', text)
    length = len(text)
    return length/total_length

def percentage_end_sc(text):
    total_length = len(text)
    text = re.sub(r'[;]$', '', text)
    length = len(text)
    return length/total_length

def word_function(text):
    result = re.findall(r'function', text)
    if result:
        return 1
    return 0

def word_nil(text):
    result = re.findall(r'\bnil\b', text)
    if result:
        return 1
    return 0

def word_null(text):
    result = re.findall(r'\bnull\b', text)
    if result:
        return 1
    return 0

def word_var(text):
    result = re.findall(r'\bvar\b', text)
    if result:
        return 1
    return 0

def percentage_ds(text):
    total_length = len(text)
    text = re.sub(r'[$]', '', text)
    length = len(text)
    return length/total_length

def word_bool(text):
    result = re.findall(r'\bbool\b', text)
    if result:
        return 1
    return 0


def word_tl(text):
    result = re.findall(r'\btaskLoop\b', text)
    if result:
        return 1
    return 0


def word_elsif(text):
    result = re.findall(r'\belsif\b', text)
    if result:
        return 1
    return 0

def hashes(text):
    result = re.findall(r'[.#]', text)
    if result:
        return 1
    return 0

def percentage(text):
    result = re.findall(r'[%]', text)
    if result:
        return 1
    return 0

def word_final(text):
    result = re.findall(r'\breturn\b', text)
    if result:
        return 1
    return 0

def word_def(text):
    result = re.findall(r'\bdef\b', text)
    if result:
        return 1
    return 0
