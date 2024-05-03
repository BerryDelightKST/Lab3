import price_info as infoma

def test_cost_fruit():
    cost=infoma.cost_of_fruits('pineapple',5)
    assert (cost==13.5)

def test_total():
    answer=infoma.total_cost_shopping()
    assert (answer==46.75)
    