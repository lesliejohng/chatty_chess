""" I am Theresa.
	
	This creates an analysis board. It is based on 
    'piece-centric' approach. 
	
	The 64 elelments of the board hold either an empty
	square or a piece. 
	
	The squares and pieces are self-aware and are able
	to report on factors which affect them. 
	
	A piece, for example knows is it is being attackers, 
	or is undefended. A square knows, for example, which 
	colour controls it, or whether it is important for 
	tactical or strategic reasons.
	
	This information is used to decide on moves and to
	inform my conversations about the position"""
	
import chess

def generateConnectedSquares():
    """I am Therasa.
    
    Here I establish which squares on a blank chess
    board are related to each other through potential 
    chess moves. This information is key to my approach
    to looking for chess moves.
    
    It is the pieces that tie squares together the rules
    of their movements interconnect parts of the chess
    board.
    
    I originally used lists and a dictionary to create
    the connected square list then I awoke one morning 
    worrying if the list would be altered later and 
    wanting the final output to be a tuple of tuples.
    
    To calculate connected squares I am using the 
    following variables:
    
    boardCSL - a list of connected squares
        This is the variable that forms the basis for
        the output, is converted to a tuple (boardCST) 
        which is then returned
    squareCSL - a list of connected squares
        This is the variable used to build a list
        of those squares connected to a given
        square. Before being added to boardCSL it is
        converted to a tuple. (squareCST)
    squareCST - a tuple of connected squares for a
        given square on the board
    boardCST  - a tuple containing tuples for each
        square of the board which give the connected
        squares    
    
    In these variable the square numbers are 
    referenced using the same convention used by
    Python Chess using the number 0 to 63 where 0 is
    the square a1, 1 is b1, ... 8 is a2 ... 63 is h8.
    
    Connected squares are discovered by adding to or 
    subtacting from the square number of the square
    being checked being checked and then ensuring that
    this calculation remains within the boundaries of
    the board.
    
    These boundary checks cover both the top/bottom and
    left/right edges of the board.    
    
    In this approach I use a visualisation based on the
    points of of a compassfrom White's viewpoint:
    - North, South, East, West are the Rook moves from
        that square.
    - North-East, South East, South-West and North-West
        are the Bishop Moves from that square and
    - a single step to the North North East, East North 
        East, East South East, South South East, South
        South West, West South West, West North West and
        North by North West ( a favorite film of mine )
        are the Knight moves from that square.
        
    'I love chess both as a game and because of what it
    can teach us about life. Theresa' 
    """
    
    boardCSL = []

    for square in range(64):
        squareCSL = []
        # northerly moves along file
        s = square + 8
        while s < 64:
            squareCSL.append(s)
            s = s + 8
        # North North East move by knight
        s = square + 17
        if s % 8 > square % 8:
            if s < 64:
                squareCSL.append(s) 
        # North East moves along diagonal
        s = square + 9
        while s % 8 > square % 8:
            if s < 64:
                squareCSL.append(s)
            s = s + 9
        # East North East knight move
        s = square + 10
        if s % 8 > square % 8:
            if s < 64:
                squareCSL.append(s) 
        # Easterly moves along rank
        s = square + 1
        while s % 8 > square % 8:
            squareCSL.append(s)
            s = s + 1
        # East South East knight move
        s = square - 6
        if s % 8 > square % 8:
            if s >= 0:
                squareCSL.append(s)
        # South East moves along diagonal
        s = square - 7
        while s % 8 > square % 8:
            if s >= 0:
                squareCSL.append(s)
            s = s - 7
        # South South East knight move
        s = square - 15
        if s % 8 > square % 8:
            if s >= 0:
                squareCSL.append(s)
        # Southerly moves along Rank
        s = square - 8
        while s >= 0:
            squareCSL.append(s)
            s = s - 8
        # South South West Knight move
        s = square - 17
        if s % 8 < square % 8:
            if s >= 0:
                squareCSL.append(s)
        # South Westerly along diagomal
        s = square - 9
        while s % 8 < square % 8:
            if s >= 0:
                squareCSL.append(s)
            s = s - 9
        # West South West Knight move 
        s = square - 10
        if s % 8 < square % 8:
            if s >= 0:
                squareCSL.append(s)
        # Westerly moves along rank
        s = square - 1
        while s % 8 < square % 8:
            if s >= 0:
                squareCSL.append(s) 
            s = s - 1
        # West North West knight move
        s = square + 6
        if s % 8 < square % 8:
            if s < 64:
                squareCSL.append(s)
        # North West moves along diagonal
        s = square + 7
        while s % 8 < square % 8:
            if s < 64:
                squareCSL.append(s)
            s = s + 7
        # North North West Knight move
        s = square + 15
        if s % 8 < square % 8:
            if s < 64:
                squareCSL.append(s)
        squareCST= tuple(squareCSL)
        boardCSL.append(squareCST)
        del squareCST
    boardCST = tuple(boardCSL)
    return boardCST
	
connectedSquares = generateConnectedSquares()


