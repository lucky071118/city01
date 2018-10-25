
FILE_NAME = 'result.txt'

def write_result_file(sum_result):
    with open(FILE_NAME,'w') as output_file:
        for user_name, location_rank_list in sum_result.items():
            output_file.write(user_name)
            output_file.write(':')
            for index, location in enumerate(location_rank_list):
                output_file.write(location)
                if index < len(location_rank_list)-1:
                    output_file.write(',')
                else:
                    output_file.write('\n')

if __name__ == '__main__':
    pass