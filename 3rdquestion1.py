import queue

# Create a Priority Queue object
friends_priority_queue = queue.PriorityQueue()

# Add friends with assigned priority to the queue
friends_priority_queue.put((2, "Ashfaq Ahmed"))
friends_priority_queue.put((1, "Abdul Rehman"))
friends_priority_queue.put((3, "Shujath Ali Khan"))

# Remove the friend with the highest priority from the queue
highest_priority_friend = friends_priority_queue.get()

# Display the friends added to the priority queue and the one removed based on priority
print("Friends and their priorities added to the queue:")
print("(Priority, Friend)")
print("(2, 'Ashfaq Ahmed')")
print("(1, 'Abdul Rehman')")
print("(3, 'Shujath Ali Khan')")

print("\nFriend removed based on priority:", highest_priority_friend[1])
