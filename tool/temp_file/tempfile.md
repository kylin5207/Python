# Tempfile临时文件

## 一、简介

### 1. 应用场景

> Python的`tempfile`模块是用来创建临时文件或者文件夹的跨平台工具。在大型数据处理项目中，有的处理结果是不需要向用户最终展示的，但是它们的应用又是贯穿项目始终的，在这种情况下，我们就需要使用`tempfile`模块来解决这种问题。



### 2. 四类接口

​	这四个高级接口提供了自动清除功能并且可以作为上下文管理器使用。

- TemporaryFile
- NamedTemporaryFile
- SpooledTemporaryFile
- TemporaryDirectory

![image-20220728170354287](/Users/a123/Library/Application Support/typora-user-images/image-20220728170354287.png)



### 3. 两个底层函数`mkstemp()`和`mkdtemp()`

​	用于生成临时底层的临时文件和文件夹，在使用完它们的时候需要手动清除。

![image-20220728170513786](/Users/a123/Library/Application Support/typora-user-images/image-20220728170513786.png)

### 4. 操作函数

`tempfile`模块还有一些针对文件、文件夹属性的操作函数：

![image-20220728170635252](/Users/a123/Library/Application Support/typora-user-images/image-20220728170635252.png)

`tempfile`的所有用户可调用函数和构造函数都带有额外参数，通过这些参数可以实现对临时文件目录和位置的管理。此模块会在共享临时目录中安全地创建临时文件，并给创建临时文随机起个名



## 二、临时文件创建

### 1. 高级临时文件对象创建函数

#### (1) Temporaryfile()

​	 返回一个类文件对象用作临时存储区，它使用与mkstemp()函数相同规则的安全重建文件模式，它一关闭就会被销毁（包括针对垃圾收集对象的隐式关闭）。需要注意的是，在Unix系统环境，文件的目录要么根本不创建，要么在文件创建后立即删除。也就是说，代码不会依赖于此函数创建的临时文件，包括它们的名称，这也是这个函数与NamedTemporaryfile函数的不同之处。

​	  使用：

```python
tempfile.TemporaryFile(mode='w+b', buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, errors=None)
```

> 参数说明
>
> `mode`参数：默认为`w+r`，以便文件在被创建时可以执行读写操作。
> `buffering`、`encoding`、`errors`和`newline`参数：用于解释`open()`函数行为。
>  `dir`、`prefix`和`suffix`参数：与`mkstemp()`具有相同的含义和默认设置。

```python
fp = tempfile.TemporaryFile(mode='w+b', buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, errors=None)

fp.write(b'Hello, Kylin')

# 读取数据
fp.seek(0)
print(fp.read())
```

​	另外，该函数生成的对象可以用作上下文管理器（参见示例）。完成上下文管理或销毁文件对象后，临时文件将从文件系统中删除。

####    (2) NamedTemporaryfile()

​	 除了NamedTemporaryfile()函数实现了在文件系统中只有一个可见名之外，其作用与TemporaryFile()功能完全相同。执行完该函数后，我们可以从返回的类文件对象的name属性中检索文件名称。在Unix系统上，在命名的临时文件处于打开状态时，可以使用该名称打开生成的文件.

```python
fp_2 = NamedTemporaryFile(mode='w+b', buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, delete=True, error=None)
```

> 使用方式和TemporaryFile基本一致，只是多了delete参数。
>
> 如果该参数为`True`（默认），则文件一关闭则被删除。返回的对象始终是一个类文件对象，其文件属性是底层的真实文件对象。也就是说，这个类文件对象可以在`with`上下文管理中使用，就像普通文件一样。

### 2. 高级临时目录创建函数

​	`TemporaryDirectory`函数使用与`mkdtemp()`相同的规则安全地创建临时目录。生成的对象可以用作上下文管理器（这里给出示例）。完成上下文或销毁临时目录对象后，新创建的临时目录及其所有内容将从文件系统中删除。

```python
temp_dir = TemporaryDirectory(suffix=None, prefix=None, dir=None)
```

> 调用该函数后，创建的目录名可以从返回对象的`name`属性中检索到。当返回的对象作为上下文管理器时，该名称将被分配给`with`语句中`as`子句的目标。另外，可以通过调用`cleanup()`方法显式清理目标。

### 3. 底层临时文件创建

  `	mkstemp()`函数以尽可能安全的方式创建临时文件，与`TemporaryFile()`函数不同，用户需要负责临时文件的删除。

```python
tmp_file = mkstemp(suffix=None, prefix=None, dir=None, text=False)
```

> 函数参数选项：
>
> - suffix：文件后缀，默认为None。如果不是None，文件名将以设置后缀结尾。
>
>   注意，mkstemp()函数不会在文件名和后缀之间加一个点，如果需要可以自行添加。
>
> - prefix：文件前缀，默认为None。如果不是None，文件以该前缀为开头；否则使用默认前缀，默认的前缀是由gettempprefix()或gettempprefixb()的返回值确定。
>
> - dir：文件创建的目录，默认为None，如果不是None，则使用默认目录；默认目录是从所使用的系统列表中选择的，但是用户可以通过设置TMPDIR、TEMP或TMP环境变量来控制目录位置。
>
> - text：文本类型，默认为False，即以二进制模式打开。如果为true，则以文本格式打开。

`mkstemp()`返回一个元组，该元组包含一个用于打开文件的操作系统级别（OS-leve）句柄（有`os.open()`函数返回）和该文件绝对路径名

![image-20220728173811792](/Users/a123/Library/Application Support/typora-user-images/image-20220728173811792.png)