# IDE
## jupyter
```bash
pip3 intall jupyter 
```
```bash
jupyter notebook
```


## Pycharm Autopep8的配置
- 安装autopep8
```bash
pip3 install autopep8
```
- 命令行格式运行
```bash
autopep8 --in-place --aggressive --aggressive <filename>
```
- Pycharm中集成Autopep8
1. File -> Settings… ->Tools -> External Tools -> 点击“+”号添加
2. 配置好以下信息:
* Name：autopep8
* Program：C:\Python27\Scripts\autopep8.exe（在python的Scripts目录下）
* Arguments：--in-place --aggressive --aggressive $FilePath$
* Working directory：$ProjectFileDir$
* Output filters：$FILE_PATH$\:$LINE$\:$COLUMN$\:.*
3. 右键点击需要规范的文件，在菜单中找到External Tools -> autopep8

** NOTE: **
上面是完全按照标准的PEP8规范进行代码格式化的。但是有一些规范，可以忽略，此时可以在Parameters中加入—ignore参数。如：
`Parameters：--in-place --aggressive --ignore=E123,E133,E50 $FilePath$`
--ignore后面的E123等就是PEP8的规范代号，具体所指的规则，可以在这里查看到：
[https://pep8.readthedocs.io/en/latest/intro.html#configuration](https://pep8.readthedocs.io/en/latest/intro.html#configuration)

