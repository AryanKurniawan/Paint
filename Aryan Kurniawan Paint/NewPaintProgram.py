#CAT'S PAINT, by: Aryan Kurniawan
#bucket tool, text tool, dot tool, gradient tool

#MODULE IMPORTS--------------
from random import*
from pygame import*
from math import*
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename   
#SCREEN SIZE-----------------------
size=(1024,768)
screen = display.set_mode(size)
screen.fill((255,255,255))
           
running =True
mx,my=0,0

#FONT-------------------------------
font.init()
font = font.SysFont("Chalk Duster", 30)

#MUSIC
init()

#BACKGROUND------------------------
#Screen Background
background = image.load ("background.jpg")
screen.blit(background,(0,0))
#Talking Cat Helper
catBackground=image.load("catBackground.png")
screen.blit(catBackground,(-120,350))
#Logo
logo=image.load("logo.png")
screen.blit(logo,(-2,0))
#Thinking Bubble
tBubbleIcon=image.load("thinkBubble.png")
tBubbleIcon = transform.scale(tBubbleIcon,(240,220))#Resize

#CANVAS-------------------------------------------------
draw.rect(screen,(0,0,0),(245,25,668,560))#Canvas Outline
canvasRect=Rect(250,30,658,550)
draw.rect(screen,(255,255,255),canvasRect)

#VARIABLES--------------
tab="tools"#Starts on tools tab
stamp=""#Starts on no stamp
tool="" #Starts as no tool
col=(0,0,0) #Colour starts as black
width=10#Starts on 10
shape=""#Starts on no shape
b=3#tools Boarder width
saying=0#Starts on introductory saying
selected=(255,255,100)#When tool selected, yellow back
undolist=[screen.subsurface(canvasRect).copy()] #constantly copies canvas
redolist=[]
extra=""
trail=[]#for fade tool
root = Tk() #for save tool
root.withdraw()#for save tool

#SAYINGS--------------------------------
sayings=["Welcome to Cat's Paint! Begin by hovering on a tool to use or get information on it",
         "Colour Pallatte: Choose your desired colour. Chosen colour is indicated by the tool helper",
         "Tools Tab:Click tool to begin.Change colour using colour pallatte and width using scroll wheel",
         "Stamps Tab: Resize stamp using scroll wheel, right click to reposition one you've just placed",
         "Backgrounds Tab: Click a background and make it your background!",
         "Shapes Tab:Click shape to begin.Change colour using colour pallatte and width using scrollwheel",
         "Pencil Tool: Left click canvas to draw. Change width using scroll wheel (max width=6)",
         "Eraser Tool: Left click to erase canvas. Change width using scroll wheel",
         "Brush Tool: Left click canvas for circular brush head, right click for square brush head",
         "Spray Tool: Left click to spray in circle, right click to spray in square",
         "Highlighter Tool: Left click to highlight desired colour, right click to unhighlight",
         "Smudge Tool: Left click to smudge dark, right click to smudge light",
         "Line Tool: Click to being drawing, hold to change length, and release to draw line",
         "Unfilled Rectangle Tool: Click to begin drawing, hold to change size, and release to draw",
         "Filled Rectangle Tool: Click to begin drawing, hold to change size, and release to draw",
         "Unfilled Circle:Click to begin drawing, hold to change size, and release to draw",
         "Filled Circle:Click to begin drawing, hold to change size, and release to draw",
         "Clean canvas: Click to completely clean the canvas",
         "Eyedrop tool: Click anywhere on the screen to make it the colour",
         "Polygon Tool: Click a set a points and reclick your first point to make a polygon",
         "Polygon complete!",
         "Tool helper: Shows width of tool and colour. Stamps width multiplied by 10",
         "Save tool: Saves current image of canvas",
         "Load tool: Loads last saved image onto canvas",
         "Undo tool: Undos last update to canvas or last redo",
         "Redo tool: Redos last undo",
         "Dotter tool: Click the canvas to start dotting away",
         "Fade tool: Click to fade from red to blue",
         "Canvas Fill: Click which colour you want the canvas to be"]

#sayings=27

#TAB RECTS---------------------------------------------
toolsTabRect=Rect(0,651,110,21)
toolsTab=image.load("toolsTab.png")
screen.blit(toolsTab,toolsTabRect)
screen.blit(font.render("TOOLS",True,(255,255,0)),(27,651))

stampsTabRect=Rect(146,651,110,21)
stampsTab=image.load("stampsTab.png")
screen.blit(stampsTab,stampsTabRect)
screen.blit(font.render("STAMPS",True,(255,255,0)),(165,651))

shapesTabRect=Rect(292,651,110,21)
shapesTab=image.load("shapesTab.png")
screen.blit(shapesTab,shapesTabRect)
screen.blit(font.render("SHAPES",True,(255,255,0)),(312,651))

backgroundsTabRect=Rect(438,651,110,21)
backgroundsTab=image.load("backgroundTab.png")
screen.blit(backgroundsTab,backgroundsTabRect)
screen.blit(font.render("BACKS",True,(255,255,0)),(460,651))

extrasTabRect=Rect(584,651,110,21)
extrasTab=image.load("extrasTab.png")
screen.blit(extrasTab,extrasTabRect)
screen.blit(font.render("EXTRAS",True,(255,255,0)),(608,651))

#COLOUR CHART-----------------------------------------------------
colourChart = screen.blit(image.load("colourChart.jpg"),(834,651))
draw.rect(screen,(0,0,0),(745-b,683-b,75+2*b,75+2*b))

#SPEECH BUBBLE---------------------------------------------------------------------------------------------------------------------------------------------
speechBubbleBoarder=[(100,550-b),(115+b,595-b),(1010+b,595-b),(1010+b,635+b),(20-b,635+b),(20-b,595-b),(85-b,595-b),(100,550-b)]
draw.polygon(screen,(0,0,0),speechBubbleBoarder,0)
speechBubble=[(100,550),(115,595),(1010,595),(1010,635),(20,635),(20,595),(85,595),(100,550)]
draw.polygon(screen,(255,255,255),speechBubble,0)

def backRects():
        #Tool Backs
        xs=[15,105,195,285,375,465,555,645]
        for x in xs:
            draw.rect(screen,(0,0,0),(x-b,687-b,70+2*b,70+2*b))
            #Highlights back when hovering over with mouse
            if Rect(15-b,687-b,70+2*b,70+2*b).collidepoint(mx,my):
                draw.rect(screen,(255,0,0),(15-b,687-b,70+2*b,70+2*b))
            if Rect(105-b,687-b,70+2*b,70+2*b).collidepoint(mx,my):
                draw.rect(screen,(255,0,0),(105-b,687-b,70+2*b,70+2*b))
            if Rect(195-b,687-b,70+2*b,70+2*b).collidepoint(mx,my):
                draw.rect(screen,(255,0,0),(195-b,687-b,70+2*b,70+2*b))
            if Rect(285-b,687-b,70+2*b,70+2*b).collidepoint(mx,my):
                draw.rect(screen,(255,0,0),(285-b,687-b,70+2*b,70+2*b))
            if Rect(375-b,687-b,70+2*b,70+2*b).collidepoint(mx,my):
                draw.rect(screen,(255,0,0),(375-b,687-b,70+2*b,70+2*b))
            if Rect(465-b,687-b,70+2*b,70+2*b).collidepoint(mx,my):
                draw.rect(screen,(255,0,0),(465-b,687-b,70+2*b,70+2*b))
            if Rect(555-b,687-b,70+2*b,70+2*b).collidepoint(mx,my):
                draw.rect(screen,(255,0,0),(555-b,687-b,70+2*b,70+2*b))
            if Rect(645-b,687-b,70+2*b,70+2*b).collidepoint(mx,my):
                draw.rect(screen,(255,0,0),(645-b,687-b,70+2*b,70+2*b))

#TOOL RECTS AND ICONS==============================
#Tools Back-----------------------------
toolsBack = image.load ("toolsBack.png")
toolsBackRect=Rect(0,672,730,100)

#Tool Rects-------------------------
#Pencil Tool
pencilRect=Rect(15,687,70,70)
pencilIcon=image.load("pencil.png")
pencilCol=(255,255,255)

#Eraser Tool
eraserRect=Rect(105,687,70,70)
eraserIcon=image.load("eraser.png")
eraserCol=(255,255,255)

#Brush Tool
brushRect=Rect(195,687,70,70)
brushIcon=image.load("brush.png")
brushCol=(255,255,255)

#Spray Tool
sprayRect=Rect(285,687,70,70)
sprayIcon=image.load("spray.png")
sprayCol=(255,255,255)

#Highlighter Tool
highlightRect=Rect(375,687,70,70)
highlightIcon=image.load("highlight.png")
cover = Surface((1200,675)).convert()# make blank Surface
cover.set_alpha(55)
cover.set_colorkey((255,0,255))
highlightCol=(255,255,255)

#Smudge Tool
smudgeRect=Rect(465,687,70,70)
smudgeIcon=image.load("smudge.png")
smudgeCol=(255,255,255)

bucketRect=Rect(555,687,70,70)
bucketCol=(255,255,255)
bucketIcon=image.load("bucket.png")
           
eyedropRect=Rect(645,687,70,70)
eyedropIcon=image.load("eyedrop.png")
eyedropCol=(255,255,255)

#STAMPS RECT AND ICONS=====================
#Stamps Back-------------------------------
stampsBack = image.load ("stampsBack.png")
stampsBackRect=Rect(0,672,730,100)

#Stamps Rects------------------------------
#Orange Cat
orangeCatRect=Rect(15,687,70,70)
orangeCatIcon=image.load("orangeCat.png")
orangeCatCol=(255,255,255)

#Orange Kitten
orangeKittenRect=Rect(105,687,70,70)
orangeKittenIcon=image.load("orangeKitten.png")
orangeKittenCol=(255,255,255)
           
#Scared Cat
scaredCatRect=Rect(195,687,70,70)
scaredCatIcon=image.load("scaredCat.png")
scaredCatCol=(255,255,255)
                     
#Jumping Cat
jumpingCatRect=Rect(285,687,70,70)
jumpingCatIcon=image.load("jumpingCat.png")
jumpingCatCol=(255,255,255)
           
#Eating Cat
eatingCatRect=Rect(375,687,70,70)
eatingCatIcon=image.load("eatingCat.png")
eatingCatCol=(255,255,255)
           
#Yarn
yarnRect=Rect(465,687,70,70)
yarnIcon=image.load("yarn.png")                 
yarnCol=(255,255,255)
           
#Mouse
mouseRect=Rect(555,687,70,70)
mouseIcon=image.load("mouse.png")
mouseCol=(255,255,255)
           
#Nyan Cat
nyanCatRect=Rect(645,687,70,70)
nyanCatIcon=image.load("nyanCat.png")
nyanCatCol=(255,255,255)
           
#SHAPES RECT AND ICONS=====================
#Shapes Back-------------------------------
shapesBack = image.load ("shapesBack.png")
shapesBackRect=Rect(0,672,730,100)

#Shapes Rects-------------------------
#Line Rect
lineRect=Rect(15,687,70,70)
lineIcon=image.load("line.png")
lineCol=(255,255,255)

#Unfilled Rect
unfilledRectRect=Rect(105,687,70,70)
unfilledRectIcon=image.load("unfilledRect.png")
unfilledRectCol=(255,255,255)

#Filled Rect
filledRectRect=Rect(195,687,70,70)
filledRectIcon=image.load("filledRect.png")
filledRectCol=(255,255,255)
           
#Unfilled Circle
unfilledCircleRect=Rect(285,687,70,70)
unfilledCircleIcon=image.load("unfilledCircle.png")
unfilledCircleCol=(255,255,255)
           
#Filled Circle
filledCircleRect=Rect(375,687,70,70)
filledCircleIcon=image.load("filledCircle.png")
filledCircleCol=(255,255,255)
           
#Unfilled Polygon
unfilledPolygonRect=Rect(465,687,70,70)
unfilledPolygonIcon=image.load("unfilledPolygon.png")
unfilledPolygonCol=(255,255,255)
polyMode="poly1"
polypoints=[]
polyWidths=[]
polyCols=[]
polyRects=[]
polygon=""#polygon mode not selected

#Filled Polygon
filledPolygonRect=Rect(555,687,70,70)
filledPolygonIcon=image.load("filledPolygon.png")
filledPolygonCol=(255,255,255)

canvasFill=Rect(645,687,70,70)

#BACKGROUND RECT AND ICONS========================
#Background Back----------------------------------
backgroundBack = image.load ("backgroundBack.png")
backgroundBackRect=Rect(0,672,730,100)

#Background Rects-------------------------
#Basement
basementRect=Rect(23,687,100,70)
basementIcon=image.load("basement.jpg")

#Play Place
playPlaceRect=Rect(169,687,100,70)
playPlaceIcon=image.load("playPlace.jpg")

#Park
parkRect=Rect(315,687,100,70)
parkIcon=image.load("park.jpg")

#Space
spaceRect=Rect(461,687,100,70)
spaceIcon=image.load("space.jpg")

#Heaven
heavenRect=Rect(607,687,100,70)
heavenIcon=image.load("heaven.jpg")

#EXTRAS RECT AND ICONS========================
#Extras Back----------------------------------
extrasBack = image.load ("extrasBack.png")
extrasBackRect=Rect(0,672,730,100)

#Extras Rects-----------------------------------
#Music Stuff---------------------------------
#Music 1
music1Rect=Rect(15,687,70,70)
music1Icon=image.load("music1.png")
music1Col=(255,255,255)

#Music 2
music2Rect=Rect(105,687,70,70)
music2Icon=image.load("music2.png")
music2Col=(255,255,255)

#Music 3
music3Rect=Rect(195,687,70,70)
music3Icon=image.load("music3.png")
music3Col=(255,255,255)
           
#Music 4
music4Rect=Rect(285,687,70,70)
music4Icon=image.load("music4.png")
music4Col=(255,255,255)
           
#Music 5
music5Rect=Rect(375,687,70,70)
music5Icon=image.load("music5.png")
music5Col=(255,255,255)

#Music 6
music6Rect=Rect(465,687,70,70)
music6Icon=image.load("music6.png")
music6Col=(255,255,255)  

#Cool tools--------------------------
#Fade
fadeRect=Rect(555,687,70,70)
fadeIcon=image.load("fade.png")
fadeCol=(255,255,255)

#Dotter
dotterRect=Rect(645,687,70,70)
dotterIcon=image.load("dotter.png")
dotterCol=(255,255,255)

#catSound=mixer.Sound("catSound.mp3")

while running:
    click=False #for polygon tool
    for e in event.get():
        if e.type == QUIT:     
            running = False
        if e.type==MOUSEBUTTONUP:
            #Undo and Redo Stuff
            if e.button == 1 and canvasRect.collidepoint(e.pos):#When mouse is over canvas...
                copy1=screen.subsurface(canvasRect).copy() #copy the canvas
                undolist.append(copy1)#every copy of canvas goes into a list
                redolist = []#redolist is cleared
        if e.type==MOUSEBUTTONDOWN:
            #Save and load stuff
            if e.button==1:
               # catSound.play()
                if saveRect.collidepoint(e.pos):
                    saying=22
                    fileName = asksaveasfilename(parent=root,title="Save the image as...")
                    if fileName!="":
                        if "." not in fileName:
                            fileName+=".png"
                            #print(fileName)                    
                            image.save(screen.subsurface(canvasRect),(fileName))
                if loadRect.collidepoint(e.pos):
                    saying=23
                    loadFile = askopenfilename(parent=root,title="Open Image:")
                    if loadFile!="":
                        loadPic=image.load(loadFile)
                        screen.blit(loadPic,canvasRect)
                        tool=""
                #Undo and Redo Stuff
                if undoRect.collidepoint(mx,my) and len(undolist) > 1:
                    saying=24
                    stamp=""#Prevents stamp being printed
                    redolist.append(undolist[-1])#takes last undo list copy and puts it in redo list
                    del(undolist[-1]) #deletes last copy from undo list so...
                    screen.blit(undolist[-1],canvasRect) #blits the copy BEFORE latest canvas change
                if redoRect.collidepoint(mx,my) and len(redolist) > 0:
                    saying=25
                    stamp=""#Prevents stamp being printed
                    screen.blit(redolist[-1],canvasRect)#blits copy of canvas before undo (most recent redo is copy BEFORE last undo)
                    undolist.append(redolist[-1]) #puts copy of last redo into undo --> so you can undo the redo
                    del(redolist[-1]) #deletes it from redo list
            cover.fill((255,0,255)) #For highlighter tool
            copy1=screen.copy()#for highlighter tool
            if e.button==1:
                copy2=screen.copy()#For shape and stamp tools
                click=True#for polygon tool
                startx,starty = e.pos #For shape tools
            if e.button==4: #change size with mousewheel
                width+=1
            if e.button==5:
                width-=1
            if width<=0:
                width=1 # Prevents negative width
            if width>=36:
                width=36 # Maximum width, for size/colour helper
                
    smx,smy = mx,my #Smudge tool mx,my          
    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()
    mpos=mouse.get_pos()
    
    #COLOUR SELECTION-------------------
    draw.rect(screen,(200,200,200),(745,683,75,75))
    draw.circle(screen,(col),(782,720),width)
    if Rect(745,683,75,75).collidepoint(mx,my):
        saying=21
    if colourChart.collidepoint(mx,my):
        saying=1
        if mb[0] == 1:
            col = screen.get_at((mx,my))            
            #print(width)           
            #print(col)

    #SAYINGS--------------------------------------------
    draw.polygon(screen,(255,255,255),speechBubble,0)
    speech = font.render(sayings[saying], True, (0,0,0))
    screen.blit(speech,(25,602))
    
    #STATS INDICATORS============================================
    screen.blit(tBubbleIcon,(0,210))
    #COLOUR VALUE--------------------------------------------------
    screen.blit(font.render("Colour Values:",True,(col)),(35,250))
    cValue = font.render(str(col), True, (col))
    screen.blit(cValue,(35,270))
    #MOUSE COORDS------------------------------------------------
    screen.blit(font.render("Mouse Coords:",True,(0,0,0)),(35,290))
    mCoords = font.render(str(mouse.get_pos()), True, (0,0,0))
    screen.blit(mCoords,(35,310))
    #WIDTH VALUE
    screen.blit(font.render("Width:"+str(width),True,(0,0,0)),(35,330))
    if tab=="stamps":
        screen.blit(font.render("Width:"+str(width*10),True,(0,0,0)),(35,330))

    #SIDE RECTS========================================================
    #Back Rects------------------------------------------------------
    draw.rect(screen,(0,0,0), (10-b,165-b,50+2*b,50+2*b))#load rect
    sbys=[55,195,335,475]#Starting y-coords of back of function tools
    for sby in sbys:
        draw.rect(screen,(0,0,0),(928-b,sby-b,75+2*b,75+2*b))
        #Highlights back when hovering over with mouse
        if Rect(928-b,55-b,70+2*b,70+2*b).collidepoint(mx,my):
            draw.rect(screen,(255,0,0),(928-b,55-b,75+2*b,75+2*b))
        if Rect(928-b,195-b,70+2*b,70+2*b).collidepoint(mx,my):
            draw.rect(screen,(255,0,0),(928-b,195-b,75+2*b,75+2*b))
        if Rect(928-b,335-b,70+2*b,70+2*b).collidepoint(mx,my):
            draw.rect(screen,(255,0,0),(928-b,335-b,75+2*b,75+2*b))
        if Rect(928-b,475-b,70+2*b,70+2*b).collidepoint(mx,my):
            draw.rect(screen,(255,0,0),(928-b,475-b,75+2*b,75+2*b))
        if Rect((10-b,165-b,50+2*b,50+2*b)).collidepoint(mx,my):#load rect
            draw.rect(screen,(255,0,0), (10-b,165-b,50+2*b,50+2*b))
    #Function Rects------------------------------------------------
    #Undo Rect
    undoRect=Rect(928,55,75,75)
    draw.rect(screen,(255,255,255),undoRect)
    undoIcon=image.load("undo.png")
    screen.blit(undoIcon,undoRect)
    #Redo Rect
    redoRect=Rect(928,195,75,75)
    draw.rect(screen,(255,255,255),redoRect)
    redoIcon=image.load("redo.png")
    screen.blit(redoIcon,redoRect)
    #Clean Rect
    cleanRect=Rect(928,335,75,75)
    draw.rect(screen,(255,255,255),cleanRect)
    cleanIcon=image.load("clean.png")
    screen.blit(cleanIcon,cleanRect)
    #Save Rect
    saveRect=Rect(928,475,75,75)
    draw.rect(screen,(255,255,255),saveRect)
    saveIcon=image.load("save.png")
    screen.blit(saveIcon,saveRect)
    #Load Rect
    loadRect=Rect(10,165,50,50)
    draw.rect(screen,(255,255,255),loadRect)
    loadIcon=image.load("load.png")
    screen.blit(loadIcon,loadRect)
        
    #TAB SELECTION-----------------------------------
    if toolsTabRect.collidepoint(mx,my) and mb[0]==1: 
        tab="tools"
        saying=2
        #print(tab)

    if stampsTabRect.collidepoint(mx,my) and mb[0]==1:
        tab="stamps"
        saying=3
        stamp=""#Resets stamp as no stamp
        #print(tab)

    if backgroundsTabRect.collidepoint(mx,my) and mb[0]==1:
        tab="backgrounds"
        saying=4
        background=""#Resets background as no background
        #print(tab)

    if shapesTabRect.collidepoint(mx,my) and mb[0]==1:
        tab="shapes"
        saying=5
        #print(tab)

    if extrasTabRect.collidepoint(mx,my) and mb[0]==1:
        tab="extras"
        #print(tab)

        


    #TOOLS TAB=================================================
    #TOOLS INTERFACE------------------------------------------
    if tab=="tools":
        screen.blit(toolsBack,toolsBackRect)#tab background
        backRects()#draws back rects and enables higlight function               
        #TOOL ICONS------------------------------
        #Pencil Icon
        draw.rect(screen,(pencilCol),pencilRect)
        screen.blit(pencilIcon,pencilRect)
        #Eraser Icon
        draw.rect(screen,(eraserCol),eraserRect)
        screen.blit(eraserIcon,eraserRect)
        #Brush Icon
        draw.rect(screen,(brushCol),brushRect)
        screen.blit(brushIcon,brushRect)
        #Spray Icon
        draw.rect(screen,(sprayCol),sprayRect)
        screen.blit(sprayIcon,(280,687))
        #Highlight Icon
        draw.rect(screen,(highlightCol),highlightRect)
        screen.blit(highlightIcon,(360,687))
        #Smudge Icon
        draw.rect(screen,(smudgeCol),smudgeRect)
        screen.blit(smudgeIcon,(485,687))
        #Bucket Icon                   
        draw.rect(screen,(bucketCol),bucketRect)
        screen.blit(bucketIcon,bucketRect)
        #Eyedrop Icon
        draw.rect(screen,eyedropCol,eyedropRect)
        screen.blit(eyedropIcon,eyedropRect)

        

        #TOOLS SELECTION-------------------------------       
        if pencilRect.collidepoint(mx,my):
            saying=6
            if mb[0]==1:
                tool="pencil"
                #print(tool)

        if eraserRect.collidepoint(mx,my):
            saying=7
            if mb[0]==1:
                tool="eraser"
                #print(tool)

        if brushRect.collidepoint(mx,my):
            saying=8
            if mb[0]==1:
                tool="brush"
                #print(tool)

        if sprayRect.collidepoint(mx,my):
            saying=9
            if mb[0]==1:
                tool="spray"
                #print(tool)

        if highlightRect.collidepoint(mx,my):
            saying=10
            if mb[0]==1:
                tool="highlight"
                #print(tool)

        if smudgeRect.collidepoint(mx,my):
            saying=11
            if mb[0]==1:
                tool="smudge"
                #print(tool)



        if eyedropRect.collidepoint(mx,my):
            saying=18
            if mb[0]==1:
                tool="eyedrop"
                #print(tool)

        if bucketRect.collidepoint(mx,my):
            if mb[0]==1:
                tool="bucket"
                #print(tool)
                
        #CANVAS DRAW-------------------------                
        if mb[0]==1 or mb[2]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)

        #TOOL USE-----------------------
            if tool=="bucket":
                bucketCol=selected
            else:
                bucketCol=(255,255,255)
                
            if tool=="eyedrop":
                eyedropCol=selected
                if mb[0]==1:
                    col = screen.get_at((mx,my))                   
            else:
                eyedropCol=(255,255,255)
           
            if tool=="highlight":
                highlightCol=selected
                if mb[0]==1:
                    draw.circle(cover,(col),(mx,my),width)
                if mb[2]==1:
                    draw.circle(cover,(255,255,255),(mx,my),width)#right click to unhighlight
                if 1 in mb:
                    screen.blit(copy1,(0,0))
                    screen.blit(cover,(0,0))
            else:
                highlightCol=(255,255,255)

                
            if tool == "spray":
                sprayCol=selected
                if mb[0]==1:#sprays in circle shape
                    for spraySpeed in range(10): #Speed of spray, greater faster
                        sprayX=randint(-width,width)
                        sprayY=randint(-width,width)
                        if (sprayX**2+sprayY**2)**0.5<width: #Less than radius draws a circle(equidistant at single point)
                            draw.circle(screen,col,(mx+sprayX,my+sprayY),0)
                if mb[2]==1:#sprays in rectangle shape
                    for spraySpeed in range(10): #Speed of spray, greater faster
                        sprayX=randint(-width,width)
                        sprayY=randint(-width,width)
                        if (sprayX**2+sprayY**2)**0.5<width+100: #Always less than radius so draws rectangle
                            draw.circle(screen,col,(mx+sprayX,my+sprayY),0)
            else:
               sprayCol=(255,255,255)
           
            if tool=="smudge":
                smudgeCol=selected
                lightSmudge = Surface((width*2,width*2),SRCALPHA) 
                draw.circle(lightSmudge,(255,255,255,20),(width,width),width)#using alpha
                darkSmudge = Surface((width*2,width*2),SRCALPHA)       
                draw.circle(darkSmudge,(0,0,0,44),(width,width),width)#cannot change colour, col,44
                if mx!=smx or my!=smy:
                    if mb[0]==1:
                        col=(0,0,0)
                        screen.blit(darkSmudge, (mx-width,my-width))       
                    if mb[2]==1:
                        screen.blit(lightSmudge, (mx-width,my-width))
            else:
               smudgeCol=(255,255,255)
           
            if tool=="brush":
                brushCol=selected
                if mb[0]==1:#circle brush
                    draw.line(screen,col,(oldmx,oldmy),(mx,my),width*2)  
                    draw.circle(screen,col,(oldmx,oldmy),width)    
                    draw.circle(screen,col,(mx,my),width)     
                if mb[2]==1:#square brush
                    draw.line(screen,col,(oldmx,oldmy),(mx,my),int(width*2)) 
                    draw.rect(screen,col,(oldmx-width/2,oldmy-width/2,width*2,width*2))                     
                    draw.rect(screen,col,(mx-width/2,my-width/2,width*2,width*2))
            else:
               brushCol=(255,255,255)
           
            if tool=="pencil":
                pencilCol=selected
                if mb[0]==1:
                    draw.line(screen,(col),(oldmx,oldmy),(mx,my),width)
                    if width>6:#lines no greater than width=4
                        width=6
            else:
                pencilCol=(255,255,255)
        
            if tool=="eraser":
                eraserCol=selected
                if mb[0]==1:
                    draw.line(screen,(255,255,255),(oldmx,oldmy),(mx,my),width)
            else:
                eraserCol=(255,255,255)
                              
    oldmx,oldmy=mx,my

    #STAMPS TAB=================================================
    #STAMPS INTERFACE------------------------------------------
    if tab=="stamps":
        screen.blit(stampsBack,stampsBackRect)#tab back
        backRects()#draws back rects and enables higlight function
        #STAMPS ICONS--------------------------------------------
        #Orange Cat
        draw.rect(screen,(orangeCatCol),orangeCatRect)
        orangeCatIcon2= transform.scale(orangeCatIcon,(70,70))
        screen.blit(orangeCatIcon2,orangeCatRect)
        #Orange Kitten
        draw.rect(screen,(orangeKittenCol),orangeKittenRect)
        orangeKittenIcon2= transform.scale(orangeKittenIcon,(90,90))
        screen.blit(orangeKittenIcon2,(90,675))
        #Scared Cat
        draw.rect(screen,(scaredCatCol),scaredCatRect)
        scaredCatIcon2= transform.scale(scaredCatIcon,(70,70))
        screen.blit(scaredCatIcon2,scaredCatRect)
        #Jumping Cat
        draw.rect(screen,(jumpingCatCol),jumpingCatRect)
        jumpingCatIcon2= transform.scale(jumpingCatIcon,(70,70))
        screen.blit(jumpingCatIcon2,jumpingCatRect)
        #Eating Cat
        draw.rect(screen,(eatingCatCol),eatingCatRect)
        eatingCatIcon2= transform.scale(eatingCatIcon,(70,70))
        screen.blit(eatingCatIcon2,eatingCatRect)
        #Yarn
        draw.rect(screen,(yarnCol),yarnRect)
        yarnIcon2= transform.scale(yarnIcon,(70,70))
        screen.blit(yarnIcon2,yarnRect)
        #Mouse
        draw.rect(screen,(mouseCol),mouseRect)
        mouseIcon2= transform.scale(mouseIcon,(70,70))
        screen.blit(mouseIcon2,mouseRect)
        #Nyan Cat
        draw.rect(screen,(nyanCatCol),nyanCatRect)
        nyanCatIcon2= transform.scale(nyanCatIcon,(70,70))
        screen.blit(nyanCatIcon2,nyanCatRect)



        #STAMPS SELECTION-------------------------------        
        if orangeCatRect.collidepoint(mx,my):
            if mb[0]==1:
                stamp="orange cat"
                #print(stamp)

        if orangeKittenRect.collidepoint(mx,my):
            if mb[0]==1:
                stamp="orange kitten"
                #print(stamp)

        if scaredCatRect.collidepoint(mx,my):
            if mb[0]==1:
                stamp="scared cat"
                #print(stamp)

        if jumpingCatRect.collidepoint(mx,my):
            if mb[0]==1:
                stamp="jumping cat"
                #print(stamp)

        if eatingCatRect.collidepoint(mx,my):
            if mb[0]==1:
                stamp="eating cat"
                #print(stamp)

        if yarnRect.collidepoint(mx,my):
            if mb[0]==1:
                stamp="yarn"
                #print(stamp)

        if mouseRect.collidepoint(mx,my):
            if mb[0]==1:
                stamp="mouse"
                #print(stamp)
                
        if nyanCatRect.collidepoint(mx,my):
            if mb[0]==1:
                stamp="nyan cat"
                #print(stamp)

        #CANVAS DRAW-------------------------                
        if mb[0]==1 or mb[2]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)

            #STAMP USE----------------------------------    
            if stamp=="orange cat":
                orangeCatCol=selected
                screen.blit(copy2,(0,0))
                orangeCatIcon3 = transform.scale(orangeCatIcon,(width*10,width*10))#Resize
                screen.blit(orangeCatIcon3,(mx-width*10/2,my-width*10/2))
            else:
                orangeCatCol=(255,255,255)

            if stamp=="orange kitten":
                orangeKittenCol=selected
                screen.blit(copy2,(0,0))
                orangeKittenIcon3 = transform.scale(orangeKittenIcon,(width*10,width*10))#Resize
                screen.blit(orangeKittenIcon3,(mx-width*10/2,my-width*10/2))
            else:
                orangeKittenCol=(255,255,255)

            if stamp=="scared cat":
                scaredCatCol=selected
                screen.blit(copy2,(0,0))
                scaredCatIcon3 = transform.scale(scaredCatIcon,(width*10,width*10))#Resize
                screen.blit(scaredCatIcon3,(mx-width*10/2,my-width*10/2))
            else:
                scaredCatCol=(255,255,255)

            if stamp=="jumping cat":
                jumpingCatCol=selected
                screen.blit(copy2,(0,0))
                jumpingCatIcon3 = transform.scale(jumpingCatIcon,(width*10,width*10))#Resize
                screen.blit(jumpingCatIcon3,(mx-width*10/2,my-width*10/2))
            else:
                jumpingCatCol=(255,255,255)            


            if stamp=="eating cat":
                eatingCatCol=selected
                screen.blit(copy2,(0,0))
                eatingCatIcon3 = transform.scale(eatingCatIcon,(width*10,width*10))#Resize
                screen.blit(eatingCatIcon3,(mx-width*10/2,my-width*10/2))
            else:
                eatingCatCol=(255,255,255)            

            if stamp=="yarn":
                yarnCol=selected
                screen.blit(copy2,(0,0))
                yarnIcon3 = transform.scale(yarnIcon,(width*10,width*10))#Resize
                screen.blit(yarnIcon3,(mx-width*10/2,my-width*10/2))
            else:
                yarnCol=(255,255,255)            

            if stamp=="mouse":
                mouseCol=selected
                screen.blit(copy2,(0,0))
                mouseIcon3 = transform.scale(mouseIcon,(width*10,width*10))#Resize
                screen.blit(mouseIcon3,(mx-width*10/2,my-width*10/2))
            else:
                mouseCol=(255,255,255)            

            if stamp=="nyan cat":
                nyanCatCol=selected
                screen.blit(copy2,(0,0))
                nyanCatIcon3 = transform.scale(nyanCatIcon,(width*10,width*10))#Resize
                screen.blit(nyanCatIcon3,(mx-width*10/2,my-width*10/2))
            else:
                nyanCatCol=(255,255,255)            


    #SHAPES TAB=================================================
    #SHAPES INTERFACE------------------------------------------
    if tab=="shapes":
        screen.blit(shapesBack,shapesBackRect)#tab back
        backRects()#draws back rects and enables higlight function
        #SHAPES ICONS------------------------------
        #Line Icon
        draw.rect(screen,(lineCol),lineRect)
        screen.blit(lineIcon,lineRect)
        #Unfilled Rect Icon
        draw.rect(screen,(unfilledRectCol),unfilledRectRect)
        screen.blit(unfilledRectIcon,unfilledRectRect)
        #Filled Rect Icon
        draw.rect(screen,(filledRectCol),filledRectRect)
        screen.blit(filledRectIcon,filledRectRect)
        #Unfilled Circle Icon
        draw.rect(screen,(unfilledCircleCol),unfilledCircleRect)
        screen.blit(unfilledCircleIcon,unfilledCircleRect)
        #Filled Circle Icon
        draw.rect(screen,(filledCircleCol),filledCircleRect)
        screen.blit(filledCircleIcon,filledCircleRect)
        #Unfilled Polygon
        draw.rect(screen,unfilledPolygonCol,unfilledPolygonRect)
        screen.blit(unfilledPolygonIcon,unfilledPolygonRect)
        #Filled Polygon
        draw.rect(screen,filledPolygonCol,filledPolygonRect)
        screen.blit(filledPolygonIcon,filledPolygonRect)
        #CanvasFill
        draw.rect(screen,(col),canvasFill)

        #SHAPES SELECTION-----------------------------
        if lineRect.collidepoint(mx,my):
            saying=12
            if mb[0]==1:
                polygon=""#Prevents polygon tools from being highlighted
                shape="line"
                #print(shape)

        if unfilledRectRect.collidepoint(mx,my):
            saying=13
            if mb[0]==1:
                polygon=""
                shape="unfilled Rect"
                #print(shape)

        if filledRectRect.collidepoint(mx,my):
            saying=14
            if mb[0]==1:
                polygon=""
                shape="filled Rect"
                #print(shape)

        if unfilledCircleRect.collidepoint(mx,my):
            saying=15
            if mb[0]==1:
                polygon=""
                shape="unfilled Circle"
                #print(shape)

        if filledCircleRect.collidepoint(mx,my):
            saying=16
            if mb[0]==1:
                polygon=""
                shape="filled Circle"
                #print(shape)

        if unfilledPolygonRect.collidepoint(mx,my):
            saying=19
            if mb[0]==1:
                shape="polygon"
                polygon="unfilled"
                #print(shape)

        if filledPolygonRect.collidepoint(mx,my):
            saying=19
            if mb[0]==1:
                shape="polygon"
                polygon="filled"
                #print(shape)

        if canvasFill.collidepoint(mx,my):
            saying=34
            if mb[0]==1:
                draw.rect(screen,col,canvasRect)

                
        #CANVAS DRAW-------------------------                
        if mb[0]==1 or mb[2]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)

            #SHAPE USE-----------------------
            if polygon=="unfilled":
                unfilledPolygonCol=selected
            else:
                unfilledPolygonCol=(255,255,255)

            if polygon=="filled":
                filledPolygonCol=selected
            else:
                filledPolygonCol=(255,255,255)
                
            if shape=="line":
                lineCol=selected
                screen.blit(copy2,(0,0))
                draw.line(screen,col, (startx,starty),(mx,my),width)
            else:
                lineCol=(255,255,255)
                
            if shape=="unfilled Rect":
                unfilledRectCol=selected
                screen.blit(copy2,(0,0))
                draw.rect(screen,col,(startx,starty,mx-startx,my-starty),width)
                if width>5:#lines no greater than width=10
                    width=5
            else:
                unfilledRectCol=(255,255,255)
                                    
            if shape=="filled Rect":
                filledRectCol=selected
                screen.blit(copy2,(0,0))
                draw.rect(screen,col,(startx,starty,mx-startx,my-starty))
            else:
                filledRectCol=(255,255,255)
                
            if shape=="unfilled Circle":
                unfilledCircleCol=selected
                screen.blit(copy2,(0,0))
                if min(abs(mx-startx),abs(my-starty))>width*2: 
                    draw.ellipse(screen,col,(min(startx,mx),min(starty,my),abs(mx-startx),abs(my-starty)),width)
                else:
                    draw.ellipse(screen,col,(min(startx,mx),min(starty,my),abs(mx-startx),abs(my-starty)),0)
            else:
                unfilledCircleCol=(255,255,255)
                            
            if shape=="filled Circle":
                filledCircleCol=selected
                screen.blit(copy2,(0,0))
                draw.ellipse(screen,col,(min(startx,mx),min(starty,my),abs(mx-startx),abs(my-starty)))
            else:
                filledCircleCol=(255,255,255)

        #POLYGON SHAPES---------------------------------------
        if click and canvasRect.collidepoint(mx,my):#ensures first click is on canvas
            screen.set_clip(canvasRect)
            
            if shape=="polygon":
                if width<4:
                    width=4
                if click and polyMode=="poly1":
                    #print("1")
                    polypoints.append([mx,my])
                                      
                    polyWidths.append(width)
                    polyWidth=(polyWidths[-1])#Takes most recently updated polyWidth
                    
                    polyCols.append(col)
                    polyCol=(polyCols[-1])
                    
                    polyRect=Rect(mx-width/2,my-width/2,width,width)
                    polyRects.append(polyRect)
                    polyRect=(polyRects[-1])
                    draw.rect(screen,(polyCol),polyRect)
                    
                    polyMode="poly2"
                elif click and polyMode=="poly2":
                    #print("2")
                    polypoints.append([mx,my])
                    draw.line(screen,(polyCol),polypoints[-2],polypoints[-1],polyWidth)
                    
                    if click and polyRect.collidepoint(mx,my):
                        polypoints.append(polypoints[0])
                        saying=20

                        if polygon=="unfilled":
                            draw.polygon(screen,(polyCol),polypoints,width+2)
                            
                        if polygon=="filled":
                            draw.polygon(screen,(polyCol),polypoints,0)
                            
                        polypoints=[]
                        polyMode="poly1"                

    #BACKGROUND TAB=================================================
    #BACKGROUND INTERFACE------------------------------------------
    if tab== "backgrounds":
        screen.blit(backgroundBack,backgroundBackRect)#tab back
        #Background Backs
        bxs=[23,169,315,461,607]
        for x in bxs:
            draw.rect(screen,(0,0,0),(x-b,687-b,100+2*b,70+2*b))
            if Rect(23-b,687-b,70+2*b,70+2*b).collidepoint(mx,my):
                draw.rect(screen,(255,0,0),(23-b,687-b,100+2*b,70+2*b))
            if Rect(169-b,687-b,70+2*b,70+2*b).collidepoint(mx,my):
                draw.rect(screen,(255,0,0),(169-b,687-b,100+2*b,70+2*b))
            if Rect(315-b,687-b,70+2*b,70+2*b).collidepoint(mx,my):
                draw.rect(screen,(255,0,0),(315-b,687-b,100+2*b,70+2*b))
            if Rect(461-b,687-b,70+2*b,70+2*b).collidepoint(mx,my):
                draw.rect(screen,(255,0,0),(461-b,687-b,100+2*b,70+2*b))
            if Rect(607-b,687-b,70+2*b,70+2*b).collidepoint(mx,my):
                draw.rect(screen,(255,0,0),(607-b,687-b,100+2*b,70+2*b))

        #BACKGROUND ICONS------------------------------------------
        #Basement
        basementIcon2= transform.scale(basementIcon,(100,70))
        screen.blit(basementIcon2,basementRect)
        #Play Place
        playPlaceIcon2= transform.scale(playPlaceIcon,(100,70))
        screen.blit(playPlaceIcon2,playPlaceRect)
        #Park
        parkIcon2= transform.scale(parkIcon,(100,70))
        screen.blit(parkIcon2,parkRect)
        #Space
        spaceIcon2= transform.scale(spaceIcon,(100,70))
        screen.blit(spaceIcon2,spaceRect)
        #Heaven
        heavenIcon2= transform.scale(heavenIcon,(100,70))
        screen.blit(heavenIcon2,heavenRect)

        #BACKGROUND USE-----------------------------
        if basementRect.collidepoint(mx,my) and mb[0]==1:
            basementIcon3= transform.scale(basementIcon,(658,550))
            screen.blit(basementIcon3,canvasRect)

        if playPlaceRect.collidepoint(mx,my) and mb[0]==1:
            playPlaceIcon3= transform.scale(playPlaceIcon,(658,550))
            screen.blit(playPlaceIcon3,canvasRect)

        if parkRect.collidepoint(mx,my) and mb[0]==1:
            parkIcon3= transform.scale(parkIcon,(658,550))
            screen.blit(parkIcon3,canvasRect)

        if heavenRect.collidepoint(mx,my) and mb[0]==1:
            heavenIcon3= transform.scale(heavenIcon,(658,550))
            screen.blit(heavenIcon3,canvasRect)

        if spaceRect.collidepoint(mx,my) and mb[0]==1:
            spaceIcon3= transform.scale(spaceIcon,(658,550))
            screen.blit(spaceIcon3,canvasRect)

    #EXTRAS TAB=================================================
    #EXTRAS INTERFACE------------------------------------------
    if tab== "extras":
        #Tab Background
        screen.blit(extrasBack,extrasBackRect)
        backRects()
        #Extras ICONS------------------------------
        #Line Icon
        draw.rect(screen,(music1Col),music1Rect)
        screen.blit(music1Icon,(15,700,70,70))
        #Unfilled Rect Icon
        draw.rect(screen,(music2Col),music2Rect)
        screen.blit(music2Icon,(105,700,70,70))
        #Filled Rect Icon
        draw.rect(screen,(music3Col),music3Rect)
        screen.blit(music3Icon,(195,700,70,70))
        #Unfilled Circle Icon
        draw.rect(screen,(music4Col),music4Rect)
        screen.blit(music4Icon,(285,700,70,70))
        #Filled Circle Icon
        draw.rect(screen,(music5Col),music5Rect)
        screen.blit(music5Icon,(375,700,70,70))
        #Nyan Song Icon
        draw.rect(screen,(music6Col),music6Rect)
        screen.blit(music6Icon,(465,700,70,70))        
        #Dotter Icon
        draw.rect(screen,(dotterCol),dotterRect)
        screen.blit(dotterIcon,(dotterRect))
        #Fade Icon
        draw.rect(screen,(fadeCol),fadeRect)
        screen.blit(fadeIcon,(fadeRect))

        

        #EXTRAS SELECTION-----------------------------
        if music1Rect.collidepoint(mx,my):
            if mb[0]==1:
                saying=28
                extra="music1"
                
        if music2Rect.collidepoint(mx,my):
            if mb[0]==1:
                saying=29
                extra="music2"

                
        if music3Rect.collidepoint(mx,my):
            if mb[0]==1:
                saying=30
                extra="music3"

                
        if music4Rect.collidepoint(mx,my):
            if mb[0]==1:
                saying=31
                extra="music4"

                
        if music5Rect.collidepoint(mx,my):
            if mb[0]==1:
                saying=32
                extra="music5"


        if music6Rect.collidepoint(mx,my):
            if mb[0]==1:
                saying=33
                extra="music6"

                
        if dotterRect.collidepoint(mx,my):
            saying=26
            if mb[0]==1:
                extra="dotter"
                #print(extra)
                
        if fadeRect.collidepoint(mx,my):
            saying=27
            if mb[0]==1:
                extra="fade"
                #print(extra)


                
        #CANVAS DRAW-------------------------                
        if mb[0]==1 or mb[2]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)

            #EXTRA USE-----------------------
            if extra=="music1":
                music1Col=selected
                mixer.music.load("music1.mp3")       # load a MUSIC object
                mixer.music.play()
            else:
                music1Col=(255,255,255)

            if extra=="music2":
                music2Col=selected
                mixer.music.load("music2.mp3")       # load a MUSIC object
                mixer.music.play()
            else:
                music2Col=(255,255,255)
                
            if extra=="music3":
                music3Col=selected
                mixer.music.load("music3.mp3")       # load a MUSIC object
                mixer.music.play()
            else:
                music3Col=(255,255,255)

            if extra=="music4":
                music4Col=selected
                mixer.music.load("music4.mp3")       # load a MUSIC object
                mixer.music.play()
            else:
                music4Col=(255,255,255)

            if extra=="music5":
                music5Col=selected
                mixer.music.load("music5.mp3")       # load a MUSIC object
                mixer.music.play()
            else:
                music5Col=(255,255,255)
                
            if extra=="music6":
                music6Col=selected
                mixer.music.load("music6.mp3")       # load a MUSIC object
                mixer.music.play()
            else:
                music6Col=(255,255,255)

            if extra=="dotter":
                dotterCol=selected
                mx-=mx%20
                my-=my%20
                draw.circle(screen,(255,0,0),(mx,my),10)
            else:
                dotterCol=(255,255,255)
                
            if extra=="fade":
                fadeCol=selected
                trail.append([mx,my,255])

                for circ in trail:
                     if circ[2]>0:
                        circ[2]-=3
                        draw.circle(screen,(circ[2],255-circ[2],255-circ[2]),circ[:2],width)
            else:
                fadeCol=(255,255,255)

                    
        
    #CLEAN CANVAS--------------------------------------
    if cleanRect.collidepoint(mx,my):
        saying=17
        if mb[0]==1:
            draw.rect(screen,(255,255,255),canvasRect)
            polypoints=[]
            polyMode="poly1"
            trail=[]
            #print("cleaning")
                
    screen.set_clip(None)
    display.flip()  # all drawing happens to memory, this copies it to the screen


quit()
