import turtle
import random

t = turtle.Turtle()
t.up()
t.ht()
t.speed(0)
dot_size = 3

def put_a_dot(position):
    t.goto(position)
    t.dot(dot_size)
    
def is_point_inside_triangle(p1, p2, p3, p):
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

    d1 = sign(p, p1, p2)
    d2 = sign(p, p2, p3)
    d3 = sign(p, p3, p1)

    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

    return not (has_neg and has_pos)
def get_middle_point(pos1, pos2):
    x = (pos1[0] + pos2[0]) / 2
    y = (pos1[1] + pos2[1]) / 2
    return x,y

Shape = input("Do you want to use a shape saved in 'Shape log.txt'? \n Type the name of the shape that you want to use.\n If you don't want to, type 'skip'.")

def get_coordinates():
    coordinates = []
    for i in range(3):
        x = float(input(f"Enter the x-coordinate for point {i+1}: "))
        y = float(input(f"Enter the y-coordinate for point {i+1}: "))
        coordinates.append((x, y))
    return coordinates

points = get_coordinates()
p1 = points[0]
p2 = points[1]
p3 = points[2]
put_a_dot(p1)
put_a_dot(p2)
put_a_dot(p3)

max_x = max(p1[0],p2[0],p3[0])
min_x = min(p1[0],p2[0],p3[0])
max_y = max(p1[1],p2[1],p3[1])
min_y = min(p1[1],p2[1],p3[1])

Save = input("Do you want to save this position data? (Y/N) ")
if Save == 'Y':
    Name = input("What is the name? ")

# 판별할 점의 좌표를 입력받습니다.

while True:
    x = random.uniform(min_x, max_x)
    y = random.uniform(min_y, max_y)
    # 세 점과 판별할 점의 좌표를 튜플로 만듭니다.

    p = [x, y]

    # 한 점이 삼각형 안에 있는지 판별합니다.
    inside = is_point_inside_triangle(p1, p2, p3, p)

    # 결과를 출력합니다.
    if inside:
        put_a_dot(p)
        break
while True:       
    point_decider =  random.randint(1,3)
    if point_decider == 1:
        middle_point = get_middle_point(p1, p)
    elif point_decider == 2:
        middle_point = get_middle_point(p2, p)
    else:
        middle_point = get_middle_point(p3, p)
    p = list(middle_point)
    put_a_dot(p)