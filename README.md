# StructSlender

Optimize the memory footprint of the struct in C/C++ by adjusting the order of variables.

## 结构

### StructParser

结构体解析，通过分析编译产生的中间文件`*.i`，提取所有定义的结构体，并解析其中的变量。
