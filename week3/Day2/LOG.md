## What built today ##

A safe price list where it handles errors without the system crashing.You can set price for items and the system stores safely without crashing even when a bad input is entered or a file is broken or doesn't exists.

## What learnt today ##

`.math` `.isfinite` - .math.isfinte is used to check if a number is normal, as in it has an ending not broken(goes on forever).

`FileNotFoundError`, `json.JSONDecodeError` - `FileNotFoundError,` is when ur looking for a file that doesn't exist python handles using this method without crashing and `json.JSONDecodeError` is when the content of an existing file is roken or corrupt.

## What confused me, and how I fixed it ##

Using `raises ValueError "message"` for set_price insteade of using `return False,"" or True, ""message"`.

## Design decision ##

-Use `try: except ValueError()` to make sure the system doesn't crash.

## Mutation checks ##

Removed `name = name.strip().lower()` from set_price to confirm if it would fail bcz a test that can't fail doesn' prove anything.So this tests that failed were : `def test_set_price_name_cleaning():` and `def test_set_price_empty_name():` with this error messages *E       assert False == True* and *assert ' HONEY ' not in {' HONEY ': 250.0}*

Commented `FileNotFoundError` and `json.JSONDecodeError` tests that failed were : `test_load_prices_damaged_file(tmp_path):` and `test_load_prices_empty_file(tmp_path):` with error message *JSONDecodeError, not an assert*

Commented `if not math.isfinite(price): raise ValueError("Price must be finite number.")` tests that failed were : `def test_parse_amount_nan():` and `def test_parse_amount_finite():` with error message *DID NOT RAISE ValueError*
