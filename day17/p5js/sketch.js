const example = [
    ".#.", 
    "..#", 
    "###"
];

const input = [ 
    ".#######",
    "#######.",
    "###.###.",
    "#....###",
    ".#..##..",
    "#.#.###.",
    "###..###",
    ".#.#.##."
];


let voxels = new ValueSet();
let inactiveNeighbours = new ValueSet();
let neighOffs = [];
let cycle = 0;


function initNeighOffs() {

    for ( let dx = -1; dx <= 1; dx++ ) {
    for ( let dy = -1; dy <= 1; dy++ ) {
    for ( let dz = -1; dz <= 1; dz++ ) {
        
        if ( dx == 0 && dy == 0 && dz == 0 ) {
            continue;
        }
        
        neighOffs.push( createVector( dx, dy, dz ) );

    }}}

}


function activeNeighbourCount(v, voxels) {

    let count = 0

    for (const off of neighOffs) {
        const neigh = p5.Vector.add(v, off);
        count += voxels.has(neigh);
    }

    return count;

}


function gatherInactiveNeighbours(v, currVoxels, inactiveNeighbours) {

    for (const off of neighOffs) {

        const neigh = p5.Vector.add(v, off);

        if ( currVoxels.has(neigh)) {
            continue;
        }

        inactiveNeighbours.add( neigh );

    }

}


function updateInactiveNeighbours(inactiveNeighbours, currVoxels, newVoxels) {
    
    for ( const v of inactiveNeighbours ) {

        const count = activeNeighbourCount(v, currVoxels);

        if (count == 3) {
            newVoxels.add(v);
        }

    }

}


function updateActive(v, voxels, newVoxels) {

    const count = activeNeighbourCount(v, voxels);

    if (count >= 2 && count <= 3) {
        newVoxels.add( v );
    }

}


function updateVoxels() {

    cycle++;

    let newVoxels = new ValueSet();
    inactiveNeighbours = new ValueSet();

    for (const v of voxels) {
        updateActive(v, voxels, newVoxels);
        gatherInactiveNeighbours(v, voxels, inactiveNeighbours);
    }

    updateInactiveNeighbours(inactiveNeighbours, voxels, newVoxels);
    voxels = newVoxels;

    console.log( cycle, voxels.length );

}


function parseInput( input ) {
    const dy = input.length;
    const dx = input[0].length;

    for ( let ix = 0; ix < dx; ix++ ) {
        for ( let iy = 0; iy < dy; iy++ ) {

            const x = ix - dx/2.0;
            const y = iy - dy/2.0;
            val = input[iy][ix];
            
            if ( val === '.' ) {
                continue;
            }

            voxels.add( createVector( x, dy/2-y, 0 ) );

        }
    }

}


function setup() {

    createCanvas(windowWidth, windowHeight, WEBGL);
    perspective(PI / 2.0, width / height, 0.1, 500);
    camera(-2, -3, 10, 0, -1, 0, 0, 1, 0);    

    initNeighOffs();
    parseInput( example );

}


function keyPressed() {
    updateVoxels();
}


function touchStarted( event ) {
  
    if ( touches.length === 0 ) {
      return;
    }
  
    updateVoxels();
  
}


function draw() {

    background(20, 20, 20);
    fill( 255, 255, 255 );
  
    orbitControl(5,5,5);    
    scale(1, -1);
    
    pointLight(255, 255, 255, 10, 10, 10);
    ambientLight(128);
    ambientMaterial(255,255,255);

    for (const voxel of voxels) {
        push();
        translate(voxel);
        box(1);
        pop();
    }

}