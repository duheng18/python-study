import turtle  #引入turtle库 海龟绘图体系

turtle.setup(650,350,200,200) #设定窗体
turtle.penup( ) #将画笔抬起
turtle.fd(-250) #让海龟倒退向后行进250像素，由于当前海龟画笔提起即海龟在飞行，画布上未留下任何的效果
turtle.pendown( ) #将海龟落下  将海龟从绘图中心的原点变成在图像中左侧的某一个位置上
turtle.pensize(25 ) #通过调整腰围设定当前画笔宽度为25个像素
turtle.pencolor("purple") #画笔颜色为紫色
turtle.seth(-40) #将海龟方向改为绝对的-40度方向
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done( )
                
