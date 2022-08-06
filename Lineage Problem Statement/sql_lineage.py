import sys

def get_originating_tables(sql_script):
    sql_linestripped = sql_script.strip().replace('\n',' ')
    sql_linestripped_lowercase = sql_linestripped.lower()
    first_from_clause_indx = sql_linestripped_lowercase.find('from')
    cols = sql_linestripped_lowercase[0:first_from_clause_indx]
    cols = [c.replace('select','').strip() for c in cols.split(',')]
    
    tab_dict = {}
    for i in cols:
        if i.split('.')[0] in tab_dict:
            tab_dict[i.split('.')[0]] = tab_dict[i.split('.')[0]] + ','+i.split('.')[1]
        else:
            tab_dict[i.split('.')[0]] = i.split('.')[1]
    
    tabs_queries = []
    from_idxs =  [i for i, letter in enumerate(sql_linestripped_lowercase.split(' ')) if letter == 'from']
    
    for idx,i in enumerate(from_idxs):
        if idx+1 == len(from_idxs):
            tabs_queries.append(sql_linestripped_lowercase.split(' ')[i:])
        else:
        # print(sql_linestripped_lowercase.split(' ')[i:from_idxs[idx+1]][1].replace(')','').strip())
            tabs_queries.append(sql_linestripped_lowercase.split(' ')[i:from_idxs[idx+1]])    
    
    new_tab_dict = {}
    for k in tab_dict:
        for t_q in tabs_queries:
            if 'select' in t_q[1]:
                continue
            for query in t_q:
                if k in query and len(query) <=2:
                    new_k = t_q[1].replace(')','').strip()
                    new_tab_dict[new_k] = tab_dict[k]
                    
    print("column => table")
    for k,v in new_tab_dict.items():
        for cols in v.split(","):
            print(f"""{cols} ==> {k}""")
    
    return new_tab_dict 

if __name__ == '__main__':
    sql_script = sys.argv[1]
    get_originating_tables(sql_script)