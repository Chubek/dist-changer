import time
from random import randint, seed

def replace(original, small_case=False):
    if small_case:
        rpl = ['a', 'b', 'c', 'd']
    else:
        rpl = ['A', 'B', 'C', 'D']
    
    if len(original) > 1:
        
        new_both = f"{rpl[randint(0, len(rpl) - 1)]}{rpl[randint(0, len(rpl) - 1)]}"
        new_left = f"{original[0]}{rpl[randint(0, len(rpl) - 1)]}"
        new_right = f"{rpl[randint(0, len(rpl) - 1)]}{original[1]}"

        both_cond = new_both.lower() == original.lower() or new_both.lower() == original[::-1].lower() or new_both[0].lower() == new_both[1].lower() or len(new_both) > 2
        left_cond = new_left.lower() == original.lower() or new_left.lower() == original[::-1].lower() or new_left[0].lower() == new_left[1].lower() or len(new_left) > 2
        right_cond = new_right.lower() == original.lower() or new_right.lower() == original[::-1].lower() or new_right[0].lower() == new_right[1].lower() or len(new_right) > 2


        while both_cond:
          
          new_both = f"{rpl[randint(0, len(rpl) - 1)]}{rpl[randint(0, len(rpl) - 1)]}"
          both_cond = new_both.lower() == original.lower() or new_both.lower() == original[::-1].lower() or new_both[0].lower() == new_both[1].lower() or len(new_both) > 2

        while left_cond:
          
          new_left = f"{original[0]}{rpl[randint(0, len(rpl) - 1)]}"
          left_cond = new_left.lower() == original.lower() or new_left.lower() == original[::-1].lower() or new_left[0].lower() == new_left[1].lower() or len(new_left) > 2

        while right_cond:
          
          new_right = f"{rpl[randint(0, len(rpl) - 1)]}{original[1]}"
          right_cond = new_right.lower() == original.lower() or new_right.lower() == original[::-1].lower() or new_right[0].lower() == new_right[1].lower() or len(new_right) > 2

        
        decision_rand = randint(0, 2)

        if decision_rand == 0:
            new = new_both
        elif decision_rand == 2:
            new = new_right
        else:
            new = new_left
    else:
        
        new = rpl[randint(0, len(rpl) - 1)]

        while new.lower() == original.lower():
            new = rpl[randint(0, len(rpl) - 1)]

    return new



def split_and_rpl(answrs, pcnt, small_case=False):
    ans_lst = [x.strip() for x in answrs.split(",")]


    ans_lst_length = len(ans_lst) 
    pcnt_len = round(ans_lst_length * (pcnt / 100))
    
    indices = []

    for _ in range(pcnt_len):
                
        
        ind = randint(0, ans_lst_length - 1)

        while ind in indices:
            ind = randint(0, ans_lst_length - 1)
        
        ans_lst[ind] = replace(ans_lst[ind], small_case=small_case)

        indices.append(ind)

    return ans_lst




def iter(num_iter, pcnt, txt, is_lower):
    outputs = []    
    for i in range(num_iter):
        print(f"Iteration {i + 1}")
        
        ret = split_and_rpl(txt, pcnt, small_case=is_lower)

        result = [f"Q{i + 1} {ret[i]}" for i in range(len(ret))]

        outputs.append(", ".join(result))

    return outputs
