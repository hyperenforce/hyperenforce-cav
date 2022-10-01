from tempfile import TemporaryFile

from hyper_synth.qbf import AND, EXISTS, FORALL, OR, QBF


def test_qcir_io():
    form = FORALL([1, 3, 7], EXISTS([2], AND(OR(AND(1, 2), AND(-1, -2)), EXISTS([4], FORALL([], AND(4, 5))))))
    with TemporaryFile(mode="r+") as f:
        form.to_qcir(f, [5])
        f.seek(0)
        new_form = QBF.from_qcir(f)

        assert new_form.quant_expr == form
