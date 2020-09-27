import unittest
import logic

class Test_TestIncrementDecrement(unittest.TestCase):
    def setUp(self):
        self.sample_data = [
            {
                'next_field_slug':'slugA',
                'conditions':
                [
                    {
                            'operand':'>',
                            'answer':'20',
                            'logical_operand':'and'
                    }
                    ,{
                            'operand':'<=',
                            'answer':'30',
                            'logical_operand':'or'
                    }
                ]
            },
            {
                'next_field_slug':'slugB',
                'conditions':
                [
                    {
                            'operand':'<=',
                            'answer':'20',
                            'logical_operand':'or'
                    }
                ]
            },
            {
                'next_field_slug':'slugC',
                'conditions':
                [
                    {
                            'operand':'>',
                            'answer':'30',
                            'logical_operand':'or'
                    }
                ]
            }
        ]
    def test_get_field(self):
        self.assertEqual(logic.get_next_field(self.sample_data), 'slugA')


if __name__ == '__main__':
    unittest.main()