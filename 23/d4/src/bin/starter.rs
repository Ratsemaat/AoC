use d4::p1_proc;
use d4::p2_proc;
use std::fs;

fn main(){
    let file =  fs::read_to_string("example.txt").unwrap();
    println!("{}", p1_proc(&file));
    println!("{}", p2_proc(&file));

}