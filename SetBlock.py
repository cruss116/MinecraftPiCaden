from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

tnt = 46

x, y, z = mc.player.getPos()
mc.setBlock(x, y+1, z, tnt, 1)
