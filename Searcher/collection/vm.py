'''

import os
import datetime

from django.db.models import F

from . import views
from . import lib_base
from .models_adapter import ModelVM
from .models import obModelSearcher

library = ModelVM()


async def __update_statistic_vm_files(file_vm):
    library.model_stat.objects.filter(id=1).update(file_vm=F("file_vm") + file_vm)


def __read_model_id(string):
    temp = string.split('-')
    if len(temp) == 6:
        model = obModelSearcher(satellite=temp[0], frequency=temp[1], poli=temp[2], ipFrom=temp[3],
                                                ipTo=temp[4])
        return model, int(temp[5].split('\n')[0])
    else:
        return 0


def __write_model_with_id(model, id_):
    return model.satellite + "-" + model.frequency + "-" + str(
        model.poli) + "-" + model.ipFrom + "-" + model.ipTo + "-" + \
           str(id_) + '\n'


def __get_id_model_collection(nameFile):
    temp = open(nameFile)
    returnList = dict()
    tempList = temp.readlines()
    for item in tempList:
        res = __read_model_id(item)
        if res != 0:
            a, b = res
            returnList[a] = b
    temp.close()
    return returnList


async def __get_model(vm_object):
    result = library.ob_model.objects.get_or_create(satellite=vm_object.obModelSearch.satellite,
                                                    frequency=vm_object.obModelSearch.frequency,
                                                    poli=vm_object.obModelSearch.poli,
                                                    ipFrom=vm_object.obModelSearch.ipFrom,
                                                    ipTo=vm_object.obModelSearch.ipTo)
    return result


async def __get_vm_get_or_create(vm_object, keyV):
    result = library.model_vm.objects.get_or_create(From=vm_object.From, To=vm_object.To, VM=vm_object.VM,
                                                    obModelSearch_id=keyV)
    return result


async def __get_vm_filter_first(getVM, vm_object, data, updateFileName):
    library.model_vm.objects.filter(id=getVM[0].pk).update(GP=vm_object.GP, VD=vm_object.VD,
                                                           fileName=F("fileName") + updateFileName,
                                                           time_prev=data, capacity=F("capacity") + 1)


async def __get_vm_filter_second(getVM, vm_object, data, updateFileName):
    library.model_vm.objects.filter(id=getVM[0].pk).update(GP=vm_object.GP, VD=vm_object.VD,
                                                           fileName=F("fileName") + updateFileName,
                                                           time_prev=data,
                                                           capacity=F("capacity") + 1, time_last=data)


async def __get_update_notes(getVM, vm_object):
    library.model_vm.objects.filter(id=getVM[0].pk).update(notes=getVM[0].notes + ";" + vm_object.notes)


def vm(pathVM, vm_request, vm_id):
    dirVM = os.listdir(pathVM)
    vm_cache = os.path.exists(vm_request)
    vmFile_id = os.path.exists(vm_id)

    # add new file
    if not vm_cache:
        open(vm_request, 'w').close()

    if not vmFile_id:
        open(vmFile_id, 'w').close()

    col_file = 0
    data = datetime.datetime.now()

    if len(dirVM) > 0:
        mapKeys = __get_id_model_collection(vm_id)

    for namePath in dirVM:

        file = open(pathVM + namePath)
        file_temp = open(vm_request)
        file_id = open(vm_id, 'a')

        items = file.readlines()
        items_temp = file_temp.readlines()

        file_temp.close()
        VMs = list()
        VMs_filename = set()

        file_temp = open(vm_request, 'a')

        for i in range(0, len(items), 1):

            if items[i] not in items_temp:

                file_temp.writelines(items[i])

                try:

                    vm_object = library.model_vm()
                    updateFileName = ""
                    vm_object.obModelSearch = views.parser_model(items[i])

                    try:
                        VMs_filename.add(vm_object.obModelSearch.fileName)
                        if len(VMs_filename) == len(VMs):
                            continue
                    except Exception as e:
                        print("error add list item in VMs:" + str(e))

                    temp_vm = items[i].split('-')
                    vm_object.From = temp_vm[7]
                    vm_object.To = temp_vm[8].split('\t')[0][0:2]

                    if len(temp_vm) > 9:
                        vm_object.VM = temp_vm[9].split('\n')[0]
                        if 12 == len(temp_vm):
                            vm_object.GP = temp_vm[10]
                            vm_object.VD = temp_vm[11]

                    VMs.append(vm_object)

                    try:
                        tempModelSearcher = obModelSearcher(vm_object.obModelSearch.satellite,
                                                                            vm_object.obModelSearch.frequency,
                                                                            vm_object.obModelSearch.poli,
                                                                            vm_object.obModelSearch.ipFrom,
                                                                            vm_object.obModelSearch.ipTo)
                        keyV = mapKeys[tempModelSearcher]
                    except:
                        getModel = lib_base.run_coroutine(__get_model(vm_object), 0)
                        keyV = getModel[0].pk
                        mapKeys[getModel[0]] = getModel[0].pk
                        file_id.writelines(__write_model_with_id(getModel[0], getModel[0].pk))

                    getVM = lib_base.run_coroutine(__get_vm_get_or_create(vm_object, keyV), 0)
                    updateFileName = ";" + vm_object.obModelSearch.fileName
                    if getVM[0].time_last is not None:
                        lib_base.run_coroutine(__get_vm_filter_first(getVM, vm_object, data, updateFileName), -1)
                    else:
                        lib_base.run_coroutine(__get_vm_filter_second(getVM, vm_object, data, updateFileName), -1)
                    if vm_object.notes != '':
                        lib_base.run_coroutine(__get_update_notes(getVM, vm_object), -1)


                except Exception as e:
                    file.close()
                    file_temp.close()
                    file_id.close()
                    print("error vm parser" + str(e))
                    return col_file

        file.close()
        os.remove(pathVM + namePath)
        col_file += 1

        if len(items_temp) == 200000:
            os.remove(vm_request)
            open(vm_request).close()

        if len(mapKeys) == 10000:
            os.remove(vm_id)
            open(vm_id).close()

        file_temp.close()
        file_id.close()

    lib_base.run_coroutine(__update_statistic_vm_files(col_file), -1)

    return "VM"

'''