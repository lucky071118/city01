import unittest
import write_file

class TestWriteFile(unittest.TestCase):

    def test_write_result_file(self):
        sum_result = dict()
        sum_result['user1'] = ['a','b','c','d','e']
        sum_result['user2'] = ['b','a','c','d','e']
        sum_result['user3'] = ['a','b','c','e','d']
        write_file.write_result_file(sum_result)


        with open(write_file.FILE_NAME,'r') as read_file:
            content = read_file.readlines()
            # user1
            user_name = content[0].split(':')[0]
            location_list = content[0].split(':')[1]
            self.assertEqual(user_name, 'user1')
            self.assertEqual(location_list, 'a,b,c,d,e\n')
            # user2
            user_name = content[1].split(':')[0]
            location_list = content[1].split(':')[1]
            self.assertEqual(user_name, 'user2')
            self.assertEqual(location_list, 'b,a,c,d,e\n')
            # user3
            user_name = content[2].split(':')[0]
            location_list = content[2].split(':')[1]
            self.assertEqual(user_name, 'user3')
            self.assertEqual(location_list, 'a,b,c,e,d\n')

if __name__ == '__main__':
    unittest.main()