import pytest
import os
import json


def speak(self):
    return "ook ook eee eee eee!"


def dump_config(config):
    path = os.path.expanduser('~/.conf.json')
    with open(path, 'w', encoding='utf-8') as wr:
        json.dump(config, wr, indent=4)  # indent缩进


def test_config():
    dump_config(config)
    path = os.path.expanduser('~/.conf.json')
    expected = json.load(open(path, 'r', encoding='utf-8'))
    assert expected == config


def test_config_monkeypatch(tmpdir, monkeypatch):
    monkeypatch.setenv('HOME', tmpdir.mkdir('home'))

    dump_config(config)
    path = os.path.expanduser('~/.conf.json')
    expected = json.load(path, 'r', encoding='utf-8')
    assert expected == config


def test_config_monkeypatch2(tmpdirm, monkeypatch):
    fake_home = tmpdir.mkdir('home')
    monkeypatch.setattr(os.path, 'expanduser', lambda x: x.replace('~', str(fake_home)))
    dump_config(config)
    path = os.path.expanduser('~/.config.json')
    expected = json.load(open(path, 'r', encoding='utf-8'))
    assert expected == config
