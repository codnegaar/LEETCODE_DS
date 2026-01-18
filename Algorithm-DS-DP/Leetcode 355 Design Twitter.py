'''

355 Design Twitter

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.
        Implement the Twitter class:
        Twitter() Initializes your twitter object.
        void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
        List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the
        user followed or by the user themself. Tweets must be ordered from most recent to least recent.
        void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
        void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 

Example 1:
        Input
        ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
        [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
        Output
        [null, null, [5], null, null, [6, 5], null, [5]]
        
        Explanation
        Twitter twitter = new Twitter();
        twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
        twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
        twitter.follow(1, 2);    // User 1 follows user 2.
        twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
        twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
        twitter.unfollow(1, 2);  // User 1 unfollows user 2.
        twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
 

Constraints:

1 <= userId, followerId, followeeId <= 500
0 <= tweetId <= 104
All the tweets have unique IDs.
At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.

'''

from collections import defaultdict

class Twitter(object):
    feedSize = 10

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followeeMap = defaultdict(set) # maps a person P to the set { Q | P follows Q }
        self.tweetRankMap = defaultdict(list) # maps a person to the list of tweet ranks of him
        self.tweetRankToID = dict() # maps a rank to the tweet id. Need this because higher tweet id does not guarantee it's later
        self.nextTweetRank = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweetRankMap[ userId ].append( self.nextTweetRank )
        self.tweetRankToID[ self.nextTweetRank ] = tweetId
        self.nextTweetRank += 1

        # just to save time, not absolutely necessary
        if len(self.tweetRankMap[ userId ]) > 2 * self.feedSize:
            self.tweetRankMap[userId] = self.tweetRankMap[ userId ][-self.feedSize:]

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        allTweetRanks = self.tweetRankMap[ userId ][-self.feedSize:]
        for followeeId in self.followeeMap[ userId ]:
            allTweetRanks.extend( self.tweetRankMap[ followeeId ][-self.feedSize:] )
        allTweetRanks.sort()
        newTweetRanks = allTweetRanks[-1:-self.feedSize-1:-1]

        return [ self.tweetRankToID[r] for r in newTweetRanks ]


    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId != followeeId:
            self.followeeMap[ followerId ].add( followeeId )

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId in self.followeeMap[ followerId ]:
            self.followeeMap[ followerId ].remove( followeeId )



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
