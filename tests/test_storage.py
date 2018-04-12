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
import unittest
import os

from unittest.mock import MagicMock, patch
from cmdotp.storage import Storage

def mock_urandom(*args):
    return b'\xc1\xa6\xab\xd4\xb1g8\\1\x1f\x9fl\xf6\xb5\xe5r'


class TestStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = "/tmp/database"
        self.password = b"123"
        self.iterations = 100000
        self.storage = Storage(file_path=self.file_path, password=self.password, iterations=self.iterations)

    @patch('cmdotp.storage.os')
    def test__generate_key(self, mock_os):
        mock_os.urandom = mock_urandom
        key = self.storage._generate_key(password=self.password, iterations=self.iterations)
        self.assertEqual(b'Lsd0CvZoSWVLKGzFxr10OD5rvAcXe39oWseEyombBq0=', key)

    @patch('cmdotp.storage.Fernet')
    def test__encrypt(self, mock_fernet):
        self.storage._encrypt(b'Hello world', self.password, self.iterations)
        mock_fernet().encrypt.assert_called_with(b'Hello world')

    @patch('cmdotp.storage.Fernet')
    def test__decrypt(self, mock_fernet):
        self.storage._decrypt(b'sadasdasd', self.password, self.iterations)
        mock_fernet().decrypt.assert_called_with(b'sadasdasd')
        


if __name__ == '__main__':
    unittest.main()
