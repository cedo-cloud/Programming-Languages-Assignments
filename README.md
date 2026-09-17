# GROUP 3

# Group Members
| NAME                     | REGISTRATION NUMBER                           |
| ------------------------ | --------------------------------------------- |
| Isaac Ngure              | C026-01-0902/2025                             |
| Rihana Murugi            | C026-01-2921/2025                             |
| Cedric Ochieng'          | C026-01-0985/2025                             |



# PROJECT 1: University Hostel Allocation System (Question 9: Names Bindings and Scopes)
Language used: Python
## 1. Project Overview

The **University Hostel Allocation System** is a Python 3 program developed for a Programming Languages laboratory on **names, bindings, scopes, and referencing environments**.

The system simulates hostel room allocation. Students request accommodation in specific blocks, and the program checks room availability and student category validity before allocating a room or rejecting the application.

The main purpose is not the complexity of hostel allocation, but demonstrating how Python handles **lexical scoping, nonlocal binding, global binding, shadowing, and referencing environments**.

---

## 2. Problem Statement

A university needs a simple system for processing student hostel applications. The system must:

* Store hostel room and student information.
* Validate student category ranks.
* Find rooms in the requested block.
* Check available room capacity.
* Allocate students to available rooms.
* Reject applications when requirements are not met.
* Track allocation attempts and successful allocations.

At the same time, the program demonstrates how variables are accessed and modified at different scopes.

---

## 3. Objectives

The project aims to:

1. Demonstrate **lexical (static) scoping** in Python.
2. Demonstrate **local, enclosing, global, and built-in name resolution (LEGB)**.
3. Show how `nonlocal` modifies variables in an enclosing function.
4. Show how `global` modifies module-level variables.
5. Demonstrate **variable shadowing** at different scope levels.
6. Examine the **referencing environment** at selected points in the program.
7. Apply these concepts to a practical hostel allocation scenario.

---

## 4. Technologies Used

| Technology               | Purpose                                       |
| ------------------------ | --------------------------------------------- |
| Python 3                 | Programming language                          |
| Dictionaries             | Represent rooms and student records           |
| Lists                    | Store rooms, students, and allocation results |
| Nested functions         | Demonstrate enclosing scope                   |
| `nonlocal`               | Modify variables in the enclosing function    |
| `global`                 | Modify module-level counters                  |
| `__name__ == "__main__"` | Control program execution                     |

---

## 5. Project Structure

The project is implemented as a Python program containing:

* **Named constants** – Define fixed system values.
* **Room database** – Stores room capacity and occupancy.
* **Student database** – Stores student applications.
* **Allocation engine** – Processes individual applications.
* **Reporting pipeline** – Displays results, room occupancy, and global metrics.

---

## 6. Important Constants and Variables

The program defines constants such as:

```python
DEFAULT_ROOM_CAPACITY = 2
MAX_STUDENT_CATEGORY_RANK = 3
STATUS_SUCCESS = "ALLOCATED"
STATUS_REJECTED = "DENIED"
```

The system also maintains global variables for tracking:

* Total allocation attempts.
* Total successful allocations.
* The global `status` value used for the shadowing demonstration.

---

## 7. Functions Used

| Function                    | Purpose                                                                                                    |
| --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `allocate_student(student)` | Processes one student's hostel application from validation through allocation or rejection.                |
| `confirm_space(room)`       | Nested helper function that checks room capacity and updates the selected room and local allocation count. |
| `run_allocation_pipeline()` | Processes all students and generates the allocation, occupancy, and system metric reports.                 |

### `allocate_student()`

This is the main allocation function. It:

1. Increases the global allocation-attempt counter.
2. Creates local allocation variables.
3. Defines the outer `status` variable.
4. Creates the nested `confirm_space()` function.
5. Validates the student's category.
6. Searches for rooms in the requested block.
7. Attempts allocation.
8. Returns either an allocation result or rejection reason.

### `confirm_space()`

This nested function demonstrates **enclosing scope** and `nonlocal` binding.

```python
nonlocal local_alloc_count, selected_room
```

This allows the function to modify variables belonging to `allocate_student()` rather than creating new local variables.

### `run_allocation_pipeline()`

This function controls the overall program execution. It:

* Displays the initial global status.
* Processes every student.
* Collects allocation results.
* Displays the allocation summary.
* Displays room occupancy.
* Displays global system metrics.

---

## 8. Project Flow

```text
Start
  │
  ▼
Load Room and Student Data
  │
  ▼
run_allocation_pipeline()
  │
  ▼
Process Each Student
  │
  ▼
allocate_student()
  │
  ├── Validate Category
  │       │
  │       └── Invalid → Reject
  │
  ├── Find Requested Block
  │       │
  │       └── Not Found → Reject
  │
  ├── Check Available Rooms
  │       │
  │       ├── Space Available → Allocate
  │       │
  │       └── No Space → Reject
  │
  ▼
Update Allocation Counters
  │
  ▼
Store Result
  │
  ▼
Generate Reports
  │
  ├── Allocation Summary
  ├── Room Occupancy
  └── Global Metrics
  │
  ▼
End
```

---

## 9. Scope and Binding Concepts

### Lexical Scope

`confirm_space()` is defined inside `allocate_student()`. Therefore, its enclosing scope is determined by where it appears in the source code.

Python follows the **LEGB** lookup order:

**Local → Enclosing → Global → Built-in**

### Nonlocal Binding

`local_alloc_count` and `selected_room` belong to `allocate_student()`. The `nonlocal` declaration allows `confirm_space()` to modify them.

### Global Binding

The allocation counters are defined at module level. The `global` keyword allows `allocate_student()` to update these variables.

For example:

```python
global TOTAL_ALLOCATION_ATTEMPTS
TOTAL_ALLOCATION_ATTEMPTS += 1
```

### Shadowing

The variable `status` is deliberately defined at three levels:

```text
Global scope
     ↓
allocate_student() scope
     ↓
confirm_space() scope
```

Each inner definition hides the outer definition within its own scope.

---

## 10. Referencing Environment

The project examines three checkpoints:

| Checkpoint                         | Main Scope Demonstrated                             |
| ---------------------------------- | --------------------------------------------------- |
| Inside `confirm_space()`           | Local, enclosing, and global names                  |
| Inside `allocate_student()`        | Local variables and enclosing function relationship |
| Inside `run_allocation_pipeline()` | Global variables and functions                      |

These checkpoints show which names are visible and where those names are bound.

---

## 11. Validation and Allocation Rules

The system applies the following rules:

1. A student category must not exceed the maximum category rank.
2. The requested block must exist.
3. A room must have available capacity.
4. Once allocated, the room's occupancy is increased.
5. Allocation counters are updated accordingly.
6. Applications that fail validation or capacity checks are rejected with a reason.

---

## 12. Output

The program produces three main reports:

### Allocation Summary

Shows each student's:

* ID
* Name
* Allocation status
* Assigned room or rejection reason

### Room Occupancy Report

Shows:

* Room number
* Block
* Capacity
* Current occupancy
* Remaining capacity

### System Global Metrics

Shows:

* Total allocation attempts
* Total successful allocations
* Total rejected applications

---

## 13. Running the Project

Ensure Python 3 is installed, then run the Python file from the project directory:

```bash
python main.py
```

The program will automatically execute the allocation pipeline and display the reports.

---

## 14. Project Summary

The University Hostel Allocation System provides a small but practical environment for demonstrating Python's scope and binding mechanisms.

The project uses a nested function to demonstrate **enclosing scopes and `nonlocal` binding**, global counters to demonstrate **global binding**, and multiple `status` variables to demonstrate **shadowing**.

The allocation process also provides clear referencing-environment checkpoints, allowing the relationship between local, enclosing, and global names to be observed during execution.

Overall, the project connects theoretical programming-language concepts with a simple real-world allocation problem while keeping the implementation easy to trace and understand.



# PROJECT 2: QUESTION 9: AGRICULTURAL MARKET DECISION  SUPPORT SYSTEM

Language used: LUA

# Maize Market Price Coroutine System

## 1. Introduction

The **Maize Market Price Coroutine System** is a Lua program that simulates a maize farmer monitoring prices across five fictional Kenyan markets:

* Kitale
* Eldoret
* Nakuru
* Kisumu
* Nairobi

Each market is represented by a **Lua coroutine** that generates changing maize prices over several rounds. A central scheduler controls the execution of these coroutines, records the prices separately for each market, and checks whether the farmer's selling conditions have been met.

The farmer will sell when a market price is **above KSh 4,500** and the price has **increased in two consecutive rounds**.

The project demonstrates the use of Lua **coroutines, tables, loops, conditional statements, random number generation, and cooperative scheduling**.

---

## 2. Problem Statement

A maize farmer needs to monitor prices from several markets before deciding where to sell maize.

The prices in each market change from one round to another. The system must independently monitor each market, maintain its price history, and determine when the farmer's selling conditions are satisfied.

The system is required to:

1. Model each market as a coroutine that produces changing prices.
2. Maintain a separate price history for every market.
3. Determine when a market satisfies the selling condition.
4. Stop unnecessary coroutine execution after a suitable market is selected.
5. Provide a suitable approach for situations where several markets satisfy the condition during the same round.

---

## 3. Objectives

The objectives of the project are to:

* Model each market using a Lua coroutine.
* Generate changing fictional prices for each market.
* Maintain independent price histories.
* Check whether prices exceed the KSh 4,500 threshold.
* Detect two consecutive price increases.
* Select a suitable market once the selling condition is satisfied.
* Stop unnecessary processing after market selection.
* Demonstrate cooperative coroutine scheduling in Lua.
* Provide a design for handling multiple qualifying markets in the same round.

---

## 4. Technologies Used

| Technology              | Purpose                                  |
| ----------------------- | ---------------------------------------- |
| **Lua**                 | Main programming language                |
| **Lua Coroutines**      | Represent and control individual markets |
| **Lua Tables**          | Store markets and price histories        |
| **`math.random()`**     | Generate fictional price changes         |
| **`math.randomseed()`** | Initialize random price generation       |
| **`os.time()`**         | Provide a changing random seed           |

---

# 5. System Design

The system consists of three main components:

### 5.1 Market Coroutines

Each market has its own coroutine. The coroutine maintains the current price and generates a new price whenever it is resumed.

### 5.2 Market History

Every market has its own `history` table. New prices are added to the appropriate market's history after each coroutine execution.

### 5.3 Central Scheduler

The scheduler is responsible for:

* Running the market coroutines.
* Collecting new prices.
* Updating price histories.
* Checking the selling condition.
* Detecting a suitable market.
* Stopping further processing when necessary.

---

# 6. Important Functions and Statements

## `create_market()`

The `create_market()` function creates a coroutine for an individual market.

```lua
local function create_market(start_price)
    return coroutine.create(function()
        local current_price = start_price

        while true do
            local change = math.random(-200, 300)
            current_price = current_price + change
            coroutine.yield(current_price)
        end
    end)
end
```

### Purpose

It:

* Receives the market's starting price.
* Creates a coroutine.
* Generates a random price change.
* Updates the current price.
* Uses `coroutine.yield()` to return the new price and pause execution.

---

## `coroutine.create()`

```lua
coroutine.create(function()
    ...
end)
```

Creates a new coroutine for a market.

Each market therefore has its own independent execution state.

---

## `coroutine.resume()`

```lua
local status, latest_price = coroutine.resume(market.co)
```

Resumes a market's coroutine and obtains its latest generated price.

The scheduler uses this function to control when each market produces a new price.

---

## `coroutine.yield()`

```lua
coroutine.yield(current_price)
```

Pauses the market coroutine and returns the current price to the scheduler.

When the coroutine is resumed again, it continues from where it previously stopped.

---

## `table.insert()`

```lua
table.insert(market.history, latest_price)
```

Adds the latest price to the correct market's price history.

This ensures that each market maintains its own sequence of prices.

---

## `math.random()`

```lua
local change = math.random(-200, 300)
```

Generates a fictional price fluctuation between -KSh 200 and +KSh 300.

---

## `math.randomseed()`

```lua
math.randomseed(os.time())
```

Initializes the random number generator using the current system time so that the program can produce different fictional price sequences when it is run.

---

# 7. Market Data Structure

The markets are stored in a Lua table:

```lua
local markets = {
    { name = "Kitale",  co = create_market(4200), history = {} },
    { name = "Eldoret", co = create_market(4350), history = {} },
    { name = "Nakuru",  co = create_market(4100), history = {} },
    { name = "Kisumu",  co = create_market(4300), history = {} },
    { name = "Nairobi", co = create_market(4250), history = {} }
}
```

Each market contains three important properties:

* `name` — identifies the market.
* `co` — stores the market's coroutine.
* `history` — stores all prices generated by that market.

This structure allows the scheduler to manage all markets consistently.

---

# 8. Selling Condition

The farmer's selling condition is implemented using:

```lua
if p3 > 4500 and p3 > p2 and p2 > p1 then
```

The condition checks three things:

1. The latest price is greater than **KSh 4,500**.
2. The latest price is greater than the previous price.
3. The previous price is greater than the price before it.

Therefore, the system identifies a market where the price has increased during **two consecutive rounds** and the latest price is above the required threshold.

The program only performs this check after at least three prices have been recorded:

```lua
if len >= 3 then
```

This is necessary because three price values are required to identify two consecutive increases.

---

# 9. System Workflow

The system follows the workflow below:

```text
START
  |
  v
Initialize random number generator
  |
  v
Create five market coroutines
  |
  v
Create separate price histories
  |
  v
Start central scheduler
  |
  v
Start a new round
  |
  v
Resume market coroutine
  |
  v
Generate new fictional price
  |
  v
Store price in market history
  |
  v
Check selling condition
  |
  +-----------------------+
  |                       |
  | Condition satisfied?  |
  |                       |
  +-----------+-----------+
              |
        +-----+-----+
        |           |
       YES          NO
        |           |
        v           v
Select market   Continue to
        |        next market
        v           |
Stop unnecessary    |
execution           |
        |           |
        +-----+-----+
              |
              v
         Start next round
              |
              v
             END
```

The actual program uses a `while` loop for the rounds and a `for` loop to process the individual markets.

---

# 10. Central Scheduler

The central scheduler is controlled by:

```lua
while not sale_made do
```

This means the program continues processing rounds until a suitable market is found.

Inside the scheduler:

```lua
for _, market in ipairs(markets) do
```

iterates through each market.

The market coroutine is then resumed:

```lua
local status, latest_price = coroutine.resume(market.co)
```

If execution is successful, the price is stored:

```lua
table.insert(market.history, latest_price)
```

The scheduler then checks whether the market satisfies the selling condition.

---

# 11. Stopping Unnecessary Execution

Once a suitable market is found, the program sets:

```lua
sale_made = true
```

and uses:

```lua
break
```

to stop processing the remaining markets in the current `for` loop.

The outer loop also depends on:

```lua
while not sale_made do
```

Therefore, once `sale_made` becomes `true`, the program stops the scheduler after the current iteration.

This prevents the system from continuing to process markets unnecessarily after a suitable market has been identified.

---

# 12. Handling Multiple Qualifying Markets

Lua coroutines are **cooperative**, meaning they take turns executing on the same thread rather than running truly simultaneously.

However, multiple markets can logically satisfy the farmer's condition during the same round.

The current implementation uses `break` immediately when the first qualifying market is found. This means the order of the markets in the table can affect which market is selected.

A more suitable design for simultaneous qualifying markets would be:

1. Resume **all market coroutines** for the current round.
2. Store all their latest prices.
3. Complete the current round.
4. Check the histories of all markets.
5. Identify every market that satisfies the selling condition.
6. Apply a predefined tie-breaking rule.
7. Select the desired market.
8. Stop further coroutine execution.

One possible tie-breaking rule is to select the market with the **highest current price**.

This approach prevents the first market in the list from automatically being selected simply because it was processed first.

---

# 13. Program Control Variables

The program uses two important control variables.

### `round`

```lua
local round = 1
```

Keeps track of the current simulation round.

It is incremented after each round:

```lua
round = round + 1
```

### `sale_made`

```lua
local sale_made = false
```

Indicates whether a suitable market has been found.

It initially has a value of `false` and changes to `true` when the selling condition is satisfied.

---

# 14. Error Handling

The program checks whether a coroutine was successfully resumed:

```lua
if status then
    ...
else
    print("Error resuming " .. market.name)
end
```

If `coroutine.resume()` fails, an error message identifying the affected market is displayed.

This prevents the program from assuming that every coroutine execution is always successful.

---

# 15. Safety Mechanism

The program includes a maximum of 50 rounds:

```lua
if round > 50 then
    print("\nNo suitable market found after 50 rounds.")
    break
end
```

This prevents the program from continuing indefinitely if the randomly generated prices never satisfy the selling condition.

The limit is mainly useful for testing and simulation purposes.

---

# 16. Key Concepts Demonstrated

The project demonstrates several important Lua programming concepts:

### Coroutines

Used to model independent market price generators and allow execution to pause and resume.

### Cooperative Scheduling

A central scheduler controls when each market coroutine runs.

### Tables

Used to store market information and maintain separate price histories.

### Loops

`while` manages simulation rounds while `for` processes individual markets.

### Conditional Logic

`if` statements determine whether selling conditions and execution conditions have been satisfied.

### Random Number Generation

Used to simulate changing market prices.

### State Management

Variables such as `sale_made`, `round`, and `history` maintain the state of the simulation.

---

# 17. Limitations

The current system is a simulation and has several limitations:

* The market prices are fictional and randomly generated.
* It does not retrieve real-time maize prices.
* The current implementation stops at the first qualifying market rather than evaluating all qualifying markets in the same round.
* The tie-breaking mechanism for multiple qualifying markets is described as an improved design but is not implemented in the current code.
* The 50-round limit is a testing safeguard rather than a real-world requirement.
* Lua coroutines provide cooperative execution rather than true parallel execution.

---

# 18. Possible Improvements

The system could be improved by:

* Connecting it to real maize market price data.
* Implementing the multiple-market selection mechanism.
* Allowing the farmer to set a custom price threshold.
* Supporting additional markets.
* Saving price histories to a file or database.
* Adding a graphical interface for monitoring prices.
* Displaying price trends using charts.
* Allowing the farmer to define different tie-breaking strategies.
* Adding notifications when a selling condition is satisfied.

---

# 19. Summary

The **Maize Market Price Coroutine System** demonstrates how Lua coroutines can be used to simulate multiple independent sources of changing information.

Each market is represented by a coroutine that generates fictional price updates. A central scheduler resumes these coroutines, records each market's prices separately, and checks whether the farmer's selling condition has been satisfied.

The system satisfies the main requirements of the project by providing:

* **One coroutine for each market**
* **Separate price histories**
* **Automatic selling-condition detection**
* **Controlled coroutine execution**
* **A design for handling multiple qualifying markets**

The project provides a practical demonstration of **coroutine-based programming and cooperative scheduling in Lua** while applying these concepts to a simple maize market monitoring scenario.
