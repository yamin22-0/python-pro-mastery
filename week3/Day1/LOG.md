## What built today ##

A debt colletion system where a user can add debts , the system calculates total owed , paying of debts and then debts can be saved into .json where it can be loaded so the debts are still there after the program closes.

## What learnt today ##

`.json` - is a built in python library where turns dictionary into a text for a file.
`os` - is used to check if a file exists or doesn't exists.
`tmp_path` - is a temporary file that pytest creates for u only for testing when testing session ends the file also goes and it's not saved to ur computer.

## What confused me, and how I fixed it ##

I repeated this mistake again using coma instead of colon *(will log this to bugs i repeat.)* this is the error message `'set' object is not subscriptable`


## Design decision ##

For pay_debt we first subtract then check if debt is settled(becomes 0) then the debt is removed from the system completely.

## Mutation checks ##

Removed `name = name.strip().lower()` from pay_debt to confirm if it would fail bcz a test that can't fail doesn' prove anything.So this test failed `def test_pay_debt_name_cleaning():` with this error message *E       assert False == True*