## Shop price list system ##

## What the system does ##

A small shop list system that handles errors and doesn't crash.

## Data model ##

-A dictionary of prices have name(key) and text(value - stored as a float).
-Name(key) is cleaned using `.strip()` and `.lower()`.
-(text) is handled using Try, except Valueerror.

**Example**

prices = {"milk":60.0, "bread":55.0 }

## parse_amount(text) what it takes,returns and what could go wrong. ## 

**parse_amount(text)** - Takes in a string of text representing a price input, returns float above 0

**What could go wrong**

-User may try to enter an input that's not numbers `raises ValueError, "Please enter valid price."`

-User may try to leave the input empty. `raises ValueError, "Please enter a price"`

-User may try to enter number below 0 or 0. `raises ValueError, "Please enter positive price."`

on success returns the price as a float.

## save_prices(prices,filename) what it takes,returns and what could go wrong. ## 

**save_prices(prices,filename)** Takes a dictionary and a filename and writes the dictionary into that file replacing what was there if none returns nothing.

## load_prices(filename) what it takes,returns and what could go wrong. ## 

**load_prices(filename)** Loads the filename that was created and returns dictionary or {} if no data yet.

## What is saved ##

**file name = prices.json**
**file contents**

`{"milk":60.0,"bread":55.0}` if empty returns `{}`
