# memory check 内存分析



## 一、getsizeof

​	sys.getsizeof()——以字节为单位返回对象的大小。

​	sys.getsizeof只能作为计算内存大小的参考。

```sh
>>> import pandas as pd
>>> import numpy as np
>>> import sys
>>> a = np.arange(int(1e5))
>>> a
array([    0,     1,     2, ..., 99997, 99998, 99999])
>>> a.shape
(100000,)
>>> sys.getsizeof(a)
800112
>>> b = a
>>> sys.getsizeof(b)
800112
>>> a.flags["WRITEABLE"] = False
>>> sys.getsizeof(a)
800112
>>> df = pd.DataFrame(a, copy=False)
>>> sys.getsizeof(df)
800144
```

​	可以看到，sys.getsizeof只计算实际使用的内存大小，引用所消耗的内存大小不计算。



## 二、Memory profiler内存分析器

​	这是一个python模块，用于监控进程的内存消耗以及对python程序的内存消耗进行逐行分析。它是一个纯 python 模块，依赖于psutil模块。

### 1. 安装

```sh
pip install -U memory_profiler
```

### 2. 使用

​	如果想要对某一函数做性能分析，在需要做性能分析的函数前面加装饰器 <font color='red'>@profile</font>。

​	下方代码用于计算如何不copy原始numpy数据集的情况下，创建pandas.DataFrame数据。

```sh
# check_memory.py
from memory_profiler import profile
import numpy as np
import pandas as pd

@profile
def memory_check():
    a = np.arange(int(1e6))
    a.flags["WRITEABLE"] = False
    df = pd.DataFrame(a, copy=False)
    del a
    del df
memory_check()


bash：python check_memory.py
```

​	注意：使用时，需要将程序放入py文件中，利用命令行的方式启动。若直接在ipython中使用，会报错：`ERROR: Could not find file <stdin>`

```sh
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     6    101.3 MiB    101.3 MiB           1   @profile
     7                                         def memory_check():
     8    109.0 MiB      7.7 MiB           1       a = np.arange(int(1e6))
     9    109.0 MiB      0.0 MiB           1       a.flags["WRITEABLE"] = False
    10    109.0 MiB      0.0 MiB           1       df = pd.DataFrame(a, copy=False)
    11    109.0 MiB      0.0 MiB           1       del a
    12    101.5 MiB     -7.4 MiB           1       del df
```

	>- Mem usage: 内存占用情况
	>- Increment: 执行该行代码后新增的内存



### 3. 结合shared_memory查看内存

- 写入共享内存的代码

```python
# memory_before.py
import numpy as np
from multiprocessing import shared_memory
import pandas as pd
from memory_profiler import profile

@profile
def write_memory_check_before():
    idx = np.arange(int(1e6))
    share_idx = shared_memory.SharedMemory(name='share_idx', create=True, size=idx.nbytes)
    # write memory data
    data_idx = np.ndarray(idx.shape, dtype=idx.dtype, buffer=share_idx.buf)
    data_idx[:] = idx[:]

    # load memory data
    shared_array = np.ndarray(idx.shape, dtype=float, buffer=share_idx.buf)
    share_idx.close()
    share_idx.unlink()

write_memory_check_before()
```

```sh
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     6    102.0 MiB    102.0 MiB           1   @profile
     7                                         def write_memory_check_before():
     8    109.6 MiB      7.5 MiB           1       idx = np.arange(int(1e6))
     9    109.7 MiB      0.2 MiB           1       share_idx = shared_memory.SharedMemory(name='share_idx', create=True, size=idx.nbytes)
    10                                             # write memory data
    11    109.7 MiB      0.0 MiB           1       data_idx = np.ndarray(idx.shape, dtype=idx.dtype, buffer=share_idx.buf)
    12    117.3 MiB      7.5 MiB           1       data_idx[:] = idx[:]
    13                                             
    14                                             # load memory data
    15    117.3 MiB      0.0 MiB           1       shared_array = np.ndarray(idx.shape, dtype=float, buffer=share_idx.buf)
    16    109.7 MiB     -7.5 MiB           1       share_idx.close()
    17    109.7 MiB      0.0 MiB           1       share_idx.unlink()
```





## 三、docker中使用shared_memory

​	由于在并行计算的进程中，为了避免进行大量数据传递，我们是用了`SharedMemory`对象，但是其能够放置数据的空间，也是有限的。我们尝试在`docker-compose.yml`文件中增加`shm-size`，但是失败了。并且提示`Additional property shm-size is not allowed`。因此，详细瞅瞅docker中的share memory的相关描述。

​	容器的 `/dev/shm`目录下提供了一个临时文件存储文件系统，使用 RAM 来存储文件。作为共享内存并不一定必须使用，其作为促进进程间通信(inter-process communication, IPC)的一种方式。

Docker 容器默认分配 64 MB 的共享内存：

```sh
bash:~$ docker inspect ray-head-mq | grep -i shm
"ShmSize": 67108864,
bash:~$ docker inspect ray-local-1 | grep -i shm
"ShmSize": 67108864,
bash:~$ docker inspect ray-local-2 | grep -i shm
"ShmSize": 67108864,
```

> 由于我们程序中需要的共享内存在60MB左右，而当前仅有64MB

- 为什么不直接放在`/tmp`目录下？

  `/dev/shm`存在于 RAM 中（所以相对较快），而`/tmp`驻留在磁盘（相对较慢）

- 我们可以创建一个临时文件放在shared memory中

  ```sh
  bash:/# ls -l /dev/shm
  total 0
  ```

  > 可以看出，现在什么都没有

  ```sh
  bash:/# date >/dev/shm/date.txt
  bash:/# ls -l /dev/shm/
  total 4
  -rw-r--r-- 1 root root 29 Jan  6 02:55 date.txt
  bash:/# cat /dev/shm/date.txt
  Fri Jan  6 02:55:42 UTC 2023
  ```

  ​	所以shared_memory就像一个普通的文件系统，但它在 RAM 中。

- 如何查看使用共享内存的进程

  - `ipcs -m`指令可以查看当前使用共享内存的应用

    ```sh
    ------ Shared Memory Segments --------
    key        shmid      owner      perms      bytes      nattch     status      
    0x00000000 1376256    wookie     600        7802880    2          dest         
    0x00000000 1277954    wookie     600        851968     2          dest         
    0x00000000 1277956    wookie     600        851968     2          dest        
    0x00000000 1277958    wookie     600        77824      2          dest         
    0x00000000 1671189    wookie     600        36864      2          dest         
    0x00000000 1179651    wookie     600        8011776    2          dest    
    0x00000000 1703959    wookie     600        524288     2          dest
    0x0001eaea 557069     wookie     666        16384      0
    ```

  - `ipcs -pm`

    `cpid`列给出了创建共享内存段的进程的 PID，而`lpid`列反映了与其交互的最后一个进程的 PID。

    ```sh
    ------ Shared Memory Creator/Last-op PIDs --------
    shmid      owner      cpid       lpid      
    1376256    wookie     268958     1923      
    1277954    wookie     6254       285824
    1277956    wookie     6254       285824 
    1277958    wookie     6254       285824    
    1671189    wookie     6139       504020   
    1179651    wookie     24234      285810    
    1703959    wookie     282127     479099    
    557069     wookie     125674     125674
    ```

- docker中修改shm-size的大小

  ​	由于Docker 容器默认分配 64 MB 的共享内存，而我们放置在共享内存中的数据在64MB的临界大小，为了保险起见，需要修改`shm-size`大小。

  - docker-compose似乎不支持？

    <font color='red'>我们尝试在`docker-compose.yml`文件中增加`shm-size`，但是失败了。</font>并且提示`Additional property shm-size is not allowed`。

  ```sh
  version: "3.8"
    
  services:
    ray-head-mq:
      image: nvxhub.nvxclouds.net:9443/ai/photon-hetero-xgb:0.2
      container_name: ray-head-mq
      environment:
        PUID: 1003
        PGID: 1004
        USER: $USER
        PARTY_NAME: "global_tee"
        PYTHONPATH: "/workspace:/workspace/photon"
      #shm-size: 10.24gb
      volumes:
        - ${PWD}:/workspace/
      tty: true
      security_opt:
        - "seccomp:unconfined"
      cap_add:
        #- ALL
        - SYS_PTRACE
        - NET_ADMIN
      privileged: true
      ports:
        - "9082:8000"
        - "10888:8899"
        - "12001:8265"
      networks:
        photon_deploy:
          ipv4_address: 192.168.86.20
  ```



## 四、参考文档

- docker-compose change shared_memory

  https://stackoverflow.com/questions/58952478/changing-shared-memory-size-in-docker-compose

