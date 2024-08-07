# generator—yield

## 一、What's generator?

- 在 Python 中，使用了 **yield** 的函数被称为**生成器（generator）**, 生成器就是一个特殊的函数
- 一个函数用了**yield**后，返回的是一个**迭代器对象**，此时Python解释器会**将其视作生成器**

- 生成器一定是**迭代器**，它也一定可迭代。

- 为什么要用生成器？

  有时候，函数会返回一个列表，这个列表的大小是动态的，随着参数的大小变化而变化。比如斐波那契数列——暴力递归得到的东西实在是太太太太多了！而且一旦参数过大，数列的长度就会随之变大，此时的内存占用就会变得很大。为了节省内存，我们就想着让函数返回一个迭代器，当每次循环时能够一个一个得到列表中的值，而不是直接得到一整个列表。

- 生成器对象可以使用for循环或者__next__方法，**next()函数进行遍历**。生成器对象可以转换为**列表，元组**

  需要注意的是，访问生成器对象的元素时，已经访问过的元素就无法再次访问。

- 使用生成器的好处：

  - **节省内存空间**
  - **提升代码运行速度**

  因此，一旦我们想要节约内存资源或者提升运行效率，可以考虑使用生成器！



## 二、yield

​	python中使用生成器的主要语法为yield，当我们调用生成器时，生成器会暂停并保存当前所有的运行信息，并返回 yield 后面的值。在下一次执行 **next()** 方法时，**生成器会从之前断点处开始，继续运行**。而函数的状态是和上次中断执行前完全一样的，于是函数继续执行，直到遇到 yield，再次中断。

- 示例：

  ```python
  import random
  
  left = 0
  right = 10
  random.seed(0)
  
  def generate():
      while True:
          yield random.randint(left, right)
  
  print(next(generate()))
  ```

- 每次执行到有yield的时候，**会返回yield后面的值**，并且函数会暂停，直到下次调用才继续执行函数。最后迭代终止。
- 使用yield关键字因其在迭代到某个元素的时候，才会生成对应的元素，在迭代开始之前不会将所有需要迭代的元素都生成并存储到序列中，所以使用yield关键字更能节省内存。

> 另外yield和return的功能类似，不过yield运行后不会结束函数，会暂停然后继续向下运行。而return会直接结束

### 1. next()

- 直接调用，则返回一个生成器对象

```python
IN: type(generate())
OUT: <class 'generator'>
```

- 第一次对`生成器对象`调用`next()`，相当于启动`生成器`，会从`生成器函数`的第一行代码开始执行，直到第一次执行完`yield语句`后，跳出`生成器函数`。

```python
g = generate()
print(next(g))
```

- 之后调用next()，进入生成器函数后，会从yield语句的下一句语句开始执行，然后重新运行到yield语句，执行后，跳出生成器函数。后面再次调用next()，依此类推。即执行一次next()则调用一次生成器函数，直至抛出不可迭代的错误。

<img src="../Library/Application Support/typora-user-images/image-20221025104411738.png" alt="image-20221025104411738" style="zoom:50%;" />

### 2. seed()

​	`send()`函数和`next()`函数其实很相似，唯一的区别在于`send()`函数可以传入值，而`next()`函数不能传值。

- 第一次调用时不能使用`send()`发送一个`非None`的值，否则会出错的，因为没有`yield`语句来接收这个值。

- 之前res的值是None，现在变成1，2，3，因为send是发送参数给res，因为上面讲到，return的时候，并没有把4赋值给res，下次执行的时候只好继续执行赋值操作，只好赋值为None了。

  如果用send的话，出现的情况是，先接着上一次（yield 4之后）执行，先把接受到的1，2，3等赋值给了res，然后执行打印的作用，程序执行再次遇到yield关键字，yield会返回后面的值后，程序再次暂停，直到再次调用next()方法或send()方法。

```python
"""
send的用法
"""


def fun_yield():
    print("starting fun yield")
    while True:
        res = yield 4

        print("判断yield之后是否继续执行", res)


g = fun_yield()  # 调用这个函数只是会得到一个生成器
print("函数结果是一个生成器：", g)

print("对此生成器还是进行调用：")
print("*******1*********")
print(next(g))
print("*******2*********")
print("生成器的返回值", g.send(1))
print("******3*********")
print("生成器的返回值", g.send(2))
print("******4**********")
print("生成器的返回值", g.send(3))
```



- 如果用`send`的话，出现的情况是，先接着上一次（`yield 4`之后）执行，先把接受到的1，2，3等赋值给了`res`，然后执行打印的作用，程序执行再次遇到`yield`关键字，`yield`会返回后面的值后，程序再次暂停，直到再次调用`next()`方法或`send()`方法。

注意：yield不能嵌套