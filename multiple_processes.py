"""

multiple_processes.py: Illustrate concurrent access to a shared resource (a database).

In this example, three processes are working with the same table in a shared database. 
The processes are not synchronized, so they can interfere with each other.

Run the app several times and notice the order of events.
Is the order predictable?

Modify the code to make each task take longer. 
When the task duration is 3 seconds, we'll typically got concurrency errors 
as multiple processes try to access the database at the same time.

SQLite is designed for lightweight databases, and is not ideal for high concurrency applications. 
When two processes attempt to write to a SQLite database at the same time, one will fail. 

"""