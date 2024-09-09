## JDBC
pass
## Mybatis
见Framework
## Lombok(Plugin)
### 核心注解
#### @Getter 和 @Setter 
为当前类的所有字段生成get/set方法，他们可以添加到类或是字段上，注意静态字段不会生成，final字段无法生成set方法。

另外还可以使用@Accessors来控制生成Getter和Setter的样式。

#### @ToString
为当前类生成预设的toString方法

#### @EqualsAndHashCode
快速生成比较和哈希值方法。

#### @NoArgsConstructor, @RequiredArgsConstructor 和 @AllArgsConstructor
@AllArgsConstructor和@NoArgsConstructor来快速生成全参构造和无参构造。
@RequiredArgsConstructor来快速生成参数只包含final或被标记为@NonNull的成员字段。

### 常用注解
#### @Data
使用@Data能代表@Setter、@Getter、@RequiredArgsConstructor、@ToString、@EqualsAndHashCode全部注解。
一旦使用@Data就不建议此类有继承关系，因为equal方法可能不符合预期结果（尤其是仅比较子类属性）。

#### @Value
创建不可变类
@Value 就是 @Getter @FieldDefaults(makeFinal = true, level = AccessLevel.PRIVATE) @AllArgsConstructor @EqualsAndHashCode @ToString 的集合。

#### @Builder
流畅的构建者模式
#### @Log 系列注解
简化日志记录


## Maven
### Base
```XML
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>org.example</groupId>
    <artifactId>MavenTest</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>8</maven.compiler.source>
    </properties>

</project>
```
我们可以看到，Maven的配置文件是以project为根节点，而modelVersion定义了当前模型的版本，一般是4.0.0，我们不用去修改。

groupId、artifactId、version这三个元素合在一起，用于唯一区别每个项目，别人如果需要将我们编写的代码作为依赖，那么就必须通过这三个元素来定位我们的项目，我们称为一个项目的基本坐标，所有的项目一般都有自己的Maven坐标，因此我们通过Maven导入其他的依赖只需要填写这三个基本元素就可以了，无需再下载Jar文件，而是Maven自动帮助我们下载依赖并导入。

- groupId 一般用于指定组名称，命名规则一般和包名一致，比如我们这里使用的是org.example，一个组下面可以有很多个项目。
- artifactId 一般用于指定项目在当前组中的唯一名称，也就是说在组中用于区分于其他项目的标记。
- version 代表项目版本，随着我们项目的开发和改进，版本号也会不断更新，就像LOL一样，每次赛季更新都会有一个大版本更新，我们的Maven项目也是这样，我们可以手动指定当前项目的版本号，其他人使用我们的项目作为依赖时，也可以根本版本号进行选择（这里的SNAPSHOT代表快照，一般表示这是一个处于开发中的项目，正式发布项目一般只带版本号）

- properties中一般都是一些变量和选项的配置，我们这里指定了JDK的源代码和编译版本为1.8，无需进行修改。

### Dependency

```xml
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.8.1</version>
    
    <type>jar</type>
    <scope>system</scope>
    <systemPath>C://example/test.jar</systemPath>
    <optional>true</optional>

    <exclusions>
        <exclusion>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-engine</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

- type：依赖的类型，对于项目坐标定义的packaging。大部分情况下，该元素不必声明，其默认值为jar
- scope：依赖的范围（作用域，着重讲解）
- optional：标记依赖是否可选
- exclusions：用来排除传递性依赖（一个项目有可能依赖于其他项目，就像我们的项目，如果别人要用我们的项目作为依赖，那么就需要一起下载我们项目的依赖，如Lombok）
我们着重来讲解一下scope属性，它决定了依赖的作用域范围：

  - compile ：为默认的依赖有效范围。此种依赖，在编译、运行、测试时均有效。
  - provided ：在编译、测试时有效。
  - runtime ：在运行、测试时有效。
  - test ：只在测试时有效.
  - system：作用域和provided是一样的，但是它不是从远程仓库获取，而是直接导入本地Jar包,如果scope为system，那么我们需要添加一个systemPath来指定jar文件的位置
- optional：当项目中的某些依赖不希望被使用此项目作为依赖的项目使用时，可以给依赖添加optional标签表示此依赖是可选的，默认在导入依赖时，不会导入可选的依赖
- exclusions：如果存在那种不是可选依赖，但是我们导入此项目有不希望使用此依赖，我们就可以通过排除依赖来防止添加不必要的依赖

### 继承
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>MavenTest</artifactId>
        <groupId>org.example</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <modelVersion>4.0.0</modelVersion>

    <artifactId>ChildModel</artifactId>

</project>
```
一个Maven项目可以继承自另一个Maven项目，比如多个子项目都需要父项目的依赖，我们就可以使用继承关系来快速配置。子项目pom添加了一个parent节点，表示此Maven项目是父Maven项目的子项目，子项目直接继承父项目的groupId，子项目会直接继承父项目的所有依赖，除非依赖添加了optional标签。


```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.22</version>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>5.8.1</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.27</version>
        </dependency>
        <dependency>
            <groupId>org.mybatis</groupId>
            <artifactId>mybatis</artifactId>
            <version>3.5.7</version>
        </dependency>
    </dependencies>
</dependencyManagement>
```
我们还可以让父Maven项目统一管理所有的依赖，包括版本号等，子项目可以选取需要的作为依赖，而版本全由父项目管理，我们可以将dependencies全部放入dependencyManagement节点，这样父项目就完全作为依赖统一管理。我们发现，子项目的依赖失效了，因为现在父项目没有依赖，而是将所有的依赖进行集中管理，子项目需要什么再拿什么即可，同时子项目无需指定版本，所有的版本全部由父项目决定，子项目只需要使用即.当然，父项目如果还存在dependencies节点的话，里面的内依赖依然是直接继承.

### Maven指令
- clean命令：执行后会清理整个target文件夹，在之后编写Springboot项目时可以解决一些缓存没更新的问题。
- validate命令：可以验证项目的可用性。
- compile命令：可以将项目编译为.class文件。
- install命令：可以将当前项目安装到本地仓库，以供其他项目导入作为依赖使用
- verify命令：可以按顺序执行每个默认生命周期阶段（validate，compile，package等）
- package命令：可以直接对项目的代码进行打包，生成jar文件
- test命令：可以一键测试所有位于test目录下的测试案例，测试类的名称必须是以Test结尾




## Tomcat
Tomcat就是一个典型的Web应用服务器软件，通过运行Tomcat服务器，我们就可以快速部署我们的Web项目，并交由Tomcat进行管理，我们只需要直接通过浏览器访问我们的项目即可。

## Servlet

Servlet是Java EE的一个标准，大部分的Web服务器都支持此标准，包括Tomcat，就像之前的JDBC一样，由官方定义了一系列接口，而具体实现由我们来编写，最后交给Web服务器（如Tomcat）来运行我们编写的Servlet。

那么，它能做什么呢？我们可以通过实现Servlet来进行动态网页响应，使用Servlet，不再是直接由Tomcat服务器发送我们编写好的静态网页内容（HTML文件），而是由我们通过Java代码进行动态拼接的结果，它能够很好地实现动态网页的返回。

当然，Servlet并不是专用于HTTP协议通信，也可以用于其他的通信，但是一般都是用于HTTP。