class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. Pair up position and speed, and sort them from closest to the finish line to furthest back
        # The core rule of the highway is: CARS CANNOT PASS EACH OTHER. 
        # Because of this, cars driving AHEAD act as moving roadblocks. They 
        # dictate the ultimate speed of any faster cars trapped behind them.
        #
        # 1. WHY WE SORT:
        # LeetCode gives us the cars scattered completely out of order in the 
        # input arrays. To analyze a traffic jam, we must line them up exactly 
        # as they sit on the actual pavement so we know who is behind whom.
        #
        # 2. WHY WE REVERSE (reverse=True):
        # We reverse the sort to process the cars from CLOSEST to the finish 
        # line to FURTHEST back. This allows us to process the absolute 
        # "leader" of the road first, establishing the speed of the roadblock.
        # As we work our way backward through the highway, we can easily see if 
        # the trailing cars are fast enough to crash into that leader.
        #
        # VISUAL EXAMPLE (Example 2):
        # ---------------------------------------------------------------------
        # Unsorted Scrambled Input: Positions = [4, 1, 0, 7]
        # (If we loop now, we check Mile 4, then Mile 1... we are completely 
        # blind to the leader sitting ahead of everyone at Mile 7!)
        #
        # After sorting with reverse=True, our highway looks perfect:
        #   Index 0 -> (7, 1)  <- Absolute Leader! We process this first.
        #   Index 1 -> (4, 2)  <- Stuck directly behind the leader.
        #   Index 2 -> (1, 2)  <- Trailing further back.
        #   Index 3 -> (0, 1)  <- At the very back of the highway.
        cars = sorted(zip(position, speed), reverse=True)
        stack = [] # Holds the finish times of our active fleets
        # Because 'cars_list' is a list of pairs—like [(7, 1), (4, 2), (1, 2)]—
        # Python uses a trick called "unpacking" to automatically split each 
        # pair apart on every single turn of the loop.
        #
        # Instead of grabbing the whole pair as a single item, Python captures
        # the individual members of the pair and assigns them to your variables:
        #   - 'p' always captures the 1st member (the Position number)
        #   - 's' always captures the 2nd member (the Speed number)
        #
        # 🚶 STEP-BY-STEP EXAMPLE WALKTHROUGH:
        # ---------------------------------------------------------------------
        # Turn 1: Loop grabs the first pair -> (7, 1)
        #         Python automatically sets: p = 7  and  s = 1
        #         Math: (target - p) / s -> (10 - 7) / 1 = 3.0 hours
        #
        # Turn 2: Loop grabs the next pair  -> (4, 2)
        #         Python automatically sets: p = 4  and  s = 2
        #         Math: (target - p) / s -> (10 - 4) / 2 = 3.0 hours
        #
        # Turn 3: Loop grabs the next pair  -> (1, 2)
        #         Python automatically sets: p = 1  and  s = 2
        #         Math: (target - p) / s -> (10 - 1) / 2 = 4.5 hours
        for p, s in cars:
            finish_time = (target - p) / s # 2. Calculate how many hours this specific car needs to finish
            # 3. If there is a fleet ahead of us (if stack exists), AND we are FASTER 
            # than that fleet (meaning our time_to_finish is LESS than or EQUAL to theirs)...
            if stack and finish_time <= stack[-1]:
                continue
                # We crash into them and join their fleet. 
                # We don't push our time because we are blocked and forced to slow down to their time.
            else:
                stack.append(finish_time)
                # If we are slower than the fleet ahead, we can never catch up. 
                # We form a brand-new fleet behind them and push our time onto the stack.
        return len(stack) # 4. The number of remaining fleets is simply the size of the stack
                