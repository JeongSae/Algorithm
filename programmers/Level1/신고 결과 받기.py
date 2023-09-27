def solution(id_list, reports, k):
    reports = list(set(reports))
    id_dict, report_dict = {}, {}
    for i in id_list:
        id_dict[i] = 0
        report_dict[i] = []
    
    for report in reports:
        splited_report = report.split()
        report_dict[splited_report[1]].append(str(splited_report[0]))
    
    for key, value in report_dict.items():
        if len(value) >= k:
            for v in value:
                id_dict[v] += 1
    
    return list(id_dict.values())