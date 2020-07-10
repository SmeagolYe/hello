import os

current_file_path = os.path.realpath(__file__)
print(current_file_path)
common_dir_path = os.path.split(current_file_path)[0]
print(common_dir_path)

pro_path = os.path.split(common_dir_path)[0]
print(pro_path)

conf_path = os.path.join(pro_path, "conf", "config.conf")
test_data_path = os.path.join(pro_path, "test_data", "test_data.xlsx")
test_report_path = os.path.join(pro_path, "test_result", "html_report", "test_report.html")
log_path = os.path.join(pro_path, "test_result", "log", "test_log.txt")