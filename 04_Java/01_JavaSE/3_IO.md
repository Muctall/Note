# IO
### File类
File类，它是专门用于表示一个文件或文件夹，只不过它只是代表这个文件，但并不是这个文件本身。通过File对象，可以更好地管理和操作硬盘上的文件。
```Java
public static void main(String[] args) {
    File file = new File("test.txt");   //直接创建文件对象，可以是相对路径，也可以是绝对路径
    System.out.println(file.exists());   //此文件是否存在
    System.out.println(file.length());   //获取文件的大小
    System.out.println(file.isDirectory());   //是否为一个文件夹
    System.out.println(file.canRead());   //是否可读
    System.out.println(file.canWrite());   //是否可写
    System.out.println(file.canExecute());   //是否可执行

    System.out.println(Arrays.toString(file.list()));   //快速获取文件夹下的文件名称列表
    for (File f : file.listFiles()){   //所有子文件的File对象
        System.out.println(f.getAbsolutePath());   //获取文件的绝对路径
    }

}

File file = new File("test.txt");
try (FileInputStream inputStream = new FileInputStream(file)){   //直接做参数
    System.out.println(inputStream.available());
}catch (IOException e){
    e.printStackTrace();
}
```
### 文件字节流
基于byte读取处理
```Java
public static void main(String[] args) {
    try(FileOutputStream outputStream = new FileOutputStream("output.txt"，true); //true表示开启追加模式
        FileInputStream inputStream = new FileInputStream("input.txt")) {   //可以写入多个
        byte[] bytes = new byte[10];    //使用长度为10的byte[]做传输媒介
        int tmp;   //存储本地读取字节数
        while ((tmp = inputStream.read(bytes)) != -1){   //直到读取完成为止
            outputStream.write(bytes, 0, tmp);    //写入对应长度的数据到输出流
        }
    }catch (IOException e){
        e.printStackTrace();
    }
}
```

### 文件字符流
字符流不同于字节，字符流是以一个具体的字符进行读取，因此它只适合读纯文本的文件，如果是其他类型的文件不适用，字符流只支持char[]存储
```Java
public static void main(String[] args) {
    try(FileReader reader = new FileReader("test.txt")){
        char[] str = new char[10];
        reader.read(str);
        System.out.println(str);   //直接读取到char[]中
    }catch (IOException e){
        e.printStackTrace();
    }
}

public static void main(String[] args) {
    try(FileWriter writer = new FileWriter("output.txt")){
      	writer.getEncoding();   //支持获取编码（不同的文本文件可能会有不同的编码类型）
       writer.write('牛');
       writer.append('牛');   //其实功能和write一样
      	writer.flush();   //刷新
    }catch (IOException e){
        e.printStackTrace();
    }
}
```

### 缓冲流
虽然普通的文件流读取文件数据非常便捷，但是每次都需要从外部I/O设备去获取数据，由于外部I/O设备的速度一般都达不到内存的读取速度，很有可能造成程序反应迟钝，因此性能还不够高，而缓冲流正如其名称一样，它能够提供一个缓冲，提前将部分内容存入内存（缓冲区）在下次读取时，如果缓冲区中存在此数据，则无需再去请求外部设备。同理，当向外部设备写入数据时，也是由缓冲区处理，而不是直接向外部设备写入。

BufferedInputStream/BufferedOutputStream中还存在一个专门用于缓存的数组：
```Java
/**
 * The internal buffer array where the data is stored. When necessary,
 * it may be replaced by another array of
 * a different size.
 */
protected volatile byte buf[];
```
缓冲流提供的缓冲机制，一部分内容可以被暂时保存，BufferedInputStream/BufferedOutputStream支持reset()和mark()操作
```Java
public synchronized void mark(int readlimit) {
    in.mark(readlimit);
}
```

### 转换流
```Java
InputStreamWriter writer = new OutputStreamWriter(new FileOutputStream("test.txt"));
OutputStreamWriter writer = new OutputStreamWriter(new FileOutputStream("test.txt"))
```
### 数据流
数据流DataInputStream/DataoutputStream也是FilterInputStream/FilterOutputStream的子类，同样采用装饰者模式，最大的不同是它支持基本数据类型的直接读取.
```Java
public static void main(String[] args) {
    try (DataInputStream dataInputStream = new DataInputStream(new FileInputStream("test.txt"))){
        System.out.println(dataInputStream.readBoolean());   //直接将数据读取为任意基本数据类型
    }catch (IOException e) {
        e.printStackTrace();
    }
}
public static void main(String[] args) {
    try (DataOutputStream dataOutputStream = new DataOutputStream(new FileOutputStream("output.txt"))){
        dataOutputStream.writeBoolean(false);
    }catch (IOException e) {
        e.printStackTrace();
    }
}
```
