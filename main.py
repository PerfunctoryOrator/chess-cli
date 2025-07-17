#
#  main.py
#  Chess-CLI
#
#  Created by Yashdeep Singh Fauzdar on 18/04/25.
#

class ChessBoard:

    def __init__(self, fen = ""):
        # Board setup
        self.piecePositions = [
            "r", "n", "b", "q", "k", "b", "n", "r",
            "p", "p", "p", "p", "p", "p", "p", "p",
            "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "",
            "P", "P", "P", "P", "P", "P", "P", "P",
            "R", "N", "B", "Q", "K", "B", "N", "R",
        ]

    def separator(self, showRank, xPadding, emptyRow = False, columns = 8):
        cellSpace = " " if emptyRow else "-"
        joint = "|" if emptyRow else "+"
        return ("  " if showRank else "") + joint + (cellSpace * (2 * xPadding + 1) + joint) * columns + "\n"

    def rankIndicator(self, squareNumber, flipped):
        return str(int(squareNumber / 8 + 1) if flipped else int(8 - squareNumber / 8)) + " "

    def fileIndicators(self, showRank, flipped, xPadding):
        files = ["a", "b", "c", "d", "e", "f", "g", "h"]
        if flipped:
            files.reverse()

        indicator = "  " if showRank else ""

        for file in files:
            indicator += " " + " " * xPadding + file + " " * xPadding

        return indicator

    def showBoard(self, pieceStyle = "text", showFilesRanks = True, flipped = False, xPadding = 1, yPadding = 0):
        # Define pieces
        pieceMap = {
            "R": "R", "N": "N", "B": "B",
            "Q": "Q", "K": "K", "P": "P",
            "": " ",
            "r": "r", "n": "n", "b": "b",
            "q": "q", "k": "k", "p": "p"
        } if pieceStyle == "text" else {
            "R": "♖", "N": "♘", "B": "♗",
            "Q": "♕", "K": "♔", "P": "♙",
            "": " ",
            "r": "♜", "n": "♞", "b": "♝",
            "q": "♛", "k": "♚", "p": "♟",
        }

        board = ""
        squareNumber = 0

        board += self.separator(showRank = showFilesRanks, xPadding = xPadding)
        board += (self.separator(showRank = showFilesRanks, xPadding = xPadding, emptyRow = True)) * yPadding
        if showFilesRanks:
            board += self.rankIndicator(squareNumber, flipped = flipped)

        tempPiecePositions = self.piecePositions
        if flipped:
            tempPiecePositions.reverse()


        for piece in tempPiecePositions:
            squareNumber += 1

            board += "|" + " " * xPadding + pieceMap[piece] + " " * xPadding

            if squareNumber % 8 == 0:
                board += "|\n"
                board += (self.separator(showRank = showFilesRanks, xPadding = xPadding, emptyRow = True)) * yPadding
                board += self.separator(showRank = showFilesRanks, xPadding = xPadding)
                if showFilesRanks and squareNumber != 64:
                    board += (self.separator(showRank = showFilesRanks, xPadding = xPadding, emptyRow = True)) * yPadding
                    board += self.rankIndicator(squareNumber, flipped = flipped)

        if showFilesRanks:
            board += self.fileIndicators(showRank = showFilesRanks, flipped = flipped, xPadding = xPadding)

        print(board)


board = ChessBoard()
board.showBoard()
