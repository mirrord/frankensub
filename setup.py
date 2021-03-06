#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

long_description = (
    'frankensub is a utility for automatic speech recognition and subtitle generation. '
    'It takes a video or an audio file as input, performs voice activity detection '
    'to find speech regions, makes parallel requests to Google Web Speech API to '
    'generate transcriptions for those regions, (optionally) translates them to a '
    'different language, and finally saves the resulting subtitles to disk. '
    'It supports a variety of input and output languages (to see which, run the '
    'utility with --list-src-languages and --list-dst-languages as arguments '
    'respectively) and can currently produce subtitles in either the SRT format or '
    'simple JSON.'
)

setup(
    name='frankensub',
    version='0.0.1',
    description='Auto-generates subtitles for any video or audio file',
    long_description=long_description,
    author='Anastasis Germanidis, Dane Howard',
    author_email='agermanidis@gmail.com, mirrord@gmail.com',
    url='https://github.com/mirrord/frankensub',
    packages=['frankensub'],
    install_requires=[
        'pydub>=0.24.1',
        'deep_translator>=1.3.4',
        'SpeechRecognition>=3.8.1',
        'pysrt>=1.0.1',
        'progressbar2>=3.34.3',
        'six>=1.11.0',
    ],
    license=open("LICENSE").read()
)
