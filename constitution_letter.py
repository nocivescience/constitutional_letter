from manim import *
class ContitutionScene(Scene):
    def construct(self):
        booleans=self.get_booleans()
        texs=self.get_texs(booleans)
        self.play(LaggedStartMap(Write,texs))
        self.wait()
    def get_texs(self,booleans):
        texs=VGroup() # VGroup is a group of texts
        for boolean in booleans:
            if boolean:
                tex = Text('Apruebo').set(color=BLUE)
            else:
                tex = Text('Rechazo').set(color=RED)
            tex.boolean = boolean
            texs.add(tex)
        texs.arrange_in_grid(columns=4).set(width=config['frame_width'])
        return texs
    def get_booleans(self):
        n_booleans = np.random.choice([True,True,True,False],40)
        return n_booleans