use std::fs::File;
use std::io;
use std::io::BufRead;
use std::path::Path;

// things I learned today: 1 - I am not very good at rust.
//                         2 - I am not very good with windows or vscode

fn main() {
    let path = "data/01/real.data";
    //let path = "data/01/test.data";
    //let path = "data/01/test2.data";
    let mut total:i32 = 0;
    if let Ok(lines) = read_lines(path) {
        for line in lines {
            let mut s = String::new();
            let mut first = ' ';
            let mut last = ' ';
            let blah = line.unwrap();
            print!("{} ",blah);
            for c in blah.chars() {
                if c.is_digit(10) {
                    first = c;
                    break;
                }
                s.push(c);
                //println!("{}",s);
                s = s
                    .replace("one","1")
                    .replace("two","2")
                    .replace("three","3")
                    .replace("four","4")
                    .replace("five","5")
                    .replace("six","6")
                    .replace("seven","7")
                    .replace("eight","8")
                    .replace("nine","9");
                if s.chars().last().unwrap().is_digit(10) {
                    first = s.chars().last().unwrap();
                    break;
                }
            }
            s.replace_range(.., "");

            for c in blah.chars().rev() {
                if c.is_digit(10) {
                    last = c;
                    break;
                }
                s.insert(0,c);
                //println!("{}",s);
                s = s
                    .replace("one","1")
                    .replace("two","2")
                    .replace("three","3")
                    .replace("four","4")
                    .replace("five","5")
                    .replace("six","6")
                    .replace("seven","7")
                    .replace("eight","8")
                    .replace("nine","9");
                let x = s.chars().next().unwrap();
                if x.is_digit(10) {
                    last = x;
                    break;
                }
            }
            let number:i32 = format!("{}{}",first,last).parse().unwrap();
            total += number;
            println!("{}", number)
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