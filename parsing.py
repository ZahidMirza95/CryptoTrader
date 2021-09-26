import operator # might need
import data_file
import streamlit as st
import calc
import variables


pairList = ['BTC-AUD', 'ETH-AUD', 'LTC-AUD', 'XRP-AUD', 'BCH-AUD', 'USDT-AUD', 'EOS-AUD', 'XLM-AUD', 'DOT-AUD', 'LINK-AUD', 'USDC-AUD', 'BSV-AUD', 'ADA-AUD', 'DOGE-AUD',

        'BTC-USD']

currency = ''

commands_Dict = {
    '-search': {
        'Desc': 'Search for coin(s).',
        'minArgs': 1,
        'maxArgs': 5,
        'SUBS': {
            '-c': {
                'Desc': 'Specific coin category lookup',
                'minArgs': 0,
                'maxArgs': 33,
                'syntax': None,
                'help': '[fields]'
            }
        },
        'Help': '[coinID]'
    },
    '-currency':{
        'Desc': 'Manage primary currency.',
        'minArgs': 1,
        'maxArgs': 2,
        'SUBS': {},
        'Help': '[subCommand] [args]'
    },
    '-watch':{
        'Desc': 'Watch crypto in realtime.',
        'minArgs': 1,
        'maxArgs': 1,
        'SUBS': {},
        'Help': '[coinID]'
    },
    '-pair':{
        'Desc': 'View buy and sell cost of pair across multiple exchanges',
        'minArgs': 1,
        'maxArgs': 5,
        'SUBS': {},
        'Help': '[pairID]'
    },
    '-bid':{
        'Desc': 'Switch pair side param to bids',
        'minArgs': 0,
        'maxArgs': 0,
        'SUBS': {},
        'Help': '-bid'
    },
    '-ask':{
        'Desc': 'Switch pair side param to asks',
        'minArgs': 0,
        'maxArgs': 0,
        'SUBS': {},
        'Help': '-ask'
    },
    '-q': {
        'Desc': 'Change pair quantity param',
        'minArgs': 1,
        'maxArgs': 1,
        'SUBS': {},
        'Help': '[int]'
    },
    '-info':{
        'Desc': 'Get coin specific info.',
        'minArgs': 1,
        'maxArgs': 1,
        'SUBS': {},
        'Help': '[coinID]'
    },
    '-help': {
        'Desc': 'View commands',
        'minArgs': 0,
        'maxArgs': 0,
        'SUBS': {},
        'Help': '-help'
    }
}
def quantity(splits):
    splits.remove(splits[0])
    variables.pairQuantity = splits[0]
    st.write('Pair quantity param changed to', variables.pairQuantity)

def bidsSide():
    calc.side = 'bids'
    st.write('Pair side param changed to bids')

def asksSide():
    calc.side = 'asks'
    st.write('Pair side param changed to asks')

def checkPair(splits):
    splits.remove(splits[0])
    data_file.checkPair(splits)
def watch(splits):
    for split in splits:
        if split != splits[0]:
            data_file.watch(split)

def coinInfo(splits):
    for split in splits:
        if split != splits[0]:
            data_file.coinInfo(split)

def searchCoin(splits):
    for split in splits:
        if split != splits[0] and not split.__contains__('-'):
            variables.activeCoins.append(split)
    data_file.searchCoin(variables.activeCoins, 'usd')

def manageCurrency(splits):
    cmd = splits[0]
    splits.remove(splits[0])
    for split in splits:
        if split.__contains__('-v'):
            st.write('has v')
            splits.remove(split)
            if len(splits) == 0:
                st.write('Current Currency: ' + 'usd')
                print('Current Currency: ' + 'usd')
            else:
                st.write('Invalid syntax, proper usage:', cmd, commands_Dict[cmd]['Help'])
                print('Invalid syntax, proper usage:', cmd, commands_Dict[cmd]['Help'])

        if split.__contains__('-c'):
            splits.remove(split)
            if len(splits) == 1:
                for split in splits:
                    currency = split
                    st.write('Changed primary currency to', 'usd')
            else:
                st.write('Invalid syntax, proper usage:', cmd, commands_Dict[cmd]['Help'])


def validateCommand():
    global command
    #Split command input into pieces where split[0] is main command
    splits = command.split(' ')
    cmd = splits[0]
    args = len(splits)-1
    if (args < commands_Dict[cmd]['minArgs'] or args > commands_Dict[cmd]['maxArgs']):
        st.write('Improper syntax, proper usage:', cmd, commands_Dict[cmd]['Help'])
    else:
        return True

def getCommand(input):
    global command
    command=input
    print("calling function commands with input ",input)
    commands()

    
def commands():
    global command
    splits = command.split(' ')
    cmd = splits[0]
    if commands_Dict.__contains__(cmd):
        if (cmd == '-help'):
            if(validateCommand()):
                st.write("\nCommands")
                for command in commands_Dict:
                    st.write('\t', command, ':', commands_Dict[command]['Desc'], 'Usage:', commands_Dict[command]['Help'])
                #for comm in commands_dict:
                #    st.write('\t', comm, ':', commands_dict[comm])
        if (cmd == '-search'):
            if(validateCommand()):
                searchCoin(splits)
        if (cmd == '-currency'):
            if(validateCommand()):
                manageCurrency(splits)
        if (cmd == '-info'):
            if(validateCommand()):
                coinInfo(splits)
        if (cmd == '-watch'):
            if(validateCommand()):
                watch(splits)
        if (cmd == '-pair'):
            if(validateCommand()):
                checkPair(splits)
        if cmd == '-bid':
            if validateCommand():
                bidsSide()
        if cmd == '-ask':
            if validateCommand():
                asksSide()
        if cmd == '-q':
            if validateCommand():
                quantity(splits)
    else:
        st.write('Command', command, 'does not exist\n')
    #waitCommand()


def waitCommand():
    global command
    command = input('')
    commands()


#waitCommand()