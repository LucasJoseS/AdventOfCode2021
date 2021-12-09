use std::env;
use std::fs::File;
use std::io::Read;

const ASCII_ZERO_INDEX: u32 = 48;

fn was_checked(
    map: &mut Vec<Vec<u32>>,
    dp: (usize, usize),
    if_not_check_mark_as_check: bool,
) -> bool {
    let aux: bool = map[dp.0][dp.1] == u32::MAX;
    if !aux && if_not_check_mark_as_check {
        map[dp.0][dp.1] = u32::MAX;
    }

    aux
}

fn basin_size(map: &mut Vec<Vec<u32>>, dp: (usize, usize)) -> u32 {
    let mut sum: u32 = 0;

    if dp.0 < map.len() && dp.1 < map[0].len() && map[dp.0][dp.1] < 9 {
        was_checked(map, dp, true);

        sum += basin_size(map, (dp.0 + 1, dp.1));
        sum += basin_size(map, (dp.0, dp.1 + 1));

        if dp.0 != 0 {
            sum += basin_size(map, (dp.0 - 1, dp.1));
        }

        if dp.1 != 0 {
            sum += basin_size(map, (dp.0, dp.1 - 1));
        }
        sum += 1;
    }

    sum
}

fn main() {
    let filename = env::args().nth(1).expect("Not has a file to open");

    let mut content = String::new();
    let mut file = File::open(filename).expect("File not found");
    file.read_to_string(&mut content)
        .expect("Can't open the file");

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

    let mut deep_points: Vec<(u32, (usize, usize))> = Vec::new();
    let line_size = heightmap[0].len();
    let col_size = heightmap.len();

    if heightmap[0][0] < heightmap[0][1] && heightmap[0][0] < heightmap[1][0] {
        deep_points.push((heightmap[0][0], (0, 0)));
    }

    if heightmap[0][line_size - 1] < heightmap[0][line_size - 2]
        && heightmap[0][line_size - 1] < heightmap[1][line_size - 1]
    {
        deep_points.push((heightmap[0][line_size - 1], (0, line_size - 1)));
    }

    if heightmap[col_size - 1][0] < heightmap[col_size - 1][1]
        && heightmap[col_size - 1][0] < heightmap[col_size - 2][0]
    {
        deep_points.push((heightmap[col_size - 1][0], (col_size - 1, 0)));
    }

    if heightmap[col_size - 1][line_size - 1] < heightmap[col_size - 1][line_size - 2]
        && heightmap[col_size - 1][line_size - 1] < heightmap[col_size - 2][line_size - 1]
    {
        deep_points.push((
            heightmap[col_size - 1][line_size - 1],
            (col_size - 1, line_size - 1),
        ));
    }

    // check upper and down lines
    for i in 1..line_size - 1 {
        if heightmap[0][i] < heightmap[0][i + 1]
            && heightmap[0][i] < heightmap[0][i - 1]
            && heightmap[0][i] < heightmap[1][i]
        {
            deep_points.push((heightmap[0][i], (0, i)));
        }
        if heightmap[col_size - 1][i] < heightmap[col_size - 1][i + 1]
            && heightmap[col_size - 1][i] < heightmap[col_size - 1][i - 1]
            && heightmap[col_size - 1][i] < heightmap[col_size - 2][i]
        {
            deep_points.push((heightmap[col_size - 1][i], (col_size - 1, i)))
        }
    }

    // check right and left lines
    for i in 1..col_size - 1 {
        if heightmap[i][0] < heightmap[i][1]
            && heightmap[i][0] < heightmap[i - 1][0]
            && heightmap[i][0] < heightmap[i + 1][0]
        {
            deep_points.push((heightmap[i][0], (i, 0)))
        }
        if heightmap[col_size - i][line_size - 1] < heightmap[col_size - i][line_size - 2]
            && heightmap[col_size - i][line_size - 1] < heightmap[col_size - i - 1][line_size - 1]
            && heightmap[col_size - i][line_size - 1] < heightmap[col_size - i + 1][line_size - 1]
        {
            deep_points.push((
                heightmap[col_size - i][line_size - 1],
                (col_size - 1, line_size - 1),
            ));
        }
    }

    // check the middle
    for col in 1..col_size - 1 {
        for line in 1..line_size - 1 {
            let num = heightmap[col][line];

            if num < heightmap[col - 1][line]
                && num < heightmap[col][line + 1]
                && num < heightmap[col][line - 1]
                && num < heightmap[col + 1][line]
            {
                deep_points.push((num, (col, line)));
            }
        }
    }
    let mut risk: u32 = 0;
    for (num, _index) in &deep_points {
        risk += num + 1;
    }

    let mut basins: Vec<u32> = Vec::new();
    for (_value, pos) in &deep_points {
        basins.push(basin_size(&mut heightmap, *pos));
    }

    let mut mult = 1;

    for _ in 0..3 {
        let max = basins.iter().max().unwrap();
        print!("{} ", *max);
        mult *= *max;

        let index = basins.iter().position(|x| *x == *max).unwrap();
        basins.remove(index);
    }
    println!("{}", mult)
}
