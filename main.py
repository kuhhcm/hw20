import time
import random
import threading

# # Задание 1
# def write_random_number(file):
#     random_number = random.randint(1, 100)
#     time.sleep(1)
#     with open(file, 'w') as file:
#         file.write(str(random_number))

# file = 'random_number.txt'
# write_random_number(file)

# # Задание 2
# def write_random_number(file):
#     random_number = random.randint(1, 100)
#     time.sleep(1)
#     with open(file, 'w') as file:
#         file.write(str(random_number))

# start = time.time()
# for i in range(1,1000):
#     file = f'random_number{i}.txt'
#     write_random_number(file)
# end = time.time()
# print("Время :", end - start)


# # Задание 3
# def write_random_number(filename):
#     random_number = random.randint(1, 100)
#     time.sleep(1)
#     with open(filename, 'w') as f:
#         f.write(str(random_number))

# def main():
#     start_time = time.time()
#     threads = []

#     for i in range(1, 1001):
#         filename = f"random_number_{i}.txt"
#         t = threading.Thread(target=write_random_number, args=(filename,))
#         threads.append(t)
#         t.start()

#     for thread in threads:
#         thread.join()

#     end_time = time.time()
#     print(f"Время выполнения: {end_time - start_time} секунд")
    
# main()