import logging
from common import pro_path

"""指定输出到控制台还是指定的文件"""
fh = logging.FileHandler(pro_path.log_path) #输出到指定文件
sh = logging.StreamHandler() #输出到控制台

"""定制日志输出格式"""
formatter = "%(asctime)s = %(levelname)s = %(message)s"
dfmt = "%a, %d %b %Y %H:%M:%S"

"""指定日志级别"""
logging.basicConfig(level=logging.DEBUG, handlers=[fh, sh], format=formatter, datefmt=dfmt)