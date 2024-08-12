#!/usr/bin/env python3

"""
- https://github.com/kodecocodes/swift-algorithm-club/tree/master/Myers%20Difference%20Algorithm
- https://blog.jcoglan.com/2017/02/15/the-myers-diff-algorithm-part-2/
- http://www.xmailserver.org/diff2.pdf
- https://medium.com/skyrise/the-myers-diff-algorithm-and-kotlin-observable-properties-69dfb18541b

"""
def diff(s1: str, s2: str):
    """
    Find the smallest edits required
    records the best value of x we can reach at each (d, k) position:
    """
    # Get the most number of moves we can make
    N, M = len(s1), len(s2)
    MAX = N + M

    # Store the latest x value for each k
    # Enough space for positive and negative k values
    V = [None] * (2 * MAX + 2)
    # Algoritm starts at position 1
    # This represents a point on line k = 1 where x = 0.
    # This is therefore the point ( 0, -1 ).
    # We are guaranteed to move down from this point, which takes us to ( 0, 0 ) as required.
    V[1] = 0

    history = []

    for d in range(0, MAX + 1):
        history.append(V[:])
        # We have + 1 because we start at index 1
        # Determine the best move we can make from the previous position
        for k in range(-d, d + 1, 2):
            # Move downward, inserts
            if (k == -d or (k != d and V[k-1] < V[k+1])):
                x = V[k+1]
            else:
            # Move rightward and take x as one greater than the previous k-1, removes
                x = V[k-1] + 1
            # Calculate y from this chosen x value and the current k.
            # We find y by having k = x-y
            y = x - k    
            
            # Check if we can take any diagonal step (snake)
            # As long as we've not deleted the entire s1 string or
            # added the entire s2 string, and the elements of each string at
            # the current position are the same, we can increment both x and y. 
            while x < N and y < M and s1[x] == s2[y]:
                x,y = x + 1, y + 1
            
            # Store the value of x reach at the current k line
            V[k] = x

            # We return d if we've reached the bottom-right position
            # telling the caller the minimum number of edits required to convert from a to b.
            if x >= N and y >= M:
                # history.append(V[:])
                return history
        # history.append(V[:])
    assert False, "Not find edit script"

tuple_list_int = tuple[list[(int, int)], list[(int, int)]]

def backtracking(history: list[list[int]], x: int, y: int) \
    -> tuple_list_int:
    """
    Get the path to follow and the trace given a history from Myers algorithm
    """

    path, trace = [], []
    path.append((x,y))

    # Iterate in reverse order each (d,v)
    for d in range(len(history) - 1, 0, -1):
        k = x-y
        # Move downward, inserting
        if k == -d or (k != d and history[d][k-1] < history[d][k+1]):
            prevk = k + 1
        else:
        # Move rightward, removes
            prevk = k - 1
        prevx = history[d][prevk]
        prevy = prevx - prevk

        # Get diagonal moves at (x,y)
        while x > prevx and y > prevy:
            trace.append((x,y))
            x, y = x - 1, y - 1
            path.append((x,y))
        x, y = prevx, prevy
        path.append((x,y))

    return path, trace

def get_common_subsequence(trace: list[tuple[int, int]], new: str) -> str:
    common_subsequence = ""
    for _, i in trace:
        common_subsequence += new[i - 1]
    return common_subsequence[::-1]

def main():
    s1 = "abcabba"
    s2 = "cbabac"
    # s1 = "cbaba"
    # s2 = "acabb"
    # s1 = "AGGTAB"
    # s2 = "GXTXAYB"
    # s1 = "BD"
    # s2 = "ABCD"
    
    with open("f1.txt") as f1:
        lines1 = [line.rstrip() for line in f1.readlines()]

    with open("f2.txt") as f2:
        lines2 = [line.rstrip() for line in f2.readlines()]


    history = diff(s1, s2)
    print(history)
    path, trace = backtracking(history, len(s1), len(s2))
    common_subseqence = get_common_subsequence(trace, s2)
    print(f"path -> {path}")
    print(f"trace -> {trace}")
    print(f"commong subsequence -> {common_subseqence}")

if __name__ == '__main__':
    main()
