#program threadpoool with 5 different passs
import concurrent.futures
import random
import string

#generate random file
def generate_random_file():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(5))

#save file
def save_file(filename, contents):
    with open(filename,'w') as file:
        file.write(contents)

#task
def task(thread_id):
    random_filename = generate_random_file()
    random_number = random.randint(1, 100)
    content =f"Thread-{thread_id} Generated Random Numbers:{random_number}"
    print(f"Thread-{thread_id} is in filename : {random_filename}.txt")
    save_file(f"{random_filename}.txt",content)

if __name__ == "__main__":
    num_threads = 5
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executors:
        futures = [executors.submit(task,i) for i in range(num_threads)]
        concurrent.futures.wait(futures)
