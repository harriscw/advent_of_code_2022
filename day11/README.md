# Fully cheated on part 2 here

Part 2 was a little tougher for me, probably because it was a little more math based.

I had a couple of organic ideas for part 2.  One was switching from holding numbers in list to dictionary.  Another idea I had was to look for when the pattern from round 1 repeated and then reset the state to the original state, e.g. if round 1 goes "monkey 0 -> monkey 1, monkey 1 -> monkey 2, etc" and you see that state again then just reset.  And another idea was to read/write from disk so you had to handle less giant numbers at a time.  The first two didn't work and I didn't implement the last one.

Eventually I started cheating.  At first I just didn't understand many of the solutions, e.g. [this](https://aoc.just2good.co.uk/2022/11) was too much for me to follow.  I got a bit of a clue on [this post](https://www.reddit.com/r/adventofcode/comments/zifqmh/comment/izr6668/), which lead me to try to test if a new worry level was divisible by the product of the tests.  If so we could divide by that number and continue the pattern with a lower number?  Unfortunately this didn't happen early enough so the code just started to crawl as usual.  But that helped me better understand [the top comment in the reddit solutions thread](https://www.reddit.com/r/adventofcode/comments/zifqmh/comment/izrd7iz/) which just lays it out for you clearly.

Will have to think more to fully understand why just remainders of the product of the test rules can be used.  A good lesson though on asking the question "how can i get the same pattern of results with smaller numbers?"