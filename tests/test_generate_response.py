import unittest
from unittest.mock import patch
from src.ui.interface import generate_response
from src.llm.google_llm import GoogleLLM


class TestGenerateResponse(unittest.TestCase):

    @patch.object(GoogleLLM, '_call')
    def test_successful_response(self, mock_call):
        mock_call.return_value = "This is a test response."
        response = generate_response("test prompt")
        self.assertEqual(response, "This is a test response.")
        mock_call.assert_called_once()

    @patch.object(GoogleLLM, '_call')
    def test_api_failure(self, mock_call):
        mock_call.side_effect = Exception("API error")
        response = generate_response("test prompt")
        self.assertEqual(response, "An error occurred.")  # Or handle differently
        mock_call.assert_called_once()