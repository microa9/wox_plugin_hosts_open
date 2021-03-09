#!/usr/bin/python
# -*- coding: utf-8 -*-

from wox import Wox, WoxAPI
import shlex
import winreg
import subprocess

class Main(Wox):

    def query(self, key):

        return [{  # 選択時に呼ばれるメソッド名
            'Title': 'Open hosts.',
            'SubTitle': 'Open hosts.',
            'IcoPath': 'icon.png',
            'JsonRPCAction': {'method': 'action', 'parameters': [],
                              'dontHideAfterAction': False},
            }]

    def action(self):
        subprocess.Popen([self.get_default_windows_app('.txt'),
                         r'C:\Windows\System32\drivers\etc\hosts'])
        pass

    def get_default_windows_app(self, suffix):
            class_root = winreg.QueryValue(winreg.HKEY_CLASSES_ROOT, suffix)
            with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r'{}\shell\open\command'.format(class_root)) as key:
                command = winreg.QueryValueEx(key, '')[0]
                return shlex.split(command)[0]


if __name__ == '__main__':
    Main()
