from numbers2String import num2text_gr


def test01():
    assert num2text_gr(0) == "μηδέν"
    assert num2text_gr(1) == "ένα"
    assert num2text_gr(2) == "δύο"
    assert num2text_gr(3) == "τρία"
    assert num2text_gr(4) == "τέσσερα"
    assert num2text_gr(100) == "εκατό"
    assert num2text_gr(101) == "εκατόν ένα"
    assert num2text_gr(150000) == "εκατόν πενήντα χιλιάδες "
    assert num2text_gr(150001) == "εκατόν πενήντα χιλιάδες ένα"
