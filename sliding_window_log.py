'''Coding Problem 1: Rate Limiter (Sliding Window Log)
Implement a class-based Rate Limiter for an API endpoint that restricts a user to K requests per N seconds.'''

import time
from collections import deque

class RateLimiter:
    def __init__(self, max_requests:int, window_secs:int):
        self.max_requests=max_requests
        self.windows_secs=window_secs

        self.user_requests={}

    def allow_request(self, user_id:str)->bool:
        current_time = time.time()

        if user_id not in self.user_requests:
            self.user_requests[user_id]=deque()
        
        timestamps=self.user_requests[user_id]

        while timestamps and current_time-timestamps[0]>self.windows_secs:
            timestamps.popleft()
        
        if len(timestamps)<self.max_requests:
            timestamps.append(current_time)
            return True
        return False

limiter = RateLimiter(max_requests=11, window_secs=1)
for i in range(5):
    print(limiter.allow_request("user_1"))
    time.sleep(0.4)
