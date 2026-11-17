import collections
import heapq

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = collections.defaultdict(list)  # userId -> list of [count, tweetId]
        self.followMap = collections.defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # Ensure a user always follows themselves
        self.followMap[userId].add(userId)

        # Collect the most recent tweet pointer from each followee
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                # Push negative count for max-heap behavior, along with tweetId, followeeId, and index
                heapq.heappush(minHeap, (-count, tweetId, followeeId, index - 1))

        # Extract up to 10 most recent tweets
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, nextIndex = heapq.heappop(minHeap)
            res.append(tweetId)
            
            # If there are more tweets from this followee, push the next recent one
            if nextIndex >= 0:
                prev_count, prev_tweetId = self.tweetMap[followeeId][nextIndex]
                heapq.heappush(minHeap, (-prev_count, prev_tweetId, followeeId, nextIndex - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId] and followerId != followeeId:
            self.followMap[followerId].remove(followeeId)