'''s='AI is important for its potential to change how we live, work and play. It has been effectively used in business to automate tasks done by humans, including customer service work, lead generation, fraud detection and quality control. In a number of areas, AI can perform tasks much better than humans. Particularly when it comes to repetitive, detail-oriented tasks, such as analyzing large numbers of legal documents to ensure relevant fields are filled in properly, AI tools often complete jobs quickly and with relatively few errors. Because of the massive data sets it can process, AI can also give enterprises insights into their operations they might not have been aware of. The rapidly expanding population of generative AI tools will be important in fields ranging from education and marketing to product design.'
i=97
c=0
for j in range(65,190):
    abc=ord(i)
    ABC=ord(j)
    for k in range(len(s)):
        if ABC==s[k] or abc==s[k]:            
            c=c+1
            for i in range(len(s)):
                if s[i]=='.'or s[i]==' ' or s[i]==',':

                else:
                    c=c+1
        
    i=i+1'''
#task2
s='AI is important for its potential to change how we live, work and play. It has been effectively used in business to automate tasks done by humans, including customer service work, lead generation, fraud detection and quality control. In a number of areas, AI can perform tasks much better than humans. Particularly when it comes to repetitive, detail-oriented tasks, such as analyzing large numbers of legal documents to ensure relevant fields are filled in properly, AI tools often complete jobs quickly and with relatively few errors. Because of the massive data sets it can process, AI can also give enterprises insights into their operations they might not have been aware of. The rapidly expanding population of generative AI tools will be important in fields ranging from education and marketing to product design.'
i=97
c=0
abc=''
ABC=''
alpha=0
for j in range(65,91):
    abc=chr(i)
    ABC=chr(j)
    for k in range(len(s)):
        if ABC==s[k] or abc==s[k]:            
            c=c+1
            alpha=alpha+1
    i=i+1
    print(f'letter {ABC} is {c} times')
    c=0
print('Total alphabets in paragraph ',alpha)
print('Total characters are ',len(s))
    
