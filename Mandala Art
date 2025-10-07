import turtle, colorsys
turtle.bgcolor("black")
t=turtle.Turtle(); #객체 생성
t.speed(0) #가장 빠른 속도, 애니메이션 없이 즉시 그리기 
turtle.colormode(255) #RGB 0~255 범위 
n=36 #색상 변화 단계
h=0 #색상 값 

for i in range(72): #72번 반복(360도/5도=72),숫자가 커질수록 더 큰 꽃잎
  col=colorsys.hsv_to_rgb(h,1,1) #HSV->RGB(무지개 색상)
  t.pencolor(int(col[0]*255), int(col[1]*255), int(col[2]*255))
  #파스텔 톤 hsv_to_rgb(h,0.5,1) 어두운 톤 hsv_to_rgb(h,1,0.7)
  for _ in range(6): #꽃잎(육각형 모양) 하나 그리기
    t.circle(60) #반지를 60의 원, 숫자가 커질수록 더 큰 원
    t.left(60) #60도 회전, 숫자가 작아질수록 더 큰 회전각
  t.left(5) #전체 패턴 5도 회전
  h+=1/n #색상 조금씩 변경
  h%=1 #h가 1을 넘으면 0으로 순환











