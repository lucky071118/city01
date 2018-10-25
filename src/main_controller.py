import summary
# import user_based_collaborative_filtering_recommendation as user_based_recommendation
# import item_based_collaborative_filtering_recommendation as item_based_recommendation
# import geographical_clustering_phenomenon_recommendation as geographical_recommendation
# import content_based_filtering_recommendation as content_based_recommendation
# import popularity_recommendation

def main():
    rank_dict = {}
    # rank_dict['user-based collaborative filtering'] = user_based_recommendation.recommend()
    # rank_dict['item-based collaborative filtering'] = item_based_recommendation.recommend()
    # rank_dict['geographical clustering phenomenon'] = geographical_recommendation.recommend()
    # rank_dict['content-based filtering'] = content_based_recommendation.recommend()
    # rank_dict['popularity'] = popularity_recommendation.recommend()
    summary.sum(rank_dict)

    

if __name__ == '__main__':
    main()