import unittest
import summary

class TestSummary(unittest.TestCase):
        

    def test_compute_score(self):
        keys = list(summary.INDEPENDENT_VARIABLE_DICT.keys())
        key1 = keys[0]
        key2 = keys[1]
        key3 = keys[2]
        summary.INDEPENDENT_VARIABLE_DICT[key1] = 1
        summary.INDEPENDENT_VARIABLE_DICT[key2] = 1
        summary.INDEPENDENT_VARIABLE_DICT[key3] = 1
        rank_dict1 = {
            'user1':['a','b','c','e','d'],
            'user2':['d','b','a','e','c'],
            'user3':['e','b','c','a','d'],
        }
        rank_dict2 = {
            'user1':['b','a','e','c','d'],
            'user2':['d','b','a','e','c'],
            'user3':['b','a','e','c','d'],
        }
        rank_dict3 = {
            'user1':['b','a','e','c','d'],
            'user2':['d','b','a','e','c'],
            'user3':['b','a','e','c','d'],
        }
        all_recommendation_rank_dict = dict()
        all_recommendation_rank_dict[key1] = rank_dict1
        all_recommendation_rank_dict[key2] = rank_dict2
        all_recommendation_rank_dict[key3] = rank_dict3
        
        all_user_score = summary.compute_score(all_recommendation_rank_dict)

        self.assertEqual(len(all_user_score), 3)
        
        # user1
        self.assertEqual(len(all_user_score['user1']), 5)
        self.assertEqual(all_user_score['user1']['a'], 298)
        self.assertEqual(all_user_score['user1']['b'], 299)
        self.assertEqual(all_user_score['user1']['c'], 292)
        self.assertEqual(all_user_score['user1']['d'], 288)
        self.assertEqual(all_user_score['user1']['e'], 293)

        # user2
        self.assertEqual(len(all_user_score['user2']), 5)
        self.assertEqual(all_user_score['user2']['a'], 294)
        self.assertEqual(all_user_score['user2']['b'], 297)
        self.assertEqual(all_user_score['user2']['c'], 288)
        self.assertEqual(all_user_score['user2']['d'], 300)
        self.assertEqual(all_user_score['user2']['e'], 291)

        # user3
        self.assertEqual(len(all_user_score['user3']), 5)
        self.assertEqual(all_user_score['user3']['a'], 295)
        self.assertEqual(all_user_score['user3']['b'], 299)
        self.assertEqual(all_user_score['user3']['c'], 292)
        self.assertEqual(all_user_score['user3']['d'], 288)
        self.assertEqual(all_user_score['user3']['e'], 296)

    def test_create_output_rank(self):
        all_user_score = {}
        all_user_score['user1'] = {
            'a': 298,
            'b': 299,
            'c': 292,
            'd': 288,
            'e': 293
        }
        all_user_score['user2'] = {
            'a': 294,
            'b': 297,
            'c': 288,
            'd': 300,
            'e': 291
        }

        all_user_score['user3'] = {
            'a': 295,
            'b': 299,
            'c': 292,
            'd': 288,
            'e': 296
        }
        
        result = summary.create_output_rank(all_user_score)
        self.assertEqual(len(result), 3)

        self.assertEqual(len(result['user1']), 5)
        self.assertEqual(len(result['user2']), 5)
        self.assertEqual(len(result['user3']), 5)

        # user1
        self.assertEqual(result['user1'][0], 'b')
        self.assertEqual(result['user1'][1], 'a')
        self.assertEqual(result['user1'][2], 'e')
        self.assertEqual(result['user1'][3], 'c')
        self.assertEqual(result['user1'][4], 'd')
        # user2
        self.assertEqual(result['user2'][0], 'd')
        self.assertEqual(result['user2'][1], 'b')
        self.assertEqual(result['user2'][2], 'a')
        self.assertEqual(result['user2'][3], 'e')
        self.assertEqual(result['user2'][4], 'c')
        # user3
        self.assertEqual(result['user3'][0], 'b')
        self.assertEqual(result['user3'][1], 'e')
        self.assertEqual(result['user3'][2], 'a')
        self.assertEqual(result['user3'][3], 'c')
        self.assertEqual(result['user3'][4], 'd')
        



if __name__ == '__main__':
    unittest.main()

