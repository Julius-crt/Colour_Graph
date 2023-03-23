import numpy as np
import sys
import pygame
from queue import Queue

pygame.init()

if(len(sys.argv) != 2):
    print("Please put a Number between 0-16777215")
    raise SystemExit

#Globale Variablen-----------------------------------------------------------------------
screenpix = xpixel,ypixel = 1080, 720
arrayx, arrayy = xpixel, int(ypixel/1.25)
oldx, oldy = arrayx,arrayy
brushcol = 0  #0
brushwith = 10 #10
backcol= 16777210 #0-16777215 0xrrggbbaa
planecol = sys.argv[1] #egal #109 #199 #199199
#TODO evtl. farben als RGB valuesdarstellen

#Hilfsfunktionen-------------------------------------------------------------------------
def initArray(backgroundcolor:int, border:int, borderwith:int, xpix:int, ypix:int):
    array = np.full((xpix,ypix),backgroundcolor)
    array[0:(int(borderwith/2)), : ] = border
    array[ : ,0:(int(borderwith/2))] = border
    array[-(int(borderwith/2)): , : ] = border
    array[ : , -(int(borderwith/2)):  ] = border
    return array

def find_neighbors(array, boarder:int,  old_val:int, new_val:int, x: int, y: int):

    # Finding north, south, east, west neighbors
    possible_neighbors = [(x, y+1),(x+1, y+0),(x+0, y-1),(x-1, y+0)]

    # Exclusing neighbors that should not be colored because they are borders or out of bound
    neighbors =  []
    for possible_neighbor in possible_neighbors:
        if (possible_neighbor[0] >= 0 and possible_neighbor[1] >= 0 and possible_neighbor[0] < array.shape[0] and possible_neighbor[1] < array.shape[1]):
            if array[possible_neighbor] == old_val and array[possible_neighbor] != boarder:
                neighbors.append(possible_neighbor)
    return neighbors

def floodFill(array: np.array, boarder:int, new_val:int,x:int, y:int,):
    old_val = array[x,y]
    if new_val == old_val or array[x,y] == boarder:
        return

    q = Queue(maxsize=0)
    q.put((x,y))

    # Coloring the initial location
    array[x,y] = new_val
    durchl = 0

    while not q.empty():
        durchl += 1
        current_loc = q.get()

        possible_neighbors = find_neighbors(array, boarder, old_val, new_val, current_loc[0], current_loc[1])

        # Coloring as we are enqueuing neighbors
        for neighbor in possible_neighbors:
            array[neighbor] = new_val
            q.put(neighbor)

        if(durchl > 16384 * 60):
            
            break

#TODO die flächen und ihre anliegenden flächen erkenn
#TODO Sie in einen Graph einlesen
#TODO einen Coloring algorithmus schreiben, der als input eine liste von farben bekomm

#----------------------------------------------------------------------------------------

pixelarray = initArray(backcol,brushcol,brushwith,arrayx,arrayy)

screen = pygame.display.set_mode((xpixel,ypixel))
pygame.display.set_caption('CathUpKurs Project: Julius')
clock = pygame.time.Clock()


#jede loop iteration ist ein Frame im Game
while True:
    # Process player inputs here.--------------------------------------------------------
    # ...
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        #EVENT='MALEN'
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons == (1,0,0):
                x1, y1 = event.pos
                print(str(event.pos))
                durchlaeufe = 1
                #TODO den initpunkt neu festlegen und in funktion kapseln, hat leider keine abbruchbedingung
                while (x1 != oldx) or (y1 != oldy):
                    durchlaeufe = durchlaeufe +1
                    pixelarray[oldx-2:oldx+2,oldy-2:oldy+2] = brushcol
                    if(oldx >= x1):
                        oldx -= 1
                    else:
                        oldx += 1
                    if(oldy >= y1):
                        oldy -= 1
                    else:
                        oldy += 1
                    if(durchlaeufe > 1000):
                        break
        #EVENT='FÜLLEN'
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 2:#mitteclick
                pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:#rechtsclick
                print("rechtsclick")
                x2,y2 = event.pos
                floodFill(pixelarray,brushcol,planecol,x2,y2) 
                    


    # Do logical updates here.-----------------------------------------------------------
    # ...
    # TODO Button einfügen, mit colour picker


    # Render the graphics here.----------------------------------------------------------
    # ...
    screen.fill("dim grey")
    pygame.draw.rect(screen,"black",pygame.Rect(70,arrayy+50 ,100,35))

    showarray = pygame.pixelcopy.make_surface(pixelarray)
    #showing the numpy array
    screen.blit(showarray, (0, 0))

    #------------------------------------------------------------------------------------
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
    #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