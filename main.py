import PySimpleGUI as sg
finalize=True
def newboard():
    window["11"].update("")
    window["12"].update("")
    window["13"].update("")
    window["21"].update("")
    window["22"].update("")
    window["23"].update("")
    window["31"].update("")
    window["32"].update("")
    window["33"].update("")
def wincheck(tictac):
    #1 means game not finished
    #2 means X wins
    #3 means O wins
    if (tictac[0][0]==1 and tictac[0][1]==1 and tictac[0][2]==1)or(tictac[0][0]==2 and tictac[0][1]==2 and tictac[0][2]==2):
        if tictac[0][0]==1:
            return 2
        else:
            return 3
    elif (tictac[1][0]==1 and tictac[1][1]==1 and tictac[1][2]==1)or(tictac[1][0]==2 and tictac[1][1]==2 and tictac[1][2]==2):
        if tictac[1][0]==1:
            return 2
        else:
            return 3
    elif (tictac[2][0]==1 and tictac[2][1]==1 and tictac[2][2]==1)or(tictac[2][0]==2 and tictac[2][1]==2 and tictac[2][2]==2):
        if tictac[2][0]==1:
            return 2
        else:
            return 3
    elif (tictac[0][0]==1 and tictac[1][0]==1 and tictac[2][0]==1)or(tictac[0][0]==2 and tictac[1][0]==2 and tictac[2][0]==2):
        if tictac[0][0]==1:
            return 2
        else:
            return 3
    elif (tictac[0][1]==1 and tictac[1][1]==1 and tictac[2][1]==1)or(tictac[0][1]==2 and tictac[1][1]==2 and tictac[2][1]==2):
        if tictac[0][1]==1:
            return 2
        else:
            return 3
    elif (tictac[0][2]==1 and tictac[1][2]==1 and tictac[2][2]==1)or(tictac[0][2]==2 and tictac[1][2]==2 and tictac[2][2]==2):
        if tictac[0][2]==1:
            return 2
        else:
            return 3
    elif (tictac[0][0]==1 and tictac[1][1]==1 and tictac[2][2]==1)or(tictac[0][0]==2 and tictac[1][1]==2 and tictac[2][2]==2):
        if tictac[0][0]==1:
            return 2
        else:
            return 3
    elif (tictac[0][2]==1 and tictac[1][1]==1 and tictac[2][0]==1)or(tictac[0][2]==2 and tictac[1][1]==2 and tictac[2][0]==2):
        if tictac[0][2]==1:
            return 2
        else:
            return 3
    else:
        return 1
def tiecheck(tictac):
    if wincheck(tictac)==1 and tictac[0][0]!=0 and tictac[0][1]!=0 and tictac[0][2]!=0 and tictac[1][0]!=0 and tictac[1][1]!=0 and tictac[1][2]!=0 and tictac[2][0]!=0 and tictac[2][1]!=0 and tictac[2][2]!=0:
        return True
    else:
        return False
layout = [[sg.Text("Player 1's Turn",key="TITLE")],
          [sg.Button(' ',size=(6,3),key="11"),sg.Button(' ',size=(6,3),key="12"),sg.Button(' ',size=(6,3),key="13")],
          [sg.Button(' ',size=(6,3),key="21"),sg.Button(' ',size=(6,3),key="22"),sg.Button(' ',size=(6,3),key="23")],
          [sg.Button(' ',size=(6,3),key="31"),sg.Button(' ',size=(6,3),key="32"),sg.Button(' ',size=(6,3),key="33")],
          [sg.Text('Player 1: 0',key="p1points")],
          [sg.Text('Player 2: 0',key="p2points")],
          [sg.Button('Reset Points',key='rp'),sg.Button('Reset Round',key='rr')]]
playerone=0
playertwo=0
board=[[0,0,0],[0,0,0],[0,0,0]]
window=sg.Window('TicTacToe', layout)
turn="p1"#True = Player 1 Turn, False = Player 2 Turn
while True:
    if turn=='p1':
        window["TITLE"].update("Player 1's Turn")
    elif turn=='p2':
        window["TITLE"].update("Player 2's Turn")
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if event == 'rp':
        playerone=0
        playertwo=0
        window["p1points"].update("Player 1: " + str(playerone))
        window["p2points"].update("Player 2: " + str(playertwo))
    elif event == 'rr':
        window["11"].update("")
        window["12"].update("")
        window["13"].update("")
        window["21"].update("")
        window["22"].update("")
        window["23"].update("")
        window["31"].update("")
        window["32"].update("")
        window["33"].update("")
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    if event!='rr' and event!='rp' and turn=="p1":
        cx=int(event[0])-1#event is coordinates
        cy=int(event[1])-1
        board[cx][cy]=1
        turn="p2"
    elif event!='rr' and event!='rp' and turn=="p2":
        cx = int(event[0]) - 1
        cy = int(event[1]) - 1
        board[cx][cy]=2
        turn="p1"
    for i in range(3):
        for j in range(3):
            if board[i][j]==1:
                window[str(i+1)+str(j+1)].update("X")#str is converting coordinates in button key value
            elif board[i][j]==2:
                window[str(i+1)+str(j+1)].update("O")
    if wincheck(board)==2:
        window["TITLE"].update("Player 1 Won!")
        playerone=playerone+1
        window["p1points"].update("Player 1: "+str(playerone))
        window["11"].update("")
        window["12"].update("")
        window["13"].update("")
        window["21"].update("")
        window["22"].update("")
        window["23"].update("")
        window["31"].update("")
        window["32"].update("")
        window["33"].update("")
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        turn="p1"
    elif wincheck(board)==3:
        window["TITLE"].update("Player 2 Won!")
        playertwo=playertwo+1
        window["p2points"].update("Player 2: "+str(playertwo))
        window["11"].update("")
        window["12"].update("")
        window["13"].update("")
        window["21"].update("")
        window["22"].update("")
        window["23"].update("")
        window["31"].update("")
        window["32"].update("")
        window["33"].update("")
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        turn="p2"
    if tiecheck(board)==True:
        window["11"].update("")
        window["12"].update("")
        window["13"].update("")
        window["21"].update("")
        window["22"].update("")
        window["23"].update("")
        window["31"].update("")
        window["32"].update("")
        window["33"].update("")
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]