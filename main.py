# On importe le module discord.py

import discord
import random

# Ajouter un composant de discord.py
from discord.ext import commands

# Donner le token pour que le bot se connecte
token = "Nzc3NTI2MjU4Nzk1OTM3Nzky.X7EtwQ.ubIEHtAGXjb3GLoBv6J9uOPyifk"

# pour le footer de l'embed
funFact = ["L'eau mouille",
           "Le feu brule",
           "Lorsque vous volez, vous ne touchez pas le sol",
           "Winter is coming", "Mon créateur est Titouan",
           "Il n'est pas possible d'aller dans l'espace en restant sur terre",
           "La terre est ronde",
           "La moitié de 2 est 1",
           "7 est un nombre heureux",
           "Les allemands viennent d'allemagne",
           "Le coronavirus est un virus se répandant en Europe, en avez vous entendu parler ?",
           "J'apparais 2 fois dans l'année, a la fin du matin et au début de la nuit, qui suis-je ?",
           "Le plus grand complot de l'humanité est",
           "Pourquoi lisez vous ca ?"]

# une commande
# !regles

# Créer le bot
bot = commands.Bot(command_prefix='!')


# Detecter lorsque le bot est allumer
@bot.event
async def on_ready():
    print("Le bot est pret !")
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game("Aider la commu"))


# Créer la commande !regles
# ctx = récupère le contexte (qui a envoyer la commande, sur quelle sallon,...)
@bot.command()
async def regles(ctx):
    embed = discord.Embed(
        title='**REGLES**',
        description='Respecter les règles suivantes',
        colour=discord.Colour.dark_blue()
    )
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

    embed.add_field(name='Les règles', value='1. Pas d\'insultes\n2. Pas de propos discriminant\n3. Pas de spam' ,inline=True)
    embed.set_footer(text='Le STAFF')
    await ctx.send(embed=embed)


# Clear
@bot.command()
async def clear(ctx, nombre: int):
    await ctx.channel.purge(limit=nombre + 1)


# Ban
@bot.command()
async def ban(ctx, user: discord.User, *, reason=None):
    await user.ban(reason=reason)
    reason = "".join(reason)

    embed = discord.Embed(
        title='**Banissement**',
        description='Un modérateur a frappé !',
        colour=discord.Colour.dark_blue()
    )
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(
        url='https://static.wikia.nocookie.net/shingekinokyojin/images/5/55/SNK_Chronicles_affiche.jpg/revision/latest?cb=20200720204148&path-prefix=fr')
    embed.add_field(name='Membre banni', value=user.name, inline=True)
    embed.add_field(name='Raison', value=reason, inline=True)
    embed.add_field(name='Modérateur', value=ctx.author.name, inline=True)
    embed.set_footer(text=random.choice(funFact))
    await ctx.send(embed=embed)

# Unban
@bot.command()
async def unban(ctx, *, user):
    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user

        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned **{user.name}**')

# Créer la commande !bienvenue @pseudo
@bot.command()
async def bienvenue(ctx, nouveau_membre: discord.Member):
    # Récupère le nom
    pseudo = nouveau_membre.mention

    # Executer le message de bienvenue
    await ctx.send(
        f"Bienvenue à {pseudo} sur le serveur discord ! N'oublie pas de faire **!regles** afin de consulter les règle du serveur !")


# Verifier l'erreur
@bienvenue.error
async def on_command_error(ctx, error):
    # Detecter cette erreur
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("La commande est : !bienvenue @pseudo")


# Phrase avant le démarage du bot
print("Lancement du bot...")

# Le connecter au serveur
bot.run(token)
