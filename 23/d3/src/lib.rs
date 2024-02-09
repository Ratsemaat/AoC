pub fn add(left: usize, right: usize) -> usize {
    left + right
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }
}


pub fn p1_proc(input: &str)->String {
    let mut nums: Vec<(usize, usize, u32)> = vec![];
    let mut symbs: Vec<(usize,usize)> = vec![];
    let mut sum=0;

    let mut num = "".to_string();
    for (i, line) in input.split("\n").enumerate() {
        for (j, char) in line.chars().enumerate(){
            if char.is_digit(10){
                num.push(char);
            } else {
                if num != "" {
                    nums.push((i, j-num.len(), num.parse().unwrap()));
                    num="".to_string();
                }
                if char!='.'{
                    symbs.push((i,j));
                }
            }
        }
        if num != "" {
            nums.push((i, line.len()-num.len()-1, num.parse().unwrap()));
            num="".to_string();
        }
    }


    for (a,b,c) in nums {
        let mut candidates: Vec<(usize,usize)> = vec![];
        if b>0 {
            candidates.push((a,b-1));
            candidates.push((a+1,b-1));
            if a>0{
                candidates.push((a-1,b-1));
            }
        }
        candidates.push((a,b+1+(c.checked_ilog10().unwrap_or(0) as usize)));

        for i in 0..((c.checked_ilog10().unwrap_or(0) + 2) as usize){
            if a>0{
                candidates.push((a-1,b+i));
            }
            candidates.push((a+1,b+i));
        }
        
        let mut found = false;
        for cand in candidates{
            if symbs.contains(&cand){
                found= true;
                break;
            }
        }
        if found{
            println!("{}", c);
            sum+=c;
        }
    }

    sum.to_string()

}

pub fn p2_proc(input: &str)->String {
    let mut nums: Vec<(usize, usize, u32)> = vec![];
    let mut symbs: Vec<(usize,usize, u32)> = vec![];
    let mut sum=0;

    let mut num = "".to_string();

    let mut grid: Vec<Vec<char>> = vec![];


    for (i, line) in input.split("\n").enumerate() {
        let mut temp = vec![];
        for (j, char) in line.chars().enumerate(){
            temp.push(char);
        }
        grid.push(temp);
    }

    for (i, row) in grid.iter().enumerate(){
        for (j, char) in row.iter().enumerate(){
            if *char=='*'{
          
               let mut nums = vec![];
               if i>0 {
                 let mut x = find_numbers(&grid[i-1], j);
                 nums.extend(x);
               }
                nums.extend(find_numbers(row, j));


               if i+1< grid.len() {
                 nums.extend(find_numbers(&grid[i+1],j));
               }

               if nums.len()==2{
                println!("{},{}", &nums[0], &nums[1]);

                 sum+= &nums[0] * &nums[1]
               }
            }
        }
    }

    return sum.to_string();
}

fn find_numbers(input: &Vec<char>, i:usize)-> Vec<u32>{
    let mut nums = vec![];
    let mut begin = i;
    let mut end =i;
    let mut num_growing = false;
    if i>0 {
        if input[i-1].is_digit(10){
            begin=i-1;
            while begin-1>=0 && input[begin-1].is_digit(10) {
                begin-=1;
                if begin==0{
                    break
                }
            }
            num_growing = true;
        } else {
            begin=i;
        }
    }

    if !(input[i].is_digit(10)){
        if num_growing{
            let k:String = input[begin..i].iter().collect();
            nums.push(k.parse().unwrap());
            num_growing=false;
        } 
        begin=i+1;
    } else{
        num_growing=true;
    }

    if i+1 < input.len(){
        if !(input[i+1].is_digit(10)){
            if num_growing{
                let k:String = input[begin..(i+1)].iter().collect();
                nums.push(k.parse().unwrap());
            } 
        } else {
            while end+1<input.len() && input[end+1].is_digit(10){
                end+=1;
            }
            let k:String = input[begin..end+1].iter().collect();
                 println!("{}", k);

                nums.push(k.parse().unwrap());
        }
    }
    return nums;
}