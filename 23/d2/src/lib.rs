use regex::Regex;


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
    let mut sum=0;
    for (i, line) in input.split("\n").enumerate() {
        let parts = line.split(":").nth(1).unwrap();
        let games = parts.split(";");
        let mut success= true;
        for game in games{
            let mut reds=0;
            let mut blues=0;
            let mut greens=0;
            let draws = game.split(",");
            for draw in draws{
                let  re = Regex::new(r"(\d+)\s(\w+)").unwrap();

                let Some(caps) = re.captures(draw) else {
                    println!("{}","error");

                    continue};
                if &caps[2] == "red"{
                    reds += &caps[1].parse().unwrap();
                }
                if &caps[2] == "green"{
                    greens += &caps[1].parse().unwrap();
                }
                if &caps[2] == "blue"{
                    blues += &caps[1].parse().unwrap();
                }
            }

            if reds >12 || blues>14 || greens > 13 {
                success=false;
                break;
            } 
        }
        if success{
            sum+=1+i;
        }
        
    }
    sum.to_string()
}

pub fn p2_proc(input: &str)->String{
    let mut sum=0;
    for (i, line) in input.split("\n").enumerate() {
        let parts = line.split(":").nth(1).unwrap();
        let games = parts.split(";");
        let mut max_reds=0;
        let mut max_blues=0;
        let mut max_greens=0;
        for game in games{
            let mut reds=0;
            let mut blues=0;
            let mut greens=0;
            let draws = game.split(",");
            for draw in draws{
                let  re = Regex::new(r"(\d+)\s(\w+)").unwrap();

                let Some(caps) = re.captures(draw) else {
                    println!("{}","error");

                    continue};
                if &caps[2] == "red"{
                    reds += &caps[1].parse().unwrap();
                }
                if &caps[2] == "green"{
                    greens += &caps[1].parse().unwrap();
                }
                if &caps[2] == "blue"{
                    blues += &caps[1].parse().unwrap();
                }   

                if greens>max_greens{
                    max_greens=greens;
                }
                if blues>max_blues{
                    max_blues = blues;
                }
                if reds > max_reds{
                    max_reds=reds;
                }
            }
           
        }
        println!("{}", max_reds*max_greens*max_blues);
        sum+=max_reds*max_greens*max_blues;
        
    }
    sum.to_string()
}