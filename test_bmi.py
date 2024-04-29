import Lab2.bmi as bmi
def test_bmi_normal_weight():
    result = 0
    bmi_for_test = 20
    ans = bmi.is_healthy(bmi_for_test)
    assert (result==ans)

def test_bmi_over_weight():
    result = 1
    bmi_for_test = 26
    ans = bmi.is_healthy(bmi_for_test)
    assert (result==ans)


def test_bmi_under_weight():
    result = -1
    bmi_for_test = 11
    ans = bmi.is_healthy(bmi_for_test)
    assert (result==ans)
