# -*- coding: utf-8 -*-
import sys
from . import colors
from .utils import join_args, join_args_and_kwargs

@join_args_and_kwargs
def success(message, details):
    if details:
        message = '{} ({})'.format(message, details)
    print(colors.green + message + colors.default)

@join_args_and_kwargs
def warning(message, details):
    if details:
        message = '{} ({})'.format(message, details)
    print(colors.yellow + message + colors.default)

@join_args_and_kwargs
def failure(message, details):
    if details:
        message = '{} ({})'.format(message, details)
    print(colors.red + message + colors.default)

@join_args_and_kwargs
def error(message, details):
    if details:
        message = '{} ({})'.format(message, details)
    sys.exit(colors.red + message + colors.default)

@join_args
def unknown_error(message):
    fcode = sys._getframe(1).f_code
    sys.exit(colors.red + '{}:{} {}'.format(fcode.co_filename, fcode.co_name, message) + colors.default)

