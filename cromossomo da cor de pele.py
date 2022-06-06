import random
ancestral = [146,128,113]
class Entity():
    R = ancestral[0]
    G = ancestral[1]
    B = ancestral[2]
    def __init__(self):
        pass
    def SkinColor(X,Y,Z,M):
        R = 0
        G = 0
        B = 0
        melaninamultiplyer = M
        
        for i in range(0,X+melaninamultiplyer):
            print("ISSO AQUI",X)
            y = random.randint(0,1)
            R += y
            print("R",R)
            print(melaninamultiplyer)
            if(R > 255):
                R = 255
        for i in range(0,Y+melaninamultiplyer // 2):
            y = random.randint(-1,1)
            G += y
            if(G > 255):
                G = 255
        for i in range(0,Z+melaninamultiplyer):
            y = random.randint(-1,1)
            B += y
            if(B > 255):
                G = 255
        cor = [R,G,B]
        return (cor)
    def BodySize():
        pass
    skinColor = SkinColor(R,G,B,random.randint(-200,200))
    def genes(self):
        self.RGB = self.skinColor
        return self.RGB

pai = Entity()
filho = Entity()
print(pai.skinColor)
