import unittest
from unittest.mock import MagicMock, patch
from lambda_function import lambda_handler

class TestLambdaHandler(unittest.TestCase):
    @patch('lambda_function.boto3')
    def test_labmda_handler(self, mock_boto3):
        dynamodb = mock_boto3.resource.return_value
        table = dynamodb.Table.return_value

        mock_response = {'Item': {'id': '1', 'views': 5}}
        table.get_item.return_value = mock_response

        event = {}
        context = MagicMock()
        result = lambda_handler(event, context)

        self.assertEqual(result, 6)
        
        table.put_item.assert_called_with(Item={'id': '1', 'views': 6})

if __name__ == '__main__':
    unittest.main()