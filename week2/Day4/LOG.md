## What built today ##

Today i built a library system which a user can add books ,borrow a book and return a book. It also keeps track of books across different titles.It has 4 functions and 24 tests.(tested with pytest).


## What learnt today ##

-Learnt `mutation check` - which is a way to check if a test fails because a test that doesn't fail doesn't prove anything at all.You intentionally make a code break on purpose validation checks so that the test fails to do a mutation check. eg changing `<= 0` to `< 0` in *return_book made* *test_return_book_nothing_out* fail.

## What confuse me today ##

Today some things confused me: 

1.The `pytest failures` sometime pytest would tell me asserterror `assert ['python 101'] == 'python 101'.` etc so i had to find ways to fix 

2.I was making a test for `test_return_book_empty_title` but instead of calling `return_book` function i accidentally called `borrow_book` function but it passed because the borrow_book function had the same vaildation check for empty input.
