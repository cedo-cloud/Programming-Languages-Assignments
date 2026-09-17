DEFAULT_ROOM_CAPACITY = 2
MAX_STUDENT_CATEGORY_RANK = 3

STATUS_SUCCESS = "ALLOCATED"
STATUS_REJECTED = "DENIED"

status = "GLOBAL_STATUS: Hostel System Active"

TOTAL_ALLOCATION_ATTEMPTS = 0
TOTAL_SUCCESSFUL_ALLOCATIONS = 0


rooms_db = [
    {"room_no": "A101", "block": "Block A", "capacity": 2, "occupied": 1},
    {"room_no": "A102", "block": "Block A", "capacity": 2, "occupied": 2},
    {"room_no": "B201", "block": "Block B", "capacity": 3, "occupied": 2},
    {"room_no": "B202", "block": "Block B", "capacity": 2, "occupied": 0},
    {"room_no": "C301", "block": "Block C", "capacity": 1, "occupied": 1},
    {"room_no": "C302", "block": "Block C", "capacity": 2, "occupied": 0},
]


students_db = [
    {
        "id": "STU001",
        "name": "Alice Wanjiku",
        "category": 1,
        "requested_block": "Block A"
    },
    {
        "id": "STU002",
        "name": "Brian Ochieng",
        "category": 2,
        "requested_block": "Block A"
    },
    {
        "id": "STU003",
        "name": "Catherine Mwangi",
        "category": 1,
        "requested_block": "Block B"
    },
    {
        "id": "STU004",
        "name": "David Kiprop",
        "category": 3,
        "requested_block": "Block B"
    },
    {
        "id": "STU005",
        "name": "Emmanuel Omondi",
        "category": 2,
        "requested_block": "Block C"
    },
    {
        "id": "STU006",
        "name": "Faith Cherono",
        "category": 1,
        "requested_block": "Block C"
    },
    {
        "id": "STU007",
        "name": "George Ndung'u",
        "category": 4,
        "requested_block": "Block A"
    },
    {
        "id": "STU008",
        "name": "Hannah Achieng",
        "category": 2,
        "requested_block": "Block X"
    },
    {
        "id": "STU009",
        "name": "Ian Mutua",
        "category": 3,
        "requested_block": "Block A"
    },
    {
        "id": "STU10",
        "name": "Julia Hassan",
        "category": 1,
        "requested_block": "Block B"
    }
]


def allocate_student(student: dict) -> dict:
    global TOTAL_ALLOCATION_ATTEMPTS

    TOTAL_ALLOCATION_ATTEMPTS += 1
    local_alloc_count = 0
    selected_room = None

    status = f"OUTER_STATUS: Processing Allocation for {student['name']}"

    def confirm_space(room: dict) -> bool:
        nonlocal local_alloc_count, selected_room

        status = f"INNER_STATUS: Checking Space in Room {room['room_no']}"

        if room["occupied"] < room["capacity"]:
            room["occupied"] += 1
            selected_room = room["room_no"]
            local_alloc_count += 1

            print(
                f"    [Shadowing Check - Inner Scope] "
                f"status = '{status}'"
            )

            return True

        return False

    if student["category"] > MAX_STUDENT_CATEGORY_RANK:
        return {
            "student_id": student["id"],
            "name": student["name"],
            "status": STATUS_REJECTED,
            "reason": "Invalid Category Rank"
        }

    matching_rooms = [
        room for room in rooms_db
        if room["block"] == student["requested_block"]
    ]

    if not matching_rooms:
        return {
            "student_id": student["id"],
            "name": student["name"],
            "status": STATUS_REJECTED,
            "reason": "Requested Block Not Found"
        }

    allocation_successful = False

    for room in matching_rooms:
        if confirm_space(room):
            allocation_successful = True

            global TOTAL_SUCCESSFUL_ALLOCATIONS
            TOTAL_SUCCESSFUL_ALLOCATIONS += 1

            break

    print(
        f"    [Shadowing Check - Outer Scope] "
        f"status = '{status}'"
    )

    if allocation_successful:
        return {
            "student_id": student["id"],
            "name": student["name"],
            "status": STATUS_SUCCESS,
            "room": selected_room,
            "block": student["requested_block"],
            "alloc_attempt": local_alloc_count
        }

    return {
        "student_id": student["id"],
        "name": student["name"],
        "status": STATUS_REJECTED,
        "reason": "Block Capacity Full"
    }


def run_allocation_pipeline():
    print("=" * 70)
    print(" UNIVERSITY HOSTEL ALLOCATION SYSTEM - EXECUTION TRACE")
    print("=" * 70)

    print(
        f"\n[Shadowing Check - Global Scope] "
        f"status = '{status}'"
    )

    allocation_results = []

    print("\n--- Processing Allocations ---")

    for student in students_db:
        print(
            f"\nProcessing Student: "
            f"{student['id']} ({student['name']})"
        )

        allocation_results.append(
            allocate_student(student)
        )

    print("\n" + "=" * 70)
    print(" ALLOCATION SUMMARY REPORT")
    print("=" * 70)

    print(
        f"{'ID':<8} | {'Name':<18} | "
        f"{'Status':<10} | {'Room/Reason'}"
    )
    print("-" * 68)

    for result in allocation_results:
        detail = result.get(
            "room",
            result.get("reason", "N/A")
        )

        print(
            f"{result['student_id']:<8} | "
            f"{result['name']:<18} | "
            f"{result['status']:<10} | "
            f"{detail}"
        )

    print("\n" + "=" * 70)
    print(" ROOM OCCUPANCY & CAPACITY")
    print("=" * 70)

    print(
        f"{'Room No':<8} | {'Block':<10} | "
        f"{'Capacity':<10} | {'Occupied':<10} | {'Remaining'}"
    )
    print("-" * 60)

    for room in rooms_db:
        remaining = room["capacity"] - room["occupied"]

        print(
            f"{room['room_no']:<8} | "
            f"{room['block']:<10} | "
            f"{room['capacity']:<10} | "
            f"{room['occupied']:<10} | "
            f"{remaining}"
        )

    print("\n" + "=" * 70)
    print(" SYSTEM GLOBAL METRICS")
    print("=" * 70)

    print(
        f"Total Allocation Attempts    : "
        f"{TOTAL_ALLOCATION_ATTEMPTS}"
    )
    print(
        f"Total Successful Allocations : "
        f"{TOTAL_SUCCESSFUL_ALLOCATIONS}"
    )
    print(
        f"Total Rejected Applications  : "
        f"{TOTAL_ALLOCATION_ATTEMPTS - TOTAL_SUCCESSFUL_ALLOCATIONS}"
    )


if __name__ == "__main__":
    run_allocation_pipeline()