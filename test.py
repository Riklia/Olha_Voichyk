from common import DropboxTest
import unittest

global test
test = DropboxTest()


def test_upload_file():
    response = test.upload_file()
    assert response.status_code == 200


def test_get_file_metadata():
    response = test.get_file_metadata()
    assert response.status_code == 200


def test_delete_file():
    response = test.delete_file()
    assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
