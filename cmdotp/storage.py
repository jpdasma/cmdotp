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
import json
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class Storage(object):
    """
    """

    def __init__(self, password, *args, **kwargs):
        self.password = password
        self.key = self._generate_key(password)
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

    def export_encrypted(self, file_path, password=""):
        """
        """
        key = self.key if not password else self._generate_key(password)

    def export_plain_text(self, file_path):
        """
        """
        pass

    def _generate_key(self, password):
        pass

    def _encrypt(self, password=""):
        key = self.key if not password else self._generate_key(password)

    def _decrypt(self, password=""):
        key = self.key if not password else self._generate_key(password)

    def _json_to_binary(self):
        pass

    def _binary_to_json(self):
        pass
