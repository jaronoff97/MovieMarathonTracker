# MovieMarathonTracker
This repository is meant to track watching for any movie/ tv marathon. I'm going to be using it for tracking my MCU content usage.

## Usage

The usage is really simple.

Have a sheet named `InitialSheet.csv` and run the script with `python tracker.py`

You'll now be loaded into the prompt like so:

```
Welcome to your marvel tracker!!!
What action would you like to do?
> 
```

## Commands

* Help
	* Get the available commands
* Next n items
	* Display the next {n} items you need to watch
* Watched n items
	* Mark that you watched {n} items
* Unwatched n items
	* Unmark that you watched {n} items,maybe you want to rewatch some more, or you messed up marking
* Get info
	* Get some basic metadata
* Get categories
	* Get avaialble categories for filtering
* Set categories (comma seperated categories)
	* Set avaialble categories to filter
	* Example: Movie,Tv,Other
* Exit
	* Self explanatory

## Examples

```
What action would you like to do?
> next 10 items
==========NEXT 10 ITEMS==========
1:	Captain America: The First Avenger
2:	Agent Carter S01E01: Now is Not the End
3:	Agent Carter S01E02: Bridge and Tunnel
4:	Agent Carter S01E03: Time and Tide
5:	Agent Carter S01E04: The Blitzkrieg Button
6:	Agent Carter S01E05: The Iron Ceiling
7:	Agent Carter S01E06: A Sin to Err
8:	Agent Carter S01E07: Snafu
9:	Agent Carter S01E08: Valediction
10:	Agent Carter
==========NEXT 10 ITEMS==========
What action would you like to do?
> watch 2 items
What action would you like to do?
> next 10 items
==========NEXT 10 ITEMS==========
1:	Agent Carter S01E02: Bridge and Tunnel
2:	Agent Carter S01E03: Time and Tide
3:	Agent Carter S01E04: The Blitzkrieg Button
4:	Agent Carter S01E05: The Iron Ceiling
5:	Agent Carter S01E06: A Sin to Err
6:	Agent Carter S01E07: Snafu
7:	Agent Carter S01E08: Valediction
8:	Agent Carter
9:	Agent Carter S02E01: The Lady in the Lake
10:	Agent Carter S02E02: A View in the Dark
==========NEXT 10 ITEMS==========
What action would you like to do?
> unwatch 1 item
What action would you like to do?
> next 5 items
==========NEXT 5 ITEMS==========
1:	Agent Carter S01E01: Now is Not the End
2:	Agent Carter S01E02: Bridge and Tunnel
3:	Agent Carter S01E03: Time and Tide
4:	Agent Carter S01E04: The Blitzkrieg Button
5:	Agent Carter S01E05: The Iron Ceiling
==========NEXT 5 ITEMS==========
What action would you like to do?
> get info
==========GET INFO==========
	1 pieces of content
	124 hours of content
	250 pieces of content left
	12017 hours of content left
==========GET INFO==========
What action would you like to do?
> set categories movie
What action would you like to do?
> get categories
==========GET Categories==========
Current Categories:
movie
Available Categories:
tv,movie,other
==========GET Categories==========
What action would you like to do?
> next 5 items
==========NEXT 5 ITEMS==========
1:	Iron Man
2:	Iron Man 2
3:	The Incredible Hulk
4:	Thor
5:	Avengers
==========NEXT 5 ITEMS==========
```


## Next Steps

I'm going to be adding in some more metadata and info for different items in the rewatch. I'm planning on connecting iMDB and a couple of other APIs that would get information on where to watch it. I'm also going to add in information like if you're only binging on TV, Movies, or everything.




