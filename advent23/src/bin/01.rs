use std::fs::File;
use std::io;
use std::io::BufRead;
use std::path::Path;

fn main() {
    //let path = "data/01/real.data";
    //let path = "data/01/test.data";
    let path = "data/01/test2.data";
    let mut total:i32 = 0;
    if let Ok(lines) = read_lines(path) {
        for line in lines {
            if let Ok(s) = line {
                let fixed = s
                    .replace("one","1")
                    .replace("two","2")
                    .replace("three","3")
                    .replace("four","4")
                    .replace("five","5")
                    .replace("six","6")
                    .replace("seven","7")
                    .replace("eight","8")
                    .replace("nine","9");
                let digits: Vec<char> = fixed.chars().filter(|c| c.is_digit(10)).collect();
                if let Some(first) = digits.first() {
                    if let Some(last) = digits.last() {
                        let number:i32 = format!("{}{}",first,last).parse().unwrap();
                        total += number;
                        println!("{}", number)
                    }
                }
            }
        }
    }
    println!("{}", total)
}


fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    let res = io::BufReader::new(file);
    Ok(res.lines())
}