use std::env;
use std::fs::File;
use std::io::Read;

const ASCII_ZERO_INDEX: u32 = 48;

fn main() {
    let filename = env::args()
        .nth(1)
        .expect("Not has a file to open");

    let mut content = String::new();
    let mut file = File::open(filename).expect("File not found");
    file.read_to_string(&mut content).expect("Can't open the file");

    let mut heightmap: Vec<Vec<u32>> = Vec::new();
    let content = content.split("\n");

    for line in content {
        let mut hline: Vec<u32> = Vec::new();
    
        for char in line.chars() {
            let num: u32 = char.into();
            let num = num - ASCII_ZERO_INDEX;
    
            hline.push(num);
        }
    
        heightmap.push(hline);
    }

    let mut deep_points: Vec<u32> = Vec::new();
    let line_size = heightmap[0].len();
    let col_size = heightmap.len();

    if heightmap[0][0] < heightmap[0][1] && heightmap[0][0] < heightmap[1][0] {
        deep_points.push(heightmap[0][0]);
    
    }

    if heightmap[0][line_size-1] < heightmap[0][line_size-2] && heightmap[0][line_size-1] < heightmap[1][line_size-1] {
        deep_points.push(heightmap[0][line_size-1]);
    }

    if heightmap[col_size-1][0] < heightmap[col_size-1][1] && heightmap[col_size-1][0] < heightmap[col_size-2][0] {
        deep_points.push(heightmap[col_size-1][0]);
    }

    if heightmap[col_size-1][line_size-1] < heightmap[col_size-1][line_size-2] && heightmap[col_size-1][line_size-1] < heightmap[col_size-2][line_size-1] {
        deep_points.push(heightmap[col_size-1][line_size-1]);
    }

    // check upper and down lines
    for i in 1..line_size-1 {
        if heightmap[0][i] < heightmap[0][i+1] && heightmap[0][i] < heightmap[0][i-1] && heightmap[0][i] < heightmap[1][i] {
            deep_points.push(heightmap[0][i])
        }
        if heightmap[col_size-1][i] < heightmap[col_size-1][i+1] && heightmap[col_size-1][i] < heightmap[col_size-1][i-1] && heightmap[col_size-1][i] < heightmap[col_size-2][i] {
            deep_points.push(heightmap[col_size-1][i])
        }
    }

    // check right and left lines
    for i in 1..col_size-1 {
        if heightmap[i][0] < heightmap[i][1] && heightmap[i][0] < heightmap[i-1][0] && heightmap[i][0] < heightmap[i+1][0] {
            deep_points.push(heightmap[i][0])
        }
        if heightmap[col_size-i][line_size-1] < heightmap[col_size-i][line_size-2] && heightmap[col_size-i][line_size-1] < heightmap[col_size-i-1][line_size-1] && heightmap[col_size-i][line_size-1] < heightmap[col_size-i+1][line_size-1] {
            deep_points.push(heightmap[col_size-i][line_size-1])
        }
    }

    // check the middle
    for col in 1..col_size-1 {
        for line in 1..line_size-1 {
            let num = heightmap[col][line];

            if num < heightmap[col-1][line] && num < heightmap[col][line+1] && num < heightmap[col][line-1] && num < heightmap[col+1][line] {
                deep_points.push(num);
            }
        }
    }

    println!("{:?}", deep_points);

    let mut risk: u32 = 0;
    for num in deep_points {
        risk += num +1;
    }

    println!("{}", risk);
}