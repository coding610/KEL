import KEL 


class MoveWallComp:
    def start(self, comps):
        self.hold = False

    def update(self, comps) -> list:
        if KEL.Input('K_SPACE'):
            self.hold = True 

        if self.hold:
            comps['TransformRectComp'].yLT += 1

        return comps
