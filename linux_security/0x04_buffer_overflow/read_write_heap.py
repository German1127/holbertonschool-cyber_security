#!/usr/bin/python3

"""
heap_modifier.py - Script to locate and replace a specific string in the heap of a running process.

Usage:
    python3 heap_modifier.py pid target_string new_string

Parameters:
    pid - Target process ID
    target_string - ASCII string to locate in the heap memory
    new_string - ASCII string to replace the target_string
"""

import sys

def modify_heap_memory(pid, target_string, new_string):
    """
    Locate and replace a string in the heap memory of a specified process.

    Args:
        pid (int): ID of the target process
        target_string (bytes): String to find in the heap
        new_string (bytes): String to overwrite the target_string
    """
    maps_file_path = f"/proc/{pid}/maps"
    mem_file_path = f"/proc/{pid}/mem"

    try:
        with open(maps_file_path, "r") as maps_file:
            heap_info = None
            for line in maps_file:
                if "[heap]" in line:
                    heap_info = line.strip()
                    break

            if not heap_info:
                print("Error: Heap section not found.")
                return


            heap_start, heap_end = [int(addr, 16) for addr in heap_info.split()[0].split("-")]

        with open(mem_file_path, "r+b") as mem_file:
            mem_file.seek(heap_start)
            heap_content = mem_file.read(heap_end - heap_start)


            if len(new_string) > len(target_string):
                print("Warning: New string is longer than the target string. This may lead to issues.")


            position = heap_content.find(target_string)
            if position == -1:
                print("Error: Target string not found in heap.")
                return


            mem_file.seek(heap_start + position)
            mem_file.write(new_string.ljust(len(target_string), b'\x00'))

            print(f"Successfully replaced '{target_string.decode()}' with '{new_string.decode()}' in the heap.")

    except PermissionError:
        print("Error: Insufficient permissions. Try running with elevated privileges (e.g., sudo).")
    except FileNotFoundError:
        print("Error: Process not found. Verify the PID.")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")

def main():
    """
    Main entry point to parse arguments and execute the heap modification.
    """
    if len(sys.argv) != 4:
        print("Usage: python3 heap_modifier.py pid target_string new_string")
        sys.exit(1)

    try:
        pid = int(sys.argv[1])
    except ValueError:
        print("Error: PID must be a valid integer.")
        sys.exit(1)

    target_string = sys.argv[2].encode()
    new_string = sys.argv[3].encode()

    modify_heap_memory(pid, target_string, new_string)

if __name__ == "__main__":
    main()

