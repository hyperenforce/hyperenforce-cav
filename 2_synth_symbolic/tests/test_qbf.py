from hyper_synth.qbf import (AND, EQUIVALENT, EXISTS, FALSE, FORALL, IMPLIES,
                             NOT, OR, SYMBOL, TRUE)


def test_qbf():

    assert NOT(NOT(1)).to_simplified() == SYMBOL(1)
    assert NOT(NOT(NOT(1))).to_simplified() == SYMBOL(-1)
    assert AND(TRUE, OR(FALSE, AND(FALSE, 1), 2)).to_simplified() == SYMBOL(2)
    assert FORALL([1], NOT(EXISTS([], TRUE))).to_simplified() == TRUE

    assert AND(1, 1).to_simplified() == SYMBOL(1)
    assert not AND(1, 1) == AND(1)

    assert FORALL([1, 2], OR(1, 2, -1)).substitute({2: 3}) == FORALL([1, 3], OR(1, 3, -1))


def test_qbf_prenex():

    assert AND(NOT(FORALL([1], 1)), FORALL([2], 2)).to_prenex().to_simplified() ==\
           FORALL([2], EXISTS([1], AND(-1, 2))).to_simplified()

    assert IMPLIES(OR(1, EXISTS([1,2], AND(1, 2))), FORALL([3], NOT(3))).to_prenex().to_simplified() ==\
           FORALL([1, 2, 3], OR(AND(OR(-1, -2), -1), -3))


def test_qbf_solver():

    # Solver returns None if no solution is found
    assert FORALL([1], EXISTS([2], EQUIVALENT(1, 2))).find_solution([]) is not None
    assert EXISTS([1], FORALL([2], EQUIVALENT(1, 2))).find_solution([]) is None

    assert list(FORALL([1], EXISTS([2], AND(3, EQUIVALENT(1, 2)))).find_solution([3])) == [3]
