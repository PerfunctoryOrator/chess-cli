#
#  main.py
#  chess-py
#
#  Created by Yashdeep Singh Fauzdar on 18/04/25.
#

class ChessBoard:

    BOARD_PADDING = 2

    def __init__(self, pieceStyle = "text"):
        if pieceStyle == "text":
            self.pieces = {
                "R": "R", "N": "N", "B": "B",
                "Q": "Q", "K": "K", "P": "P",
                "": " ",
                "r": "r", "n": "n", "b": "b",
                "q": "q", "k": "k", "p": "p",
            };
        elif pieceStyle == "figurine":
            self.pieces = {
                "R": "♖", "N": "♘", "B": "♗",
                "Q": "♕", "K": "♔", "P": "♙",
                "": " ",
                "r": "♜", "n": "♞", "b": "♝",
                "q": "♛", "k": "♚", "p": "♟",
            };

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

    def separator(self, columns = 8, showRank = True):
        return ("  " if showRank else "") + "+" + ("-" * (2 * self.BOARD_PADDING + 1) + "+") * columns + "\n"

    def rankIndicator(self, squareNumber, flipped = False):
        return str(int(squareNumber / 8 + 1) if flipped else int(8 - squareNumber / 8)) + " "

    def fileIndicators(self, showRank = True, flipped = False):
        files = ["a", "b", "c", "d", "e", "f", "g", "h"]
        if flipped:
            files.reverse()

        if showRank:
            indicator = "  "
        else:
            indicator = ""

        for file in files:
            indicator += " " + " " * self.BOARD_PADDING + file + " " * self.BOARD_PADDING

        return indicator

    def showBoard(self, flipped = False):
        board = ""
        squareNumber = 0

        board += self.separator()
        board += self.rankIndicator(squareNumber, flipped = flipped)

        tempPiecePositions = self.piecePositions
        if flipped:
            tempPiecePositions.reverse()


        for piece in tempPiecePositions:
            squareNumber += 1

            board += "|" + " " * self.BOARD_PADDING + self.pieces[piece] + " " * self.BOARD_PADDING

            if squareNumber % 8 == 0:
                board += "|\n"
                board += self.separator()
                if squareNumber != 64:
                    board += self.rankIndicator(squareNumber, flipped = flipped)

        board += self.fileIndicators(flipped = flipped)
        print(board)


board = ChessBoard(pieceStyle = "text")
board.showBoard()
