In-Memory Key Value Database with Transactions

This project is a simple in-memory database I wrote for my Data Processing and Storage assignment. It works like a small version of a real database that supports transactions so updates only become visible once they are committed. If something goes wrong, everything can be rolled back so the state stays consistent.

The database stores key value pairs where keys are strings and values are integers. You can open a transaction, make updates, and then either commit them or discard them. Only one transaction can be active at any time, which keeps things straightforward.

Features

begin_transaction() starts a new transaction

put(key, value) stages an update inside the active transaction

get(key) returns the committed value for a key

commit() applies all staged changes to the main state

rollback() cancels everything staged in the transaction

Uncommitted changes stay invisible to get() until commit() is called. This matches the behavior shown in the assignment examples.

How It Works

The implementation uses two dictionaries:

main_state stores all committed values

transaction_state stores temporary changes waiting to be committed

There is also a simple boolean that tracks whether a transaction is active.
When commit is called, everything in transaction_state moves into main_state.
When rollback is called, the staged changes are discarded and the database returns to the original state.

The behavior is simple, predictable, and follows the assignment requirements closely.

Project Structure
inmemory-db/
│
├── inmemory_db.py      implementation
├── main.py             example usage and testing
└── README.md

How to Run

Make sure Python 3 is installed.
You can check with:

python --version


Navigate into the project folder:

cd <your folder path>


Run the example file:

python main.py


There are no additional dependencies or setup steps.

Reflection

If this were a full official assignment, a few improvements would make it clearer and easier to grade. The instructions should clearly state how get() behaves during a transaction since that guides the design choices. A provided test suite or grading script would help standardize grading and reduce ambiguity. It would also be helpful to specify what types of errors or exceptions should be thrown. Optional extensions like nested transactions or delete operations could make the project more interesting and give students more opportunities to demonstrate their understanding.

Reflection

If this were turned into a full assignment, some small changes would make it clearer and easier to grade. The instructions should explicitly say how get() should behave during a transaction, since that affects how students design their code. It would also help to include a small set of official test cases, or a grading script, so the expected behavior is completely consistent. Clearer requirements for what types of errors or exceptions should be thrown would remove ambiguity. Optional extensions like nested transactions, delete operations, or more detailed interfaces could make the assignment more interesting for students who want to go further.
