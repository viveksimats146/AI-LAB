# Minimax Algorithm Example

def minimax(depth, node_index, is_maximizing, values):
    """
    depth: current depth in the game tree
    node_index: index of the current node
    is_maximizing: True for Max player, False for Min player
    values: list of leaf node values
    """
    # Base case: reached leaf node
    if depth == 2:
        return values[node_index]

    # Maximizing player's turn
    if is_maximizing:
        return max(
            minimax(depth + 1, node_index * 2, False, values),
            minimax(depth + 1, node_index * 2 + 1, False, values)
        )
    # Minimizing player's turn
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, values),
            minimax(depth + 1, node_index * 2 + 1, True, values)
        )


# ----------------------------------------------------------
# Leaf nodes (final outcomes)
values = [3, 5, 2, 9]

# Depth of the tree = 2  (Root -> Min -> Leaves)
optimal_value = minimax(0, 0, True, values)
print("The optimal value for the maximizing player is:", optimal_value)

# ----------------------------------------------------------
# Determine best move (Left or Right subtree)
left_subtree = min(values[0], values[1])   # Min node on left
right_subtree = min(values[2], values[3])  # Min node on right

best_move = "Left" if max(left_subtree, right_subtree) == left_subtree else "Right"

print("The maximizing player should choose:", best_move)
