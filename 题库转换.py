import csv

step = '题干'
question = ''
option = ['','','','','']
option_no = 0
answer = ''
end_of_question = False
rows = []
with open('doc.txt') as f:
    for line in f:
        '''
        判断大类
        '''
        if '一、单项选择题' in line:
            question_type = '单选'
            continue
        elif '二、多项选择题' in line:
            question_type = '多选'
            continue
        elif '三、判断题' in line:
            question_type = '判断'
            continue
        elif '四、问答题' in line:
            question_type = '问答'
            continue
        
        '''
        分为题干、选项、答案三种类型，其中题干与答案是单行，选项可能是多行
        '''
        if step == '题干':
            question = line[line.find('.')+1:].lstrip().replace('\n', '')
            step = '选项答案'
        elif step == '选项答案':
            if line[:2] == '答案':
                answer = line[line.find('：')+1:].lstrip().replace('\n', '')
                step = '题干'
                end_of_question = True
            else:
                option[option_no] = line[line.find('.')+1:].lstrip().replace('\n', '')
                option_no += 1
        
        if end_of_question:
            rows.append([question,question_type,option[0],option[1],option[2],option[3],'',answer,''])
            option = ['','','','','']                
            option_no = 0
            end_of_question = False

header = ['题干','题型','选择项1','选择项2','选择项3','选择项4','解析','答案','得分']
with open('doc.csv','w',newline='') as f:
    ff = csv.writer(f)
    ff.writerow(header)
    ff.writerows(rows)
