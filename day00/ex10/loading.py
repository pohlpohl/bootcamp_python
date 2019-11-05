import time
import sys


def ft_progress(listy):
    start_time = time.time()
    list_max = max(listy)
    for i in listy:
        elapsed = time.time() - start_time
        prog = round(float(i) / float(list_max) * 100)
        bar_prog = int(round(prog / 100 * 23))
        eta = round(elapsed * list_max / (i + 0.000001), 2)
        sys.stdout.write('ETA: {:.2f}s [{:3}%][{}>{}] {}/{}\
 | elapsed time {}s\r'.format(eta, int(prog), bar_prog * '=\
', (23 - bar_prog) * ' ', i, list_max, round(elapsed, 2)))
        sys.stdout.flush()
        yield i


listy = range(333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)

print("\n...")
print(ret)
