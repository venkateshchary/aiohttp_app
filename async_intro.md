 
 Eg-:You are cooking in a restaurant. An order comes in for eggs and toast.

# Synchronous: 
  you cook the eggs, then you cook the toast.
# Asynchronous, single threaded: 
  you start the eggs cooking and set a timer. 
  You start the toast cooking, and set a timer. While they are both cooking, you clean the kitchen. 
  When the timers go off you take the eggs off the heat and the toast out of the toaster and serve them.
# Asynchronous, multithreaded: 
  you hire two more cooks, one to cook eggs and one to cook toast. 
  Now you have the problem of coordinating the cooks so that they do not conflict with each other in the kitchen when sharing resources. 
  And you have to pay them.
  
  # asyncio
 
 ## EVENT:
 An event loop manages and distributes the execution of different tasks. It registers them and handles distributing the flow of control between them.

## Coroutines:
(covered above) are special functions that work similarly to Python generators, on await they release the flow of control back to the event loop. A coroutine needs to be scheduled to run on the event loop, once scheduled coroutines are wrapped in Tasks which is a type of Future.
## Futures:
represent the result of a task that may or may not have been executed. This result may be an exception.
