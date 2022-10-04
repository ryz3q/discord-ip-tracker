import discord
import asyncio
import requests
import datetime
import os
from discord.ext import commands
from pyrsistent import field

TOKEN = "token"

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='.', intents = intents)

@client.event
async def on_ready(): 
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def clear(ctx, amount=100000*100):
  if commands.has_permissions(manage_messages=True):
    await ctx.channel.purge(limit=amount)
    return

@client.command()
async def ip(ctx, *, ipaddr: str = '9.9.9.9'):
    r = requests.get(f"https://json.geoiplookup.io/{ipaddr}")
    geo = r.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP Address', 'value': geo['ip']},
        {'name': 'Hostname', 'value': geo['hostname']},
        {'name': 'Connection Type', 'value': geo['connection_type']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Country', 'value': geo['country_name']},
        {'name': 'Country Code', 'value': geo['country_code']},
        {'name': 'Continent', 'value': geo['continent_name']},
        {'name': 'Continent Code', 'value': geo['continent_code']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'District', 'value': geo['district']},
        {'name': 'ZIP Code', 'value': geo['postal_code']},
        {'name': 'Latitude', 'value': geo['latitude']},
        {'name': 'Longitude', 'value': geo['longitude']},
        {'name': 'Timezone', 'value': geo['timezone_name']},
        {'name': 'Currency Code', 'value': geo['currency_code']},
        {'name': 'Currency Name', 'value': geo['currency_name']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Organization', 'value': geo['org']},
        {'name': 'ASN Organization', 'value': geo['asn_org']},
        {'name': 'ASN Number', 'value': geo['asn_number']},
        {'name': 'ASN', 'value': geo['asn']},
        {'name': 'Premium', 'value': geo['premium']},
        {'name': 'Status', 'value': geo['success']},

    ]
    for field in fields:
        if field['value']:
            em.set_footer(text='\u200b')
            em.timestamp = datetime.datetime.utcnow()
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed = em)

client.run(TOKEN)