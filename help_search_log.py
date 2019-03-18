class Search_file_content:
    @staticmethod
    def search_content(search_file,begin_string,end_string):
        f1=open(search_file,encoding='utf-8')
        content=f1.read()
        length=len(begin_string)
        list1=[]
        start=None
        while content.find(begin_string,start)!=-1:
            index_1= content.find(begin_string,start)+length
            index_2= content.find(end_string,index_1)
            list1.append(content[index_1:index_2])
            start=index_2

        f1.close()
        return list1
    @staticmethod
    def write_content(content_file):
        f2 = open(content_file, 'w', encoding='utf-8')
        for each_line in Search_file_content.search_content(search_file,begin_string,end_string):
            f2.write(each_line+';'+'\n')
        f2.close()

if __name__=='__main__':
    search_file=r'D:\github\onenote\myonenote\0318.txt'
    begin_string='sql['
    end_string=']'
    Search_file_content.write_content(content_file=r'D:\github\onenote\myonenote\sql.log')