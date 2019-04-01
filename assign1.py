import random

sample1 = "100100111101";
sample2 = "1001";
sample3 = "0010";
sample4 = "1001001010010000110100101";
# prob range 0.0 - 1.0 mean 0% - 100%
prob = round(random.uniform(0.0,1.0),1);

# ======================== Unreliable transmission ========================
def func1(str1, p):
    str1 = str(str1); 
    length_t = len(str1);
    list_str = list(str1);
    for i in range(0,length_t):
        prob_bit = round(random.uniform(0.0,1.0),1);
        # print(f"[index:{i}] prob_bit : {prob_bit} , prob : {prob}");
        if prob_bit <= p:
            if list_str[i] == '1': list_str[i] = 0;
            elif list_str[i] == '0': list_str[i] = 1;
            else:
                continue;
        else:
            continue;
    
    str2 = ''.join(str(i) for i in list_str);
    # print(f"Before :[{str1}]\n");
    # print(f"After  :[{str2}]\n");

    return str2
# ======================== Parity bit ========================
# p_type 
    # one data frame
    # 1:odd
    # 2.even

    # 3:two-dimensional odd
    # 4:two-dimensional even
    # many data frames
def func2_1(str1, p_type, size):
    final_code = '';
    str1 = str(str1);
    # One dimensional
    if p_type == 1 or p_type == 2:

        count = 0;
        list_str = list(str1);

        for i in list_str:
            if i == "1": count+= 1;

       
        if  p_type == 1:
            if  count%2 == 0:
                list_str.append(1);
            else:
                list_str.append(0);
            
            print("[ ODD PARITY ]");
            print(str1);
            str2 =''.join(str(i) for i in list_str)
            print(str2);
        else:
            if  count%2 == 0:
                list_str.append(0);
            else:
                list_str.append(1);

            print("[ EVEN PARITY ]");
            print(str1);
            str2 =''.join(str(i) for i in list_str)
            print(str2);
            final_code = str2;
    else:
        # Two dimensional
        if  (size-1)*(size-1) == len(str1):
            list_str = [['0' for x in range(size-1)] for y in range(size-1)];
            c_temp=0;
            for i in range(size-1):
                for j in range(0,size-1):
                    list_str[i][j] = str1[c_temp];
                    c_temp+=1;
            list_str2 = [['0' for x in range(size)] for y in range(size)];

            for i in range(size-1):
                count = 0;
                for j in range(size-1):
                    list_str2[i][j] = list_str[i][j];
                    if list_str2[i][j] == '1':
                        count+=1;
                if p_type ==3:
                    if  count%2 == 0:
                        list_str2[i][size-1] = '1';
                    else:
                        list_str2[i][size-1] = '0';
                else:
                    if  count%2 == 0:
                        list_str2[i][size-1] = '0';
                    else:
                        list_str2[i][size-1] = '1';
            for i in range(size-1):
                count = 0;
                for j in range(size-1):
                    if list_str2[j][i] == '1':
                        count+=1;
                if p_type ==3:
                    if  count%2 == 0:
                        list_str2[size-1][i] = '1';
                    else:
                        list_str2[size-1][i] = '0';
                else:
                    if  count%2 == 0:
                        list_str2[size-1][i] = '0';
                    else:
                        list_str2[size-1][i] = '1';
            count=0;
            for i in range(size):
                if list_str2[size-1][i] == '1':
                    count+=1;
            if p_type ==3:
                    if  count%2 == 0:
                        list_str2[size-1][size-1] = '1';
                    else:
                        list_str2[size-1][size-1] = '0';
            else:
                    if  count%2 == 0:
                        list_str2[size-1][size-1] = '0';
                    else:
                        list_str2[size-1][size-1] = '1';
            # for i in range(size-1):
            #     print(list_str[i]);
            
            # print("==============================");
            # for i in range(size):
            #     print(list_str2[i]);
            stroriginal = ""
            strfinal = ""
            for i in range(size-1):
                stroriginal += ''.join(str(k) for k in list_str[i]);
            for i in range(size):
                strfinal += ''.join(str(k) for k in list_str2[i]);
            # print(stroriginal);
            # print(strfinal);
            final_code = strfinal
        else:
            print("ERROR PUT THE PROPER SIZE FOR YOUR CODEWORD");
  
    return final_code;


def func2_1(str1, p_type, size):
    if p_type == 1 or p_type == 2:
        if p_type == 1:
            length_t = len(str1)
            c = 0;
            for i in range(length_t-1):
                if str1[i] == 1: c+=1;
                
            
            if c%2 == 0:
            elif c%2 == 1:
            else: print("[ERROR]");

    elif p_type == 3 or p_type == 4:

    else: print("[ERROR IN INPUT PARAMETER 2 ");

# output1 = func1(sample1,prob);
output2 = func2_1(func1(sample4,prob),4,6);





# print(output1);
print(output2);
