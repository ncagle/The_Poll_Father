# -*- coding: utf-8 -*-
#¸¸.·´¯`·.¸¸.·´¯`·.¸¸
# ║╚╔═╗╝║  │┌┘─└┐│  ▄█▀‾
# ======================= #
#     Poll Daddy Hack     #
#  Created by Alex Beals  #
#        2016-02-20       #
#  dado3212/PollDaddyHack #
# ======================= #
#     Voting Bot (Tor)    #
# Updated by Kenny McAvoy #
#        2017-06-28       #
#  kennymcavoy/VotingBot  #
# ======================= #
#   Voting Bot (Poll.fm)  #
#   Forked by James Chen  #
#        2020-05-04       #
#   jchen3652/VotingBot   #
# ======================= #
#    The Poll Father v4   #
#   Forked by Nat Cagle   #
#        2022-09-07       #
#  ncagle/The_Poll_Father #
# ======================= #

import requests, re, json, time, random
requests.packages.urllib3.disable_warnings()



#            ___________________________________________________
#           | Automatically casts votes for new Polldaddy       |
#           | Poll.fm polls. Provide the following from the     |
#           | poll url and inspecting the element of your       |
#           | preferred choice on the site:                     |
#           | poll_id = https://poll.fm/<poll_id>               |
#           | answer_id = button PDI_answer value=<"answer_id"> |
#           |                                                   |
#           |       *quack*                                     |
#           |                                       *quack*     |
#           |                      *quack*                      |
#           |                                                   |
#      _    /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
#   __(.)< ‾
#~~~\___)~~~



'''
╔════════════════════╗
║ Initial Parameters ║
╚════════════════════╝
'''
#----------------------------------------------------------------------
#base_url = "https://polldaddy.com/poll/"  =>  "https://poll.fm/"
base_url = "https://poll.fm/"
redirect = ""

useragents = []
current_useragent = ""

proxies = []
current_proxy = {"http":""}
current_proxy_num = -1


'''
╔═══════════════════╗
║ General Functions ║
╚═══════════════════╝
'''
#----------------------------------------------------------------------
def get_all_useragents():
    f = open("useragent.txt", "r")
    for line in f:
        useragents.append(line.rstrip('\n').rstrip('\r'))
    f.close()

def choose_useragent():
    k = random.randint(0, len(useragents)-1)
    current_useragent = useragents[k]
    #print current_useragent

#-----------------------------------
def get_all_proxies():
    f = open("proxy.txt", "r")
    for line in f:
        proxies.append(line.rstrip('\n').rstrip('\r'))
    f.close()

def choose_proxy():
    k = random.randint(0, len(proxies)-1)
    current_num = k
    current_proxy["http"] = proxies[k]


'''
╔════════════════╗
║ Tool Functions ║
╚════════════════╝
'''
#----------------------------------------------------------------------
def vote_once(form, value):
    c = requests.Session()
    # Chooses useragent randomly
    choose_useragent()
    redirect = {"Referer": base_url + str(form) + "/", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "User-Agent": current_useragent, "Upgrade-Insecure-Requests":"1", "Accept-Encoding": "gzip, deflate, sdch", "Accept-Language": "en-US,en;q=0.8"}

    # Chooses proxy randomly
    choose_proxy()
    try:
        init = c.get(base_url + str(form) + "/", headers=redirect, verify=False, proxies=current_proxy)
    except:
        print "error with proxy"
        #proxies.remove(current_proxy_num)
        return None

    # Search for the data-vote JSON object
    data = re.search("data-vote=\"(.*?)\"",init.text).group(1).replace('&quot;','"')
    data = json.loads(data)
    # Search for the hidden form value
    pz = re.search("type='hidden' name='pz' value='(.*?)'",init.text).group(1)
    # Build the GET url to vote
    #request = "https://polldaddy.com/vote.php?va="  =>  "https://poll.fm/vote.php?va="
    request = "https://poll.fm/vote.php?va=" + str(data['at']) + "&pt=0&r=0&p=" + str(form) + "&a=" + str(value) + "%2C&o=&t=" + str(data['t']) + "&token=" + str(data['n']) + "&pz=" + str(pz)
    try:
        send = c.get(request, headers=redirect, verify=False, proxies=current_proxy)
    except:
        print "error with proxy"
        #proxies.remove(current_proxy_num)
        return None

    return ("revoted" in send.url)

#-----------------------------------
def vote(form, value, times, wait_min = None, wait_max = None):
    global redirect
    # For each voting attempt
    i = 1
    while i < times+1:
        b = vote_once(form, value)
        # If successful, print that out, else try waiting for 60 seconds (rate limiting)
        if not b:
            # Randomize timing if set
            if wait_min and wait_max:
                seconds = random.randint(wait_min, wait_max)
            else:
                seconds = 3

            print "Voted (time number " + str(i) + ")!"
            time.sleep(seconds)
        else:
            print "Locked.  Sleeping for 60 seconds."
            i-=1
            time.sleep(60)
        i += 1


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


'''
╔══════════════════════════════════╗
║ Poll Parameters and Main Process ║
╚══════════════════════════════════╝
'''
#----------------------------------------------------------------------
# Initialize these to the specific form and how often you want to vote
#https://polldaddy.com/poll/11192890
#<input class="css-radiobutton pds-radiobutton"
#		type="radio"
#		id="PDI_answer51184563"
#		value="51184563"
#		name="PDI_answer11192890">
poll_id = 11192890      # Default = 0
answer_id = 51184563    # Default = 0
number_of_votes = 500   # Default = 10
wait_min = 5            # Default = None
wait_max = 10           # Default = None

#-----------------------------------
get_all_proxies()
get_all_useragents()
vote(poll_id, answer_id, number_of_votes, wait_min, wait_max)
