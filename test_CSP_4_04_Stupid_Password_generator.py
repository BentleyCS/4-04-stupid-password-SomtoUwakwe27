import CSP_4_04_Stupid_Password_generator as HW
def test_stupid_password():
    assert HW.stupidPassword(2,4)==["11aa2", "11ab2", "11ac2", "11ad2", "11ba2", "11bb2", "11bc2", "11bd2", "11ca2", "11cb2", "11cc2", "11cd2", "11da2", "11db2", "11dc2", "11dd2"]
    assert HW.stupidPassword(3,1) == ["11aa2", "11aa3", "12aa3", "21aa3", "22aa3"]
