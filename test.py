
code = "ABAAACADAFAGAJAIAHANAYAUAMABATARAEBAAUAMANAQAEAQAWACAAAVAZ"
objectives = [("Own a Horse", "AA"),("Gain 2 Dragon Souls", "AB"),("Get a Follower", "AC"),("Join the Thieves' Guild", "AD"),("Join the Dark Brotherhood", "AE"),("Get Launched By a Giant", "AF"),("Pick Up the Lusty Argonian", "AG"),("Escape From Jail", "AH"), ("Get One or Two Handed to 40", "AI"),("Join the Civil War", "AJ"),("Acqure one Daedric Artifact", "AK"), ("Eat a Human Heart", "AL"), ("Own a House", "AM"),("Discover 20 Location", "AN"),("Become a Werewolf or Vampire", "AO"),("Learn Bound Bow", "AP"),("Acquire 6000 Gold", "AQ"),("Win a Fist Fight", "AR"),("Go to Jail With a Bounty of 1000+", "AS"),("Unlock 3 Shouts", "AT"),("Discover All Capitals", "AU"),("Kill 2 Giants", "AV"),("Find a Standing Stone (except trio)", "AW"),("Mine 10 Ore Veins", "AX"),("Collect 3 Unusual Gems", "AY"), ("Get Destruction to 40", "AZ"),("Get Archery to 40", "BA")]

x = 0
code_list =[]
while x < 25:
    val = code[x*2]  + code[(x*2) + 1]
    code_list.append(val)
    x = x + 1

print(code_list)
return_list = []
for code_val in code_list:
    for obj in objectives:
        if code_val == obj[1]:
            return_list.append(obj)
print(return_list)
    

