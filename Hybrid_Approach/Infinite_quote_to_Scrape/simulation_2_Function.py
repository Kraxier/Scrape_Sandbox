import threading
import queue
import time

def scroll_simulator(data_queue, max_items=10, delay=0.7):
    """
    Simulates a scrolling task that discovers new items and puts them on a queue.
    """
    for i in range(1, max_items + 1):
        item = f"quote #{i}"
        print(f"[SCROLL] Found {item}")
        data_queue.put(item)
        time.sleep(delay)
    # Signal “end of data”
    data_queue.put(None)
    print("[SCROLL] Done scrolling.")

def extractor(data_queue, processing_delay=0.5):
    """
    Simulates extracting/processing items coming from the scroll_simulator.
    """
    while True:
        item = data_queue.get()
        if item is None:
            # No more data
            break
        print(f"[EXTRACT] Processing {item}")
        time.sleep(processing_delay)
    print("[EXTRACT] No more items to process. Shutting down.")

def main():
    # Shared queue between the two functions
    q = queue.Queue()

    # Create threads
    t_scroll = threading.Thread(target=scroll_simulator, args=(q,))
    t_extract = threading.Thread(target=extractor,       args=(q,))

    # Start both “in parallel”
    t_scroll.start()
    t_extract.start()

    # Wait for both to finish
    t_scroll.join()
    t_extract.join()

    print("All work complete.")

if __name__ == "__main__":
    main()
