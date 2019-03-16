class Search_file_content:
    @staticmethod
    def search_content(search_file,begin_string,end_string):
        f1=open(search_file,encoding='utf-8')
        content=f1.readlines()
        length=len(begin_string)
        list1=[]
        for i in content:
            if i.find(begin_string)!=-1:
                index_1= i.find(begin_string)+length
                index_2= i.find(end_string,index_1)
                list1.append(i[index_1:index_2])
        f1.close()
        return list1
    @staticmethod
    def write_content(content_file):
        f2 = open(content_file, 'w', encoding='utf-8')
        for each_line in Search_file_content.search_content(search_file,begin_string,end_string):
            f2.write(each_line+'\n')
        f2.close()

if __name__=='__main__':
    search_file=r'D:\github\onenote\myonenote\app_20190315.log'
    begin_string='session['
    end_string=']'
    Search_file_content.write_content(content_file=r'D:\github\onenote\myonenote\sql2.log')