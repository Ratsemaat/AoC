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
    "".to_string()
}