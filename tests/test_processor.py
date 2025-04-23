"""
Tests for the transcript processor
"""

import unittest
import os
from src.transcript_processor import TranscriptProcessor
from src.utils import remove_timestamps

class TestProcessor(unittest.TestCase):
    """Test cases for transcript processing functionality"""
    
    def test_remove_timestamps(self):
        """Test timestamp removal function"""
        text = "Hello [00:15] this is a test [01:23] with timestamps."
        expected = "Hello  this is a test  with timestamps."
        self.assertEqual(remove_timestamps(text), expected)
    
    def test_load_from_file(self):
        """Test loading transcript from file"""
        # This is a placeholder test that would need a sample file
        processor = TranscriptProcessor()
        self.assertTrue(isinstance(processor, TranscriptProcessor))

if __name__ == '__main__':
    unittest.main()