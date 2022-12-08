from PIL import Image, ImageDraw
import discord
import cube
import mytoken
intents = discord.Intents.all()
client = discord.Client(command_prefix=';', intents=intents)
cub = cube.cube()
token1 = mytoken.mytoken()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event

async def on_message(message):
    if message.author == client.user:
        return
    if message.author.id != token1.myID:
        return
    s = message.content
    if len(s)>=1 and s[0]==";":
        s = s[1:]
        '''
        if s in cub.moves:
            cub.apply_move(s)
            await message.channel.send(cub.to_string())
        '''
            
        if s == "Jperm":
            cub.apply_alg(cub.Jbperm)
        elif s == "Tperm":
            cub.apply_alg(cub.Tperm)
        elif s == "cornerswap":
            cub.apply_alg(cub.OPcorner)
        elif s == "scramble":
            cub.solve()
            await message.channel.send(cub.get_scramble())
            await message.channel.send(cub.to_string())
            await message.channel.send(file=discord.File("3bld.jpg"))
        elif s == "print":
            await message.channel.send(cub.to_string())
        elif s == "solve":
            cub.solve()
            await message.channel.send(cub.to_string())
        else:
            cub.apply_blind_algs(s)
            await message.channel.send("bruh")
            await message.channel.send(cub.to_string())

client.run(token1.s)