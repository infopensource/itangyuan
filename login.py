import os, sys
import wmi
import hashlib
import base64

c = wmi.WMI()
#处理器
def printCPU():
    tmpdict = {}
    tmpdict["CpuCores"] = 0
    for cpu in c.Win32_Processor():     
        tmpdict["cpuid"] = cpu.ProcessorId.strip()
        tmpdict["CpuType"] = cpu.Name
        tmpdict['systemName'] = cpu.SystemName
        try:
            tmpdict["CpuCores"] = cpu.NumberOfCores
        except:
            tmpdict["CpuCores"] += 1
        tmpdict["CpuClock"] = cpu.MaxClockSpeed 
        tmpdict['DataWidth'] = cpu.DataWidth
    #print (tmpdict)
    return  tmpdict


#主板
def printMain_board():
    boards = []
    # print len(c.Win32_BaseBoard()):
    for board_id in c.Win32_BaseBoard():
        tmpmsg = {}
        tmpmsg['UUID'] = board_id.qualifiers['UUID'][1:-1]   #主板UUID,有的主板这部分信息取到为空值，ffffff-ffffff这样的
        tmpmsg['SerialNumber'] = board_id.SerialNumber                #主板序列号
        tmpmsg['Manufacturer'] = board_id.Manufacturer       #主板生产品牌厂家
        tmpmsg['Product'] = board_id.Product                 #主板型号
        boards.append(tmpmsg)
    #print (boards)
    return boards

#BIOS
def printBIOS():
    bioss = []
    for bios_id in c.Win32_BIOS():
        tmpmsg = {}
        tmpmsg['BiosCharacteristics'] = bios_id.BiosCharacteristics   #BIOS特征码
        tmpmsg['version'] = bios_id.Version                           #BIOS版本
        tmpmsg['Manufacturer'] = bios_id.Manufacturer.strip()                 #BIOS固件生产厂家
        tmpmsg['ReleaseDate'] = bios_id.ReleaseDate                   #BIOS释放日期
        tmpmsg['SMBIOSBIOSVersion'] = bios_id.SMBIOSBIOSVersion       #系统管理规范版本
        bioss.append(tmpmsg)
    #print (bioss)
    return bioss

#硬盘
def printDisk():
    disks = []
    for disk in c.Win32_DiskDrive():
        # print disk.__dict__
        tmpmsg = {}
        tmpmsg['SerialNumber'] = disk.SerialNumber.strip()
        tmpmsg['DeviceID'] = disk.DeviceID
        tmpmsg['Caption'] = disk.Caption
        tmpmsg['Size'] = disk.Size
        tmpmsg['UUID'] = disk.qualifiers['UUID'][1:-1]
        disks.append(tmpmsg)

    return disks

#电池信息，只有笔记本才会有电池选项
def printBattery():
    isBatterys = False
    for b in c.Win32_Battery():
        isBatterys = True
    return isBatterys

#网卡mac地址：
def printMacAddress():
    macs = []
    for n in  c.Win32_NetworkAdapter():
        mactmp = n.MACAddress
        if mactmp and len(mactmp.strip()) > 5:
            tmpmsg = {}
            tmpmsg['MACAddress'] = n.MACAddress
            tmpmsg['Name'] = n.Name
            tmpmsg['DeviceID'] = n.DeviceID
            tmpmsg['AdapterType'] = n.AdapterType
            tmpmsg['Speed'] = n.Speed
            macs.append(tmpmsg)
    #print (macs)
    return macs

def computerNum():
    cpu=printCPU()['cpuid'].replace('0','A')
    board=printMain_board()[0]['UUID'].split('-')[-1]
    disk=printDisk()[0]['UUID'].split('-')[0]
    num=cpu+board+disk
    bytes_num = num.encode("utf-8")
    str_num= base64.b64encode(bytes_num)
    return str(str_num)[2:-1]

def regNum(computerNum):
    str_num = base64.b64decode(computerNum)
    m=hashlib.md5()
    m.update(str_num)
    return str(base64.b64encode(str(m.hexdigest()).encode("utf-8")))[2:-1]
    
    
