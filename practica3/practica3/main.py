def get_distance_to_point(self, x, y):
        return sqrt((self.x - x)**2 + (self.y - y)**2)

    def move_to_point(self, x, y):
        distance = self.get_distance_to_point(x, y)
        while distance > 0.1:
            dx = x - self.x
            dy = y - self.y
            angle_to_target = atan2(dy, dx)
            # Assuming constant speed for simplicity
            self.x += 0.1 * cos(angle_to_target)
            self.y += 0.1 * sin(angle_to_target)
            distance = self.get_distance_to_point(x, y)
            time.sleep(0.1)


