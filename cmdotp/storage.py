# -*- coding: utf-8 -*-
# Copyright (C) 2018 Julian Paul Dasmariñas
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import os
import base64
import json

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Storage(object):
    """
    """

    def __init__(self, file_path, password, iterations=100000, *args, **kwargs):
        self.file_path = file_path
        self.password = password
        self.iterations = iterations
        self.key = self._generate_key(password, iterations)
        self.args = args
        self.kwargs = kwargs

    def write(self):
        """
        """
        pass

    def read(self):
        """
        """
        pass

    def export_encrypted(self, file_path, password="", iterations=100000):
        """
        """
        key = self.key if not password else self._generate_key(password, iterations)

    def export_plain_text(self, file_path):
        """
        """
        pass

    def _generate_key(self, password, iterations=100000):
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=iterations, backend=default_backend())
        return base64.urlsafe_b64encode(kdf.derive(password))

    def _encrypt(self, word=b"", password="", iterations=100000):
        key = self.key if not password else self._generate_key(password, iterations)
        fernet = Fernet(key)
        return fernet.encrypt(word)

    def _decrypt(self, word=b"", password="", iterations=100000):
        key = self.key if not password else self._generate_key(password, iterations)
        fernet = Fernet(key)
        return fernet.decrypt(word)

    def _json_to_binary(self):
        pass

    def _binary_to_json(self):
        pass
