# Assignment-1
# Author- Jay Shah
# Date- 02/04/2023
# Iterative Deepening search (IDS) and A-star algorithms to solve a puzzle problem


"""What it does:
It's like a GPS for puzzles. It helps us find the best way to solve a puzzle like the 8-puzzle which is a grid of numbers with a missing tile.

It uses a smart strategy called "A-star search" and  “Iterative deepening”
 to figure out the shortest path to the solution.

How to use it:

Tell it the starting position of the puzzle pieces.Imagine the numbers lined up in a row,l ike this:[[1, 2, 3, 0, 4,5,6,7,8]. The “0” is the missing tile.

The script will do its work using sthe code and give us a list of moves to make.

Keep in mind:

The script assumes you're starting with a solvable puzzle. It won't tell us if the puzzle is impossible to solve.

The "A-star search" is good at finding the best path, but it can be even better with some extra guidance. That's why we might add more "heuristics" in the future, which are like little hints to help the search find the solution faster.
It would be awesome to show the puzzle-solving in action! We're thinking about adding pictures or animations to make it more fun to watch."""


import heapq


# the heuristic function
def heuristic(state):
    # goal state
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # total distance
    distance = 0

    # this will go in Loop each number
    for number in state:
        current_index = state.index(number)
        goal_index = goal_state.index(number)
        distance_x = goal_index % 3 - current_index % 3
        distance_y = goal_index // 3 - current_index // 3
        distance += abs(distance_x) + abs(distance_y)

    return distance


# function to apply the move
def applyMove(puzzle, move):
    new_puzzle = puzzle[:]

    empty_tile_index = new_puzzle.index(0)
    new_puzzle[empty_tile_index] = new_puzzle[move]
    new_puzzle[move] = 0
    return new_puzzle


# this will generate moves either to go up or down or side
def generateMoves(puzzle):
    possible_moves = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4, 6],
        4: [1, 3, 5, 7],
        5: [2, 4, 8],
        6: [3, 7],
        7: [4, 6, 8],
        8: [5, 7],
    }

    empty_tile_index = puzzle.index(0)
    return possible_moves[empty_tile_index]


# now we will go to iterating deepening


def iterativeDeepening(puzzle):
    # max depth of the function is 200
    max_depth = 200

    for depth in range(1, max_depth + 1):
        result = depthLimitedDFS(puzzle, depth)

        if result is not None:
            return result
    return None


# this will go to depth limited search
def depthLimitedDFS(puzzle, depth):

    if isGoalState(puzzle):
        return []

    # it will Check if we've reach the depth limit or not
    if depth == 0:
        return None

    # Generate the moves
    possible_moves = generateMoves(puzzle)

    for move in possible_moves:
        new_puzzle = applyMove(puzzle, move)
        result = depthLimitedDFS(new_puzzle, depth - 1)
        if result is not None:
            return [move] + result
    return None


# this is the function of goal state
def isGoalState(puzzle):
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    return puzzle == goal_state


# A-star search function
def astar(puzzle):
    open_states = []  # Stores states that are yet to be explored
    explored_states = set()  # Stores states that have been explored

    # Create an initial state with heuristic value, g-value, puzzle state, and path
    initial_state = (heuristic(puzzle), 0, puzzle, [])
    heapq.heappush(
        open_states, initial_state
    )  # Add the initial state to the open_states list

    # Start exploring states until there are no more states left in the open_states list
    while open_states:
        f, g, state, path = heapq.heappop(open_states)

        # Check if the current state is the goal state
        if state == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            return path  # If it is, return the path that led to the goal

        explored_states.add(tuple(state))
        possible_moves = generateMoves(state)

        # Explore each possible move
        for move in possible_moves:
            new_state = applyMove(state, move)
            new_g = g + 1  # Increment the g-value by 1 for the new state

            # Calculate the heuristic value for the new state
            h = heuristic(new_state)

            # Calculate the f-value (heuristic + g-value) for the new state
            new_f = new_g + h

            # Check if the new state has not been explored before
            if tuple(new_state) not in explored_states:
                # Add the new state to the open_states list with its f-value, g-value, state, and path
                heapq.heappush(open_states, (new_f, new_g, new_state, path + [move]))
    return []
