use d1::p1_proc;
use d1::p2_proc;
use std::fs;

fn main(){
    let file =  fs::read_to_string("input.txt").unwrap();
    println!("{}", p1_proc(&file));
    println!("{}", p2_proc(&file));

}