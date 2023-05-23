import threading
import time

# def worker():
#     """Thread worker function"""
#     print("Worker thread started")
#     # Do some work...
#     print("Worker thread finished")
# t = threading.Thread(target=worker)     # Create a new thread
# t.start()   # Start the thread
# t.join()    # Wait for the thread to finish
# print("Main thread finished")


def print_numbers():
    for i in range(10):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        print(letter)
        time.sleep(0.5)

# Create two threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start the threads
t1.start()
t2.start()

# Wait for the threads to finish
t1.join()
t2.join()


# import threading
# import queue

# def process_message(message):
#     # Process the message, e.g. parse the text, extract attachments, etc.
#     # ...

#     return processed_message

# def send_message_to_database(processed_message):
#     # Save the processed message to a database
#     # ...

#     return save_status

# # Create a queue to hold incoming chat messages
# message_queue = queue.Queue()

# def message_handler():
#     while True:
#         # Get the next message from the queue
#         message = message_queue.get()

#         # Process the message in a separate thread
#         t = threading.Thread(target=process_message, args=(message,))
#         t.start()

#         # Wait for the message processing thread to complete
#         t.join()

#         # Send the processed message to a database in a separate thread
#         t = threading.Thread(target=send_message_to_database, args=(processed_message,))
#         t.start()

#         # Wait for the message saving thread to complete
#         t.join()

# # Start the message handler thread
# message_handler_thread = threading.Thread(target=message_handler)
# message_handler_thread.start()

# # In the main thread of the chat application, add incoming messages to the queue
# while True:
#     message = receive_message()
#     message_queue.put(message)
