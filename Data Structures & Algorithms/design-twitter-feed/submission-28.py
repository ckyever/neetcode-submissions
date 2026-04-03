class Twitter:

    def __init__(self):
        self.followers = defaultdict(set) # user_id: set[followee ids]
        self.tweets = defaultdict(list) # user_id: [[time, tweetId, userId, previousIndex]]
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        previousIndex = len(self.tweets[userId]) - 1
        self.tweets[userId].append([self.time, tweetId, userId, previousIndex])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.followers[userId]
        followees.add(userId)
        minHeap = []

        for userId in followees:
            if self.tweets[userId]:
                minHeap.append(self.tweets[userId][-1])

        heapq.heapify(minHeap)

        newsfeed = []
        while len(newsfeed) < 10 and minHeap:
            _, tweetId, userId, nextTweetIndex = heapq.heappop(minHeap)
            newsfeed.append(tweetId)
            if nextTweetIndex >= 0:
                heapq.heappush(minHeap, self.tweets[userId][nextTweetIndex])

        return newsfeed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            if followeeId in self.followers[followerId]:
                self.followers[followerId].remove(followeeId)
