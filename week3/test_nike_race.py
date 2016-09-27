# Just do it

from nike_race import Nike, Footrace


def test_can_create_nike():
    nike = Nike(5)
    assert nike.acceleration == 5
    assert nike.location == 0


def test_can_create_footrace():
    footrace = Footrace(150)
    assert footrace.distance == 150


def test_can_add_nike_to_race():
    footrace = Footrace(150)
    nike = Nike(1)
    footrace.add_nike(nike)
    assert footrace.nikes == [nike]


def test_can_add_nikes_to_race():
    footrace = Footrace(150)
    nike1 = Nike(1)
    nike2 = Nike(1)
    nike3 = Nike(1)
    footrace.add_nikes([nike1, nike2, nike3])
    assert footrace.nikes == [nike1, nike2, nike3]


def test_can_tick_all_nikes_forward():
    footrace = Footrace(300)
    nike1 = Nike(4)
    nike2 = Nike(2)
    nike3 = Nike(3)
    footrace.add_nikes([nike1, nike2, nike3])
    footrace.tick()
    assert footrace.nikes[0].location == 4
    assert footrace.nikes[1].location == 2
    assert footrace.nikes[2].location == 10


def test_can_notify_if_nike_has_not_won():
    footrace = Footrace(4)
    nike = Nike(1)
    footrace.add_nike(nike)
    footrace.tick()
    assert footrace.has_won() == False


def test_can_notify_if_nike_has_won():
    footrace = Footrace(4)
    nike = Nike(1)
    footrace.add_nike(nike)
    footrace.tick()
    footrace.tick()
    footrace.tick()
    footrace.tick()
    assert footrace.has_won() == True


def will_tell_you_who_won():
    footrace = Footrace(4)
    nike1 = Nike(1)
    nike2 = Nike(2)
    nike3 = Nike(3)
    footrace.add_nikes([nike1, nike2, nike3])
    footrace.tick()
    footrace.tick()
    footrace.has_won()
    assert footrace.winner == nike2


def test_will_announce_winer_correctly_if_they_are_past_the_finish_line():
    footrace = Footrace(25)
    nike1 = Nike(4)
    nike2 = Nike(7)
    nike3 = Nike(5)

    footrace.add_nikes([nike1, nike2, nike3])

    while not footrace.has_won():
        footrace.tick()
    assert footrace.winner == nike2
