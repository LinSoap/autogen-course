# __init__.py

# 可在此处添加包级别的初始化代码。

# 例如，您可以从子模块导入重要的类或函数，
# 使它们可以直接通过包名访问。
# 示例:
from .model_config import model_client 
# from . import submodule1
# from .submodule2 import ImportantClass

# 如果包包含多个子模块，并且您希望在导入包时自动加载它们，
# 可以使用 __all__ 列表来指定要导入的子模块名称。
__all__ = ['model_client']
