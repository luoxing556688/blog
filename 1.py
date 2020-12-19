#coding=utf-8

teacherlist=[{'id': 1, 'name': '罗老师', 'clsname': '全栈第五期'}, {'id': 1, 'name': '罗老师', 'clsname': '全栈六期'}, {'id': 1, 'name': '罗老师', 'clsname': '全栈六期'}, {'id': 2, 'name': '赵老师', 'clsname': '全栈六期'}, {'id': 2, 'name': '赵老师', 'clsname': '全栈七期'}, {'id': 3, 'name': '钱老师', 'clsname': '全栈九七'}, {'id': 3, 'name': '钱老师', 'clsname': '全栈八期'}, {'id': 4, 'name': '孙老师', 'clsname': '全栈六期'}, {'id': 5, 'name': '李老师', 'clsname': '全栈第五期'}, {'id': 5, 'name': '李老师', 'clsname': '全栈七期'}]
result={}
for row in teacherlist:
    nid=row['id']
    if  nid in result:
        result[nid]['clsname'].append(row['clsname'])
    else:
        result[nid]={'id':row['id'],'name': row['name'], 'clsname':[row['clsname']] }

print(result)




