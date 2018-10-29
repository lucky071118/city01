import summary
import write_file
import model_validation
import configparser
import collaborative_filtering
import home_recommendation
import content_based_recommendation
import popularity_recommendation
import average_location_recommendation

config = configparser.ConfigParser()
config.read('setting.config')
do_validation = config['VALIDATION']['do_validation']


def main():
    rank_dict = {}
    rank_dict['collaborative_filtering'] = collaborative_filtering.recommend()
    rank_dict['home'] = home_recommendation.recommend()
    rank_dict['content_based_filtering'] = content_based_recommendation.recommend()
    rank_dict['popularity'] = popularity_recommendation.recommend()
    rank_dict['average_location'] = average_location_recommendation.recommend()
    sum_result = summary.sum(rank_dict)
    write_file.write_result_file(sum_result)

    if do_validation == 'yes':
        model_validation.test_result()
    

if __name__ == '__main__':
    main()