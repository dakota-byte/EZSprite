import csv
import os
import pygame

# Allows creation of a "Scene", otherwise called a MultiSprite
# Scenes are made of multiple "SimpleSprites"


class MultiSprite:
    def __init__(self):
        self.SimpleSprites = []
        self.icsv = None
        self.sceneBounds = []
        self.sceneiBounds = []

    def addSimpleSprite(self, ss):
        self.SimpleSprites.append(ss)

    def defineSceneBounds(self, sb):
        for s in sb:
            self.sceneBounds.append(s)

    def defineSceneiBounds(self, sb):
        for s in sb:
            self.sceneiBounds.append(s)

    def getAllBounds(self, px, py):
        bounds = []
        for sprite in self.SimpleSprites:
            someBounds = sprite.getBoundaryRects(self.sceneBounds, px, py)
            for someBound in someBounds:
                bounds.append(someBound)
        return bounds

    def drawEntireScene(self, window, px, py):
        for sprite in self.SimpleSprites:
            sprite.drawMap(window, px, py)

    def containsInteractive(self):
        if self.icsv is None:
            return False
        return True

    def addInteractive(self, icsv):
        self.icsv = icsv

    def getAlliBounds(self, px, py):
        bounds = []
        types = []

        someBounds = self.icsv.getBoundaryRects(self.sceneiBounds, px, py)
        for someBound in someBounds:
            bounds.append(someBound)

        x, y = px, py
        _map = self.icsv.returnCSV()[0]
        for row in _map:
            x = px
            for tile in row:
                if int(tile) != -1:
                    types.append(int(tile))
                x += self.icsv.bitsize
            y += self.icsv.bitsize

        return bounds, types


class SimpleSprite:
    def __init__(self, spritesheet, bitsize, scalesize=1):
        self.spritesheet = pygame.image.load(spritesheet)
        newSize = (self.spritesheet.get_width() * scalesize, self.spritesheet.get_height() * scalesize)
        self.spritesheet = pygame.transform.scale(self.spritesheet, newSize)
        self.bitsize = bitsize * scalesize
        self.cols = int(self.spritesheet.get_width() / self.bitsize)
        self.rows = int(self.spritesheet.get_height() / self.bitsize)

        self.csv = []

    def addCSV(self, _csv):
        _map = []
        with open(os.path.join(_csv)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                _map.append(list(row))
        self.csv.append(_map)

    def returnCSV(self):
        return self.csv

    def getBoundaryRects(self, bounds, xp, yp):
        returnBounds = []
        for i in range(len(self.csv)):
            x, y = xp, yp
            _map = self.csv[i]
            for row in _map:
                x = xp
                for tile in row:
                    for bound in bounds:
                        if int(bound) == int(tile):
                            boundRect = pygame.Rect(x, y, self.bitsize, self.bitsize)
                            returnBounds.append(boundRect)
                    x += self.bitsize
                y += self.bitsize
        return returnBounds

    def getTile(self, tile):
        tile = int(tile)
        x = int(tile / self.cols)
        y = int(tile % self.cols)
        return x * self.bitsize, y * self.bitsize

    # Draws a tile from the spritesheet to a loc(ation) (x, y)
    def drawTile(self, window, loc, tile):
        tile = self.getTile(tile)
        window.blit(self.spritesheet, (loc[0], loc[1]), (tile[1], tile[0], self.bitsize, self.bitsize))

    def drawMap(self, window, xp=0, yp=0):
        for i in range(len(self.csv)):
            x, y = xp, yp
            _map = self.csv[i]
            for row in _map:
                x = xp
                for tile in row:
                    if int(tile) != -1:
                        self.drawTile(window, (x, y), tile)
                    x += self.bitsize
                y += self.bitsize
