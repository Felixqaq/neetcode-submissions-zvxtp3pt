import copy

class Twitter:
    def __init__(self):
        self.tweet = {}
        self.time = 0
        self.following = {}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        maxheap = self.tweet.get(userId, [])
        heapq.heappush(maxheap, [-self.time, tweetId])
        self.tweet[userId] = maxheap

        followers = self.following.get(userId, set())
        followers.add(userId)
        self.following[userId] = followers

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        followers = self.following.get(userId, set())
        maxFeed = 10
        tempTweet = copy.deepcopy(self.tweet)

        while maxFeed:
            mf = None
            maxTime = 0
            maxTweet = None

            for follower in followers:
                maxheap = tempTweet.get(follower)
                if maxheap and -1 * maxheap[0][0] > maxTime:
                    mf = follower
                    maxTweet = maxheap[0][1]
                    maxTime = -1 * maxheap[0][0]

            if maxTweet:
                res.append(maxTweet)
                heapq.heappop(tempTweet[mf])

            maxFeed -= 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        followers = self.following.get(followerId, set())
        followers.add(followeeId)
        self.following[followerId] = followers

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        followers = self.following.get(followerId, set())
        followers.discard(followeeId)
        self.following[followerId] = followers
