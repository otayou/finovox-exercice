"""
Test Cases for files Web Service
"""
from unittest import TestCase
import os
from service.app import app
from service import status

class FilesTest(TestCase):
    """Test Cases for files Web Service"""

    def setUp(self):
        self.folder_path = os.path.abspath("test_folder")
        app.config.update(FOLDER_PATH= self.folder_path)
        self.client = app.test_client()
        
    ############################################################
    #  T E S T   C A S E S
    ############################################################
    def test_index(self):
        """It should return the index page"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(b"Fichiers", response.data)

    def test_list_files(self):
        """It should return a list of files in the directory"""
        expected_files = os.listdir(self.folder_path)
        expected_files.sort()
        result = self.client.get("/api/files")
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        json_data = result.get_json()
        returned_files = json_data["files"]
        returned_files.sort()
        self.assertEqual(returned_files, expected_files)

    def test_download_file(self):
        """It should download a file in the directory"""
        test_filename = "test_file.txt"
        test_filepath = os.path.join(self.folder_path, test_filename)
        test_content = b"Hello, this is a test file."

        with open(test_filepath, "wb") as f:
            f.write(test_content)

        response = self.client.get(f"/download/{test_filename}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, test_content)
        self.assertIn("attachment", response.headers.get("Content-Disposition", ""))

    def test_download_file_not_found(self):
        """It should return 404 if the file does not exist"""
        non_existent_filename = "file_does_not_exist.txt"
        response = self.client.get(f"/download/{non_existent_filename}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn(b"File not found", response.data)

    def test_health(self):
        """It should be healthy"""
        response = self.client.get("/health")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.get_json()
        self.assertEqual(data['message'], 'OK')