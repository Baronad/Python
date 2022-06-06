import turtle


# wn är ett kommand som man kan använda för att redirectas till pythons bibliotek för att utforska information i wordnet
wn = turtle.Screen()
wn.title("Making two different jumping styles")
wn.bgcolor("green")
wn.setup(height=500, width=800)
wn.tracer(0)

GROUND_LEVEL = -40

# MARK
# Här har jag ritat marken och senare satt marken som en collider
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)
pen.shape("circle")
pen.color("blue")
pen.penup()

# LINJE
# Här har jag assignat marken höjd
pen.goto(-400, GROUND_LEVEL)
pen.pendown()
pen.goto(400, GROUND_LEVEL)
pen.penup()

# Hade jag använt mig av jumper.speed(2) hade farten förddubblats
# Jag har även assignat vilken färg, höjd och bredd på bollen
# jumper.dy bestämmer hur högt bollen hoppar
# På nedvägen ska bollen gå till -300 för att sedan nå ground leveln

jumper = turtle.Turtle()
jumper.speed(1)
jumper.shape("circle")
jumper.color("blue")
jumper.penup()
jumper.width = 20
jumper.height = 20
jumper.dy = 3
jumper.dx = 3
jumper.i = 0
jumper.state = "ready"
jumper.goto(-300, GROUND_LEVEL + jumper.height / 2)


# assignat gravitation
GRAVITY = -0.05


# Definierat ordet jump, utan det hade alla koder med jump inte känts igen
def jump():
    jumper.dy = 4


# Gjort så att när man trycker D så hoppar man
wn.listen()
wn.onkeypress(jump, "D")

while True:
    # GRAVITATION
    jumper.dy += GRAVITY

    # RÖRELSE
    y = jumper.ycor()
    y += jumper.dy
    jumper.sety(y)

    # KONTAKTMARK
    if jumper.ycor() < GROUND_LEVEL + jumper.height / 2:
        jumper.sety(GROUND_LEVEL + jumper.height / 2)
        i+=1
        jumper.dy = (y/100)*i

    wn.update()

