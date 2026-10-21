from stockfish import Stockfish


def main():
    # Initialize Stockfish (make sure path is correct)
    stockfish = Stockfish(path="./stockfish/stockfish-windows-x86-64-avx2.exe")

    # Moves played so far from starting position
    moves = []
    
    while True:
        opponent_move = input("Enter opponent_move: ")
        moves.append(opponent_move)
        # Set position from moves
        stockfish.set_position(moves)

        # Get best move from Stockfish
        best_move = stockfish.get_best_move()
        moves.append(best_move)
        print(f"All moves: {moves}")
        print("Best move:", best_move)
        print(stockfish.get_board_visual())
    
if __name__ == "__main__":
    main()
