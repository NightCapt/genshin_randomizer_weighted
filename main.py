import random

# these numbers are the weighted probability of character strength. Higher the number, higher the chances of
# that rarity showing up. The idea is to create more scuffed randomizer runs.
# the characters Zajef77 doesn't have or built are commented out but can be commented back in.
# all character power is taken from zajef tierlist spreadsheet

TOP_META = 10  # added Nahida
META = 20  # added Layla
VIABLE = 30  # added Dori
SHIT = 35
BALLS = 5  # this rarity is for bennett xingqiu fischl


characters = ["Bennett"]
character_weight = [BALLS]

characters.append("Childe")
character_weight.append(TOP_META)

characters.append("Xingqiu")
character_weight.append(BALLS)

characters.append("Mona")
character_weight.append(META)

# characters.append("Kokomi")
# character_weight.append(TOP_META)

characters.append("Barbara")
character_weight.append(VIABLE)

characters.append("Ayato")
character_weight.append(TOP_META)

characters.append("Yelan")
character_weight.append(TOP_META)

characters.append("Xiao")
character_weight.append(META)

characters.append("Sucrose")
character_weight.append(TOP_META)

characters.append("Venti")
character_weight.append(TOP_META) # unsure about this, change if you want

characters.append("Kazuha")
character_weight.append(TOP_META)

characters.append("Jean")
character_weight.append(META)

characters.append("MC")
character_weight.append(TOP_META)

characters.append("Sayu")
character_weight.append(VIABLE)

# characters.append("Heizou")
# character_weight.append(META)

characters.append("Beidou")
character_weight.append(META)

characters.append("Raiden")
character_weight.append(TOP_META)

characters.append("Lisa")
character_weight.append(META)

characters.append("Fischl")
character_weight.append(BALLS)

characters.append("Keqing")
character_weight.append(META)

characters.append("Razor")
character_weight.append(VIABLE) #feel free to change this as well

# characters.append("Sara")
# character_weight.append(VIABLE)

# characters.append("Yae")
# character_weight.append(META)

# characters.append("Kuki")
# character_weight.append(META)

# characters.append("Dori")
# character_weight.append(VIABLE)

# characters.append("Ayaka")
# character_weight.append(TOP_META)

characters.append("Rosaria")
character_weight.append(META)

characters.append("Kaeya")
character_weight.append(META)

# characters.append("Ganyu")
# character_weight.append(META)

# characters.append("Eula")
# character_weight.append(META) #

characters.append("Diona")
character_weight.append(META)

characters.append("Qiqi")
character_weight.append(VIABLE)

characters.append("Chongyun")
character_weight.append(VIABLE)

characters.append("ALOY")
character_weight.append(SHIT)

# characters.append("Layla")
# character_weight.append(VIABLE)

# characters.append("Shenhe")
# character_weight.append(META)

characters.append("Xiangling")
character_weight.append(TOP_META)

characters.append("Diluc")
character_weight.append(VIABLE)

characters.append("Hu Tao")
character_weight.append(TOP_META)

characters.append("Xinyan")
character_weight.append(SHIT)

characters.append("Amber")
character_weight.append(SHIT)

characters.append("Yoimiya")
character_weight.append(META)

characters.append("Klee")
character_weight.append(VIABLE)

characters.append("Yanfei")
character_weight.append(VIABLE)

characters.append("Thoma")
character_weight.append(META)

characters.append("Zhongli")
character_weight.append(META)

characters.append("Albedo")
character_weight.append(META)

characters.append("Ningguang")
character_weight.append(VIABLE)

characters.append("Noel")
character_weight.append(VIABLE)

# characters.append("Itto")
# character_weight.append(META)

characters.append("Gorou")
character_weight.append(META)

# characters.append("Tighnari")
# character_weight.append(META)

characters.append("Collei")
character_weight.append(META)

characters.append("Nahida")
character_weight.append(TOP_META)

i = 0
while i < 15:
    character_in_bracket = random.choices(characters, character_weight)
    character = character_in_bracket[0]

    index = characters.index(character)
    del characters[index]
    del character_weight[index]
    i = i + 1
    print(character + ", ", end="")
