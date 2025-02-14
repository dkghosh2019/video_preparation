import unittest
import os
import json
from src.jbuilder.jsonBuilder import create_metadata_json  # Correct path!

class TestJsonBuilder(unittest.TestCase):

    def setUp(self):
        # ***CRITICAL: Use paths relative to the tests directory***
        self.test_data_dir = "test_data"  # Directory for test data (create this directory!)
        os.makedirs(self.test_data_dir, exist_ok=True) # Create test directory if it doesn't exist

        self.title_file = os.path.join(self.test_data_dir, "title.txt")
        self.description_file = os.path.join(self.test_data_dir, "description.txt")
        self.tags_file = os.path.join(self.test_data_dir, "tags.txt")
        self.metadata_file = os.path.join(self.test_data_dir, "metadata.txt")
        self.output_json_file = os.path.join(self.test_data_dir, "metadata.json")

        # Create dummy test files (This is what you were missing!)
        with open(self.title_file, "w", encoding="utf-8") as f:
            f.write("Test Title")
        with open(self.description_file, "w", encoding="utf-8") as f:
            f.write("Test Description")
        with open(self.tags_file, "w", encoding="utf-8") as f:
            f.write("tag1\ntag2")  # Two tags, each in a new line
        with open(self.metadata_file, "w", encoding="utf-8") as f:
            f.write("video_language = en\n")
            f.write("title_language = en\n")
            f.write("location_description = Test Location\n")
            f.write("video_category_id = 22\n")
            f.write("video_privacy_status = private\n")
            f.write("notify_subscribers = true\n")

    def tearDown(self):
        # Clean up (remove the files and directory)
        os.remove(self.title_file)
        os.remove(self.description_file)
        os.remove(self.tags_file)
        os.remove(self.metadata_file)
        if os.path.exists(self.output_json_file):
            os.remove(self.output_json_file)
        os.rmdir(self.test_data_dir) # Remove the test data directory


    def test_create_metadata_json(self):
        create_metadata_json(self.title_file, self.description_file, self.tags_file, self.metadata_file, self.output_json_file)

        # ... (rest of the test logic - same as before)
        # Check if the output file was created
        self.assertTrue(os.path.exists(self.output_json_file))

        # Optionally, check the content of the JSON file
        with open(self.output_json_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(data['video_title'], "Test Title")
            self.assertEqual(data['video_description'], "Test Description")
            self.assertEqual(data['video_keywords'], "tag1,tag2")
            self.assertEqual(data['video_language'], "en")
            self.assertEqual(data['title_language'], "en")
            self.assertEqual(data['location_description'], "Test Location")
            self.assertEqual(data['video_category_id'], "22")
            self.assertEqual(data['video_privacy_status'], "private")
            self.assertEqual(data['notify_subscribers'], True)



    # Example of other test cases
    def test_create_metadata_json_empty_files(self):
        # Create empty test files
        open(self.title_file, "w").close()
        open(self.description_file, "w").close()
        open(self.tags_file, "w").close()
        open(self.metadata_file, "w").close()

        create_metadata_json(self.title_file, self.description_file, self.tags_file, self.metadata_file, self.output_json_file)

        self.assertTrue(os.path.exists(self.output_json_file))
        with open(self.output_json_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(data['video_title'], "")
            self.assertEqual(data['video_description'], "")
            self.assertEqual(data['video_keywords'], "")
            # ... check other empty values

    def test_create_metadata_json_comments_only(self):
        with open(self.metadata_file, "w") as f:
            f.write("# video_language = en\n")  # Only comments
            f.write("# title_language = en\n")
            f.write("# location_description = Test Location\n")
            f.write("# video_category_id = 22\n")
            f.write("# video_privacy_status = private\n")
            f.write("# notify_subscribers = true\n")
        create_metadata_json(self.title_file, self.description_file, self.tags_file, self.metadata_file, self.output_json_file)
        self.assertTrue(os.path.exists(self.output_json_file))
        with open(self.output_json_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(data.get('video_language'), None)  # Check for default values or None

    def test_create_metadata_json_invalid_metadata_line(self):
        with open(self.metadata_file, "w") as f:
            f.write("video_language = en\n")
            f.write("invalid line\n")  # Invalid line
            f.write("title_language = en\n")
        create_metadata_json(self.title_file, self.description_file, self.tags_file, self.metadata_file, self.output_json_file)
        self.assertTrue(os.path.exists(self.output_json_file))
        with open(self.output_json_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(data['video_language'], "en")
            self.assertEqual(data.get('title_language'), "en")  # Check if other values are read correctly


if __name__ == '__main__':
    unittest.main()