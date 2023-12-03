use std::fs::File;
use std::io;
use std::io::BufRead;
use std::path::Path;

fn main() {
    let rgb = [12,13,14]; // r,g,b

    let path = "data/02/test.data";
    //let path = "data/02/real.data";
    for line in read_lines(path).unwrap() {
        let s = line.unwrap();
        let mut parts = s.split(": ");

        let game = parts.next().unwrap();
        println!("{:#?}",game);
    }
}


fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    let res = io::BufReader::new(file);
    Ok(res.lines())
}