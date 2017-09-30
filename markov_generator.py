import discord
import botMain
import config
from discord.ext import commands
import time
import commandModules.message_interface as message_interface
import checks
import commandModules.db_driver_mysql as mysql
import random
import math

def admin_permission():
    def predicate(ctx):
        if ctx.message.author.id == config.ownerID:
            return True
        try:
            return ctx.message.channel.permissions_for(ctx.message.author).manage_messages
        except:
            return False
    return commands.check(predicate)

class Markov():

    def __init__(self, bot):
        self.bot = bot
        self.message = message_interface.message_handler()

    def does_markov_exist(self, user_id):
        pass
        # Check if user_id is in markov_chain db

    def get_markov_chain(self, user_id):
        pass
        # Return a dictionary/tuple list of the users generated markov chain

    @commands.command(name="markov", pass_context=True)
    @admin_permission()
    async def imitate(self, ctx):
        """
        Will return a markov chain using your most recent messages imitating you

        Usage: !imitate @OkBread, !imitate <user_id>, !imitate me
        """
        message = ctx.message.content.strip(' ').split(' ')
        user_id = ''
        if len(message) == 1:
            response = self.message.returnMarkovMsgError()
            await self.bot.say(response)
        elif message[1].casefold() == 'me'.casefold():
            user_id = ctx.message.author.id
            print(user_id)
        else:
            user_id = message[1][2:-1]
            print(user_id)

        # if(does_markov_exist(user_id)):
        #     markov_chain = get_markov_chain(user_id)
        #     # Do something with chain
        # else:
        #     # Make chain

def shittyMarkov(inMessage, numWords):
    if numWords <= 0:
        return "You're a fucking retard"
    #numWords is the number of words to use in HashMap key to generate mapping

    # I'm assuming this turns the input message into a list
    inMessage.split(' ')

    #get max length to iterate to
    maxLen = len(inMessage) - numWords + 1

    #create dictionary
    myMap = {}

    #
    for i in range(0, maxLen):
        # for each starting point, first n words goes into the key
        mapKey = inMessage[i]
        if numWords >= 2:
            for j in range(1, numWords - 1):
                mapKey = mapKey + " " + inMessage[i+j]

        # the n+1 word becomes the value for the pair
        mapValue = inMessage[i+numWords]

        # build the map
        if mapKey not in myMap:
            # create key-value pair in dictionary
            # key is pair of words
            myMap[mapKey] = [mapValue]
        else:
            # add mapValue to the end of the list
            myMap[mapKey] = myMap[mapKey].append(mapValue)

    return myMap

def useMarkov(inMap, numWords):
    if numWords <= 0:
        return "You're a fucking retard"

    # inMap is the hashmap created above: string is

    # variables to decide:
    # how to start the message
    # how to end the message

    # arbitrary test variables
    outputLength = 10
    myMessage = list(inMap.keys())[0]

    while(len(myMessage)<outputLength):
        # randomly select next word from the array of values

        # create key
        thisKey = myMessage[len(myMessage) - numWords]
        if numWords >= 2:
            for i in range(1, numwords-1):
                thisKey = thiskey + " " + myMessage[len(myMessage) - numWords + i]

        # randomly determine which value to take from the value array
        valIndex = floor(random.random() * len(inMap[thisKey]))

        # take the randomly
        myMessage.append(inMap[thisKey][valIndex])
    return myMessage

def setup(bot):
    bot.add_cog(Markov(bot))
