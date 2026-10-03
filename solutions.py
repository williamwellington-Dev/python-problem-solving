"""
Selected solutions to problems from "109 Python Problems for CCPS 109"
by Ilkka Kokkarinen (https://github.com/ikokkari/PythonProblems).

Author: William Wellington
All functions pass the course's automated tester (tester109.py).
"""


def josephus(n, k):
    """Josephus problem: n people stand in a circle and every k-th person is eliminated.
    Returns the order in which people are eliminated.
    """
    ndx = k
    lineUp = list(range(1, n + 1))
    order = []
    while len(lineUp) != 0:
        while ndx > len(lineUp):
            ndx -= len(lineUp)
        order.append(lineUp[ndx - 1])
        del lineUp[ndx - 1]

        ndx += k - 1
    return order


def first_preceded_by_smaller(items, k=1):
    """Returns the first element of items that has at least k smaller elements
    somewhere before it in the list, or None if no element qualifies.
    """
    for i in range(len(items)):
        j = 0
        count = 0
        while j < i:
            if items[j] < items[i]:
                count += 1
            j += 1
        if count >= k:
            return items[i]
    return None


def reverse_ascending_sublists(items):
    """Splits items into maximal strictly ascending runs, reverses each run in place,
    and returns the resulting list.
    """
    if items == []:
        return []
    result = [[items[0]]]
    for i in range(1, len(items)):
        if items[i - 1] < items[i]:
            result[-1].append(items[i])
        else:
            result.append([items[i]])
    reverse_result = [j[::-1] for (i, j) in enumerate(result, 1)]
    flatten = lambda *n: (
        e for a in n for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,))
    )

    return list(flatten(reverse_result))


def collapse_intervals(items):
    """Collapses a sorted list of distinct integers into a compact range string,
    e.g. [1, 2, 3, 5, 7, 8] -> '1-3,5,7-8'.
    """
    result = ""
    if len(items) <= 1:
        return str(items[0])
    else:
        i = 0
        long = len(items)
        while i < long - 1:
            if items[i + 1] - items[i] != 1:
                result = result + str(items[i]) + ","
                i += 1
            else:
                result = result + str(items[i]) + "-"
                while (i < len(items) - 1) and (items[i + 1] - items[i] == 1):
                    i += 1
                else:
                    if i < len(items):
                        result = result + str(items[i]) + ","
                        i += 1
                    else:
                        return result
        if items[-1] - items[-2] != 1:
            result += str(items[-1])
        if result[-1] == ",":
            return result[:-1]
        return result


def knight_jump(knight, start, end):
    """Checks whether a generalized knight can jump from start to end in k-dimensional
    space: the absolute coordinate differences must be a rearrangement of the knight's move.
    """
    knight = list(knight)
    difference = [0] * len(knight)

    for i, value in enumerate(difference):
        difference[i] = abs(start[i] - end[i])

    for i, value in enumerate(knight):
        if value in difference:
            difference.remove(value)

    if len(difference) == 0:
        return True
    return False


def give_change(amount: int, coins):
    """Greedy change-making: breaks amount into coins, using the largest coin
    possible at each step. Coins are given in descending order.
    """
    change = []
    idx = 0
    while amount:
        if amount - coins[idx] >= 0:
            change.append(coins[idx])
            amount -= coins[idx]
        else:
            idx += 1
    return change


def milton_work_point_count(hand, trump="notrump"):
    """Estimates the strength of a 13-card bridge hand using the Milton Work point
    count (A=4, K=3, Q=2, J=1), adjusted for hand shape, long suits, and short
    suits when there is a trump suit.
    """

    suits = {"spades": 0, "hearts": 0, "diamonds": 0, "clubs": 0}

    points = 0

    for card in hand:

        value, suit = card

        if value == "ace":
            points += 4
        elif value == "king":
            points += 3
        elif value == "queen":
            points += 2
        elif value == "jack":
            points += 1

        suits[suit] += 1

    if sorted(suits.values()) == [3, 3, 3, 4]:
        points -= 1
        return points

    for suit, n in suits.items():

        if n >= 7:
            points += 3
        elif n == 6:
            points += 2
        elif n == 5:
            points += 1

        if trump != "notrump" and suit != trump:
            if n == 0:
                points += 5
            elif n == 1:
                points += 3

    return points


def eliminate_neighbours(items):
    """Given a permutation of 1..n, repeatedly removes the smallest remaining number
    together with its larger neighbour. Returns how many removals it takes until
    the largest number n is eliminated.
    """
    if len(items) == 1:
        return 1
    items = list(items)
    n = len(items)
    counter = 0
    for i in range(1, n + 1):
        if i in items:
            counter += 1
            if len(items) == 1:
                items.pop(0)
                break
            index1 = items.index(i)
            index2 = index1 - 1

            if index2 < 0 or (
                (index1 + 1) < len(items) and items[index1 + 1] > items[index2]
            ):
                index2 = index1 + 1

            value = items[index2]

            if index1 > index2:
                index1 = index2

            items.pop(index1)
            items.pop(index1)

            if value == n:
                break
    return counter


def words_with_given_shape(words, shape):
    """Returns the words whose letter-to-letter 'shape' matches the given pattern,
    where each step is 1 (next letter is higher), 0 (same) or -1 (lower).
    """
    wlist = []
    for word in words:
        if len(word) != len(shape) + 1:
            continue
        slist = [
            1 if word[i] < word[i + 1] else 0 if word[i] == word[i + 1] else -1
            for i in range(len(word) - 1)
        ]
        if slist == shape:
            wlist.append(word)
    return wlist


def perimeter_limit_split(a, b, p):
    """Returns the minimum number of straight cuts needed to split an a x b rectangle
    into pieces whose perimeters are all at most p. Solved with recursion plus
    memoization (dynamic programming) in perimeter_limit_split_dp.
    """
    dp = [[None] * (b + 1) for i in range(a + 1)]
    return perimeter_limit_split_dp(a, b, p, dp)


def perimeter_limit_split_dp(a, b, p, dp):
    """Recursive helper for perimeter_limit_split. dp[a][b] caches the best answer
    for an a x b piece so each subproblem is solved only once.
    """
    if p >= 2 * (a + b):
        return 0
    m1 = m2 = M1 = M2 = 0
    m = float("inf")
    if a > 1:
        for i in range(1, a // 2 + 1):
            m1 = perimeter_limit_split_dp(i, b, p, dp) if dp[i][b] == None else dp[i][b]
            m2 = (
                perimeter_limit_split_dp(a - i, b, p, dp)
                if dp[a - i][b] == None
                else dp[a - i][b]
            )
            m = min(1 + m1 + m2, m)
    if b > 1:
        for i in range(1, b // 2 + 1):
            m1 = perimeter_limit_split_dp(a, i, p, dp) if dp[a][i] == None else dp[a][i]
            m2 = (
                perimeter_limit_split_dp(a, b - i, p, dp)
                if dp[a][b - i] == None
                else dp[a][b - i]
            )
            m = min(1 + m1 + m2, m)
    dp[a][b] = m
    return m
