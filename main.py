print("\n\nHello! This is a mad-lib!\nIf you want to play, please type yes. If not, please type no.")
confirm = input("\nyes or no? ")
stub = 0

while confirm != "yes" and confirm != "no":
    print("\nhey.. I don't think you typed yes or no.. I'm not very smart so I has to be either and quite literally"
          " \"yes\" or \"no\". Lets try again.")
    confirm = input("\nyes or no? ")


if confirm == "no" and stub == 0:
    print("\n\nAww, that's not fun... I made an entire program to play mad-libs... lets try that again")
    stub += 1
    confirm = input("\none more time! yes or no? ")
while confirm == "no" and stub == 1:
    print("\n\nyou're really not funny,\nI didn't code anything if you say no more than twice so just say yes please :'(")
    confirm = input("\nhere we go c: yes or no? ")

fir_adj = ""
sec_adj = ""
thi_plu = ""
fou_nou = ""
fif_nou = ""
six_nou = ""
sev_adj = ""
eig_plu = ""
nin_adj = ""
ten_ver = ""
ele_adj = ""

if confirm == "yes":
    print("\nAlright alright!! Lets get it started! First I'll need adjective. Words that describe nouns.")
    fir_adj = input("\nGive me an adjective! ")
    sec_adj = input("Give me a second adjective! ")
    sev_adj = input("Give me a third adjective! ")
    nin_adj = input("Give me a fourth adjective! ")
    ele_adj = input("Give me a fifth adjective! ")
    print("\nokay that's it for the adjectives, now lets do plural nouns. Like nouns, but plural.")
    thi_plu = input("\nGive me a plural noun! ")
    eig_plu = input("Give me a second plural noun! ")
    print("\nthank you, thank you. Now for the nouns. yknow, person, place, thing.")
    fou_nou = input("\nGive me a noun! ")
    fif_nou = input("Give me a second noun! ")
    six_nou = input("Give me a third noun! ")
    print("\nwe're almost done, now I just need a verb")
    ten_ver = input("last but not least.. a verb please, but not ending in \"ing\"! ")

    wait = ""

    print("\noh my god, that was a lot. Luckily we did it for a reason. Here ya go! A lil madlib for ya!\n "
            "But wait! In order to see it, you have to say that you love me c:")
    wait = input("Type \"I love you!\" ")

    while wait != "I love you!":
        print("\noops! I think something went wrong.. I didn't hear you. Try again maybe?")
        wait = input("Type \"I love you!\" ")

if "I love you!" == wait:
    print("\n\nWorking for Kama'aina Handyman is "+fir_adj+"!\n"
          "Every day, I get to use my "+sec_adj+" skills to fix all sorts of "+thi_plu+" around town.\n"
          "Whether it's repairing a leaky "+fou_nou+" or fixing a broken "+fif_nou+", "
            "I always feel like a real "+six_nou+" when I'm on the job.\n"
          "Plus, the team at Kama'aina Handyman is always "+sev_adj+" and full of "+eig_plu+", which makes the "
                                                                                            "workday fly by.\n"
          "Of course, there are always a few "+nin_adj+" customers who make me want to "+ten_ver+", but that's all "
                                                                                                 "part of the job.\n"
          "All in all, I'm grateful to work for Kama'aina Handyman and be a part of such a "+ele_adj+" team.")
