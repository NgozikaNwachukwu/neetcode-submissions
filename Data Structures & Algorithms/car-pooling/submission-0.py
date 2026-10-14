class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Create an events array to track pickups and drop-offs
        events = []

        for i, trip in enumerate(trips):
            passengers, pickup, dropoff = trips[i]
            #could also write: for i, trip in enumerate(trips):
                                    #passengers = trip[0]
                                    #pickup = trip[1]
                                    #dropoff = trip[2]

            # Positive passengers means pickup
            events.append((pickup, passengers))

            # Negative passengers means drop-off
            events.append((dropoff, -passengers))

        # Convert events into a min heap
        # Smallest kilometre will be popped first
        heapq.heapify(events)

        # Track the number of passengers currently in the car
        currentPassengers = 0

        while events:

            # Get the next pickup or drop-off event
            km, passengers = heapq.heappop(events)

            # Add passengers for pickup, subtract for drop-off
            currentPassengers += passengers

            # If we exceed capacity, the trip is impossible
            if currentPassengers > capacity:
                return False

        # All trips were completed without exceeding capacity
        return True

    
# TIME COMPLEXITY: O(n log n)
# - Let n be the number of trips.
# - The first for loop runs n times: O(n).
# - Each trip creates 2 events (pickup and drop-off), so events contains 2n elements.
# - heapq.heapify(events) takes O(2n) = O(n).
# - The while loop runs 2n times because we pop every event from the heap.
# - Each heappop() takes O(log(2n)) = O(log n).
# - All 2n heap pops therefore take O(2n * log(2n)) = O(n log n).
# - Overall: O(n) + O(n) + O(n log n) = O(n log n).

# SPACE COMPLEXITY: O(n)
# - The events array stores 2 events for each of the n trips: O(2n).
# - heapq.heapify() modifies events in place, so it does not create another heap.
# - Variables like currentPassengers, km, and passengers use O(1) space.
# - Overall: O(2n) + O(1) = O(n).


        