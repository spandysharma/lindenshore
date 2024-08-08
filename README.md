### Approach ###

* I tried to find cycles in the Transaction Receipt Event Logs to point to possible arbitrage. I did this by comparing the different sources and destinations for the Transfer events and checking when a destination had already been seen as a source.
* However, this led me to find false positives thus showing that not all cycles reflect arbitrage trades.
* My next steps would be to use Swap events to filter false positives and use that to calculate profit by getting the difference of outgoing and incoming values.

Thank you for the opportunity!
