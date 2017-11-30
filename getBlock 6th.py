from mcpi.minecraft import Minecraft
mc = Minecraft.create()

answer = input("Create a crater? Y/N")

pos = mc.player.getPos()
mc.setBlocks(pos.x + 1000, pos.y + 1000, pos.z + 1000, pos.x - 1000, pos.y - 1000, pos.z - 1000, 0)
mc.postToChat("Boom!")
