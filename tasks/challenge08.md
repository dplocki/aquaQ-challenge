# Cron Flakes

While out shopping, you realise you're not sure how much milk and cereal you have in the house. What you do have however is a handy terminal session (preferably running kdb+, but other languages are acceptable), and a csv of milk and cereal purchases (in ml and g, respectively), which you've updated every time you've been shopping in the last while.

Once per day, if you have enough of both, you use 100ml of milk and 100g of cereal. Milk always expires on the 5th day after you buy it, after you use it that morning, and you always use your oldest unexpired milk to avoid waste. You always buy new milk after breakfast, and cereal before breakfast (i.e. never use milk as soon as you get it, but you can use cereal as soon as you get it if you already have milk).

For example, if on day 1 you buy 1000ml of cereal and 1000g of milk, and then on day 5 you buy 1000ml of milk, your milk and cereal up to day six would look like this:

```txt
day milk cereal
---------------
1   1000 1000
2   900  900
3   800  800
4   700  700
5   1600 600
6   1000 500
```

On days 1, 2, 3, and 4, you use 100g each of milk and cereal, without any new milk or cereal coming in. On day 5, you have breakfast as normal and later get your 1000g of milk. On day 6, you use 100g of your oldest milk and none of your newest milk, then throw the old milk away, leaving you with 1000g of milk, while cereal has steadily reduced to 500g.

It's currently one day after the last date in your input - what's the sum of your remaining milk and cereal?