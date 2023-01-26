import asyncio
import multiprocessing
import django

django.setup()


def run_coroutine(coroutine, result):
    """
    -1 - use and not give to body result
    0 - get first argument
    1 - get all result
    """
    try:
        coroutine.send(None)
    except Exception as e:
        if result == 0:
            return e.args[0]
        elif result == 1:
            return e.args


# for no async
def __run_search_task(fun, name):
    try:
        asyncio.run(fun)
    except Exception as e:
        print("fun with name '" + str(name) + "' for process coroutine: " + str(e.args))


list_pools = list()


def __run_methods(fun, name, is_async):
    # fun = port_parser.port_parser("z:/stat_temp/Port/"), name = "Port"
    if not is_async:
        __run_search_task(fun, name)
    else:
        run_coroutine(fun, -1)


def turn_server():
    for item in list_pools:
        list_pools.remove(item)
        item[0].terminate()


def __delete_process(name_pool):
    global list_pools
    for item in list_pools:
        if item[1] == name_pool:
            list_pools.remove(item)
            item[0].terminate()
            break


def __find_process(find_name_process):
    global list_pools
    for item in list_pools:
        if item[1] == find_name_process:
            return True
    return False


# send need list
def run_server_collect(list_fun, list_args, list_name, list_pool_process):
    global list_pools

    # start multi process
    for i in range(0, len(list_fun), 1):
        if not __find_process(list_name[i]):
            try:
                arguments = tuple(str(list_args[i]).split(';'))
                pool = multiprocessing.Pool(list_pool_process[i])
                pool.apply_async(func=list_fun[i], args=arguments, callback=__delete_process)
                list_pools.append([pool, list_name[i]])
            except Exception as e:
                print("error start process: '" + list_name[i] + "'" + str(e.args))


# all make for developer
def test(fun, name, is_async):
    __run_methods(fun, name, is_async)
    print("test good")
