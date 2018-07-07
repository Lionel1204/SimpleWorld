class Config:
    MAXSPECIES = 3
    MAXPROGRAM = 40
    MAXCREATURES = 50
    MAXHEIGHT = 20
    MAXWIDTH = 20
    HILLSKIPROUND = 1

if __name__ == "__main__":
    print(Config.MAXCREATURES)
    print(Config.MAXHEIGHT)
    print(Config.MAXWIDTH)
    print(Config.MAXSPECIES)
    print(Config.MAXPROGRAM)
