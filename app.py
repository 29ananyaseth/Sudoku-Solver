from flask import Flask, request, jsonify
from src.solver import solve_sudoku
from src.validator import validate_board

app = Flask(__name__)

@app.route("/solve", methods=["POST"])
def solve():
    try:
        # Get the board from the request
        data = request.json
        board = data.get("grid", [])
        
        # Validate the board
        if not validate_board(board):
            return jsonify({"error": "Invalid Sudoku grid"}), 400
        
        # Solve the board
        if solve_sudoku(board):
            return jsonify({"solved": True, "grid": board})
        else:
            return jsonify({"solved": False, "error": "No solution exists"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "Sudoku Solver API is running!"

if __name__ == "__main__":
    app.run(debug=True)
