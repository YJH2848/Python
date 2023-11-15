import cProfile
from memory_profiler import profile 

#성능 측정을 위한 라이브러리
@profile
def append():
    result = []
    for i in range(1000000):

        result.append(i)
#         # print(result)

def ListComprehension():
    result = [i for i in range(1000000)]
    # print(result)

    
if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    
    # append()

    # ListComprehension()


    profiler.disable()
    profiler.print_stats(sort='cumulative')
