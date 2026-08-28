# 355. Design Twitter
# https://leetcode.com/problems/design-twitter/
# Medium

from collections import defaultdict
from typing import List


class Twitter:
    def __init__(self):
        raise Exception("Not solved yet")

    def postTweet(self, userId: int, tweetId: int) -> None:
        raise Exception("Not solved yet")

    def getNewsFeed(self, userId: int) -> List[int]:
        raise Exception("Not solved yet")

    def follow(self, followerId: int, followeeId: int) -> None:
        raise Exception("Not solved yet")

    def unfollow(self, followerId: int, followeeId: int) -> None:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def test_example1(self):
        t = Twitter()
        t.postTweet(1, 5)
        self.assertEqual(t.getNewsFeed(1), [5])
        t.follow(1, 2)
        t.postTweet(2, 6)
        self.assertEqual(t.getNewsFeed(1), [6, 5])
        t.unfollow(1, 2)
        self.assertEqual(t.getNewsFeed(1), [5])

    def test_empty_feed(self):
        t = Twitter()
        self.assertEqual(t.getNewsFeed(1), [])

    def test_user_sees_own_tweets_without_following(self):
        t = Twitter()
        t.postTweet(1, 1)
        t.postTweet(1, 2)
        self.assertEqual(t.getNewsFeed(1), [2, 1])

    def test_feed_ignores_unfollowed_users(self):
        t = Twitter()
        t.postTweet(2, 1)
        t.postTweet(3, 2)
        self.assertEqual(t.getNewsFeed(1), [])

    def test_feed_shows_followed_users(self):
        t = Twitter()
        t.follow(1, 2)
        t.postTweet(2, 17)
        t.postTweet(1, 9)
        self.assertEqual(t.getNewsFeed(1), [9, 17])

    def test_unfollow_removes_tweets_from_feed(self):
        t = Twitter()
        t.follow(1, 2)
        t.postTweet(2, 1)
        t.unfollow(1, 2)
        self.assertEqual(t.getNewsFeed(1), [])

    def test_unfollow_non_followed_user_is_noop(self):
        t = Twitter()
        t.postTweet(2, 1)
        t.unfollow(1, 2)
        self.assertEqual(t.getNewsFeed(1), [])

    def test_limit_to_ten_most_recent(self):
        t = Twitter()
        for i in range(1, 21):
            t.postTweet(1, i)
        self.assertEqual(t.getNewsFeed(1), list(range(20, 10, -1)))

    def test_limit_mixed_authors(self):
        t = Twitter()
        t.follow(1, 2)
        for i in range(1, 11):
            t.postTweet(1, 100 + i)
        for i in range(1, 13):
            t.postTweet(2, 200 + i)
        self.assertEqual(
            t.getNewsFeed(1), [212, 211, 210, 209, 208, 207, 206, 205, 204, 203]
        )

    def test_follow_then_post_then_unfollow_cycle(self):
        t = Twitter()
        t.follow(1, 2)
        t.postTweet(2, 10)
        t.unfollow(1, 2)
        t.follow(1, 2)
        self.assertEqual(t.getNewsFeed(1), [10])
        t.unfollow(1, 2)
        self.assertEqual(t.getNewsFeed(1), [])

    def test_follow_replaces_multiple_relationships(self):
        t = Twitter()
        t.follow(1, 2)
        t.follow(1, 3)
        t.postTweet(2, 5)
        t.postTweet(3, 6)
        self.assertEqual(t.getNewsFeed(1), [6, 5])
        t.unfollow(1, 2)
        self.assertEqual(t.getNewsFeed(1), [6])
        t.unfollow(1, 3)
        self.assertEqual(t.getNewsFeed(1), [])

    def test_followee_own_feed_unchanged_by_follower(self):
        t = Twitter()
        t.follow(1, 2)
        t.postTweet(2, 5)
        self.assertEqual(t.getNewsFeed(2), [5])
        self.assertEqual(t.getNewsFeed(1), [5])

    def test_follow_self_is_ignored(self):
        t = Twitter()
        t.follow(1, 1)
        self.assertEqual(t.getNewsFeed(1), [])
        t.postTweet(1, 5)
        self.assertEqual(t.getNewsFeed(1), [5])

    def test_unfollow_self_is_noop(self):
        t = Twitter()
        t.postTweet(1, 5)
        t.unfollow(1, 1)
        self.assertEqual(t.getNewsFeed(1), [5])

    def test_tweet_zero_id(self):
        t = Twitter()
        t.postTweet(1, 0)
        self.assertEqual(t.getNewsFeed(1), [0])

    def test_recency_by_post_order_not_tweet_id(self):
        t = Twitter()
        t.postTweet(1, 10000)
        t.postTweet(1, 1)
        self.assertEqual(t.getNewsFeed(1), [1, 10000])

    def test_max_ids_in_range(self):
        t = Twitter()
        t.follow(500, 499)
        t.postTweet(499, 10000)
        t.postTweet(500, 9999)
        self.assertEqual(t.getNewsFeed(500), [9999, 10000])

    def test_many_users_star_follow(self):
        t = Twitter()
        for i in range(2, 501):
            t.follow(1, i)
            t.postTweet(i, i)
        feed = t.getNewsFeed(1)
        self.assertEqual(feed, list(range(500, 490, -1)))

    def test_follow_after_posting(self):
        t = Twitter()
        t.postTweet(2, 7)
        t.follow(1, 2)
        self.assertEqual(t.getNewsFeed(1), [7])


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, Linked List, Design, Heap (Priority Queue)
