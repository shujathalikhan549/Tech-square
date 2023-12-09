import queue

# Create a Queue object
my_queue = queue.Queue()

# Add an element to the queue
my_queue.put("Shujath Ali Khan")

# Pop an element from the queue
popped_element = my_queue.get()

# Show output
print("Element added to the queue:", "Shujath Ali Khan")
print("Element popped from the queue:", popped_element)
