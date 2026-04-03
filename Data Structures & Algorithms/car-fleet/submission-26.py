class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            cars.append([position[i], speed[i]])
            
        cars.sort(key=lambda item: item[0], reverse = True)

        fleets = [] # Time of arrivals

        for car in cars:
            position, speed = car
            arrival_time = (target - position) / speed
            if fleets:
                if fleets[-1] < arrival_time:
                    # This car arrives after the car in front so it is a separate fleet
                    fleets.append(arrival_time)
            else:
                fleets.append(arrival_time)


        return len(fleets)