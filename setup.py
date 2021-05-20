from setuptools import setup, find_packages

setup(
  name = 'tkit-memory-performer-xl',
  packages = find_packages(exclude=['examples']),
  version = '0.0.1.0',
  license='Apache License 2.0 ',
  description = 'Memory performer-XL, a variant of performer-XL that uses linear attention update long term memory',
  author = 'Terry Chan',
  author_email = 'napoler2008@gmail.com',
  url = 'https://github.com/napoler/memory-transformer-xl',
  keywords = ['attention mechanism', 'artificial intelligence', 'transformer', 'deep learning'],
  install_requires=[
      'torch',
      'performer-pytorch>=1.0.10',
      'mogrifier'
  ],
  classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'License :: OSI Approved :: Apache License 2.0',
      'Programming Language :: Python :: 3.6',
  ],
)


# 上传发布帮助

# https://www.notion.so/terrychanorg/PyPi-pip-b371898f30ec4f268688edebab8d7ba1



# ## 打包项目

# ```
# pip install wheel # 安装wheel模块

# python setup.py sdist  # 源码包
# python setup.py bdist_wheel --universal # 打包为无需build的wheel。其中--universal表示py2和py3通用的pure python模块。不满足通用或pure条件的模块不需加此参数
# ```

# ## 上传项目

# 先在pypi注册一个账户：[https://pypi.org/account/register/](https://pypi.org/account/register/)

# 然后安装上传所需模块：

# `pip install twine`

# 最后上传：

# `twine upload dist/*`