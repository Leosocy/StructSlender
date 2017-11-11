# StructSlender

Optimize the memory footprint of the struct in C/C++ by adjusting the order of variables.

通过调整变量声明的顺序，优化C/C++结构体的内存占用。

**`使用StructSlender的前提是源代码要编译通过!`**

## 结构

### Usage

```shell
python slender.py -i ./data -o Slender.result
```

- -i: *.i所在的文件夹路径，递归搜索该路径下所有的.i文件
- -o: 优化结果存储文件路径(优化结果包括：需要优化的结构体、该结构体占用内存大小、优化后的结构体、优化后的结构体占用内存大小)

### SPM(Structure Preprocessing Module) 结构体预处理模块

#### 功能

1. 加载所有.i文件。
2. 调用gcc编译.i，确保编译通过。
3. 预处理，去除.i中的无用信息(预编译信息、全局变量、函数声明等与结构体无关的内容)。
4. 实现一个有限状态机，分割.i，生成list，传递给DAM模块。


### DAM(Data Adapter Module) 数据适配模块

#### 功能


### DSM(Data Structure Manager) 数据结构管理器

#### 功能
