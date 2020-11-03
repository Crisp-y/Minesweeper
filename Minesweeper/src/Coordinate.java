import java.util.ArrayList;

public class Coordinate {
    private int x;
    private int y;

    public Coordinate(int y, int x){
        this.y = y;
        this.x = x;
    }

    public int getX(){
        return x;
    }

    public int getY() {
        return y;
    }

    public boolean equals(Coordinate other){
        return x == other.getX() && y == other.getY();
    }

    public boolean equals(int y, int x){
        return x == this.x && y == this.y;
    }

    // Create and return an arraylist of all the surrounding coordinates
    public ArrayList<Coordinate> getSurrounds(){
        ArrayList<Coordinate> coords = new ArrayList<>();
        for (int i = -1; i < 2; i++) {
            for (int j = - 1; j < 2; j++) {
                coords.add(new Coordinate(y+i, y+j));
            }
        }
        coords.remove(this);
        return coords;
    }
}
