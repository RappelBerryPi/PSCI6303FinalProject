#!/usr/bin/env python

import random
import math

voting_preference_major = ["D", "R"]
voting_preference_minor = ["O", "I"]
voting_plan_2024_major = ["D", "R"]
voting_plan_2024_minor = ["O", "I"]

random.seed(1234)
with open("0-data/experiment_data.csv", "w") as f:
    f.write("general_voting_preference, number_of_troll_tweets_seen, number_of_troll_tweets_interacted_with, number_of_troll_tweets_reported, voting_plan_2024, treated\n")
    for i in range(0, 500):

        # select general_voting_preference
        general_voting_preference = random.choice(voting_preference_major)
        if (random.random() < 0.25):
            general_voting_preference = random.choice(voting_preference_minor)

        # select voting plan for 2024
        voting_plan_2024 = random.choice(voting_plan_2024_major)
        if (random.random() < 0.25):
            voting_plan_2024 = random.choice(voting_plan_2024_minor)

        # randomly generate the effected and non-effected users
        number_of_troll_tweets_seen = random.randint(0, 250)
        if (random.random() > 0.6):
            number_of_troll_tweets_interacted_with = random.randint(0, number_of_troll_tweets_seen)
            number_of_troll_tweets_reported = 0
            treated = False
        else:
            if (random.random() > 0.5):
                number_of_troll_tweets_interacted_with = random.randint(0, number_of_troll_tweets_seen)
            else:
                number_of_troll_tweets_interacted_with = random.randint(0, math.floor(number_of_troll_tweets_seen / 2))
            number_of_troll_tweets_reported = random.randint(0, number_of_troll_tweets_seen - number_of_troll_tweets_interacted_with)

            # set the voting plan to be the same unless the following conditions are tru
            old_voting_plan = voting_plan_2024
            voting_plan_2024 = general_voting_preference
            if number_of_troll_tweets_reported > number_of_troll_tweets_interacted_with:
                if (random.random() < 0.1):
                    voting_plan_2024 = old_voting_plan
            else:
                if (random.random() > 0.1):
                    voting_plan_2024 = old_voting_plan
            treated = True
        f.write("{},{},{},{},{},{}\n".format(general_voting_preference, number_of_troll_tweets_seen, number_of_troll_tweets_interacted_with, number_of_troll_tweets_reported, voting_plan_2024, treated))
