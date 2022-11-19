import pytest

from showbotlib.showbot import ShowTelegramBot


def test_output():
    test_out = """Name: Family Guy
Network Name: FOX
Network Country Name: United States
Summary:<b>Family Guy</b> follows Peter Griffin the endearingly ignorant dad, and his hilariously offbeat family of middle-class New Englanders in Quahog, RI. Lois is Peter's wife, a stay-at-home mom with no patience for her family's antics. Then there are their kids: 18-year-old Meg is an outcast at school and the Griffin family punching bag; 13-year-old Chris is a socially awkward teen who doesn't have a clue about the opposite sex; and one-year-old Stewie is a diabolically clever baby whose burgeoning sexuality is very much a work in progress. Rounding out the Griffin household is Brian the family dog and a ladies' man who is one step away from AA."""

    bot = ShowTelegramBot("tocken")
    assert bot.find_show_answer("Family Guy") == test_out


def test_add_favorites():
    bot = ShowTelegramBot("tocken")
    assert (
        bot.add_to_favorites(1, "Family Guy")
        == "Family Guy has been added to the favorites list"
    )
    assert (
        bot.add_to_favorites(1, "Rick and Morty")
        == "Rick and Morty has been added to the favorites list"
    )
    assert (
        bot.add_to_favorites(2, "Typical Rick")
        == "Typical Rick has been added to the favorites list"
    )
    assert bot.add_to_favorites(2, "This show must be not founded") == "Show not found"
    assert bot.get_favorites(1) == "Family Guy\nRick and Morty\n"
    assert bot.get_favorites(2) == "Typical Rick\n"
    assert bot.get_favorites(3) == "You don't have favorite shows"


def test_remove_favorites():
    bot = ShowTelegramBot("tocken")
    bot.add_to_favorites(1, "Family Guy")
    bot.add_to_favorites(1, "Rick and Morty")
    bot.add_to_favorites(2, "Typical Rick")
    assert bot.get_favorites(1) == "Family Guy\nRick and Morty\n"
    assert bot.get_favorites(2) == "Typical Rick\n"
    assert bot.get_favorites(3) == "You don't have favorite shows"
    assert (
        bot.remove_from_favorites(1, "Rick and Morty")
        == "Show Rick and Morty has been removed from the favorites list"
    )
    assert bot.get_favorites(1) == "Family Guy\n"
    assert (
        bot.remove_from_favorites(1, "Rick and Morty")
        == "You don't have this show in your favorites"
    )
    assert bot.remove_from_favorites(1, None) == "Show not found"
    assert bot.get_favorites(1) == "Family Guy\n"
    assert bot.get_favorites(2) == "Typical Rick\n"
    assert bot.get_favorites(3) == "You don't have favorite shows"
    assert (
        bot.remove_from_favorites(1, "Family Guy")
        == "Show Family Guy has been removed from the favorites list"
    )
    assert (
        bot.remove_from_favorites(2, "Typical Rick")
        == "Show Typical Rick has been removed from the favorites list"
    )
    assert bot.get_favorites(3) == "You don't have favorite shows"
    assert bot.get_favorites(2) == "You don't have favorite shows"
    assert bot.get_favorites(1) == "You don't have favorite shows"
