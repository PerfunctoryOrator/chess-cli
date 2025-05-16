//
//  main.swift
//  Chess-CLI
//
//  Created by Yashdeep Singh Fauzdar on 11/04/25.
//

import Foundation

let piecePositions = [
    "r", "n", "b", "q", "k", "b", "n", "r",
    "p", "p", "p", "p", "p", "p", "p", "p",
    "", "", "", "", "", "", "", "",
    "", "", "", "", "", "", "", "",
    "", "", "", "", "", "", "", "",
    "", "", "", "", "", "", "", "",
    "P", "P", "P", "P", "P", "P", "P", "P",
    "R", "N", "B", "Q", "K", "B", "N", "R",
]

func separator(_ columns: Int = 8, showRank: Bool = true) -> String {
    return (showRank ? "  " : "") + "+" + String(repeating: "-----+", count: columns) + "\n"
}
func rankIndicator(_ squareNumber: Int, flipped: Bool = false) -> String {
    return String(flipped ? squareNumber / 8 + 1 : 8 - squareNumber / 8) + " "
}
func fileIndicators(showRank: Bool = true, flipped: Bool = false) -> String {
    let files = ["a", "b", "c", "d", "e", "f", "g", "h"]
    var indicator = showRank ? "  " : ""
    for file in flipped ? files.reversed() : files {
        indicator += "   " + file + "  "
    }
    return indicator
}

func showBoard(flipped: Bool = false) {
    var board = ""
    var squareNumber = 0
    board += separator()
    board += rankIndicator(squareNumber, flipped: flipped)
    for piece in flipped ? piecePositions.reversed() : piecePositions {
        squareNumber += 1
        board += "|  " + (piece == "" ? " " : piece) + "  "
        if squareNumber % 8 == 0 {
            board += "|\n"
            board += separator()
            if squareNumber != 64 {
                board += rankIndicator(squareNumber, flipped: flipped)
            }
        }
    }
    board += fileIndicators(flipped: flipped)
    print(board)
}

showBoard()
