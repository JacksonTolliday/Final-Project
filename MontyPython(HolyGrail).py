from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

class Person(Sprite):
    """
    
    """
    asset = ImageAsset("images/platformer_sprites_base.png",
        Frame(0, 0, 64, 64), 8, 'horizontal')
    asset.append("images/platformer_sprites_base -left.png",
        Frame(0, 0, 64, 64), 8, 'horizontal')
    
    def __init__(self, position):
        super().__init__(Person.asset, position)
        self.vl = 0
        self.vr = 0
        self.tv = 0
        Game.listenKeyEvent("keydown", "w", self.jump)
        Game.listenKeyEvent("keydown", "a", self.left)
        Game.listenKeyEvent("keydown", "d", self.right)
        Game.listenKeyEvent("keydown", "s", self.drop)
        self.fxcenter = self.fycenter = 0.5
        self.thrust = 0
        self.animater = 0
        self.animatel = 16


    def step(self):
        self.tv = self.vr - self.vl
        if self.tv > 6:
            self.tv = 6
        if self.tv < -6:
            self.tv = -6
        self.x += self.tv
        print('step')
        if self.tv > 0:
            self.setImage(0)
            self.setImage(self.animater)
            self.animater += 0.5
            if self.animater == 8:
                self.animater = 0
        if self.tv < 0:
            self.setImage(16)
            self.setImage(self.animatel)
            self.animatel -= 0.5
            if self.animatel == 8:
                self.animatel = 16
        else:
            pass
        

    def left(self, event):
        self.vl += 1
        
    def right(self, event):
        self.vr += 1
    
    def jump(self, event):
        self.thrust = 1

    def drop(self, event):
        self.thrust = -1

class Game(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self):
        super().__init__()
        # Background
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        Person((200,200))


    def step(self):
        for player in self.getSpritesbyClass(Person):
            player.step()


myapp = Game()
myapp.run()
