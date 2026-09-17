#GROUP 3

#Group Members
| NAME                     | REGISTRATION NUMBER                           |
| ------------------------ | --------------------------------------------- |
| Isaac Ngure              | C026-01-0902/2025                             |
| Rihana Murugi            | C026-01-2921/2025                             |
| Cedric Ochieng'          | C026-01-0985/2025                             |



# PROJECT 1: University Hostel Allocation System

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
