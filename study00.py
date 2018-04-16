#  Daily Study 00
#  16/04/18

CANVAS = 300
rectSize = 70
rectNum = 10
rectDist = 2

getDist = rectNum * rectDist #get total rects before centering by subtracting position x.
offset = 50

frameNumber = 50 #GET RID OF size() before using newPage(), otherwise the framerate will be messed up.

for f in range (frameNumber):
    newPage(CANVAS, CANVAS)
    frameDuration(1/30)
    
    rect(0,0,CANVAS,CANVAS)
    
    step = 2 * pi * f / frameNumber
    print(sin(step))

    translate(CANVAS / 2 - getDist / 2 ,CANVAS / 2) 
    fill(1)
    stroke(0)

    rotateAngle = 90 * sin(step)
    startRotate = rotateAngle
    endRotate = rotateAngle + 240

    for i in range (rectNum):
        frame = i / rectNum #get access to every item individually
        
        save()
        translate(i * rectDist+sin(step))
        rotate(startRotate * frame + (endRotate - startRotate))
        rect((-rectSize / 2) + 80,- rectSize / 2 ,rectSize - 10,rectSize -10)
        restore()
        
        save()
        translate(i * rectDist+sin(step))
        rotate(startRotate * frame + (endRotate - startRotate))
        rect((-rectSize / 2) - 80,- rectSize / 2 ,rectSize - 10,rectSize -10)
        restore()
        

        save()
        translate(i * rectDist+sin(step)) #if putting outside save() ~ restore(), value will be different.
        scale(0.4,1)
        rotate(startRotate + frame)
        rect(-rectSize / 2,- rectSize / 2,rectSize,rectSize)
        restore()
 
        
    
    
saveImage("study00.gif")
    
