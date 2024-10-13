from manim import *

class GravityBox(Scene):
    def construct(self):

        G = 0.000003      
        dx = ValueTracker(0) # Does nothing, but somehow this program breaks without????

        dot_c = Dot([0, 0, 0])
        mass_c = 2000

        dot_o = Dot([0, 2, 0])
        mass_o = 1
        velocity_o = np.array([0.03, 0.0, 0.0])
        
        path = VMobject()
        path.set_points_as_corners([dot_o.get_center(), dot_o.get_center()]).set_stroke(opacity=0.5)

        def update_path(path):
            previous = path.copy()
            previous.add_points_as_corners([dot_o.get_center()])
            path.become(previous)

        def get_acceleration(vec_moved, vec_pull, vec_pull_mass):
            vec_dist = np.subtract(vec_pull, vec_moved)
            length = np.sqrt(vec_dist[0]**2 + vec_dist[1]**2)
            if length == 0:
                #length = 0.01
                return 0
            norm_dist = np.divide(vec_dist, length)
            acceleration = G * (vec_pull_mass/(length**2))
            return np.multiply(norm_dist, acceleration)

        def dot_updater(obj):
            nonlocal velocity_o
            velocity_o = velocity_o + get_acceleration(dot_o.get_center(), dot_c.get_center(), mass_c)
            obj.shift(velocity_o)

        dot_o.add_updater(dot_updater)
        path.add_updater(update_path)       

        self.add(dot_c, dot_o, path)
        self.play(dx.animate.set_value(11), run_time=25)
        
class GravityBox2(Scene):
    def construct(self):

        G = 0.000006     
        dx = ValueTracker(0) # Does nothing, but somehow this program breaks without????

        dot_c = Dot([2, -2, 0])
        mass_c = 2000
        velocity_c = np.array([-0.03, 0.0, 0.0])

        dot_o = Dot([-2, 2, 0])
        mass_o = 2000
        velocity_o = np.array([0.03, 0.0, 0.0])
        
        path = VMobject()
        path.set_points_as_corners([dot_o.get_center(), dot_o.get_center()]).set_stroke(opacity=0.5)

        path2 = VMobject()
        path2.set_points_as_corners([dot_c.get_center(), dot_c.get_center()]).set_stroke(opacity=0.5)

        def update_path(path):
            previous = path.copy()
            previous.add_points_as_corners([dot_o.get_center()])
            path.become(previous)

        def update_path2(path):
            previous = path.copy()
            previous.add_points_as_corners([dot_c.get_center()])
            path.become(previous)

        def get_acceleration(vec_moved, vec_pull, vec_pull_mass):
            vec_dist = np.subtract(vec_pull, vec_moved)
            length = np.sqrt(vec_dist[0]**2 + vec_dist[1]**2)
            if length == 0:
                #length = 0.01
                return 0
            norm_dist = np.divide(vec_dist, length)
            acceleration = G * (vec_pull_mass/(length**2))
            return np.multiply(norm_dist, acceleration)

        def dot_o_updater(obj):
            nonlocal velocity_o
            velocity_o = velocity_o + get_acceleration(dot_o.get_center(), dot_c.get_center(), mass_c)
            obj.shift(velocity_o)
        
        def dot_c_updater(obj):
            nonlocal velocity_c
            velocity_c = velocity_c + get_acceleration(dot_c.get_center(), dot_o.get_center(), mass_o)
            obj.shift(velocity_c)

        dot_o.add_updater(dot_o_updater)
        dot_c.add_updater(dot_c_updater)
        path.add_updater(update_path)
        path2.add_updater(update_path2)       

        self.add(dot_c, dot_o, path, path2)
        self.play(dx.animate.set_value(11), run_time=15)