import chess
import azg_chess.players as players
from functools import partial
from azg.Arena import Arena
from azg_chess.game import (
    BLACK_PLAYER,
    BOARD_DIMENSIONS,
    INVALID_MOVE,
    NUM_PIECES,
    NUM_SQUARES,
    VALID_MOVE,
    WHITE_PLAYER,
    ChessGame,
    PlayerID,
)




#os.environ["CUDA_VISIBLE_DEVICES"]=""



b = chess.Board()
#b.push(chess.Move.from_uci("e2e4"))

#p_stockfish_1350 = players.StockfishChessPlayer(engine_path='/usr/games/stockfish',engine_elo=1350)
p_random = players.RandomChessPlayer()
p_geo1 = players.GeochriPlayer(parameters_file='model_data/iter_1.tar',mcts_steps_per_move = 50)
p_geo2 = players.GeochriPlayer(parameters_file='model_data/iter_2.tar',mcts_steps_per_move = 50)
p_geo3 = players.GeochriPlayer(parameters_file='model_data/iter_3.tar',mcts_steps_per_move = 50)
p_geo4 = players.GeochriPlayer(parameters_file='model_data/iter_4.tar',mcts_steps_per_move = 50)
p_geo5 = players.GeochriPlayer(parameters_file='model_data/iter_5.tar',mcts_steps_per_move = 50)

TOTAL_GAMES = 5


def play_players(player1, player2, board, num_games = TOTAL_GAMES):
    outcomes = []
    for current_game in range(num_games):
        b.reset()
        print(f"========================= GAME {current_game+1} of {num_games}")
        while not (b.is_game_over()):
            m = player1.choose_move(b)
            print(m.uci())
            b.push(m)
            print(b)
            if b.is_game_over():
                break
            m = player2.choose_move(b.mirror())
            m = chess.Move(chess.square_mirror(m.from_square), chess.square_mirror(m.to_square), m.promotion)
            #m = player2.choose_move(b)
            print(m.uci())
            b.push(m)
            print(b)
            print("-----")

        print(b.outcome().result())
        outcomes.append(b.outcome().result())

    print(outcomes)

play_players(p_geo5,p_geo1, b, TOTAL_GAMES)