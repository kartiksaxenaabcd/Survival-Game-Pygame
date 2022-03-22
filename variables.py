
intro_screen = True
game_initialise = False
game_running = False
death_screen = False

screensize = (800,480)

gametitle = "Survival Game"

bgcolour = (50, 50, 50)

playervelocity = 4

enemyvelocity = 1               

enemyanimalpawnrate =  6         # 1 - 10

w0 = 10                         # Individual enemy animal weights
w1 = 70
w2 = 100
w3 = 160
w4 = 300
w5 = 500
w6 = 800
w7 = 1200
w8 = 1700
w9 = 2200
w10 = 2800

enemyweights = (w0, w1, w2, w3, w4, w5, w6, w7, w8, w9, w10)

enemynutrition = (10,15,30,50,75,100,125,150,200,275) # Affects player weight.

enemyanimaltypespawn = ((w1,	6,	8.5,	9.5,	10,	11,	11,	11,	11,	11,	11,	7),
                    (w2,	4,	8,	9,	9.7,	10,	11,	11,	11,	11,	11,	7),
                    (w3,	2,	5,	8,	9.5,	9.8,	10,	11,	11,	11,	11,	5),
                    (w4,	2,	4,	6,	9,	9.4,	10,	11,	11,	11,	11,	5),
                    (w5,	1.5,	3,	4.5,	5.5,	8,	9.5,	9.8,	10,	11,	11,	4),
                    (w6,	1,	2.5,	4.5,	5.7,	7,	8.5,	9,	9.9,	10,	11,	4),
                    (w7,	1.5,	2.5,	3.5,	5.5,	6,	8.5,	9.5,	9.8,	10,	11,	3),
                    (w8,	2,	3,	4,	5.3,	5.5,	8.5,	8.9,	9.4,	10,	11,	3),
                    (w9,	2.5,	4,	5,	6,	6.5,	8,	8.5,	9.2,	9.5,	10,	4),
                    (w10,	2.5,	4,	5,	6,	6.5,	8,	8.5,	9.2,	9.5,	10,	4))

player_animal_size = ((w1,"02"),(w2,"03"),(w3,"04"),(w4,"05"),
                   (w5,"06"), (w6,"07"),(w7,"08"),(w8,"09"),
                   (w9,"10"), (w10,"11"))

player_animal_start_size = 20

animalfiles = ("eanimal01.png", "eanimal02.png", "eanimal03.png", "eanimal04.png",
            "eanimal05.png", "eanimal06.png", "eanimal07.png", "eanimal08.png",
            "eanimal09.png", "eanimal10.png")

eanimal_wiggle_values = {"eanimal01.png":3, "eanimal02.png":5, "eanimal03.png":7, "eanimal04.png":9,
                      "eanimal05.png":11, "eanimal06.png":14, "eanimal07.png":17, "eanimal08.png":20,
                      "eanimal09.png":15, "eanimal10.png":30}

endscore = 3000
