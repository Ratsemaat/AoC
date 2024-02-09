
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }
}

pub fn p1_proc(input: &str)->String{

    let mut sum =0;
    for line in input.split("\n"){
        
        let  mut a=0;
        let mut b=0;

        
        for el in line.chars(){
            if (el.is_ascii_digit()) {
                b=el.to_digit(10).unwrap();
                if(a==0){
                    a=el.to_digit(10).unwrap();
                }
            } 
        }
        sum += 10*a +b;
    }


    sum.to_string()
}

pub fn p2_proc(input: &str)->String{
    let arr = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

    let mut sum =0;
    for line in input.split("\n"){
        
        let  mut a=0;
        let mut b=0;
        let mut s = line.to_string();

        for (i,num) in arr.iter().enumerate(){
            let mut str = num.to_string();
            str.push_str(&(1+i).to_string());
            str.push_str(num);
            s = s.replace(num, &str);
        }

        println!("{}", s);
        
        for el in s.chars(){
        

            if el.is_ascii_digit() {
                b=el.to_digit(10).unwrap();
                if(a==0){
                    a=el.to_digit(10).unwrap();
                }
            } 
        }
        sum += 10*a +b;
    }


    sum.to_string()
}