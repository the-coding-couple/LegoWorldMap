# LegoWorldMap

Programmatically representing lego world map to ultimately to uniquely style the oceans

## Goal: programmatically represent and style the [lego world map](https://www.lego.com/en-us/product/world-map-31203)

- The map is represented by a series of square blocks that can be put together to make the world map.

- One block size is made of 16x16 squares.

- The map has 5 rows and 8 columns (top left block is the (0,0) coordinate and the bottom right block is the (4, 7) coordinate).

- Which means there are a total of 5x8=40 blocks and a total of 16x16x40 = 10,240 squares.

## Part 1: Create a grid representing world map (style A) with only white/navy squares included

- the [blocks](blocks) folder contains photos of each block and their lego pieces (and numbers), named by coordinate in map

### Idea 1: Do this by hand, one block at a time

### Idea 2: Take an image and program a way to translate it into a grid

- use neural net to read numbers of block images?

### Part 1 Solution

We gathered images of the map blocks from the lego handbook for this project and were able to pinpoint pixel values from each square to indicate what color square it is.

## Part 2: Create ways to view the grid, block by block and the whole map

- matplotlib
- other python grid viewers?

### Part 2 Solution

We used python notebooks to populate a numpy grid with the square values and then constructed a colored grid that contains ther RGB values where 1 pixel represents 1 square. This can be viewed with matplotlib and is saved as [colored_grid.jpg](colored_grid.jpg).

## Part 3: Make a website viewer of grid to interact with it


## Part 4: Style the empty parts of the map with the remaining squares (detailed in map uilding guide)

- etch-a-sketch type idea
- program to randomly draw it
- math to draw it (eg fractals)
- transfer art/photos onto the grid

## Notes

so all packages are contained within project itself and not just system, we all will have same setup

- python3 -m pip install virtualenv
- pip3 install virtualenv

- created env: python3 -m virtualenv env
- activated env: source env/bin/activate

- packages installed with pip3 install:
  numpy, matplotlib, opencv-python, glob2, flask, flask-sqlalchemy, Pillow

- activate virtual environment: source env/bin/activate
- load dependency packages:  pip3 install -r requirements.txt

python3 app.py >> <http://localhost:5000/>
