# def test_hilarious_thing():
#     assert 1 == 2


def hand_counter(hand):
    total = 0
    for card in hand:
        if card in ["K", "Q", "J"]:
            total += 10
        elif card == "A":
            if total + 11 > 21:
                total += 1
            else:
                total += 11
        else:
            total += card
    return total


def test_hand_counter_counts_up_all_vals_in_a_list():
        hand = [2, 4, 6]
        result = hand_counter(hand)
        assert result == 12


def test_hand_counter_counts_up_all_vals_in_a_list_with_K():
        hand = ["K", 4]
        result = hand_counter(hand)
        assert result == 14


def test_hand_counter_counts_up_all_vals_in_a_list_with_Q():
        hand = ["Q", 10]
        result = hand_counter(hand)
        assert result == 20


def test_hand_counter_counts_up_all_vals_in_a_list_with_J():
        hand = ["J", 5]
        result = hand_counter(hand)
        assert result == 15


def test_hand_counter_counts_up_all_vals_in_a_list_with_A():
        hand = ["A", 4]
        result = hand_counter(hand)
        assert result == 15


def test_hand_counter_counts_up_all_vals_in_a_list_with_A_as_1():
        hand = [10, "J", "A"]
        result = hand_counter(hand)
        assert result == 21


def test_hand_counter_counts_up_all_vals_in_a_list_with_A_as_11():
        hand = ["A", 9, "J"]
        result = hand_counter(hand)
        assert result == 20
