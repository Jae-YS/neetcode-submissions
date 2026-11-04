class Twitter:

    def __init__(self):
        self.follows = {}
        self.tweets = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((-self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        candidates = list(self.tweets.get(userId, []))
        for followee in self.follows.get(userId, set()):
            candidates.extend(self.tweets.get(followee, []))

        heapq.heapify(candidates)
        feed = []
        while candidates and len(feed) < 10:
            _, tweetId = heapq.heappop(candidates)
            feed.append(tweetId)
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)