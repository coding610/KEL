import KEL


class MyRandomComp:
    def start(self, comps):
        self.move = False

    def update(self, comps):
        # Just moving The component

        inp = KEL.Input('K_SPACE')

        if inp == 'Down':
            self.move = True

        if inp == 'Up':
            self.move = False
        
        if self.move == True:
            comps['TransformRectComp'].yLT += 1
        
        return comps




wallComps = [KEL.TransformRectComp(), KEL.RenderRectComp(), MyRandomComp()]
KEL.KELCORE.addObject('Wall', KEL.EmptyModel(), wallComps)
print(KEL.KELCORE.objects)

KEL.KELCORE.start()
run = True
while run:
    KEL.KELCORE.updateEngine()


    if KEL.rawInput('type', 'QUIT'):
        run = False
