use std::collections::{HashMap, HashSet};

fn main() {
    println!("Hello, world!");

    let lines = std::io::stdin().lines().map(|x| x.unwrap()).collect::<Vec<String>>();
    
    let mut nodes: HashMap<char, Vec<(i32, i32)>> = HashMap::new();
    for (i, line) in lines.iter().enumerate() {
        for (j, c) in line.chars().enumerate().filter(|(_, c)| *c != '.') {
            nodes.entry(c).or_default().push((i as i32, j as i32));
        }
    }

    let r: i32 = lines.len() as i32;
    let c: i32 = lines[0].len() as i32;

    let mut anodes: HashSet<(i32, i32)> = HashSet::new();
    for (t, v) in &nodes {
        for i in 0..v.len() {
            for j in i+1..v.len() {
                let dx = v[j].0 - v[i].0;
                let dy = v[j].1 - v[i].1;

                let mut nx = v[j].0;
                let mut ny = v[j].1;

                while nx >= 0 && nx < r && ny >= 0 && ny < c {
                    anodes.insert((nx, ny));
                    nx += dx;
                    ny += dy;
                }
 
                nx = v[i].0;
                ny = v[i].1;

                while nx >= 0 && nx < r && ny >= 0 && ny < c {
                    anodes.insert((nx, ny));
                    nx -= dx;
                    ny -= dy;
                }
            }
        }
        
    }
    println!("{:?}", anodes.len()); 

}
