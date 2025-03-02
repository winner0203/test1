#CH05-Lab08 사용자가 원하는 도형 그리기

import turtle
t = turtle.Turtle( )
t.shape("turtle")
x1 = int(input("큰 원의 중심좌표 x1: "))
y1 = int(input("큰 원의 중심좌표 y1: "))
r1 = int(input("큰 원의 반지름: "))
x2 = int(input("작은 원의 중심좌표 x2: "))
y2 = int(input("작은 원의 중심좌표 y2: "))
r2 = int(input("작은 원의 반지름: "))

t.penup( )
t.goto(x1, y1)
yy1 = y1 - r1		# circle( )의 특성으로 인해 원을 그리는 위치 조정
t.goto(x1, yy1)
t.pendown( )
t.circle(r1)

t.penup( )
t.goto(x2, y2)
yy2 = y2 - r2		# circle( )의 특성으로 인해 원을 그리는 위치 조정
t.goto(x2, yy2)
t.pendown( )
t.circle(r2)

dist = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5  	#두 원의 중심사이의 거리

if dist == 0:
    turtle.write("동심원")
elif dist == r1 - r2:
    turtle.write("내접")
elif r1 - r2 < dist < r1 + r2:
    turtle.write("두 점에서 만납니다.")
elif dist > r1 + r2:
    turtle.write("만나지 않고 외부에 있습니다.")
elif dist == r1 + r2:
    turtle.write("외접")
elif dist < r1 - r2:
    turtle.write("만나지 않고 내부에 있습니다.")


