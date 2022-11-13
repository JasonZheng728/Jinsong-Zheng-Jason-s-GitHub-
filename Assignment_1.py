import os.path
import shutil

# 1.1 Create directory
path1 = 'D:\\Users\\jason\\PycharmProjects\\Assignment1\\NewDirectory11\\SubDirectory111\\SubDirectory1111\\SubDirectory11111'
if not os.path.exists(path1):
    os.makedirs(path1)
path2 = 'D:\\Users\\jason\\PycharmProjects\\Assignment1\\NewDirectory22\\SubDirectory222\\SubDirectory2222\\SubDirectory22222'
if not os.path.exists(path2):
    os.makedirs(path2)
path3 = 'D:\\Users\\jason\\PycharmProjects\\Assignment1\\NewDirectory33\\SubDirectory333\\SubDirectory3333\\SubDirectory33333'
if not os.path.exists(path3):
    os.makedirs(path3)

# 1.2 Delete directory
os.rmdir('D:\\Users\\jason\\PycharmProjects\\Assignment1\\NewDirectory11\\SubDirectory111\\SubDirectory1111\\SubDirectory11111')
# shutil.rmtree('D:\\Users\\jason\\PycharmProjects\\Assignment1\\NewDirectory11\\SubDirectory111\\SubDirectory1111\\SubDirectory11111')

# 1.3 List files and subdirectories
list1 = os.listdir('D:\\Users\\jason\\PycharmProjects\\Assignment1')
print(list1)
# os.path.split('D:\\Users\\jason\\PycharmProjects\\Assignment1')

# 1.4 Move file or subdirectory to another location
shutil.move('D:\\Users\\jason\\PycharmProjects\\Assignment1\\NewDirectory33\\SubDirectory333\\SubDirectory3333\\SubDirectory33333','D:\\Users\\jason\\PycharmProjects\\Assignment1\\NewDirectory11\\SubDirectory111\\SubDirectory1111\\SubDirectory11111')

# 2.1 Create binary file
fp1 = open('D:\\Users\\jason\\PycharmProjects\\Assignment1\\NewDirectory11\\SubDirectory111\\SubDirectory1111\\SubDirectory11111\\BinaryFile1','wb')
fp1.close()
fp2 = open('D:\\Users\\jason\\PycharmProjects\\Assignment1\\NewDirectory22\\SubDirectory222\\SubDirectory2222\\SubDirectory22222\\BinaryFile2','wb')
fp2.close()
fp3 = open('D:\\Users\\jason\\PycharmProjects\\Assignment1\\NewDirectory33\\SubDirectory333\\SubDirectory3333\\SubDirectory33333\\BinaryFile3','wb')
fp3.close()

# 2.2 Delete binary file
os.remove('D:\\Users\\jason\\PycharmProjects\\Assignment1\\NewDirectory22\\SubDirectory222\\SubDirectory2222\\SubDirectory22222\\BinaryFile1')

# 2.3 Move binary file
shutil.move('D:\\Users\\jason\\PycharmProjects\\Assignment1\\NewDirectory22\\SubDirectory222\\SubDirectory2222\\SubDirectory22222','D:\\Users\\jason\\PycharmProjects\\Assignment1\\NewDirectory33\\SubDirectory333\\SubDirectory3333\\SubDirectory33333')

# 2.4 Read binary file (returns file content)
fp1 = open('D:\\Users\\jason\\PycharmProjects\\Assignment1\\NewDirectory11\\SubDirectory111\\SubDirectory1111\\SubDirectory11111\\BinaryFile1','rb+')
fp1.readlines()
fp1.close()

# 3.1 Create log text file
fp4 = open('D:\\Users\\jason\\PycharmProjects\\Assignment1\\NewDirectory11\\SubDirectory111\\SubDirectory1111\\SubDirectory11111\\LogTextFile4.txt','w+')
fp4.close()
fp5 = open('D:\\Users\\jason\\PycharmProjects\\Assignment1\\NewDirectory22\\SubDirectory222\\SubDirectory2222\\SubDirectory22222\\LogTextFile5.txt','w+')
fp5.close()
fp6 = open('D:\\Users\\jason\\PycharmProjects\\Assignment1\\NewDirectory33\\SubDirectory333\\SubDirectory3333\\SubDirectory33333\\LogTextFile6.txt','w+')
fp6.close()

# 3.2 Delete log text file
os.remove('D:\\Users\\jason\\PycharmProjects\\Assignment1\\NewDirectory22\\SubDirectory222\\SubDirectory2222\\SubDirectory22222\\LogTextFile5.txt')

# 3.3 Move log text file
shutil.move('D:\\Users\\jason\\PycharmProjects\\Assignment1\\NewDirectory22\\SubDirectory222\\SubDirectory2222\\SubDirectory22222','D:\\Users\\jason\\PycharmProjects\\Assignment1\\NewDirectory33\\SubDirectory333\\SubDirectory3333\\SubDirectory33333')

# 3.4 Readfile (returns file content)
fp7 = open('D:\\Users\\jason\\PycharmProjects\\Assignment1\\NewDirectory33\\SubDirectory333\\SubDirectory3333\\SubDirectory33333\\LogTextFile7.txt','w+', encoding = 'utf-8')
fp7.write("Life is short, study Python!")
fp7.readlines()
fp7.close()

# 3.5 Append a line to the end of the log text file
fp7 = open('D:\\Users\\jason\\PycharmProjects\\Assignment1\\NewDirectory33\\SubDirectory333\\SubDirectory3333\\SubDirectory33333\\LogTextFile7.txt','a+', encoding = 'utf-8')
fp7.writelines('Glory belongs to Ukraine!')
fp7.close()

# 4.1 Create buffer file
class Buffer:
    # queue = [], status = True, meta_dict = {}, useage_pct = 0
    def _init_(self, name, max_q_length = 100, max_data_size = 1000, memory_limit = 10000, fs = None, persist_method = None, persist_params = None, file_io = None, db_io = None):
        self.name = name
        self.max_q_length = max_q_length
        self.max_data_size = max_data_size
        self.memory_limit = memory_limit
        self.fs = fs
        self.persist_method = persist_method
        self.persist_params = persist_params
        # IO method
        self.file_io = file_io
        self.db_io = db_io
        self.is_io = fs.not_bad(file_io)
        # standard property
        self.queue = []
        self.status = True
        self.meta_dict = {}
        self.usage_pct = 0
    # Store data
    def push(self, data, meta_dict = None, verbose = False):
        if self.status:
            # 1 combine data and time stamp as tuple, try to push
            fs_ms = self.fs.get_ts_str_by_precision(p = 'us')
            data_tuple = data, fs_ms
            if verbose:
                print(data_tuple)
            queue_size_or_false = self.fs.add_ele_to_list_if_ok(data_tuple, self.queue, fs=self.fs)
            # 2 If push data successfully
            if queue_size_or_false:
                # Create key name
                key_name = '_'.join([self.fs.obj_md5_trans(data, fs=self.fs), fs_ms])
                if verbose:
                    print(key_name, 'pushed')
                # Store data if data attach metadata
                if meta_dict:
                    self.meta_dict[key_name] = meta_dict
                    self.useage_pct = queue_size_or_false/self.memory_limit
                    if len(self.queue) >= self.max_q_length:
                        if verbose:
                            print('The length has reached maximum, change status to false')
                        self.status = False
            return queue_size_or_false
        else:
            if verbose:
                print('Queue length is over maximum' % self.max_q_length)
            return self.status
    #Consume data. Popup last data by default.
    def pop(self, pos = -1, meta_dict = None, meta_match_method = 'eq', verbose = False, reverse = True):
        if meta_dict is None:
            return self.queue.pop(pos)
        else:
            query_flat_dict = self.fs.flat_dict(meta_dict)
            base_flat_dict = self.fs.flat_dict(self.meta_dict)
            # 1 Matched list from metadata
            meta_match_list = self.fs.cmp_flat_dict(base_flat_dict,query_flat_dict,cmp_method = meta_match_method)
            # 2 Execute list to current data
            queue_md5_list = ['_'.join(x) for x in self.fs.tuple_list_md5_trans(self.queue, fs = self.fs)]
            # 3 Return intersect list
            intersect_list = list(set(meta_match_list)&set(queue_md5_list))
            # 4 Order data according to time stamp
            interect_list1 = self.fs.list_sort_str_with_dlm(intersect_list, fs = self.fs, return_mode = 2, reverse = reverse)
            if verbose:
                print(interect_list1)
                pop_list = []
                for ele in interect_list1:
                    cur_pos = queue_md5_list.index(ele)
                    pop_list.append(self.queue.pop(cur_pos))
                    return pop_list


# 4.2 Delete buffer file

# 4.3 Push element to buffer file
# Create an instance object
fp7 = open('D:\\Users\\jason\\PycharmProjects\\Assignment1\\NewDirectory33\\SubDirectory333\\SubDirectory3333\\SubDirectory33333\\test.txt','a+', encoding = 'utf-8')
buffer = Buffer('test', fs = fp7 )
# Push element
for i in range (10):
    buffer.push(i, meta_dict = {'pkey':i},verbose=True)

Pushed result of data file:
(0, '1624504262064473')
f6b903077fadd6f7f7924a2dcfd0d828_1624504262064473  pushed
(1, '1624504262064831')
35a5b1d85b7654229dfe85526c3f385f_1624504262064831  pushed
(2, '1624504262064949')
007d8c6c24a357e859f4873cf1e8a84a_1624504262064949  pushed
(3, '1624504262065086')
3ca08f64e96a37c21811c2fb4ae7c73a_1624504262065086  pushed
(4, '1624504262065194')
27a65fb6788dea8e8da166ed3b560c05_1624504262065194  pushed
(5, '1624504262065303')
a61bcbc2b566dff6ee056c589630a527_1624504262065303  pushed
(6, '1624504262065413')
815a1feaf05f95d7565e1f45cd96c9c2_1624504262065413  pushed
(7, '1624504262065521')
e3bd9338ca1241c58489e3bbe2ea6581_1624504262065521  pushed
(8, '1624504262065630')
4f04ad77210a18f9aed36e508cc8fc6c_1624504262065630  pushed
(9, '1624504262065739')
04197ec22aa365eb5fa99ecb1212f0e9_1624504262065739  pushed

# 4.4 Consume element to buffer file (LIFO)
buffer.pop(meta_dict={'pkey':9}, verbose=True)

Pop result of data file:
[(9, '1624504262065739')]