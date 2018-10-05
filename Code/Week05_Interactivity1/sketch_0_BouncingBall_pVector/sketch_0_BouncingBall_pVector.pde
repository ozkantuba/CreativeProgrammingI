PVector speed = new PVector(1 ,  3.3);  // create a new PVector object instance
PVector location = new PVector(100,100);

void setup() {
    size(200,200);
}

void draw() {
    fill(255,10);
    rect(0,0,width,height);  //transparent overlay background

    // Add the current speed to the location: vector addition
    location.add(speed);

    // Check for bouncing
    if((location.x > width) || (location.x < 0)) {
        speed.x = speed.x * -1;  //reverse speed
    }
    if ((location.y > height) || (location.y < 0)) {
        speed.y = speed.y * -1;   //reverse speed
    }

    // Display at x,y location
    fill(175);
    ellipse(location.x,location.y,16,16);
  }