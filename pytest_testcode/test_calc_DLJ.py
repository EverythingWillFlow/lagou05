import pytest


class TestCalc():

    @pytest.mark.third
    def test_mul(self, get_calc, get_muls):
        result = get_calc.mul(get_muls[0], get_muls[1])
        assert result == get_muls[2]

    @pytest.mark.fourth
    def test_div(self, get_calc, get_divs):
        result = get_calc.div(get_divs[0], get_divs[1])
        assert result == get_divs[2]

    @pytest.mark.first
    def test_add(self,get_calc,get_adds):
        result = get_calc.add(get_adds[0],get_adds[1])
        assert result == get_adds[2]

    @pytest.mark.second
    def test_sub(self,get_calc,get_subs):
        result = get_calc.sub(get_subs[0],get_subs[1])
        assert result == get_subs[2]
