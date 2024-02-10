use regex::Regex;
use std::collections::HashMap;

pub fn p1_proc (input: &str)->String {
    let mut sum = 0;

    for (i, line) in input.split("\n").enumerate(){
        let regex = Regex::new (r"Card\s*\d+:\s*([\d|\s]+)+\s*\|\s*([\d|\s]+)+$").unwrap();
        let Some(out) = regex.captures(line) else{
            println!("{}", line);
            continue
        };
        let ticket = out[1].split_whitespace();
        let winning: Vec<&str> = out[2].split_whitespace().collect();

        let mut ticket_matches=0;
        for num in ticket{
            if winning.contains(&num){
                if ticket_matches==0{
                    ticket_matches+=1;
                } else {
                    ticket_matches *=2;
                }
            }
        }
        sum += ticket_matches 
    }
    sum.to_string()

}

pub fn p2_proc (input: &str)->String {
    let mut sum = 0;
    let mut dict: HashMap<usize, u32> = HashMap::new();

    for (i, line) in input.split("\n").enumerate(){
        dict.entry(i).or_insert(1);
        let regex = Regex::new (r"Card\s*\d+:\s*([\d|\s]+)+\s*\|\s*([\d|\s]+)+$").unwrap();
        let Some(out) = regex.captures(line) else{
            continue
        };
        let ticket = out[1].split_whitespace();
        let winning: Vec<&str> = out[2].split_whitespace().collect();

        let mut ticket_matches = 0;
        for num in ticket {
            if winning.contains(&num){
                ticket_matches += 1
            }
        }
        let temp = dict.get(&i).unwrap().clone();

        sum += temp;
        if ticket_matches > 0 {
            for j in 1..(ticket_matches+1){
                let stat = dict.entry(i+(j as usize)).or_insert(1);
                *stat += temp
            }
        }
            
    }
    sum.to_string()
}