from hyper_synth.cardinality_qbf import at_most_k_form, compare_count_form
from hyper_synth.encoding import VariablePool
from hyper_synth.qbf import FALSE, TRUE


def test_at_most_k_form():
    var_pool = VariablePool(start_from=3)

    assert at_most_k_form([TRUE, FALSE, TRUE, FALSE, FALSE], k=2, var_pool=var_pool).find_solution([]) is not None
    assert at_most_k_form([TRUE, FALSE, TRUE, FALSE, FALSE], k=1, var_pool=var_pool).find_solution([]) is None

    assert at_most_k_form([1, 2], k=1, var_pool=var_pool).find_solution([1, 2]) is not None
    assert at_most_k_form([1, -1, -1, 2, 2, -2], k=2, var_pool=var_pool).find_solution([1, 2]) == {1}
    assert at_most_k_form([1, -1, -1, 2, 2, -2], k=1, var_pool=var_pool).find_solution([1, 2]) is None


def test_compare_count_form():
    var_pool = VariablePool(start_from=3)

    v1 = [FALSE, TRUE, FALSE]
    v2 = [TRUE, FALSE, TRUE]
    assert compare_count_form(v1, v2, var_pool=var_pool).find_solution([]) is not None
    assert compare_count_form(v2, v1, var_pool=var_pool).find_solution([]) is None

    assert compare_count_form([1, 1, 2, -2], [1, -1, 2, -2], var_pool=var_pool).find_solution([1, 2]) is not None
    assert 1 in compare_count_form([-1, 2], [2, 1], var_pool=var_pool).find_solution([1, 2])
    assert compare_count_form([1, 1, -1], [1], var_pool=var_pool).find_solution([1, 2]) is None


def test_coeffs():
    var_pool = VariablePool(start_from=3)

    v1 = [FALSE, TRUE, FALSE]
    v2 = [TRUE, FALSE, TRUE]
    assert compare_count_form([TRUE, TRUE, TRUE], [TRUE, FALSE, TRUE], var_pool=var_pool).find_solution([1,2]) is None
    assert compare_count_form(v1, v2, var_pool=var_pool, coeffs1=[0,3,0], coeffs2=[1,1,1]).find_solution([1,2]) is None
    assert compare_count_form(v1, v2, var_pool=var_pool, coeffs1=[0,2,1], coeffs2=[1,0,1]).find_solution([1,2]) is not None
