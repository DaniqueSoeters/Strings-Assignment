# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

player_0 = "Ruud Gullit"
player_1 = "Marco van Basten"
goal_0 = 32
goal_1 = 54

scorers = player_0 + " " + str(goal_0) + ", " + player_1 + " " + str(goal_1)

scorer_name0 = "Ruud Gullit"
when_they_scored0 = 32
scorer_name1 = "Marco van Basten"
when_they_scored1 = 54

report = (f"{scorer_name0} scored in the {when_they_scored0}nd minute\n{scorer_name1} scored in the {when_they_scored1}th minute")


# Part 2
player = "Ronald Koeman" 
first_name = player[0:player.find(" ")]
last_name_len = len(player[player.find(" ")+1:])
name_short = player[0] + ". " + player[player.find(" ")+1:]
chant = (player[0:player.find(" ")] + "! ") * (len(first_name)-1) + (player[0:player.find(" ")] + "!")
good_chant = (chant[(len(chant)-1):])!= " "
print(good_chant)