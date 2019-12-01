import csv


step_for_question = True
end_of_question = False
options = ['','','','']
option_no = 0
rows = []
header = ['题干','题型','选择项1','选择项2','选择项3','选择项4','解析','答案','得分']

'''
注意：doc.txt为gbk编码，比较适合windows平台使用，哈哈哈
'''
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
            step_for_question = True
            continue
        elif '三、判断题' in line:
            question_type = '判断'
            step_for_question = True
            continue
        elif '四、问答题' in line:
            question_type = '问答'
            step_for_question = True
            continue
        
        '''
        分为题干、选项、答案三种类型，其中题干与答案为单行，选项可能多行
        '''
        if step_for_question:
            question = line[line.find('.')+1:].lstrip().replace('\n', '')
            step_for_question = False
        else:
            if line[:2] == '答案':
                answer = line[line.find('：')+1:].lstrip().replace('\n', '')
                step_for_question = True
                end_of_question = True
            else:
                options[option_no] = line[line.find('.')+1:].lstrip().replace('\n', '')
                '''
                忽略超出四个的选项
                '''
                if option_no == 3:
                    continue
                else:
                    option_no += 1
        
        if end_of_question:
            rows.append([question,question_type,options[0],options[1],options[2],options[3],'',answer,''])
            options = ['','','','']                
            option_no = 0
            end_of_question = False


with open('doc.csv', 'w', newline='') as f:
    ff = csv.writer(f)
    ff.writerow(header)
    ff.writerows(rows)
