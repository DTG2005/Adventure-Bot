import discord
import class_descriptions
import newfile
import asyncio
import ast
import sqlite3
import importlib
import typing
import os
import random
from discord.ext import commands

def insert_returns(body):
    # insert return stmt if the last expression is a expression statement
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    # for if statements, we insert returns into the body and the orelse
    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    # for with blocks, again we insert returns into the body
    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command
    async def ping(self, ctx):
        await ctx.send(f"Pong! {self.bot.latency}")
    @commands.command
    async def eval(self, ctx, *, cmd):
        fn_name = "_eval_expr"

        cmd = cmd.strip("` ")

        cmd = "\n".join(f"  {i}" for i in cmd.splitlines())

        body = f"async def {fn_name}():\n{cmd}"

        parsed = ast.parse(body)
        body = parsed.body[0].body

        insert_returns(body)

        env = {
            'bot': ctx.bot,
            'discord': discord,
            'commands': commands,
            'ctx': ctx,
            'importlib': importlib
        }

        exec(compile(parsed, filename="<ast>", mode="exec"),  # pylint: disable=exec-used
             env)

        result = (await eval(f"{fn_name}()", env))  # pylint: disable=eval-used
        await ctx.send(f'```python\n{result}```')

def setup(bot):
    bot.add_cog(Misc(bot))